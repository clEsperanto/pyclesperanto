from typing import Callable, Optional
from functools import wraps
from toolz import curry
import inspect

from ._memory import push
from ._array import is_image, Image
from ._core import Device


@curry
def plugin_function(
    function: Callable,
    category: Optional[list] = None,
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
    category : list of str, optional
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
    function.category = category
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

        args_list = function.fullargspec.args
        index = next(
            (i for i, element in enumerate(args_list) if "input_image" in element), -1
        )
        arg_name = args_list[index]

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
                and sig.parameters[key].annotation is Device
                and value is None
            ):
                input_image = bound.arguments[arg_name]
                bound.arguments[key] = input_image.device

        # call the decorated function
        result = function(*bound.args, **bound.kwargs)

        # # Cast the result as an Array if it is not already
        # if not isinstance(result, _Array):
        #     result = _Array(result)

        return result

    # this is necessary to obfuscate pyclesperanto's internal structure
    worker_function.__module__ = "pyclesperanto"

    return worker_function
