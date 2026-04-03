import warnings
from typing import Optional, Union

import numpy as np

from . import _operators
from ._backend import _get_backend
from ._core import Device, get_device
from ._utils import _assert_supported_dtype


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
    warnings.warn(
        "Array.to_device is deprecated and will be removed in a future release. Please use Array.from_array instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return cls.from_array(arr, *args, **kwargs)


def from_array(cls, arr, dtype=None, mtype="buffer", device=None):
    """Create an pyclesperanto Array object from a numpy array (same shape, dtype, and memory).

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

    if isinstance(arr, Array) and dtype != arr.dtype:
        # dtype conversion on device
        return arr.astype(dtype)

    # we are not on the device yet, so we can convert dtype with numpy and then upload
    arr = np.asarray(arr, dtype=dtype) if dtype else np.asarray(arr)

    _assert_supported_dtype(arr.dtype)

    if device is None:
        device = get_device()

    if mtype not in ["buffer", "image"]:
        raise ValueError(
            f"Invalid memory type: {mtype}. Supported values are 'buffer' and 'image'."
        )

    return cls.create(arr.shape, arr.dtype, mtype, device).set(arr)


def empty(cls, shape, dtype=None, mtype="buffer", device=None):
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

    if device is None:
        device = get_device()

    if mtype not in ["buffer", "image"]:
        raise ValueError(
            f"Invalid memory type: {mtype}. Supported values are 'buffer' and 'image'."
        )

    _assert_supported_dtype(dtype)
    return cls.create(shape=shape, dtype=dtype, mtype=mtype, device=device)


def empty_like(cls, arr, dtype=None, mtype="buffer", device=None):
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


def zeros(cls, shape, dtype=None, mtype="buffer", device=None):
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


def zeros_like(cls, arr, dtype=None, mtype="buffer", device=None):
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


def ones_like(cls, arr, dtype=None, mtype="buffer", device=None):
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
            return func(
                *[Array.from_array(i) for i in inputs],
                **kwargs,
            )
    return NotImplemented


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
    _DLPACK_DEVICE_METAL = 8
    _DLPACK_DEVICE_OPENCL = 7

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
        target_is_cuda and src_is_cuda and src_device_id == target_device.index)
        or (target_is_opencl and src_is_opencl and src_device_id == target_device.index)
        or (target_is_metal and src_is_metal and src_device_id == target_device.index)

    needs_copy = (
        copy is True  # user forced copy
        or src_is_cpu  # source is CPU — always need to upload
        or not same_device  # different GPU device
    )

    if copy is False and needs_copy:
        raise ValueError(
            f"copy=False requested but source device ({src_device_type}, {src_device_id}) "
            f"differs from target device ({target_device.type}, {target_device.index})"
        )

    if needs_copy or src_is_cpu:
        # CPU path: materialise to numpy then upload
        if src_is_cpu:
            np_arr = np.from_dlpack(dltensor)
            return cls.from_array(np_arr, device=target_device)

        # GPU→GPU cross-device: export to numpy (host) then re-upload
        # (no direct peer-to-peer via DLPack in cle yet)
        np_arr = np.array(dltensor.get())  # triggers device→host copy via __array__
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
    setattr(BackendArray, "to_device", classmethod(to_device))
    ## dlpack support
    setattr(BackendArray, "__dlpack__", __dlpack__)
    setattr(BackendArray, "__dlpack_device__", __dlpack_device__)
    setattr(BackendArray, "from_dlpack", classmethod(from_dlpack))
    ## copy-free reshape
    # setattr(BackendArray, "reshape", reshape)

    setattr(BackendArray, "astype", _operators._astype)
    setattr(BackendArray, "max", _operators._max)
    setattr(BackendArray, "min", _operators._min)
    setattr(BackendArray, "sum", _operators._sum)
    setattr(BackendArray, "std", _operators._std)
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
