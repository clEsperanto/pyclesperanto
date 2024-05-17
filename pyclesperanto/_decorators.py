import inspect
from functools import wraps
from typing import Any, Callable, List, Optional

from toolz import curry

from ._array import Image, is_image
from ._core import Device
from ._memory import push


class CallableFunction:
    """A class representing a callable function."""

    def __call__(self, *args, **kwargs):
        pass


class PluginFunction(CallableFunction):
    """A class representing a plugin function."""

    def __init__(
        self,
        function: Callable[..., Any],
        category: Optional[List] = None,
    ):
        self.function = function
        self.fullargspec = inspect.getfullargspec(function)
        self.category = category

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


@curry
def plugin_function(
    function: PluginFunction,
    category: Optional[List] = None,
) -> Callable:
    """A decorator for kernels functions.

    The decorator allocate a device if None is provided, and push the input image to the device
    if it is not already there.
    This function can be extended to support more functionalities in the future if we need to automatised
    more behaviours on the kernels calls.

    Parameters
    ----------
    function : Callable[..., Any]
        The function to be decorated.
    category : Optional[List], optional
        The category of the function, by default None.

    Returns
    -------
    Callable
        The decorated function.
    """
    function = PluginFunction(function, category)

    @wraps(function.function)
    def worker_function(*args, **kwargs):
        sig = inspect.signature(function.function)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        arg_name = get_input_image_arg_name(function)
        process_arguments(function, bound, arg_name)

        result = function.function(*bound.args, **bound.kwargs)

        return result

    worker_function.__module__ = "pyclesperanto"

    return worker_function


def get_input_image_arg_name(function: PluginFunction) -> str:
    """Get the name of the input image argument."""
    args_list = function.fullargspec.args
    index = next(
        (i for i, element in enumerate(args_list) if "input_image" in element), -1
    )
    if index == -1:
        raise NotImplementedError(
            f"Wrong usage of decorator for the function {function.function.__name__}"
        )
    return args_list[index]


def process_arguments(
    function: PluginFunction, bound: inspect.BoundArguments, input_image_arg_name: str
):
    sig = inspect.signature(function.function)
    for key, value in bound.arguments.items():
        if (
            is_image(value)
            and key in sig.parameters
            and sig.parameters[key].annotation is Image
        ):
            bound.arguments[key] = push(value)
        if (
            key in sig.parameters
            and sig.parameters[key].annotation is Optional[Device]
            and value is None
        ):
            input_image = bound.arguments[input_image_arg_name]
            bound.arguments[key] = input_image.device
