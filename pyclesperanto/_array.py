import warnings
from typing import Optional, Union

import numpy as np

from . import _operators
from ._backend import _get_backend
from ._core import Device, get_device
from ._utils import _assert_supported_dtype, _canonical_dtype


def _get_array_class():
    """Get the _Array class from the active backend (lazy)."""
    return _get_backend()._Array


class _ArrayMeta(type):
    """Metaclass that makes isinstance/issubclass always check the *current* backend."""

    def __instancecheck__(cls, instance):
        try:
            return isinstance(instance, _get_array_class())
        except RuntimeError:
            return False

    def __subclasscheck__(cls, subclass):
        try:
            return issubclass(subclass, _get_array_class())
        except RuntimeError:
            return False

    # ------------------------------------------------------------------ #
    # Forward every attribute access to the *current* backend _Array.     #
    # This makes cle.Array.create(...) always use the right backend.      #
    # ------------------------------------------------------------------ #
    def __getattr__(cls, name):
        return getattr(_get_array_class(), name)


class Array(metaclass=_ArrayMeta):
    """Lazy proxy for the backend Array class.

    Attribute access is forwarded to the *currently active* backend _Array,
    so switching backends with select_backend() is fully transparent.

    Notes
    -----
    Known deviations from NumPy, due to backend (CLIc) limitations:

    - 64-bit dtypes are silently downcast on device: ``float64 -> float32``
      and ``int64 -> int32``.
    - ``bool`` is stored as ``uint8`` (0/1 values).
    - Arrays are limited to at most 3 dimensions.
    """

    pass


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


def set(
    self,
    arr: Union[np.ndarray, Array, list, tuple],
    origin: Optional[tuple] = None,
    region: Optional[tuple] = None,
) -> None:
    """Store an array-like structure into the Array. This is a host→device transfer.
    The memory size of the input array must match the size of the Array, or the size of the targeted region if origin and region are specified.

    Parameters
    ----------
    arr : Union[np.ndarray, Array, list, tuple]
        The memory to set from.
    origin : tuple, optional
        The origin of the region of interest, by default None
    region : tuple, optional
        The region of interest, by default None

    Returns
    -------
    Array
        The array itself.
    """
    if not isinstance(arr, (np.ndarray, Array)):
        arr = np.array(arr)

    if arr.dtype != self.dtype:
        arr = arr.astype(self.dtype)

    if region and arr.size != np.prod(region):
        raise IndexError(
            f"Value size mismatch the targeted region: {arr.size} != {np.prod(region)} ({arr.shape} != {tuple(np.squeeze(region))})"
        )
    elif not region and self.size != arr.size:
        raise IndexError(
            f"Value size mismatch the targeted region: {self.size} != {arr.size} ({self.shape} != {arr.shape})"
        )

    self._write(_prepare_array(arr), origin, region)
    return self


