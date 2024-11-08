Usage
#####

pyClesperanto is a GPU-accelerated image processing library for Python. The first step is to import the library:

.. code-block:: python

    import pyclesperanto as cle

.. warning::

    If an error is thrown at this stage, it is likely that the OpenCL driver is not installed or that you do not have a OpenCL compatible device.
    Please, check the installation of your OpenCL and drivers.

You can then explore the devices available on your computer with the `list_available_devices()` function or the `info()` function for more details:

.. code-block:: python

    # Return the name of all available devices on the computer
    print(cle.list_available_devices())

    # Return the name and information of all the devices
    print(cle.info())


If we want to work on a device we first need to select it. By default, the first device found will be automatically selected for conveniency.
You can know which device you currently working on with the `get_device()` function, and you can select another one with `select_device()`:

.. code-block:: python

    # Query the current device
    print(cle.get_device())

    # Select a device by name, substring, or index
    cle.select_device("NVIDIA RTX 4090") # full name
    cle.select_device("TX")              # substring
    cle.select_device(0)                 # device index



Memory transfer
===============

GPU devices have their own memory, which is separated from the computer memory. Therefore, you need to transfer your data to the device memory in order to process it and back to the computer memory to read the results.
This is commonly know as `copy from host to device` and `copy from device to host`. In pyclesperanto we use the functions `push`, `pull`, and `create` to manage the memory transfer.
- `push` is used to transfer data from the host to the device.
- `pull` is used to transfer data from the device to the host.
- `create` is used to allocate an empty space on the device which will be used, for example, to store a result.

These copy operations are costly in term of time as they scale with the data size. Therefore, it is a good practice to avoid them as much as possible once you are opmissing your code.

Create
------

As there is not data transfert, we only need to specify the size of the image we want to create. The image will be created on the GPU and will be empty.
The size of the image is specified as a tuple of integers following the numpy convention ``zyx``.

.. code-block:: python

    # create an empty image on the GPU of size 100x100
    gpu_image = cle.create((100, 100))

By default, this will create a 32-bit float space. You can specify the type of the image by passing a ``dtype`` argument:

.. code-block:: python

    # create an empty image on the GPU of size 100x100
    gpu_image = cle.create((100, 100), dtype=np.uint8)

It is also possible to use an other image as a template to create the new image. This will copy the size and the data type of the template image.

.. code-block:: python

    # create an empty image on the GPU with the same size and data type as the template image
    gpu_image = cle.create_like(template_image)


Push
----

The ``push`` will create a memory space on the GPU like ``create`` and then will data array from the host to this new memory space on the device.
The data array is expected to be a numpy array or share the same interface as a numpy array (e.g. dask array).

.. code-block:: python

    arr = np.random.random((100, 100)).astype(np.float32)
    # push arr to the GPU
    gpu_image = cle.push(arr)

The data pushed will keep the same data type as the array. Hence, if you push a ``uint8`` array, the data will be stored as ``uint8`` on the GPU.
The array will then use 4 times less memory than if it was stored as ``float32``. This is a good practice to keep in mind when working with GPUs as their
memory can be limited.

.. warning::

    pyclesperant does not support `64-bit` data type such as `int64` or `float64` which are the default data type in python. This is to ensure full compatibility with most of the GPU devices.
    Hence, precisiion might be lost when converting the data type to `32-bit`.

Pull
----

Finally, the ``pull`` function will transfer the data from the GPU back to the host. It will be returned has a numpy array.

.. code-block:: python

    # pull gpu_image to the host
    arr = cle.pull(gpu_image)

The data type of the array will be the same as the data type of the image on the GPU.

Free memory
-----------

Because memory on the GPU can be limited, it can be interesting to free the memory when it is not needed anymore. In pyclesperanto you can free the memory similarly to python with the `del` keyword.

.. code-block:: python

    # free the memory of the image on the GPU
    del gpu_image

.. warning::

    The memory is not freed immediately, but is marked for deletion. The memory will be freed when the garbage collector will run, which in some rare cases can take some time.


Apply an operations on images
=============================

In pyclesperanto, most function are filter or mathematic operation on images. We tried to keep the API as simple as possible with a standard convention for all the functions.

.. code-block:: python

    cle.function_name(input, output, arg0, arg1, ...)

The `output` memory is part of the function signature because GPU cannot allocate memory by itself, you need to specify the output memory space in which it will write the result.
for example, to apply a filter such as a gaussian blur, you need to specify the following code:

.. code-block:: python

    # push an image to the GPU
    gpu_input = cle.push(cpu_image)
    # create an output of the same size of the input
    gpu_output = cle.create(cpu_image.shape)
    # apply a gaussian blur with sigma_x=2 and sigma_y=2
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    # pull back the result to the host memory
    result = cle.pull(gpu_output)

Eventhough it can be a bit tedious, this code provide a total control on the data and memory being processed.
Now, it is also possible to let pyclesperanto manage some of the memory operation, like the ``push`` and ``create`` of the input and output, making your code shorter.
However we will rely here on default behavior of the functions, which might not be the most efficient in term of memory usage in some cases.

.. code-block:: python

    # apply a gaussian blur directly on a numpy array and save the result in a pyclesperanto array
    gpu_output = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)
    # pull back the result to the host
    result = cle.pull(gpu_output)

Here, the ``cpu_image`` is pushed to the GPU and the output gpu space is created automatically when calling the operation ``gaussian_blur``. The function will return a ``pyclesperanto array``.
Memory transfert are still applied in the background, but the user does not have to worry about it.

Pipeline of operations
======================

Most operation in pyclesperanto are filters. This means that you can chain them together to create a pipeline of operations.
for example, to apply a gaussian blur followed by a threshold, you can write the following code:

.. code-block:: python

    # apply a gaussian blur
    gpu_input = cle.push(cpu_image)
    gpu_output = cle.create(cpu_image.shape)
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    blurred = cle.pull(gpu_output)

    # apply a threshold
    gpu_input = cle.push(blurred)
    gpu_output = cle.create(blurred.shape)
    cle.greater_constant(gpu_output, gpu_output, constant=0.5)
    binarized = cle.pull(gpu_output)

Although this code is correct, it is not optimal due to the ``push`` and ``pull`` in between the two operations. This is code is good for protoryping as it allows to inspect the result of each operation.
But in the final version of the code, it is better to chain the operations together to avoid the memory transfert (e.g. ``push`` and ``pull``).

.. code-block:: python

    # apply a gaussian blur
    gpu_blurred = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)
    # apply a threshold
    gpu_binarized = cle.greater_constant(gpu_blurred, constant=0.5)
    # read the output on host
    binarized = cle.pull(gpu_binarized)

Here we only use ``push`` at the beginning, inside the ``gaussian_blur`` operation, and ``pull`` at the end of the pipeline when we need to access the data from the CPU.
The ``create`` operation for output data are done automatically inside each operations.
