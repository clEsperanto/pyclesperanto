from typing import Callable, Optional
from functools import wraps
from toolz import curry
import inspect

from ._memory_operations import create_like, push
from ._image import Image, is_image
from ._device import Device, get_device


@curry
def plugin_function(
    function: Callable,
    output_creator: Callable = create_like,
    # device_selector: Callable = get_device,
    categories: Optional[list] = None,
    priority: int = 0,
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
    priority : int, optional
        can be used in lists of multiple operations to differentiate multiple operations that fulfill the same purpose
        but better/faster/more general.

    Returns
    -------
    worker_function : callable
        The actual function call that will be executed, magically creating
        output arguments of the correct type.
    """

    function.fullargspec = inspect.getfullargspec(function)
    function.categories = categories
    function.priority = priority

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
                sig2 = inspect.signature(output_creator)
                # bound.arguments[key] = output_creator(
                #     *bound.args[0 : len(sig2.parameters)]
                # )
                input_image_index = function.fullargspec.args.index("input_image")
                bound.arguments[key] = output_creator(
                    bound.args[input_image_index]
                )
            if (
                key in sig.parameters
                and sig.parameters[key].annotation is Device
                and value is None
            ):
                input_image = bound.arguments["input_image"]
                bound.arguments[key] = input_image.device
                # sig2 = inspect.signature(device_selector)
                # bound.arguments[key] = device_selector()

        # call the decorated function
        return function(*bound.args, **bound.kwargs)

    # this is necessary to obfuscate pyclesperanto's internal structure
    worker_function.__module__ = "pyclesperanto"

    return worker_function