def get(
    self, origin: Optional[tuple] = None, region: Optional[tuple] = None
) -> np.ndarray:
    """Convert the Array to a numpy array. This is a device→host transfer.

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
        # "int64": self._read_int64,
        "uint8": self._read_uint8,
        "uint16": self._read_uint16,
        "uint32": self._read_uint32,
        # "uint64": self._read_uint64,
    }
    return caster[self.dtype.name](origin, region)


def __array__(self, dtype=None, copy=None) -> np.ndarray:
    """Returns a numpy array representation of the Array (NumPy >= 2.0 protocol)."""
    if copy is False:
        raise ValueError(
            "Unable to avoid copy: converting a device Array to numpy always copies."
        )
    arr = self.get()
    if dtype is not None and arr.dtype != np.dtype(dtype):
        arr = arr.astype(dtype)
    return arr


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
    warnings.warn(
        "Array.to_device is deprecated and will be removed in a future release. Please use Array.from_array instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return cls.from_array(arr, *args, **kwargs)


def from_array(cls, arr, dtype=None, *, mtype="buffer", device=None):
    """Create an pyclesperanto Array object from a numpy array (same shape, dtype, and memory).

    Note: 64-bit dtypes are silently downcast on device (``float64 -> float32``,
    ``int64 -> int32``) and ``bool`` is stored as ``uint8``, due to backend
    (CLIc) limitations.

    Parameters
    ----------
    arr : np.ndarray
        The array to convert.
    dtype : np.dtype, optional
        Override the dtype of the created Array.
    mtype : str, optional
        The memory type. By default "buffer".
    device : Device, optional
        The device on which to create the Array. If None, uses the current active device.

    Returns
    -------
    Array
        The converted array.
    """
    if isinstance(arr, Array) and dtype is None:
        # nothing to do
        return arr

    dtype = _canonical_dtype(dtype)

    if isinstance(arr, Array) and dtype != arr.dtype:
        # dtype conversion on device
        return arr.astype(dtype)

    # we are not on the device yet, so we can convert dtype with numpy and then upload
    arr = np.asarray(arr, dtype=dtype) if dtype else np.asarray(arr)
    if arr.dtype == np.bool_:
        arr = arr.astype(np.uint8)

    _assert_supported_dtype(arr.dtype)

    if device is None:
        device = get_device()

    if mtype not in ["buffer", "image"]:
        raise ValueError(
            f"Invalid memory type: {mtype}. Supported values are 'buffer' and 'image'."
        )

    return cls.create(arr.shape, arr.dtype, mtype, device).set(arr)


def empty(cls, shape, dtype=None, *, mtype="buffer", device=None):
    """Create an empty Array object from a shape.

    Parameters
    ----------
    shape : tuple, list or np.ndarray
        The shape of the array, maximum 3 elements.
    dtype : np.dtype, optional
        The dtype of the array. If None, uses float32.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None

    Returns
    -------
    Array
        A new Array object.
    """

    if len(shape) > 3:
        raise ValueError(
            f"Invalid shape: {shape}. Only up to 3 dimensions are supported."
        )

    if dtype is None:
        dtype = np.float32
    dtype = _canonical_dtype(dtype)

    if device is None:
        device = get_device()

    if mtype not in ["buffer", "image"]:
        raise ValueError(
            f"Invalid memory type: {mtype}. Supported values are 'buffer' and 'image'."
        )

    _assert_supported_dtype(dtype)
    return cls.create(shape=shape, dtype=dtype, mtype=mtype, device=device)


def empty_like(cls, arr, dtype=None, *, mtype="buffer", device=None):
    """Create an empty Array object from an other array.

    Parameters
    ----------
    arr : np.ndarray or Array or other array-like structure
        The array to create like.
    dtype : np.dtype, optional
        Override the dtype of the created Array.
    mtype : str, optional
        The memory type. By default "buffer".
    device : Device, optional
        The device on which to create the Array. If None, uses the current active device.

    Returns
    -------
    Array
        The created array.
    """
    if dtype is None:
        dtype = arr.dtype
    return cls.empty(shape=arr.shape, dtype=dtype, mtype=mtype, device=device)


def zeros(cls, shape, dtype=None, *, mtype="buffer", device=None):
    """Create an Array object full of zeros from a shape.

    Parameters
    ----------
    shape : tuple, list or np.ndarray
        The shape of the array, maximum 3 elements.
    dtype : np.dtype, optional
        The dtype of the array. If None, uses float32.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None

    Returns
    -------
    Array
        The created array.
    """
    new_array = cls.empty(shape=shape, dtype=dtype, mtype=mtype, device=device)
    new_array.fill(0)
    return new_array


def zeros_like(cls, arr, dtype=None, *, mtype="buffer", device=None):
    """Create an Array object filled with zeros from an other array.

    Parameters
    ----------
    arr : np.ndarray or Array or other array-like structure
        The array to create like.
    dtype : np.dtype, optional
        Override the dtype of the created Array.
    mtype : str, optional
        The memory type. By default "buffer".
    device : Device, optional
        The device on which to create the Array. If None, uses the current active device.


    Returns
    -------
    Array
        The created array.
    """
    if dtype is None:
        dtype = arr.dtype
    return cls.zeros(shape=arr.shape, dtype=dtype, mtype=mtype, device=device)


def ones(cls, shape, dtype=None, *, mtype="buffer", device=None):
    """Create an Array object full of ones from a shape.

    Parameters
    ----------
    shape : tuple, list or np.ndarray
        The shape of the array, maximum 3 elements.
    dtype : np.dtype, optional
        The dtype of the array. If None, uses float32.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None

    Returns
    -------
    Array
        The created array.
    """
    new_array = cls.empty(shape=shape, dtype=dtype, mtype=mtype, device=device)
    new_array.fill(1)
    return new_array


def ones_like(cls, arr, dtype=None, *, mtype="buffer", device=None):
    """Create an Array object filled with ones from an other array.

    Parameters
    ----------
    arr : np.ndarray or Array or other array-like structure
        The array to create like.
    dtype : np.dtype, optional
        Override the dtype of the created Array.
    mtype : str, optional
        The memory type. By default "buffer".
    device : Device, optional
        The device on which to create the Array. If None, uses the current active device.


    Returns
    -------
    Array
        The created array.
    """
    if dtype is None:
        dtype = arr.dtype
    return cls.ones(shape=arr.shape, dtype=dtype, mtype=mtype, device=device)


def full(cls, shape, fill_value, dtype=None, *, mtype="buffer", device=None):
    """Create an Array of a given shape filled with ``fill_value``.

    Parameters
    ----------
    shape : tuple, list or np.ndarray
        The shape of the array, maximum 3 elements.
    fill_value : scalar
        The value to fill the array with.
    dtype : np.dtype, optional
        The dtype of the array. If None, inferred from ``fill_value``.
    mtype : str, optional
        The memory type, by default "buffer"
    device : Device, optional
        The device, by default None

    Returns
    -------
    Array
        The created array.
    """
    if dtype is None:
        dtype = np.asarray(fill_value).dtype
    new_array = cls.empty(shape=shape, dtype=dtype, mtype=mtype, device=device)
    new_array.fill(fill_value)
    return new_array


def full_like(cls, arr, fill_value, dtype=None, *, mtype="buffer", device=None):
    """Create an Array filled with ``fill_value`` from another array.

    Parameters
    ----------
    arr : np.ndarray or Array or other array-like structure
        The array to create like.
    fill_value : scalar
        The value to fill the array with.
    dtype : np.dtype, optional
        Override the dtype of the created Array.
    mtype : str, optional
        The memory type. By default "buffer".
    device : Device, optional
        The device on which to create the Array. If None, uses the current active device.

    Returns
    -------
    Array
        The created array.
    """
    if dtype is None:
        dtype = arr.dtype
    return cls.full(
        shape=arr.shape,
        fill_value=fill_value,
        dtype=dtype,
        mtype=mtype,
        device=device,
    )


def arange(cls, start, stop=None, step=1, dtype=None, *, mtype="buffer", device=None):
    """Create an Array with evenly spaced values within a given interval.

    Mirrors ``numpy.arange``. The values are computed on the host and uploaded.

    Returns
    -------
    Array
        The created 1-D array.
    """
    values = np.arange(start, stop, step, dtype=dtype)
    return cls.from_array(values, mtype=mtype, device=device)


def linspace(
    cls,
    start,
    stop,
    num=50,
    endpoint=True,
    dtype=None,
    *,
    mtype="buffer",
    device=None,
):
    """Create an Array of ``num`` evenly spaced values from ``start`` to ``stop``.

    Mirrors ``numpy.linspace``. The values are computed on the host and uploaded.

    Returns
    -------
    Array
        The created 1-D array.
    """
    values = np.linspace(start, stop, num=num, endpoint=endpoint, dtype=dtype)
    return cls.from_array(values, mtype=mtype, device=device)


def eye(cls, N, M=None, k=0, dtype=None, *, mtype="buffer", device=None):
    """Create a 2-D Array with ones on a diagonal and zeros elsewhere.

    Mirrors ``numpy.eye``. The values are computed on the host and uploaded.

    Returns
    -------
    Array
        The created 2-D array.
    """
    values = np.eye(N, M, k, dtype=dtype if dtype is not None else float)
    return cls.from_array(values, mtype=mtype, device=device)


def T(self):
    """Transpose the Array, reversing the axes order (NumPy semantics).

    2D arrays are transposed with ``transpose_xy``, 3D arrays with
    ``transpose_xz`` (which reverses (z, y, x) to (x, y, z)).
    Arrays with fewer than 2 dimensions are returned unchanged.
    """
    from ._tier1 import transpose_xy, transpose_xz

    if len(self.shape) == 2:
        return transpose_xy(self)
    elif len(self.shape) == 3:
        return transpose_xz(self)
    else:
        return self


def mT(self):
    """Transpose the last two axes of the Array (NumPy ``matrix transpose``)."""
    from ._tier1 import transpose_xy

    if len(self.shape) < 2:
        raise ValueError("matrix transpose with ndim < 2 is undefined")
    return transpose_xy(self)


def real(self):
    """The real part of the Array. Device dtypes are real, returns self."""
    return self


def imag(self):
    """The imaginary part of the Array. Device dtypes are real, returns zeros."""
    from ._memory import create_like

    result = create_like(self)
    result.fill(0)
    return result


class _Flags:
    c_contiguous = True
    f_contiguous = False
    owndata = True
    writeable = True

    def __getitem__(self, key):
        mapping = {
            "C_CONTIGUOUS": self.c_contiguous,
            "C": self.c_contiguous,
            "F_CONTIGUOUS": self.f_contiguous,
            "F": self.f_contiguous,
            "OWNDATA": self.owndata,
            "WRITEABLE": self.writeable,
        }
        return mapping[key.upper()]


def flags(self):
    """Minimal information about the memory layout of the Array."""
    return _Flags()


# ufunc name -> tier1/tier2 kernel name (single input)
_UNARY_UFUNCS = {
    "sqrt": "square_root",
    "exp": "exponential",
    "exp2": "exponential2",
    "log": "logarithm",
    "log2": "logarithm2",
    "log10": "logarithm10",
    "log1p": "log1p",
    "expm1": "expm1",
    "absolute": "absolute",
    "fabs": "absolute",
    "sin": "sin",
    "cos": "cos",
    "tan": "tan",
    "arcsin": "asin",
    "arccos": "acos",
    "arctan": "atan",
    "sinh": "sinh",
    "cosh": "cosh",
    "tanh": "tanh",
    "square": "square",
    "negative": "__neg__",
    "positive": "__pos__",
    "floor": "floor",
    "ceil": "ceil",
    "trunc": "truncate",
    "sign": "sign",
    "rint": "rint",
    "isnan": "isnan",
    "isfinite": "isfinite",
}

# ufunc name -> (forward operator, reflected operator or None) in _operators
_BINARY_UFUNCS = {
    "add": ("__add__", "__radd__"),
    "subtract": ("__sub__", "__rsub__"),
    "multiply": ("__mul__", "__rmul__"),
    "divide": ("__truediv__", "__rtruediv__"),
    "true_divide": ("__truediv__", "__rtruediv__"),
    "power": ("__pow__", "__rpow__"),
    "floor_divide": ("__floordiv__", "__rfloordiv__"),
    "mod": ("__mod__", "__rmod__"),
    "remainder": ("__mod__", "__rmod__"),
    "greater": ("__gt__", "__lt__"),
    "greater_equal": ("__ge__", "__le__"),
    "less": ("__lt__", "__gt__"),
    "less_equal": ("__le__", "__ge__"),
    "equal": ("__eq__", "__eq__"),
    "not_equal": ("__ne__", "__ne__"),
    "maximum": ("maximum", "maximum"),
    "minimum": ("minimum", "minimum"),
    "hypot": ("hypot", "hypot"),
    "arctan2": ("atan2", "_atan2_reversed"),
    "logical_and": ("logical_and", "logical_and"),
    "logical_or": ("logical_or", "logical_or"),
    "logical_xor": ("logical_xor", "logical_xor"),
}


def _apply_ufunc(name, inputs):
    """Apply a supported ufunc to inputs (Arrays or scalars), or return NotImplemented."""
    from . import _operators, _tier1, _tier2

    if name in _UNARY_UFUNCS and len(inputs) == 1:
        kernel = _UNARY_UFUNCS[name]
        func = (
            getattr(_operators, kernel, None)
            or getattr(_tier1, kernel, None)
            or getattr(_tier2, kernel)
        )
        return func(inputs[0])

    if name in _BINARY_UFUNCS and len(inputs) == 2:
        fwd, rev = _BINARY_UFUNCS[name]
        x1, x2 = inputs
        if isinstance(x1, _get_array_class()):
            return getattr(_operators, fwd)(x1, x2)
        if rev is None:
            return NotImplemented
        return getattr(_operators, rev)(x2, x1)

    return NotImplemented


def _apply_reduce(ufunc_name, arr, axis=None, dtype=None, out=None, keepdims=False, initial=None, where=True):
    """Apply ufunc.reduce to an Array by routing to existing reduction kernels."""
    if initial is not None or where is not True:
        return NotImplemented
    
    from ._operators import _sum, _max, _min, _prod
    
    if axis is None:
        axis = 0
    
    if ufunc_name == "add":
        return _sum(arr, axis=axis, dtype=dtype, out=out, keepdims=keepdims)
    elif ufunc_name == "maximum":
        return _max(arr, axis=axis, out=out, keepdims=keepdims)
    elif ufunc_name == "minimum":
        return _min(arr, axis=axis, out=out, keepdims=keepdims)
    elif ufunc_name == "multiply":
        return _prod(arr, axis=axis, dtype=dtype, out=out, keepdims=keepdims)
    
    return NotImplemented


def _normalize_axis(axis, ndim):
    """Normalize and validate a single axis index."""
    if not isinstance(axis, (int, np.integer)):
        raise TypeError(f"axis must be an integer, got {type(axis).__name__}")
    axis = int(axis)
    if axis < 0:
        axis += ndim
    if not 0 <= axis < ndim:
        raise ValueError(f"axis {axis} is out of bounds for array of dimension {ndim}")
    return axis


def _apply_accumulate(ufunc_name, arr, axis=0, dtype=None, out=None):
    """Apply ufunc.accumulate to an Array using backend cumulative kernels."""
    from ._tier1 import (
        cumulative_max,
        cumulative_min,
        cumulative_product,
        cumulative_sum,
        copy,
    )

    if dtype is not None:
        arr = arr.astype(dtype)

    axis = _normalize_axis(axis, arr.ndim)
    # Backend cumulative kernels expect axis in X/Y/Z order, while NumPy axes
    # follow the array shape order. Mirror the mapping used by projections.
    backend_axis = arr.ndim - 1 - axis

    if ufunc_name == "add":
        result = cumulative_sum(arr, axis=backend_axis)
    elif ufunc_name == "maximum":
        result = cumulative_max(arr, axis=backend_axis)
    elif ufunc_name == "minimum":
        result = cumulative_min(arr, axis=backend_axis)
    elif ufunc_name == "multiply":
        result = cumulative_product(arr, axis=backend_axis)
    else:
        return NotImplemented

    if out is not None:
        if isinstance(out, tuple):
            if len(out) != 1:
                return NotImplemented
            out = out[0]
        if out is None:
            return NotImplemented
        if isinstance(out, np.ndarray):
            np.copyto(out, result.get().astype(out.dtype))
            return out
        copy(result, out)
        return out

    return result


def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    """Dispatch NumPy ufuncs to the corresponding device kernels."""
    if method == "reduce":
        return _apply_reduce(ufunc.__name__, self, **kwargs)
    if method == "accumulate":
        axis = kwargs.pop("axis", 0)
        dtype = kwargs.pop("dtype", None)
        out = kwargs.pop("out", None)
        if kwargs:
            return NotImplemented
        return _apply_accumulate(ufunc.__name__, self, axis=axis, dtype=dtype, out=out)
    if method != "__call__":
        return NotImplemented
    out = kwargs.pop("out", None)
    if kwargs:
        return NotImplemented

    ArrayCls = _get_array_class()
    inputs = [
        i if isinstance(i, ArrayCls) or np.isscalar(i) else ArrayCls.from_array(i)
        for i in inputs
    ]

    result = _apply_ufunc(ufunc.__name__, inputs)
    if result is NotImplemented:
        return NotImplemented

    if out is not None:
        if len(out) != 1 or out[0] is None:
            return NotImplemented
        target = out[0]
        if isinstance(target, np.ndarray):
            np.copyto(target, result.get().astype(target.dtype))
        else:
            from ._tier1 import copy

            copy(result, target)
        return target
    return result


def _reset_array_patch():
    """Reset the array patch flag and immediately re-patch with the new backend.

    Called when the active backend changes. This ensures that:
    1. The Array class is re-bound to the new backend's _Array class
    2. Methods are re-patched onto the new class
    3. Module-level bindings are updated so cle.Array points to the new backend
    """
    global _array_patched
    _array_patched = False

    # Re-patch the Array class with the new backend
    _patch_array_class()

    # Update module-level bindings in pyclesperanto/__init__.py
    # so that cle.Array always refers to the current backend's Array class
    import sys

    init_module = sys.modules.get("pyclesperanto")
    if init_module is not None:
        try:
            setattr(init_module, "Array", Array)
            setattr(init_module, "Image", Image)
        except Exception:
            pass  # Ignore any errors updating bindings


def __dlpack__(self, stream=None, version=(1, 0)):
    """Export as DLPack capsule (CUDA and OpenCL BUFFER only)."""
    return self._dlpack(stream, version)  # calls the C++ binding


def __dlpack_device__(self):
    """Return (device_type, device_id) tuple per DLPack spec."""
    return self._dlpack_device()  # calls the C++ binding


def from_dlpack(cls, dltensor, *, device=None, copy=None):
    """Create an Array from any object implementing the DLPack protocol.

    DLPack is a open in memory tensor structure: https://dmlc.github.io/dlpack/latest/

    The returned Array shares memory with the source tensor. This is copy-free and efficient if
    the source tensor is on the same device as the target Array, however ownership is not transferred
    (the source tensor remains responsible for freeing the memory).
    If copy is forced or necessary (e.g. cross-device), the data is copied and ownership is transferred
    to the new Array.

    Parameters
    ----------
    dltensor : object
        Any object with ``__dlpack__`` and ``__dlpack_device__`` methods,
        or a raw DLPack capsule.
    device : Device, optional
        Target cle device. If None, uses the current active device.
    copy : bool or None, optional
        - None  (default): copy only if necessary (source is on a different device)
        - True : always copy
        - False: never copy — raises if source and target devices differ

    Returns
    -------
    Array
        A cle Array sharing or copying the data from dltensor.
    """
    # DLPack device type constants
    _DLPACK_DEVICE_CPU = 1
    _DLPACK_DEVICE_CUDA = 2
    _DLPACK_DEVICE_OPENCL = 4
    _DLPACK_DEVICE_METAL = 8

    # get target device (default to current)
    target_device = device if device is not None else get_device()

    # --- resolve source device type ---
    if hasattr(dltensor, "__dlpack_device__"):
        src_device_type, src_device_id = dltensor.__dlpack_device__()
    else:
        # raw capsule — assume same device
        src_device_type, src_device_id = None, None

    # Determine whether source is on the same device as target
    target_is_cuda = target_device.type.name.upper() == "CUDA"
    target_is_opencl = target_device.type.name.upper() == "OPENCL"
    target_is_metal = target_device.type.name.upper() == "METAL"

    # Determine source device type
    src_is_cuda = src_device_type == _DLPACK_DEVICE_CUDA
    src_is_opencl = src_device_type == _DLPACK_DEVICE_OPENCL
    src_is_metal = src_device_type == _DLPACK_DEVICE_METAL
    src_is_cpu = src_device_type == _DLPACK_DEVICE_CPU

    same_device = (
        (target_is_cuda and src_is_cuda and src_device_id == target_device.index)
        or (target_is_opencl and src_is_opencl and src_device_id == target_device.index)
        or (target_is_metal and src_is_metal and src_device_id == target_device.index)
    )

    # Metal zero-copy DLPack import is not yet supported in the C++ backend;
    # force a copy through the host for Metal sources.
    needs_copy = (
        copy is True  # user forced copy
        or src_is_cpu  # source is CPU — always need to upload
        or src_is_metal  # Metal zero-copy not yet supported
        or not same_device  # different GPU device
    )

    if copy is False and needs_copy:
        raise ValueError(
            f"copy=False requested but source device ({src_device_type}, {src_device_id}) "
            f"differs from target device ({target_device.type}, {target_device.index})"
        )

    if needs_copy or src_is_cpu:
        # Materialise to numpy then upload to target device
        if hasattr(dltensor, "cpu"):
            # PyTorch-like: move to CPU first, then convert
            np_arr = np.asarray(dltensor.cpu())
        elif hasattr(dltensor, "get"):
            # cle Array or CuPy-like
            np_arr = np.asarray(dltensor.get())
        else:
            np_arr = np.from_dlpack(dltensor)
        return cls.from_array(np_arr, device=target_device)

    # Zero-copy path: same device, wrap the DLPack capsule directly
    return cls._from_dlpack(dltensor, target_device)


def _patch_array_class():
    """Patch the *current* backend _Array class with Python methods.

    Safe to call multiple times — re-patches whenever the backend changes.
    """
    # NOTE: We intentionally do NOT replace the module-level `Array` name.
    # The _ArrayMeta proxy always delegates to _get_array_class() at runtime.
    BackendArray = _get_array_class()

    setattr(BackendArray, "T", property(T))
    setattr(BackendArray, "mT", property(mT))
    setattr(BackendArray, "real", property(real))
    setattr(BackendArray, "imag", property(imag))
    setattr(BackendArray, "flags", property(flags))
    setattr(BackendArray, "set", set)
    setattr(BackendArray, "get", get)
    setattr(BackendArray, "__array_ufunc__", __array_ufunc__)
    setattr(BackendArray, "__str__", __str__)
    setattr(BackendArray, "__repr__", __repr__)
    setattr(BackendArray, "__array__", __array__)
    setattr(BackendArray, "from_array", classmethod(from_array))
    setattr(BackendArray, "empty", classmethod(empty))
    setattr(BackendArray, "empty_like", classmethod(empty_like))
    setattr(BackendArray, "zeros", classmethod(zeros))
    setattr(BackendArray, "zeros_like", classmethod(zeros_like))
    setattr(BackendArray, "ones", classmethod(ones))
    setattr(BackendArray, "ones_like", classmethod(ones_like))
    setattr(BackendArray, "full", classmethod(full))
    setattr(BackendArray, "full_like", classmethod(full_like))
    setattr(BackendArray, "arange", classmethod(arange))
    setattr(BackendArray, "linspace", classmethod(linspace))
    setattr(BackendArray, "eye", classmethod(eye))
    setattr(BackendArray, "to_device", classmethod(to_device))
    ## dlpack support
    setattr(BackendArray, "__dlpack__", __dlpack__)
    setattr(BackendArray, "__dlpack_device__", __dlpack_device__)
    setattr(BackendArray, "from_dlpack", classmethod(from_dlpack))
    ## copy-free reshape
    if "_native_reshape" not in BackendArray.__dict__:
        setattr(BackendArray, "_native_reshape", BackendArray.reshape)
    setattr(BackendArray, "reshape", _operators._reshape)

    setattr(BackendArray, "astype", _operators._astype)
    setattr(BackendArray, "copy", _operators._copy)
    setattr(BackendArray, "squeeze", _operators._squeeze)
    setattr(BackendArray, "ravel", _operators._ravel)
    setattr(BackendArray, "flatten", _operators._flatten)
    setattr(BackendArray, "item", _operators._item)
    setattr(BackendArray, "tolist", _operators._tolist)
    setattr(BackendArray, "clip", _operators._clip)
    setattr(BackendArray, "round", _operators._round)
    setattr(BackendArray, "max", _operators._max)
    setattr(BackendArray, "min", _operators._min)
    setattr(BackendArray, "sum", _operators._sum)
    setattr(BackendArray, "std", _operators._std)
    setattr(BackendArray, "mean", _operators._mean)
    setattr(BackendArray, "var", _operators._var)
    setattr(BackendArray, "prod", _operators._prod)
    setattr(BackendArray, "argmax", _operators._argmax)
    setattr(BackendArray, "argmin", _operators._argmin)
    setattr(BackendArray, "any", _operators._any)
    setattr(BackendArray, "all", _operators._all)
    setattr(BackendArray, "__pos__", _operators.__pos__)
    setattr(BackendArray, "__neg__", _operators.__neg__)
    setattr(BackendArray, "__add__", _operators.__add__)
    setattr(BackendArray, "__iadd__", _operators.__iadd__)
    setattr(BackendArray, "__radd__", _operators.__radd__)
    setattr(BackendArray, "__sub__", _operators.__sub__)
    setattr(BackendArray, "__isub__", _operators.__isub__)
    setattr(BackendArray, "__rsub__", _operators.__rsub__)
    setattr(BackendArray, "__div__", _operators.__div__)
    setattr(BackendArray, "__idiv__", _operators.__idiv__)
    setattr(BackendArray, "__rdiv__", _operators.__rdiv__)
    setattr(BackendArray, "__truediv__", _operators.__truediv__)
    setattr(BackendArray, "__itruediv__", _operators.__itruediv__)
    setattr(BackendArray, "__rtruediv__", _operators.__rtruediv__)
    setattr(BackendArray, "__mul__", _operators.__mul__)
    setattr(BackendArray, "__imul__", _operators.__imul__)
    setattr(BackendArray, "__rmul__", _operators.__rmul__)
    setattr(BackendArray, "__gt__", _operators.__gt__)
    setattr(BackendArray, "__ge__", _operators.__ge__)
    setattr(BackendArray, "__lt__", _operators.__lt__)
    setattr(BackendArray, "__le__", _operators.__le__)
    setattr(BackendArray, "__eq__", _operators.__eq__)
    setattr(BackendArray, "__ne__", _operators.__ne__)
    setattr(BackendArray, "__pow__", _operators.__pow__)
    setattr(BackendArray, "__ipow__", _operators.__ipow__)
    setattr(BackendArray, "__rpow__", _operators.__rpow__)
    setattr(BackendArray, "__abs__", _operators.__abs__)
    setattr(BackendArray, "__floordiv__", _operators.__floordiv__)
    setattr(BackendArray, "__rfloordiv__", _operators.__rfloordiv__)
    setattr(BackendArray, "__ifloordiv__", _operators.__ifloordiv__)
    setattr(BackendArray, "__mod__", _operators.__mod__)
    setattr(BackendArray, "__rmod__", _operators.__rmod__)
    setattr(BackendArray, "__imod__", _operators.__imod__)
    setattr(BackendArray, "__and__", _operators.__and__)
    setattr(BackendArray, "__or__", _operators.__or__)
    setattr(BackendArray, "__xor__", _operators.__xor__)
    setattr(BackendArray, "__invert__", _operators.__invert__)
    setattr(BackendArray, "__float__", _operators.__float__)
    setattr(BackendArray, "__int__", _operators.__int__)
    setattr(BackendArray, "__bool__", _operators.__bool__)
    # setattr(BackendArray, "_figure_to_png", _operators.__figure_to_png__)
    # setattr(BackendArray, "_png_to_html", _operators.__png_to_html__)
    setattr(BackendArray, "_repr_html_", _operators.__repr_html__)
    setattr(BackendArray, "__iter__", _operators.__iter__)
    setattr(BackendArray, "__setitem__", _operators.__setitem__)
    setattr(BackendArray, "__getitem__", _operators.__getitem__)


Image = Union[np.ndarray, Array]


def is_image(object):
    """Returns True if the given object is an image."""
    if isinstance(object, (np.ndarray, tuple, list, Array)):
        return True

    type_str = type(object).__module__ + "." + type(object).__qualname__

    return type_str in [
        "cupy._core.core.ndarray",
        "dask.array.core.Array",
        "xarray.core.dataarray.DataArray",
        "resource_backed_dask_array.ResourceBackedDaskArray",
        "torch.Tensor",
        "pyclesperanto_prototype._tier0._pycl.OCLArray",
        "napari.layers._multiscale_data.MultiScaleData",
    ]
