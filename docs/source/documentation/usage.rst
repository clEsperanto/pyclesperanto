Usage
#####

pyClesperanto is a GPU-accelerated image processing library for Python. To get started, import the library:

.. code-block:: python

    import pyclesperanto as cle

.. warning::

    If you encounter an error at this stage, it is likely that the OpenCL driver is not installed or that you do not have an OpenCL-compatible device.
    Please check the installation of OpenCL and drivers, as well as the compatibility of your system devices with OpenCL.

Next, you can explore the devices available on your computer using the `list_available_devices()` function or get more detailed information with the `info()` function:

.. code-block:: python

    # Return the name of all available devices on the computer
    print(cle.list_available_devices())

    # Return the name, index, and information on all the devices
    print(cle.info())


To work on a specific device, you need to select it.
By default, the last device found will be automatically selected for convenience at import time.
You can check which device you are currently working on with the `get_device()` function, and select another one using the `select_device()` function:

.. code-block:: python

    # Query the current device
    print(cle.get_device())

    # Select a device by name, substring, or index
    cle.select_device("NVIDIA RTX 4090") # full name
    cle.select_device("TX")              # substring
    cle.select_device(0)                 # device index



Memory transfer
===============

GPU devices have their own memory, which is separate from the computer's memory. Therefore, you need to transfer your data to the device memory to process it and back to the computer memory to read the results.
This is commonly known as `copy from host to device` and `copy from device to host`. In pyclesperanto, we use the functions `push`, `pull`, and `create` to manage memory transfer:

- `push` is used to transfer/copy data from the host to the device.
- `pull` is used to transfer/copy data from the device to the host.
- `create` is used to allocate empty space on the device, which will be used, for example, to store a result.

These copy operations are costly in terms of time as they scale with the data size. Therefore, it is good practice to avoid them as much as possible once you are optimizing your code.

Create
------

As there is no data transfer, we only need to specify the size of the image we want to create. The image will be created on the GPU and will be empty.
The size of the image is specified as a tuple of integers following the numpy convention ``zyx``.

.. code-block:: python

    # Create an empty image on the GPU of size 100x100
    gpu_image = cle.create((100, 100))

By default, this will create a 32-bit float space. You can specify the type of the image by passing a ``dtype`` argument:

.. code-block:: python

    # Create an empty image on the GPU of size 100x100 with uint8 data type
    gpu_image = cle.create((100, 100), dtype=np.uint8)

It is also possible to use another image as a template to create the new image. This will copy the size and the data type of the template image.

.. code-block:: python

    # Create an empty image on the GPU with the same size and data type as the template image
    gpu_image = cle.create_like(template_image)


Push
----

The ``push`` function will create a memory space on the GPU like ``create`` and then transfer the data array from the host to this new memory space on the device.
The data array is expected to be a numpy array or share the same interface as a numpy array (e.g., dask array).

.. code-block:: python

    arr = np.random.random((100, 100)).astype(np.float32)
    # Push arr to the GPU
    gpu_image = cle.push(arr)

The data pushed will keep the same data type as the array. Hence, if you push a ``uint8`` array, the data will be stored as ``uint8`` on the GPU.
The array will then use 4 times less memory than if it was stored as ``float32``. This is a good practice to keep in mind when working with GPUs as their memory can be limited.

.. warning::

    pyclesperanto does not support `64-bit` data types such as `int64` or `float64`, which are the default data types in Python. This is to ensure full compatibility with most GPU devices.
    Hence, precision might be lost when converting the data type to `32-bit`.

Pull
----

The ``pull`` function transfers data from the GPU back to the host. It will be returned as a numpy array.

.. code-block:: python

    # Pull gpu_image to the host
    arr = cle.pull(gpu_image)

The data type of the array will be the same as the data type of the image on the GPU.

Free memory
-----------

Because memory on the GPU can be limited, it is beneficial to free memory when it is no longer needed. In pyclesperanto, you can free memory similarly to Python using the `del` keyword.

.. code-block:: python

    # Free the memory of the image on the GPU
    del gpu_image


Apply operations on images
==========================

In pyclesperanto, most functions are filters or mathematical operations on images. We tried to keep the API as simple as possible with a standard convention for all the functions.

.. code-block:: python

    cle.function_name(input, output, arg0, arg1, ...)

The `output` memory is part of the function signature because the GPU cannot allocate memory by itself; you need to specify the output memory space in which it will write the result.
For example, to apply a filter such as a Gaussian blur, you need to specify the following code:

.. code-block:: python

    # Push an image to the GPU
    gpu_input = cle.push(cpu_image)
    # Create an output of the same size as the input
    gpu_output = cle.create(cpu_image.shape)
    # Apply a Gaussian blur with sigma_x=2 and sigma_y=2
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    # Pull back the result to the host memory
    result = cle.pull(gpu_output)

Even though it can be a bit tedious, this code provides total control over the data and memory being processed.
Now, it is also possible to let pyclesperanto manage some of the memory operations, like the ``push`` and ``create`` of the input and output, making your code shorter.
However, we will rely here on the default behavior of the functions, which might not be the most efficient in terms of memory usage in some cases.

.. code-block:: python

    # Apply a Gaussian blur directly on a numpy array and save the result in a pyclesperanto array
    gpu_output = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)
    # Pull back the result to the host
    result = cle.pull(gpu_output)

Here, the ``cpu_image`` is pushed to the GPU and the output GPU space is created automatically when calling the operation ``gaussian_blur``. The function will return a ``pyclesperanto array``.
Memory transfers are still applied in the background, but the user does not have to worry about it.

Pipeline of operations
======================

Most operations in pyclesperanto are filters. This means that you can chain them together to create a pipeline of operations.
For example, to apply a Gaussian blur followed by a threshold, you can write the following code:

.. code-block:: python

    # Apply a Gaussian blur
    gpu_input = cle.push(cpu_image)
    gpu_output = cle.create(cpu_image.shape)
    cle.gaussian_blur(gpu_input, gpu_output, sigma_x=2, sigma_y=2)
    blurred = cle.pull(gpu_output)

    # Apply a threshold
    gpu_input = cle.push(blurred)
    gpu_output = cle.create(blurred.shape)
    cle.greater_constant(gpu_output, gpu_output, constant=0.5)
    binarized = cle.pull(gpu_output)

Although this code is correct, it is not optimal due to the ``push`` and ``pull`` in between the two operations. This code is good for prototyping as it allows you to inspect the result of each operation.
But in the final version of the code, it is better to chain the operations together to avoid the memory transfers (e.g., ``push`` and ``pull``).

.. code-block:: python

    # Apply a Gaussian blur
    gpu_blurred = cle.gaussian_blur(cpu_image, sigma_x=2, sigma_y=2)
    # Apply a threshold
    gpu_binarized = cle.greater_constant(gpu_blurred, constant=0.5)
    # Read the output on host
    binarized = cle.pull(gpu_binarized)

Here we only use ``push`` at the beginning, inside the ``gaussian_blur`` operation, and ``pull`` at the end of the pipeline when we need to access the data from the CPU.
The ``create`` operation for output data is done automatically inside each operation.
