from __future__ import annotations

from ._pyclesperanto import _Array
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

setattr(_Array, "set", set)
setattr(_Array, "get", get)
setattr(_Array, "__str__", __str__)
setattr(_Array, "__repr__", __repr__)
setattr(_Array, "__array__", __array__)
setattr(_Array,"astype",_operators.astype)
setattr(_Array,"max",_operators.max)
setattr(_Array,"min",_operators.min)
setattr(_Array,"sum",_operators.sum)
setattr(_Array,"__iadd__",_operators.__iadd__)
setattr(_Array,"__sub__",_operators.__sub__)
setattr(_Array,"__div__",_operators.__div__)
setattr(_Array,"__truediv__",_operators.__truediv__)
setattr(_Array,"__idiv__",_operators.__idiv__)
setattr(_Array,"__itruediv__",_operators.__itruediv__)
setattr(_Array,"__mul__",_operators.__mul__)
setattr(_Array,"__imul__",_operators.__imul__)
setattr(_Array,"__gt__",_operators.__gt__)
setattr(_Array,"__ge__",_operators.__ge__)
setattr(_Array,"__lt__",_operators.__lt__)
setattr(_Array,"__le__",_operators.__le__)
setattr(_Array,"__eq__",_operators.__eq__)
setattr(_Array,"__ne__",_operators.__ne__)
setattr(_Array,"__pow__",_operators.__pow__)
setattr(_Array,"__ipow__",_operators.__ipow__)
setattr(_Array,"_plt_to_png",_operators._plt_to_png)
setattr(_Array,"_png_to_html",_operators._png_to_html)
setattr(_Array,"_repr_html_",_operators._repr_html_)

Image = Union[np.ndarray, _Array]

def is_image(any_array):
    return (
        isinstance(any_array, np.ndarray)
        or isinstance(any_array, tuple)
        or isinstance(any_array, list)
        or isinstance(any_array, _Array)
        or str(type(any_array))
        in [
            "<class 'cupy._core.core.ndarray'>",
            "<class 'dask.array.core.Array'>",
            "<class 'xarray.core.dataarray.DataArray'>",
        ]
    )
