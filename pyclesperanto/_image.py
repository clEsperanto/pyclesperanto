from __future__ import annotations

from typing import Union
import numpy as np

from ._pyclesperanto import _cleImage
from ._image_operators import ImageOperators
from ._device import Device
from ._types import MemoryType, DataType

class cleImage(_cleImage, ImageOperators):
    """cleImage

    GPU hosted image class

    Parameters
    ----------
    _cleImage : C++ wrapper class
        C++ OpenCL Image class running behind cleImage accessible using `super()`
    """

    def __init__(self, image: _cleImage):
        super().__init__(image)
    
    @property
    def device(self) -> Device:
        return super().GetDevice()

    @property
    def ndim(self) -> int:
        return super().Ndim()

    @property
    def dtype(self) -> type:
        return DataType(super().GetDataType()).type

    @property
    def mtype(self) -> MemoryType:
        return MemoryType(super().GetMemoryType())

    @property
    def shape(self) -> tuple:
        shape_dict = {  # type: ignore
            1: (super().Shape()[2],),
            2: (super().Shape()[1], super().Shape()[2]),
            3: (super().Shape()[0], super().Shape()[1], super().Shape()[2]),
        }
        return shape_dict[self.ndim]

    @property
    def nbytes(self) -> int:
        return super().BytesSize()

    @property
    def size(self) -> int:
        return super().Size()
    
    def get(self) -> np.ndarray:
        from ._memory_operations import pull
        return np.asarray(pull(self))
    
    def __array__(self, dtype=None) -> np.ndarray:
        if dtype is None:
            return self.get()
        else:
            return self.get().astype(dtype)

    def __str__(self) -> str:
        return str(self.get())

    def __repr__(self) -> str:
        return f"cleImage({self.get()}, dtype={self.dtype}, mtype={self.mtype})"

    def __len__(self) -> int:
        return super().__len__()

    def fill(self, value: float | int) -> None:
        """Fill memory with value

        Parameters
        ----------
        value : float | int
            Value to fill memory with
        """
        super().Fill(value)

    def copy_to(self, image: cleImage) -> None:
        """Copy image data to an other image

        Parameters
        ----------
        image : cleImage
            Image to copy data to
            Must be of the same shape and data type, and on the same device
        """
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
