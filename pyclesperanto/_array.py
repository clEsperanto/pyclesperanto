from ._pyclesperanto import _Array as Array
from ._core import Device, get_device
from ._utils import _assert_supported_dtype
from . import _operators

from typing import Union
import numpy as np


def _prepare_array(arr) -> np.ndarray:
    """Converts a given array to a numpy array with C memory layout.
    
    Parameters
    ----------
    arr : 
        The array to convert.
        
    Returns
    -------
    np.ndarray
        The converted array.
    """
    return np.require(arr, None, "C")


def __str__(self) -> str:
    """Returns a string representation of the Array."""
    return self.get().__str__()


def __repr__(self) -> str:
    """Returns a string representation of the Array."""
    repr_str = self.get().__repr__()
    extra_info = f"mtype={self.mtype}"
    return repr_str[:-1] + f", {extra_info})"


def set(self, array: np.ndarray, origin: tuple = None, region: tuple = None) -> None:
    """Set the content of the Array to the given numpy array.
    
    Parameters
    ----------
    array : np.ndarray
        The array to set from.
    origin : tuple, optional
        The origin of the region of interest, by default None
    region : tuple, optional
        The region of interest, by default None
        
    Returns
    -------
    Array
        The array itself.
    """
    if not isinstance(array, (np.ndarray, Array)):
        array = np.array(array)

    if array.dtype != self.dtype:
        array = array.astype(self.dtype)

    if region and array.size != np.prod(region):
        raise IndexError(
            f"Value size mismatch the targeted region: {array.size} != {np.prod(region)} ({array.shape} != {tuple(np.squeeze(region))})"
        )
    elif not region and self.size != array.size:
        raise IndexError(
            f"Value size mismatch the targeted region: {self.size} != {array.size} ({self.shape} != {array.shape})"
        )

    self._write(_prepare_array(array), origin, region)
    return self


def get(self, origin: tuple = None, region: tuple = None) -> np.ndarray:
    """Get the content of the Array into a numpy array.
    
    Parameters
    ----------
    origin : tuple, optional
        The origin of the region of interest, by default None
    region : tuple, optional
        The region of interest, by default None
        
    Returns
    -------
    np.ndarray
        The array itself.
    """
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
    """Returns a numpy array representation of the Array."""
    if dtype is None:
        return self.get()
    else:
        return self.get().astype(dtype)


def to_device(cls, arr, *args, **kwargs):
    """Create an Array object from a numpy array (same shape, dtype, and memory).
    
    Parameters
    ----------
    arr : np.ndarray
        The array to convert.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None
    
    Returns
    -------
    Array
        The converted array.
    """
    if isinstance(arr, Array):
        return arr
    mtype = kwargs.get("mtype", "buffer")
    device = kwargs.get("device", get_device())
    return cls.create(arr.shape, arr.dtype, mtype, device).set(arr)


def from_array(cls, arr, *args, **kwargs):
    """Create an Array object from a numpy array (same shape, dtype, and memory).
    
    Parameters
    ----------
    arr : np.ndarray
        The array to convert.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None
    
    Returns
    -------
    Array
        The converted array.
    """
    _assert_supported_dtype(arr.dtype)
    return cls.to_device(arr, *args, **kwargs)


def empty(cls, shape, dtype=float, *args, **kwargs):
    """Create an empty Array object from a shape.
    
    Parameters
    ----------
    shape : tuple, list or np.ndarray
        The shape of the array, maximum 3 elements.
    dtype : np.dtype, default float
        The dtype of the array.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None
    
    Returns
    -------
    Array
        A new Array object.
    """
    _assert_supported_dtype(dtype)
    mtype = kwargs.get("mtype", "buffer")
    device = kwargs.get("device", get_device())

    return cls.create(shape=shape, dtype=dtype, mtype=mtype, device=device)


def empty_like(cls, arr):
    """Create an empty Array object from an other array.
    
    Parameters
    ----------
    arr : np.ndarray or Array or other array-like structure
        The array to create like.
    
    Returns
    -------
    Array
        The created array.
    """
    _assert_supported_dtype(arr.dtype)
    return Array.create(arr.shape, arr.dtype, arr.mtype, arr.device)


def zeros(cls, shape, dtype=float, *args, **kwargs):
    """Create an Array object full of zeros from a shape.
    
    Parameters
    ----------
    shape : tuple, list or np.ndarray
        The shape of the array, maximum 3 elements.
    dtype : np.dtype, default float
        The dtype of the array.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None
    
    Returns
    -------
    Array
        The created array.
    """
    _assert_supported_dtype(dtype)
    new_array = cls.empty(shape=shape, dtype=dtype, *args, **kwargs)
    new_array.fill(0)
    return new_array


def zeros_like(cls, arr):
    """Create an Array object filled with zeros from an other array.
    
    Parameters
    ----------
    arr : np.ndarray or Array or other array-like structure
        The array to create like.
    
    Returns
    -------
    Array
        The created array.
    """
    _assert_supported_dtype(arr.dtype)
    return cls.zeros(
        shape=arr.shape, dtype=arr.dtype, mtype=arr.mtype, device=arr.device
    )


def T(self):
    """Transpose the Array. Only works for 2D and 3D arrays."""
    from ._tier1 import transpose_xy, transpose_xz

    if len(self.shape) == 2:
        return transpose_xy(self)
    elif len(self.shape) == 3:
        return transpose_xz(self)
    else:
        return self


def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    if method == "__call__":
        func = getattr(Array, f"__{ufunc.__name__}__", None)
        if func is not None:
            return func(*[Array.to_device(i) for i in inputs], **kwargs)
    return NotImplemented


# missing operators:
# __array_interface__
# __array_ufunc__

# Add class methods, properties and magic methods
setattr(Array, "T", property(T))
setattr(Array, "set", set)
setattr(Array, "get", get)
setattr(Array, "__array_ufunc__", __array_ufunc__)
setattr(Array, "__str__", __str__)
setattr(Array, "__repr__", __repr__)
setattr(Array, "__array__", __array__)
setattr(Array, "from_array", classmethod(from_array))
setattr(Array, "empty", classmethod(empty))
setattr(Array, "empty_like", classmethod(empty_like))
setattr(Array, "zeros", classmethod(zeros))
setattr(Array, "zeros_like", classmethod(zeros_like))

# Add operations and class methods from _operators module
setattr(Array, "astype", _operators._astype)
setattr(Array, "max", _operators._max)
setattr(Array, "min", _operators._min)
setattr(Array, "sum", _operators._sum)
setattr(Array, "__pos__", _operators.__pos__)
setattr(Array, "__neg__", _operators.__neg__)
setattr(Array, "__add__", _operators.__add__)
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
setattr(Array, "_plt_to_png", _operators.__plt_to_png__)
setattr(Array, "_png_to_html", _operators.__png_to_html__)
setattr(Array, "_repr_html_", _operators.__repr_html__)
setattr(Array, "__iter__", _operators.__iter__)
setattr(Array, "__setitem__", _operators.__setitem__)
setattr(Array, "__getitem__", _operators.__getitem__)

# Create Image type
Image = Union[np.ndarray, Array]


def is_image(object):
    """Returns True if the given object is an image."""
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
