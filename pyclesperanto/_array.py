# from __future__ import annotations

from ._pyclesperanto import _Array as Array
from ._core import Device, get_device
from . import _operators
from ._utils import assert_supported_dtype

from typing import Union
import numpy as np
import warnings


def __str__(self) -> str:
    return self.get().__str__()


def __repr__(self) -> str:
    repr_str = self.get().__repr__()
    extra_info = f"mtype={self.mtype}"
    return repr_str[:-1] + f", {extra_info})"


def set(self, array: np.ndarray, origin: tuple = None, region: tuple = None) -> None:
    # for cast array to numpy array
    if not isinstance(array, np.ndarray):
        array = np.array(array)
    if array.dtype != self.dtype:
        array = array.astype(self.dtype)

    if region and array.size != np.prod(region):
        raise ValueError(
            f"Value size mismatch the targeted region: {array.size} != {np.prod(region)} ({array.shape} != {tuple(np.squeeze(region))})"
        )
    self._write(array, origin, region)
    return self


def get(self, origin: tuple = None, region: tuple = None) -> np.ndarray:
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
    return caster[self.dtype.name](origin, region)


def __array__(self, dtype=None) -> np.ndarray:
    if dtype is None:
        return self.get()
    else:
        return self.get().astype(dtype)


def to_device(cls, arr, *args, **kwargs):
    if isinstance(arr, Array):
        return arr
    mtype = kwargs.get("mtype", "buffer")
    device = kwargs.get("device", get_device())
    return cls.create(arr.shape, arr.dtype, mtype, device).set(arr)


def from_array(cls, arr, *args, **kwargs):
    assert_supported_dtype(arr.dtype)
    return cls.to_device(arr, *args, **kwargs)


def empty(cls, shape, dtype=np.float32, *args, **kwargs):
    assert_supported_dtype(dtype)
    mtype = kwargs.get("mtype", "buffer")
    device = kwargs.get("device", get_device())
    return cls.create(shape, dtype, mtype, device)


def empty_like(cls, arr):
    assert_supported_dtype(arr.dtype)
    return Array.create(arr.shape, arr.dtype, arr.mtype, arr.device)


def zeros(cls, shape, dtype=np.float32, *args, **kwargs):
    assert_supported_dtype(dtype)
    new_array = cls.empty(shape, dtype, *args, **kwargs)
    new_array.fill(0)
    return new_array


def zeros_like(cls, arr):
    assert_supported_dtype(arr.dtype)
    return cls.zeros(arr.shape, arr.dtype, mtype=arr.mtype, device=arr.device)


def T(self):
    from ._tier1 import transpose_xy, transpose_xz

    if len(self.shape) == 2:
        return transpose_xy(self)
    elif len(self.shape) == 3:
        return transpose_xz(self)
    else:
        raise ValueError("Only 2D and 3D arrays supported.")


# missing operators:
# __array_interface__
# __array_ufunc__

setattr(Array, "T", property(T))

setattr(Array, "from_array", classmethod(from_array))
setattr(Array, "empty", classmethod(empty))
setattr(Array, "empty_like", classmethod(empty_like))
setattr(Array, "zeros", classmethod(zeros))
setattr(Array, "zeros_like", classmethod(zeros_like))

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
setattr(Array, "__iter__", _operators.__iter__)
setattr(Array, "__setitem__", _operators.__setitem__)
setattr(Array, "__getitem__", _operators.__getitem__)


Image = Union[np.ndarray, Array]


def is_image(object):
    return (
        isinstance(object, np.ndarray)
        or isinstance(object, tuple)
        or isinstance(object, list)
        or isinstance(object, Array)
        or str(type(object))
        in [
            "<class 'cupy._core.core.ndarray'>",
            "<class 'dask.array.core.Array'>",
            "<class 'xarray.core.dataarray.DataArray'>",
            "<class 'resource_backed_dask_array.ResourceBackedDaskArray'>",
            "<class 'torch.Tensor'>",
        ]
    )
