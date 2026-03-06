import inspect
from functools import wraps
from typing import Callable, Optional, get_args

from toolz import curry  # type: ignore

from ._array import Array, Image, is_image
from ._core import Device, get_device
from ._memory import push


@curry
def plugin_function(
    function: Callable,
    categories: Optional[list] = None,
) -> Callable:
    """Function decorator to ensure correct types and values of all parameters.

    The given input parameters are either of type OpenCL data/image/buffer (which the GPU
    understands) or are converted to this type (see push function). If output
    parameters of type Image are not set, an empty image is created and
    handed over.

    Parameters
    ----------
    function : callable
        The function to be executed on the GPU.
    categories : list of str, optional
        A list of category names the function is associated with

    Returns
    -------
    worker_function : callable
        The actual function call that will be executed, magically creating
        output arguments of the correct type.
    """

    sig = inspect.signature(function)  # cached once at decoration time

    @wraps(function)
    def worker_function(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # Single pass: find explicit Device arg and first image arg
        input_device = None
        input_image = None
        for value in bound.arguments.values():
            if input_device is None and isinstance(value, Device):
                input_device = value
            if input_image is None and is_image(value):
                input_image = value
            if input_device is not None and input_image is not None:
                break

        # Device resolution: explicit arg > image's device > global default
        input_image_device = getattr(input_image, "device", None)
        if not isinstance(input_image_device, Device):
            input_image_device = None
        use_device = input_device or input_image_device or get_device()

        # Push images to device, fill in missing device args
        for key, value in bound.arguments.items():
            param = sig.parameters[key]
            ann = param.annotation
            if is_image(value) and (ann is Image or Array in get_args(ann)):
                bound.arguments[key] = push(value, device=use_device)
            elif value is None and (ann is Device or Device in get_args(ann)):
                bound.arguments[key] = use_device

        return function(*bound.args, **bound.kwargs)

    worker_function.categories = categories
    worker_function.__module__ = "pyclesperanto"

    return worker_function
