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
    output_creator : callable, optional
        A function to create an output cleImage given an input cleImage. By
        default, we create output images of the same shape and type as input
        images.
    device_selector : callable, optional
        A function to select a device. By default, we use the current device instance.
    categories : list of str, optional
        A list of category names the function is associated with

    Returns
    -------
    worker_function : callable
        The actual function call that will be executed, magically creating
        output arguments of the correct type.
    """

    # function.fullargspec = inspect.getfullargspec(function)
    function.categories = categories
    # function.priority = priority

    @wraps(function)
    def worker_function(*args, **kwargs):
        sig = inspect.signature(function)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        # Get the device to use from the arguments or the input image or the current device
        input_device = next(
            (value for value in bound.arguments.values() if isinstance(value, Device)),
            None,
        )
        input_image = next(
            (value for value in bound.arguments.values() if is_image(value)), None
        )
        input_image_device = (
            getattr(input_image, "device", None) if input_image is not None else None
        )

        # if device is `cpu` or a string, set it to None
        if input_image_device == "cpu":
            input_image_device = None

        # Use input_device if available, else use the device of the input_image if it has the attribute device, else None
        use_device = input_device or input_image_device or get_device()

        # loop on all argument and if it is an image, push it to the device
        # if it is a device, set it to the use_device
        # if it is any other argument, do nothing
        for key, value in bound.arguments.items():
            if (
                is_image(value)
                and key in sig.parameters
                and (
                    sig.parameters[key].annotation is Image
                    or Array in get_args(sig.parameters[key].annotation)
                )
            ):
                bound.arguments[key] = push(value, device=use_device)
            if (
                key in sig.parameters
                and (
                    sig.parameters[key].annotation is Device
                    or Device in get_args(sig.parameters[key].annotation)
                )
                and value is None
            ):
                bound.arguments[key] = use_device

        # call the decorated function
        result = function(*bound.args, **bound.kwargs)

        return result

    worker_function.__module__ = "pyclesperanto"

    return worker_function
