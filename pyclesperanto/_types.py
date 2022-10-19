from __future__ import annotations

import inspect
import numpy as np
from typing import Union, Callable
from functools import wraps
from toolz import curry

from ._pyclesperanto import _cleImage
from ._pyclesperanto import _cleMemType, _cleDataType

mType = _cleMemType
dType = _cleDataType


class cleImage(_cleImage):
    def __init__(self) -> None:
        super().__init__()

    def __init__(self, image: _cleImage) -> None:
        super().__init__(image)

    @property
    def device(self):
        return super().GetDevice()

    @property
    def ndim(self) -> int:
        return super().Ndim()

    @property
    def dtype(self) -> dType:
        return super().GetDataType()

    @property
    def mtype(self) -> mType:
        return super().GetMemoryType()

    @property
    def shape(self) -> tuple:
        return super().Shape()

    @property
    def nbytes(self) -> int:
        return super().GetSize()

    @property
    def size(self) -> int:
        return super().size()

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

    def __len__(self) -> int:
        return super().__len__()

    def fill(self, value: float | int) -> None:
        """fill memory with value"""
        super().Fill(value)

    def copy_to(self, image: cleImage) -> None:
        """copy memory in an other image"""
        super().CopyDataTo(image)

    def absolute(self) -> cleImage:
        from ._pyclesperanto import _AbsoluteKernel_Call as op
        from ._pyclesperanto import _Create

        output = cleImage(_Create(self.device, self.shape, self.mtype))
        op(self.device, self, output)
        return output


Image = Union[np.ndarray, cleImage]


def is_image(any_array):
    return (
        isinstance(any_array, np.ndarray)
        or isinstance(any_array, tuple)
        or isinstance(any_array, list)
        or isinstance(any_array, cleImage)
        or str(type(any_array))
        in [
            "<class 'cupy._core.core.ndarray'>",
            "<class 'dask.array.core.Array'>",
            "<class 'xarray.core.dataarray.DataArray'>",
        ]
    )


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

        myself = args[0]

        # copy images to GPU, and create output array if necessary
        for key, value in bound.arguments.items():
            if (
                is_image(value)
                and key in sig.parameters
                and sig.parameters[key].annotation is Image
            ):
                bound.arguments[key] = myself.push(value)
            if (
                key in sig.parameters
                and sig.parameters[key].annotation is Image
                and value is None
            ):
                sig2 = inspect.signature(myself.create_like)
                bound.arguments[key] = myself.create_like(
                    *bound.args[1 : len(sig2.parameters) + 1]
                )

        # call the decorated function
        return function(*bound.args, **bound.kwargs)

    # this is necessary to obfuscate pyclesperanto's internal structure
    worker_function.__module__ = "pyclesperanto"

    return worker_function
