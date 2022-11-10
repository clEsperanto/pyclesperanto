from __future__ import annotations

from typing import Union
import numpy as np

from ._pyclesperanto import _cleImage
from ._pyclesperanto import _cleMemType, _cleDataType
from ._image_operators import ImageOperators

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
        if self.ndim == 3:
            return super().Shape()[-3:]
        elif self.ndim == 2:
            return super().Shape()[-2:]
        elif self.ndim == 1:
            return super().Shape()[-1]

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
