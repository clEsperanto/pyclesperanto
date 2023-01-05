from __future__ import annotations

from typing import Union
import numpy as np

from ._pyclesperanto import _cleImage
from ._pyclesperanto import _cleMemType, _cleDataType
from ._image_operators import ImageOperators
from ._device import Device

DataType = _cleDataType
MemoryType = _cleMemType


class cleImage(_cleImage, ImageOperators):
    """cleImage

    GPU hosted image class

    Parameters
    ----------
    _cleImage : C++ wrapper class
        C++ OpenCL Image class running behind cleImage accessible using `super()`
    """

    _data_type_dict = {  # type: ignore
        DataType.uint8: np.uint8,
        DataType.uint16: np.uint16,
        DataType.uint32: np.uint32,
        DataType.uint64: np.uint64,
        DataType.int8: np.int8,
        DataType.int16: np.int16,
        DataType.int32: np.int32,
        DataType.int64: np.int64,
        DataType.float32: np.float32,
    }

    def __init__(self, image: _cleImage) -> None:
        super().__init__(image)

    @property
    def device(self) -> Device:
        return super().GetDevice()

    @property
    def ndim(self) -> int:
        return super().Ndim()

    @property
    def dtype(self) -> type:
        return self._data_type_dict[super().GetDataType()]

    @property
    def mtype(self) -> MemoryType:
        return super().GetMemoryType()

    @property
    def shape(self) -> tuple:
        if self.ndim == 1:
            return (super().Shape()[2],)
        elif self.ndim == 2:
            return (super().Shape()[1], super().Shape()[2])
        elif self.ndim == 3:
            return (super().Shape()[0], super().Shape()[1], super().Shape()[2])

    @property
    def nbytes(self) -> int:
        return super().BytesSize()

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
