# from __future__ import annotations

from ._pyclesperanto import _Array as Array
from . import _operators

from typing import Union
import numpy as np
import warnings


def __str__(self) -> str:
    return self.get().__str__()


def __repr__(self) -> str:
    repr_str = self.get().__repr__()
    extra_info = f"mtype={self.mtype}"
    return repr_str[:-1] + f", {extra_info})"


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
    self._write(array)
    return self


def get(self) -> np.ndarray:
    caster = {
        "float32": self._read_float32,
        "int8": self._read_int8,
        "int16": self._read_int16,
        "int32": self._read_int32,
        "int64": self._read_int64,
        "uint8": self._read_uint8,
        "uint16": self._read_uint16,
        "uint32": self._read_uint32,
        "uint64": self._read_uint64,
    }
    return caster[self.dtype.name]()


def __array__(self, dtype=None) -> np.ndarray:
    if dtype is None:
        return self.get()
    else:
        return self.get().astype(dtype)


# missing operators:
# __setitem__
# __getitem__
# __iter__
# __array_interface__

setattr(Array, "set", set)
setattr(Array, "get", get)
setattr(Array, "__str__", __str__)
setattr(Array, "__repr__", __repr__)
setattr(Array, "__array__", __array__)
setattr(Array, "astype", _operators.astype)
setattr(Array, "max", _operators.max)
setattr(Array, "min", _operators.min)
setattr(Array, "sum", _operators.sum)
setattr(Array, "__iadd__", _operators.__iadd__)
setattr(Array, "__sub__", _operators.__sub__)
setattr(Array, "__div__", _operators.__div__)
setattr(Array, "__truediv__", _operators.__truediv__)
setattr(Array, "__idiv__", _operators.__idiv__)
setattr(Array, "__itruediv__", _operators.__itruediv__)
setattr(Array, "__mul__", _operators.__mul__)
setattr(Array, "__imul__", _operators.__imul__)
setattr(Array, "__gt__", _operators.__gt__)
setattr(Array, "__ge__", _operators.__ge__)
setattr(Array, "__lt__", _operators.__lt__)
setattr(Array, "__le__", _operators.__le__)
setattr(Array, "__eq__", _operators.__eq__)
setattr(Array, "__ne__", _operators.__ne__)
setattr(Array, "__pow__", _operators.__pow__)
setattr(Array, "__ipow__", _operators.__ipow__)
setattr(Array, "_plt_to_png", _operators._plt_to_png)
setattr(Array, "_png_to_html", _operators._png_to_html)
setattr(Array, "_repr_html_", _operators._repr_html_)

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
