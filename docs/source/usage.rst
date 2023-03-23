Usage
########

pyClesperanto is a GPU-accelerated image processing library for Python. The first step is to import the library and to see what OpenCL devices are available:

.. code-block:: python

    import pyclesperanto as cle

    print(cle.list_available_device())

.. warning::

    If an error is thrown at this stage, it is likely that the OpenCL driver is not installed or that you do not have a OpenCL compatible device. 
    Please, check the installation of your OpenCL and driver.

By default, the first device found will be automatically selected. You can know which device you currently working on, and you can select another one:

.. code-block:: python

    print(cle.info())

    cle.select_device("GTX")

The device selection is done by name. You can pass a substring of the device name, and the first device that matches will be selected. 

Memory transfer
================

It is a good practice to consider the GPU as another computer. It has its own memory, and you need to transfer data to it before processing it.
As well as transfer it back to your computer when you are done so that you can read the results. In pyclesperanto this is managed by the functions ``push``, ``pull``, and ``create``.
``push`` and ``pull`` are used to transfer data from the host to the GPU and vice versa. ``create`` is used to create an empty space on the GPU which will be then use, for example to store a result.


Create
--------

As there is not data transfert, we only need to specify the size of the image we want to create. The image will be created on the GPU and will be empty.
The size of the image is specified as a tuple of integers following the numpy convention ``zyx``.

.. code-block:: python

    # create an empty image on the GPU of size 100x100
    gpu_image = cle.create((100, 100))

By default, this will create a 32-bit float space. You can specify the type of the image by passing a ``dtype`` argument:

.. code-block:: python

    # create an empty image on the GPU of size 100x100
    gpu_image = cle.create((100, 100), dtype=np.uint8)

Push
--------

The ``push`` will create a memory space on the GPU like ``create`` but will also fill it with a data array from the host. For compatibility with the python ecosystem, the data array is expected to be a numpy array.

.. code-block:: python

    arr = np.random.random((100, 100)).astype(np.float32)
    # push arr to the GPU
    gpu_image = cle.push(arr)

The data pushed will keep the same data type as the array. Hence, if you push a ``uint8`` array, the data will be stored as ``uint8`` on the GPU. 
The array will then use 24 times less memory than if it was stored as ``float32``. This is a good practice to keep in mind when working with GPUs as their
memory is limited.

Pull
--------

Finally, the ``pull`` function will transfer the data from the GPU back to the host. It will be returned has a numpy array.

.. code-block:: python

    # pull gpu_image to the host
    arr = cle.pull(gpu_image)

The data type of the array will be the same as the data type of the image on the GPU. 

.. note:: 

    Some operation done on the GPU image may change the data type if needed. For example, the ``gaussian_blur`` will return a ``float32`` image even if the input image is ``uint8``.

.. warning::

    Not all operation will manage the datatype conversion. Only the one where it is part of the algorithm will do it. For example, the ``add_image_and_scalar`` will not convert the data type of the image.
    If the ``scalar`` add to the image reach the maximum value of the data type, the result will be staturated.


Apply operations on images
==========================

In py-clesperanto, most function will represent a filter or an operation on images. Each filter are independent and can be used in any order related to your objectives.
Therefore we standardised the API so that all functions respect the same convention.

.. code-block:: python

    cle.function_name(input, output, arg0, arg1, ...)

This convention is standard to all clesperanto languages, insuring that you can easily switch from one language to another.
It is also used as the GPU cannot determine what is the size or type of output you kernel will generate. Therefore, you need to specify the output memory space in which it will write.

for example, to apply a filter such as a gaussian blur, you need to specify the following code:

.. code-block:: python

    # push an image to the GPU
    gpu_input = cle.push(image)
    # create an output of the same size of the input
    gpu_output = cle.create(image.shape)
    # apply a gaussian blur
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    # pull back the result to the host
    result = cle.pull(gpu_output)

It is a good practice, at start, to define the input and output and pass them to the function. This will help you to properly managed the data memory between operations.
Now, it is also possible to let py-clesperanto manage the ``push`` and ``create`` of the input and output, making your code shorter and saving you time.

.. code-block:: python

    # apply a gaussian blur
    gpu_output = cle.gaussian_blur(image, sigma_x=2, sigma_y=2)
    # pull back the result to the host
    result = cle.pull(gpu_output)

Here, the ``image`` is pushed to the GPU and the output is created automatically when calling the operation ``gaussian_blur``. The function will return a ``gpu_image`` ready to be pulled back to the host.

The ``push`` and ``pull`` are data transfert between the host and the GPU. Those operation are the most costly in term of time. It is therefore a good practice to avoid them as much as possible.

Pipeline of operations
======================

As mentioned before, most of the functions in pyclesperanto are independent. This means that you can chain them together to create a pipeline of operations.
for example, to apply a gaussian blur followed by a threshold, you can write the following code:

.. code-block:: python

    # apply a gaussian blur
    gpu_input = cle.push(image)
    gpu_output = cle.create(image.shape)
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    blurred = cle.pull(gpu_output)

    # apply a threshold
    gpu_input = cle.push(blurred)
    gpu_output = cle.create(blurred.shape)
    cle.greater_constant(gpu_output, gpu_output, constant=0.5)
    binarized = cle.pull(gpu_output)

Although this code is correct, it is not optimal due to the ``push`` and ``pull`` in between the two operations.
These operations are costly and should be avoided as much as possible in the final version of the code. However they remain a necessity if one whant to inspect the result of each operation.

.. code-block:: python

    # apply a gaussian blur
    gpu_blurred = cle.gaussian_blur(image, sigma_x=2, sigma_y=2)
    # apply a threshold
    gpu_binarized = cle.greater_constant(gpu_blurred, constant=0.5)
    # read the output on host
    binarized = cle.pull(gpu_binarized)

Here we only use ``push`` at the beginning inside the ``gaussian_blur`` operation and ``pull`` at the end of the pipeline. The ``create`` is done automatically inside the operations.
