import inspect
from pathlib import Path

import numpy as np

from ._array import Array
from ._backend import _get_backend
from ._core import Device, get_device
from ._memory import create, push


def _resolve_kernel_path(kernel_source, anchor=None):
    """Resolve kernel source to either a file path or kernel code string.

    Returns the kernel code as a string. If kernel_source is a file path (.cl or .cu),
    loads and returns the file contents. Otherwise, returns kernel_source unchanged.

    Parameters
    ----------
    kernel_source : str
        Either a filename (*.cl or *.cu) or a string containing kernel code
    anchor : str, optional
        Path to a module file (__file__) used to resolve relative kernel paths.
        If provided, kernel files are resolved relative to anchor's directory.
        If not provided and kernel_source is a file, it's resolved relative to
        the caller's module directory.

    Returns
    -------
    str
        The kernel code as a string

    Raises
    ------
    FileNotFoundError
        If the kernel file cannot be found at the resolved path
    """
    if not (kernel_source.endswith(".cl") or kernel_source.endswith(".cu")):
        return kernel_source

    if anchor is not None:
        kernel_path = Path(anchor).parent / kernel_source
    else:
        caller_frame = inspect.currentframe().f_back
        caller_file = inspect.getfile(caller_frame)
        kernel_path = Path(caller_file).parent / kernel_source

    return kernel_path.read_text()


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
    anchor : str, default = None
        Path to a module file (__file__) used to resolve relative kernel paths.
        If provided, kernel files are resolved relative to anchor's directory.
        If not provided and kernel_source is a file, it's resolved relative to
        the caller's module directory. Ignored if kernel_source is a string.
    kernel_source : str
        Filename of the open.cl file to be called, or string containing the open.cl source code
    kernel_name : str
        Kernel method inside the open.cl file to be called
        most clij/clesperanto kernel functions have the same name as the file they are in
    global_size : tuple (z,y,x), default = (1, 1, 1)
        Global_size according to OpenCL definition (usually shape of the destination image).
    local_size : tuple (z,y,x), default = (0, 0, 0)
        Local_size according to OpenCL definition.
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

    kernel_source = _resolve_kernel_path(kernel_source, anchor)

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

    _get_backend()._execute(
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
    anchor : str, default = None
        Path to a module file (__file__) used to resolve relative kernel paths.
        If provided, kernel files are resolved relative to anchor's directory.
        If not provided and kernel_source is a file, it's resolved relative to
        the caller's module directory. Ignored if kernel_source is a string.
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

    kernel_source = _resolve_kernel_path(kernel_source, anchor)

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

    _get_backend()._native_execute(
        device, kernel_name, kernel_source, parameters, global_size, local_size
    )


def evaluate(expression: str, parameters: dict) -> Array:
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

    # derive the output shape from all Array parameters, allowing per-axis
    # broadcasting (e.g. shape (1, 3) with (4, 3)); the backend performs the
    # actual broadcast device-side. Incompatible shapes raise ValueError.
    shapes = [value.shape for value in parameters.values() if isinstance(value, Array)]
    out_shape = np.broadcast_shapes(*shapes) if shapes else (1, 1)

    out = create(out_shape, dtype=np.float32, device=device)
    _get_backend()._evaluate(
        device=device, expression=expression, parameters=parameters, output=out
    )
    return out
