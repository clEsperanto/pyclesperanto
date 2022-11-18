from __future__ import annotations

from typing import Union
import numpy as np

from ._pyclesperanto import _cleImage
from ._pyclesperanto import _cleMemType, _cleDataType
from ._image_operators import ImageOperators
from ._device import Device

dType = _cleDataType
mType = _cleMemType


class cleImage(_cleImage, ImageOperators):
    """cleImage

    GPU hosted image class

    Parameters
    ----------
    _cleImage : C++ wrapper class
        C++ OpenCL Image class running behind cleImage accessible using `super()`
    """

    def __init__(self, image: _cleImage) -> None:
        super().__init__(image)

    @property
    def device(self) -> Device:
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
        return super().SizeInBytes()

    @property
    def size(self) -> int:
        return super().Size()

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
