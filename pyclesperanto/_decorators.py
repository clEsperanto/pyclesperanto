from typing import Callable
from functools import wraps
from toolz import curry
import inspect

from ._memory_operations import create_like, push
from ._image import Image, is_image
from ._device import Device, get_device


@curry
def plugin_function(
    function: Callable,
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

    Returns
    -------
    worker_function : callable
        The actual function call that will be executed, magically creating
        output arguments of the correct type.
    """

    @wraps(function)
    def worker_function(*args, **kwargs):
        sig = inspect.signature(function)
        # create mapping from position and keyword arguments to parameters
        # will raise a TypeError if the provided arguments do not match the signature
        # https://docs.python.org/3/library/inspect.html#inspect.Signature.bind
        bound = sig.bind(*args, **kwargs)
        # set default values for missing arguments
        # https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults
        bound.apply_defaults()

        # copy images to GPU, and create output array if necessary
        for key, value in bound.arguments.items():
            if (
                is_image(value)
                and key in sig.parameters
                and sig.parameters[key].annotation is Image
            ):
                bound.arguments[key] = push(value)
            if (
                key in sig.parameters
                and sig.parameters[key].annotation is Image
                and value is None
            ):
                sig2 = inspect.signature(create_like)
                bound.arguments[key] = create_like(
                    *bound.args[0 : len(sig2.parameters)]
                )

            if (
                key in sig.parameters
                and sig.parameters[key].annotation is Device
                and value is None
            ):
                sig2 = inspect.signature(get_device)
                bound.arguments[key] = get_device()

        # call the decorated function
        return function(*bound.args, **bound.kwargs)

    # this is necessary to obfuscate pyclesperanto's internal structure
    worker_function.__module__ = "pyclesperanto"

    return worker_function
