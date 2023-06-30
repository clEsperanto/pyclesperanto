from __future__ import annotations

from ._pyclesperanto import _Array

from typing import Tuple, Union
import numpy as np
import warnings

from ._types import DataType, MemoryType
from ._core import Device, get_device
from ._operators import Operators


class Array(_Array, Operators):
    def __init__(self, array: _Array) -> None:
        super().__init__(array)

    @classmethod
    def create(
        self,
        shape: Tuple[int, ...],
        dtype: type = None,
        mtype: MemoryType = None,
        device: Device = None,
    ) -> Array:
        if dtype is None:
            dtype = np.float32
        if mtype is None:
            mtype = MemoryType.buffer()
        if device is None:
            device = get_device()

        z, y, x = 1, 1, 1
        if len(shape) == 3:
            z, y, x = shape
        if len(shape) == 2:
            y, x = shape
        if len(shape) == 1:
            x = shape[0]
        return Array(
            super().create(x, y, z, DataType.get_cle_dtype(dtype), mtype.type, device)
        )

    def __str__(self) -> str:
        return self.get().__str__()

    def __repr__(self) -> str:
        repr_str = self.get().__repr__()
        extra_info = f"mtype={self.mtype.name}"
        return repr_str[:-1] + f", {extra_info})"

    @property
    def itemsize(self) -> int:
        return super().itemsize

    @property
    def size(self) -> int:
        return super().size

    @property
    def ndim(self) -> int:
        return super().ndim

    @property
    def shape(self) -> Tuple[int, ...]:
        return super().shape

    @property
    def dtype(self) -> type:
        return DataType.get_np_dtype(super().dtype)

    @property
    def mtype(self):
        return MemoryType(super().mtype)

    @property
    def device(self) -> Device:
        return super().device

    def set(self, array: np.ndarray) -> None:
        if array.dtype != self.dtype:
            warnings.warn(
                f"Array dtype mismatch. Casting array to '{self.dtype.__name__}' before set().",
                RuntimeWarning,
            )
            array = array.astype(self.dtype)
        if array.size != self.size:
            raise ValueError(
                f"Array size mismatch: {array.size} != {self.size} ({array.shape} != {self.shape})"
            )
        if array.ndim != self.ndim:
            raise ValueError(
                f"Array dimension mismatch: {array.ndim} != {self.ndim} ({array.shape} != {self.shape})"
            )
        if array.shape != self.shape:
            raise ValueError(f"Array shape mismatch: {array.shape} != {self.shape}")
        super().set(array)

    def get(self) -> np.ndarray:
        caster = {
            np.float32: super().get_float32(),
            np.int8: super().get_int8(),
            np.int16: super().get_int16(),
            np.int32: super().get_int32(),
            np.int64: super().get_int64(),
            np.uint8: super().get_uint8(),
            np.uint16: super().get_uint16(),
            np.uint32: super().get_uint32(),
            np.uint64: super().get_uint64(),
        }
        return caster[self.dtype]

    def fill(self, value: float) -> None:
        super().fill(value)


Image = Union[np.ndarray, Array]


def is_image(any_array):
    return (
        isinstance(any_array, np.ndarray)
        or isinstance(any_array, tuple)
        or isinstance(any_array, list)
        or isinstance(any_array, Array)
        or str(type(any_array))
        in [
            "<class 'cupy._core.core.ndarray'>",
            "<class 'dask.array.core.Array'>",
            "<class 'xarray.core.dataarray.DataArray'>",
        ]
    )
