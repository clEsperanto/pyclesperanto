import re
from os import path
from pathlib import Path
from typing import Callable, Optional, Union

import numpy as np

from ._array import Array, Image, to_device
from ._core import Device, get_device
from ._memory import create, pull, push
from ._pyclesperanto import _evaluate, _execute, _native_execute


def execute(
    anchor=None,
    kernel_source: str = "",
    kernel_name: str = "",
    global_size: tuple = (1, 1, 1),
    local_size: tuple = (0, 0, 0),
    parameters: dict = {},
    constants: dict = {},
    device: Device = None,
):
    """Execute a kernel from a file or a string

    Call, build, and execute a kernel compatible with CLIj framework.
    The kernel can be called from a file or a string.

    Parameters
    ----------
    anchor : str, default = 'None'
        Use __file__ when calling this method and the corresponding open.cl
        file lies in the same folder as the python file calling it.
        Ignored if kernel_source is a string.
    kernel_source : str
        Filename of the open.cl file to be called, or string containing the open.cl source code
    kernel_name : str
        Kernel method inside the open.cl file to be called
        most clij/clesperanto kernel functions have the same name as the file they are in
    global_size : tuple (z,y,x), default = (1, 1, 1)
        Global_size according to OpenCL definition (usually shape of the destination image).
    parameters : dict(str, [Array, float, int])
        Dictionary containing parameters. Take care: They must be of the
        right type and in the right order as specified in the open.cl file.
    constants: dict(str, int), optional
        Dictionary with names/values which will be added to the define
        statements. They are necessary, e.g. to create arrays of a given
        maximum size in OpenCL as variable array lengths are not supported.
    device : Device, default = None
        The device to execute the kernel on. If None, use the current device
    """

    # load the kernel file
    def load_file(anchor, filename):
        """Load the opencl kernel file as a string"""
        if anchor is None:
            kernel = Path(filename).read_text()
        else:
            kernel = (Path(anchor).parent / filename).read_text()
        return kernel

    # test if kernel_source ends with .cl or .cu
    if kernel_source.endswith(".cl") or kernel_source.endswith(".cu"):
        kernel_source = load_file(anchor, kernel_source)

    # manage the device if not given
    if not device:
        device = get_device()

    # manage global range
    if not isinstance(global_size, tuple):
        if isinstance(global_size, list) or isinstance(global_size, np.ndarray):
            global_size = tuple(global_size)
        else:
            global_size = (global_size,)

    # manage local range
    if not isinstance(local_size, tuple):
        if isinstance(local_size, list) or isinstance(local_size, np.ndarray):
            local_size = tuple(local_size)
        else:
            local_size = (local_size,)

    _execute(
        device,
        kernel_name,
        kernel_source,
        parameters,
        global_size,
        local_size,
        constants,
    )


def native_execute(
    anchor=None,
    kernel_source: str = "",
    kernel_name: str = "",
    global_size: tuple = (1, 1, 1),
    local_size: tuple = (0, 0, 0),
    parameters: dict = {},
    device: Device = None,
):
    """Execute an OpenCL kernel from a file or a string

    Call, build, and execute a kernel compatible with OpenCL language.
    The kernel can be called from a file or a string.

    The parameters must still be passed as a dictionary with the correct types and order.
    Buffer parameters must be passed as Array objects. Scalars must be passed as Python native float or int.

    Warning: Only 1D buffers are supported for now.

    Parameters
    ----------
    anchor : str, default = '__file__'
        Enter __file__ when calling this method and the corresponding open.cl
        file lies in the same folder as the python file calling it.
        Ignored if kernel_source is a string.
    kernel_source : str
        Filename of the open.cl file to be called or string containing the open.cl source code
    kernel_name : str
        Kernel method inside the open.cl file to be called
        most clij/clesperanto kernel functions have the same name as the file they are in
    global_size : tuple (z,y,x), default = (1, 1, 1)
        Global_size according to OpenCL definition (usually shape of the destination image).
    local_size : tuple (z,y,x), default = (1, 1, 1)
        Local_size according to OpenCL definition (usually default is good).
    parameters : dict(str, [Array, float, int])
        Dictionary containing parameters. Take care: They must be of the
        right type and in the right order as specified in the open.cl file.
    device : Device, default = None
        The device to execute the kernel on. If None, use the current device
    """

    # load the kernel file
    def load_file(anchor, filename):
        """Load the opencl kernel file as a string"""
        if anchor is None:
            kernel = Path(filename).read_text()
        else:
            kernel = (Path(anchor).parent / filename).read_text()
        return kernel

    # test if kernel_source ends with .cl or .cu
    if kernel_source.endswith(".cl") or kernel_source.endswith(".cu"):
        kernel_source = load_file(anchor, kernel_source)

    # manage the device if not given
    if not device:
        device = get_device()

    # manage global range
    if not isinstance(global_size, tuple):
        if isinstance(global_size, list) or isinstance(global_size, np.ndarray):
            global_size = tuple(global_size)
        else:
            global_size = (global_size,)

    # manage local range
    if not isinstance(local_size, tuple):
        if isinstance(local_size, list) or isinstance(local_size, np.ndarray):
            local_size = tuple(local_size)
        else:
            local_size = (local_size,)

    _native_execute(
        device, kernel_name, kernel_source, parameters, global_size, local_size
    )


def evaluate(
    expression: str,
    parameters: dict
) -> Array:
    """Evaluate an arithmetic expression on the GPU. The expression can contain parameters which must be passed as a dictionary.
    The expression will only process element-wise operations.

    Example:
    --------
    result = evaluate("a + b * c", parameters={"a": array_a, "b": array_b, "c": 2.0})
    result = evaluate("a > pow(b,3)", parameters={"a": array_a, "b": array_b})

    Parameters
    ----------
    expression : str
        The arithmetic expression to be evaluated. It can contain parameters which must be passed as a dictionary.
    parameters : dict(str, [Array, float, int])
        Dictionary containing parameters. Take care: They must be of the
        right type and in the right order as specified in the expression.
        Buffer parameters must be passed as Array objects. Scalars must be passed as Python native float or int.
    Returns
    -------
    Array
        The result of the expression evaluation as an Array object.
    """

    # get the device from the first Array parameter, if any else use get_device()
    device = None
    for value in parameters.values():
        if isinstance(value, Array):
            device = value.device
            break
    if device is None:
        device = get_device()

    # convert all numpy arrays in parameters to Array objects
    for key, value in parameters.items():
        if isinstance(value, np.ndarray):
            parameters[key] = push(value, device=device)

    # check that all Array parameters have the same shape and get the shape
    out_shape = None
    for value in parameters.values():
        if isinstance(value, Array):
            if out_shape is None:
                out_shape = value.shape
            elif out_shape != value.shape:
                raise ValueError("All Array parameters must have the same shape")

    # Default to (1, 1) shape if no Array parameters found (all scalar)
    if out_shape is None:
        out_shape = (1, 1)

    out = create(out_shape, dtype=np.float32, device=device)
    _evaluate(device=device, expression=expression, parameters=parameters, output=out)
    return out
