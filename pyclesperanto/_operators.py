from typing import Optional, Union

import numpy as np

from ._utils import (
    _compute_range,
    _process_ellipsis_into_slice,
    _trim_index_to_shape,
)


def _get_array_class():
    """Late import to avoid circular dependency with _array.py."""
    from ._backend import _get_backend

    return _get_backend()._Array


cl_buffer_datatype_dict = {
    bool: "bool",
    np.uint8: "uchar",
    np.uint16: "ushort",
    np.uint32: "uint",
    np.uint64: "ulong",
    np.int8: "char",
    np.int16: "short",
    np.int32: "int",
    np.int64: "long",
    np.float32: "float",
    np.complex64: "cfloat_t",
    int: "int",
    float: "float",
    np.float64: "float",
}

_INTEGER_TYPES = (
    int,
    np.intp,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
)

_supported_numeric_types = tuple(cl_buffer_datatype_dict.keys())


def _astype(self, dtype: type, casting="unsafe", copy=True):
    """Convert the Array to a different data type.

    Parameters
    ----------
    dtype : type
        Target data type. ``bool`` is stored as ``uint8`` on device.
        64-bit types are silently downcast (``float64 -> float32``,
        ``int64 -> int32``) due to backend (CLIc) limitations.
    casting : str, optional
        Accepted for NumPy signature compatibility, ignored (the device
        backend always performs an unsafe cast).
    copy : bool, optional
        If True (default, matching NumPy), always return a new array.
        If False, return the array itself when the dtype already matches.
    """
    from ._utils import _canonical_dtype

    dtype = _canonical_dtype(dtype)
    if dtype not in _supported_numeric_types:
        raise ValueError(
            "dtype "
            + str(dtype)
            + " not supported. Use one of "
            + str(_supported_numeric_types)
        )
    if dtype == self.dtype and not copy:
        return self

    from ._memory import create_like
    from ._tier1 import copy as _copy_kernel

    result = create_like(self, dtype=dtype)
    _copy_kernel(input_image=self, output_image=result)
    return result


def _copy(self, *args, **kwargs):
    """Return a copy of the Array.

    Without arguments, behaves like ``numpy.ndarray.copy`` and returns a new
    Array duplicating the data. With arguments, forwards to the backend
    region-copy method (``dst, src_origin, dst_origin, region``).
    """
    if args or kwargs:
        return self._copy_region(*args, **kwargs)
    from ._tier1 import copy as _copy_kernel

    return _copy_kernel(self)


def _squeeze(self, axis=None):
    """Remove axes of length one from the Array.

    Deviation from NumPy: squeezing all axes returns a 1-element 1D Array
    instead of a 0-d array (the backend has no 0-d arrays).
    """
    shape = list(self.shape)
    if axis is None:
        new_shape = [s for s in shape if s != 1]
    else:
        if np.isscalar(axis):
            axis = (axis,)
        axis = tuple(a + len(shape) if a < 0 else a for a in axis)
        for a in axis:
            if shape[a] != 1:
                raise ValueError(
                    "cannot select an axis to squeeze out which has size not equal to one"
                )
        new_shape = [s for i, s in enumerate(shape) if i not in axis]
    if not new_shape:
        new_shape = [1]
    if tuple(new_shape) == tuple(shape):
        return self
    return _reshape_result(self, new_shape, None)


def _ravel(self):
    """Return the Array flattened to 1D, sharing the device memory."""
    return _reshape_result(self, [int(self.size)], None)


def _reshape(self, *shape):
    """Return an Array with a new shape (NumPy-compatible signature)."""
    if len(shape) == 1 and isinstance(shape[0], (tuple, list)):
        new_shape = list(shape[0])
    else:
        new_shape = list(shape)
    new_shape = [int(s) for s in new_shape]
    size = int(self.size)
    if new_shape.count(-1) > 1:
        raise ValueError("can only specify one unknown dimension")
    if -1 in new_shape:
        known = 1
        for s in new_shape:
            if s != -1:
                known *= s
        if known == 0 or size % known != 0:
            raise ValueError(
                f"cannot reshape array of size {size} into shape {tuple(new_shape)}"
            )
        new_shape[new_shape.index(-1)] = size // known
    if int(np.prod(new_shape)) != size:
        raise ValueError(
            f"cannot reshape array of size {size} into shape {tuple(new_shape)}"
        )
    return _reshape_result(self, new_shape, None)


def _flatten(self):
    """Return a 1D copy of the Array."""
    return _reshape_result(_copy(self), [int(self.size)], None)


def _item(self, *args):
    """Copy one element of the Array to a standard Python scalar.

    This avoids transferring the full buffer by reading only a 1-element ROI.
    """
    if len(args) == 0:
        if self.size != 1:
            raise ValueError("can only convert an array of size 1 to a Python scalar")
        indices = tuple(0 for _ in self.shape)
    elif len(args) == 1 and isinstance(args[0], tuple):
        indices = args[0]
    elif len(args) == 1 and isinstance(args[0], (int, np.integer)):
        flat_index = int(args[0])
        if flat_index < 0:
            flat_index += int(self.size)
        if not 0 <= flat_index < int(self.size):
            raise IndexError("index out of bounds")
        indices = np.unravel_index(flat_index, self.shape)
    else:
        indices = args

    if len(indices) != self.ndim:
        raise ValueError("incorrect number of indices for array")

    normalized = []
    for axis, idx in enumerate(indices):
        if not isinstance(idx, (int, np.integer)):
            raise TypeError("an integer is required")
        pos = int(idx)
        if pos < 0:
            pos += self.shape[axis]
        if not 0 <= pos < self.shape[axis]:
            raise IndexError("index out of bounds")
        normalized.append(pos)

    origin = [0, 0, 0]
    offset = 3 - self.ndim
    for axis, pos in enumerate(normalized):
        origin[offset + axis] = pos
    return self.get(origin, [1, 1, 1]).item()


def __float__(self):
    """Convert a size-1 Array to a Python float."""
    if self.size != 1:
        raise TypeError("only length-1 arrays can be converted to Python scalars")
    return float(self.get().reshape(-1)[0])


def __int__(self):
    """Convert a size-1 Array to a Python int."""
    if self.size != 1:
        raise TypeError("only length-1 arrays can be converted to Python scalars")
    return int(self.get().reshape(-1)[0])


def __bool__(self):
    """Return the truth value of a size-1 Array."""
    if self.size != 1:
        raise ValueError(
            "The truth value of an array with more than one element is "
            "ambiguous. Use a.any() or a.all()"
        )
    return bool(self.get().reshape(-1)[0])


def _tolist(self):
    """Return the Array as a (nested) Python list."""
    return self.get().tolist()


def _clip(self, min=None, max=None, out=None):
    """Clip the values of the Array between min and max."""
    from ._tier2 import clip

    min = float("nan") if min is None else min
    max = float("nan") if max is None else max
    return clip(self, output_image=out, min_intensity=min, max_intensity=max)


def _round(self, out=None):
    """Round the values of the Array to the nearest integer."""
    from ._tier1 import round as _round_kernel

    return _round_kernel(self, output_image=out)


def _norm_axis(axis, ndim):
    if not isinstance(axis, (int, np.integer)):
        raise TypeError(f"axis must be an integer, got {type(axis).__name__}")
    ax = int(axis)
    if ax < 0:
        ax += ndim
    if not 0 <= ax < ndim:
        raise ValueError(f"axis {axis} is out of bounds for array of dimension {ndim}")
    return ax


def _norm_axes(axis, ndim):
    if not isinstance(axis, (tuple, list)):
        return (_norm_axis(axis, ndim),)
    axes = tuple(_norm_axis(ax, ndim) for ax in axis)
    if len(set(axes)) != len(axes):
        raise ValueError(f"duplicate value in axis {axis}")
    return axes


def _axis_projection(self, prefix, axis, keepdims, **kwargs):
    from . import _tier1

    axes = _norm_axes(axis, self.ndim)
    result = self
    for ax in sorted(axes, reverse=True):
        coord = "xyz"[result.ndim - 1 - ax]
        projection = getattr(_tier1, f"{prefix}_{coord}_projection")
        result = projection(result, keep_dims=keepdims, **kwargs)
    return result


def _sum_prod_dtype(dtype):
    """Return the NumPy-compatible accumulator dtype for sum/prod full reductions.

    Mirrors NumPy's integer promotion (sum/prod of an integer array is
    computed in a wider integer type), capped at 32-bit since the device
    does not support 64-bit types.
    """
    if np.issubdtype(dtype, np.floating):
        return np.float32
    if np.issubdtype(dtype, np.unsignedinteger):
        return np.uint32
    if np.issubdtype(dtype, np.signedinteger):
        return np.int32
    return np.float32


def _full_reduce(self, value, dtype, keepdims):
    if keepdims:
        return self.from_array(np.full((1,) * self.ndim, value, dtype=dtype))
    return np.dtype(dtype).type(value)


def _slice_reduce(self, reducer, axes, dtype, keepdims):
    kept = tuple(d for d in range(self.ndim) if d not in axes)
    if not kept:
        return _full_reduce(self, reducer(self), dtype, keepdims)
    out_shape = tuple(self.shape[d] for d in kept)
    values = np.empty(out_shape, dtype=dtype)
    for idx in np.ndindex(*out_shape):
        sl = [slice(None)] * self.ndim
        for pos, d in enumerate(kept):
            sl[d] = idx[pos]
        values[idx] = reducer(self[tuple(sl)])
    if keepdims:
        shape = tuple(1 if d in axes else self.shape[d] for d in range(self.ndim))
        values = values.reshape(shape)
    return self.from_array(values)


def _write_out(out, result):
    if isinstance(out, (_get_array_class(), np.ndarray)):
        np.copyto(out, np.asarray(result).astype(out.dtype))


def _max(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    out=None,
    keepdims: bool = False,
):
    """Return the maximum of the Array, or along an axis if specified."""
    from ._tier2 import maximum_of_all_pixels

    if axis is None:
        result = _full_reduce(self, maximum_of_all_pixels(self), self.dtype, keepdims)
    else:
        result = _axis_projection(self, "maximum", axis, keepdims)
    _write_out(out, result)
    return result


def _min(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    out=None,
    keepdims: bool = False,
):
    """Return the minimum of the Array, or along an axis if specified."""
    from ._tier2 import minimum_of_all_pixels

    if axis is None:
        result = _full_reduce(self, minimum_of_all_pixels(self), self.dtype, keepdims)
    else:
        result = _axis_projection(self, "minimum", axis, keepdims)
    _write_out(out, result)
    return result


def _sum(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    dtype=None,
    out=None,
    keepdims: bool = False,
):
    """Return the sum of the Array, or along an axis if specified.

    Note: integer inputs are promoted to 32-bit (int32/uint32) rather than
    NumPy's 64-bit default, since the device does not support 64-bit types.
    """
    from ._tier2 import sum_of_all_pixels

    if axis is None:
        result = _full_reduce(
            self, sum_of_all_pixels(self), _sum_prod_dtype(self.dtype), keepdims
        )
    else:
        result = _axis_projection(self, "sum", axis, keepdims)
    _write_out(out, result)
    return result


def _mean(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    dtype=None,
    out=None,
    keepdims: bool = False,
):
    """Return the mean of the Array, or along an axis if specified.

    Note: the result dtype is always float32, since the device does not
    support float64 (NumPy promotes integer input to float64).
    """
    from ._tier3 import mean_of_all_pixels

    if axis is None:
        result = _full_reduce(self, mean_of_all_pixels(self), np.float32, keepdims)
    else:
        result = _axis_projection(self, "mean", axis, keepdims)
    _write_out(out, result)
    return result


def _std(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    dtype=None,
    out=None,
    ddof: int = 0,
    keepdims: bool = False,
):
    """Return the standard deviation of the Array, or along an axis.

    Note: the result dtype is always float32, since the device does not
    support float64 (NumPy promotes integer input to float64).
    """
    from ._tier4 import standard_deviation_of_all_pixels

    if axis is None:
        result = _full_reduce(
            self,
            standard_deviation_of_all_pixels(self, ddof=ddof),
            np.float32,
            keepdims,
        )
    elif isinstance(axis, (tuple, list)):
        axes = _norm_axes(axis, self.ndim)
        if len(axes) == 1:
            result = _axis_projection(self, "std", axes[0], keepdims, ddof=ddof)
        else:
            result = _slice_reduce(
                self,
                lambda a: standard_deviation_of_all_pixels(a, ddof=ddof),
                axes,
                np.float32,
                keepdims,
            )
    else:
        result = _axis_projection(self, "std", axis, keepdims, ddof=ddof)
    _write_out(out, result)
    return result


def _var(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    dtype=None,
    out=None,
    ddof: int = 0,
    keepdims: bool = False,
):
    """Return the variance of the Array, or along an axis if specified.

    Note: the result dtype is always float32, since the device does not
    support float64 (NumPy promotes integer input to float64).
    """
    from ._tier4 import variance_of_all_pixels

    if axis is None:
        result = _full_reduce(
            self, variance_of_all_pixels(self, ddof=ddof), np.float32, keepdims
        )
    elif isinstance(axis, (tuple, list)):
        axes = _norm_axes(axis, self.ndim)
        if len(axes) == 1:
            result = _axis_projection(self, "variance", axes[0], keepdims, ddof=ddof)
        else:
            result = _slice_reduce(
                self,
                lambda a: variance_of_all_pixels(a, ddof=ddof),
                axes,
                np.float32,
                keepdims,
            )
    else:
        result = _axis_projection(self, "variance", axis, keepdims, ddof=ddof)
    _write_out(out, result)
    return result


def _prod(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    dtype=None,
    out=None,
    keepdims: bool = False,
):
    """Return the product of the Array, or along an axis if specified.

    Note: integer inputs are promoted to 32-bit (int32/uint32) rather than
    NumPy's 64-bit default, since the device does not support 64-bit types.
    """
    from ._tier2 import product_of_all_pixels

    if axis is None:
        result = _full_reduce(
            self, product_of_all_pixels(self), _sum_prod_dtype(self.dtype), keepdims
        )
    else:
        result = _axis_projection(self, "product", axis, keepdims)
    _write_out(out, result)
    return result


def _arg_reduce(self, op, axis, keepdims):
    from . import _tier1

    ax = _norm_axis(axis, self.ndim)
    coord = "xyz"[self.ndim - 1 - ax]
    kernel = getattr(_tier1, f"{coord}_position_of_{op}_{coord}_projection")
    return kernel(self, keep_dims=keepdims)


def _arg_full_reduce(self, op):
    """Return the flat (row-major) index of the global maximum/minimum.

    Delegates to CLIc's maximum_position/minimum_position, which resolves the
    position device-side (X-then-Y-then-Z, matching NumPy's first-occurrence
    tie-break) and returns only the 3 winning coordinates, never the full buffer.
    """
    from ._tier3 import maximum_position, minimum_position

    kernel = maximum_position if op == "maximum" else minimum_position
    xyz = kernel(self)[: self.ndim]
    return int(np.ravel_multi_index(tuple(int(c) for c in reversed(xyz)), self.shape))


def _argmax(self, axis: Optional[int] = None, out=None, keepdims: bool = False):
    """Return the indices of the maximum values, over all pixels or along an axis.

    Deviation from NumPy: the result dtype is uint32 instead of int64.
    """
    if axis is None:
        result = _full_reduce(
            self, _arg_full_reduce(self, "maximum"), np.uint32, keepdims
        )
    else:
        result = _arg_reduce(self, "maximum", axis, keepdims)
    _write_out(out, result)
    return result


def _argmin(self, axis: Optional[int] = None, out=None, keepdims: bool = False):
    """Return the indices of the minimum values, over all pixels or along an axis.

    Deviation from NumPy: the result dtype is uint32 instead of int64.
    """
    if axis is None:
        result = _full_reduce(
            self, _arg_full_reduce(self, "minimum"), np.uint32, keepdims
        )
    else:
        result = _arg_reduce(self, "minimum", axis, keepdims)
    _write_out(out, result)
    return result


def _any(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    out=None,
    keepdims: bool = False,
):
    """Test whether any array element along a given axis evaluates to True."""
    result = _max(self != 0, axis=axis, keepdims=keepdims)
    if axis is None and not keepdims:
        result = bool(result)
    _write_out(out, result)
    return result


def _all(
    self,
    axis: Optional[Union[int, tuple, list]] = None,
    out=None,
    keepdims: bool = False,
):
    """Test whether all array elements along a given axis evaluate to True."""
    result = _min(self != 0, axis=axis, keepdims=keepdims)
    if axis is None and not keepdims:
        result = bool(result)
    _write_out(out, result)
    return result


def _align(x1, x2):
    """Validate array-array broadcast compatibility without host transfers.

    Scalars and other non-array operands pass through untouched. ``ndarray``
    operands are converted to backend arrays. Array operands (including
    size-1 arrays) are left as-is; only shape compatibility is checked via
    ``np.broadcast_shapes`` so incompatible operands still raise early.
    Actual broadcasting is performed device-side by the CLIc backend.
    """
    ArrayCls = _get_array_class()
    if isinstance(x2, np.ndarray):
        x2 = ArrayCls.from_array(x2)
    if not isinstance(x2, ArrayCls):
        return x1, x2
    np.broadcast_shapes(x1.shape, x2.shape)
    return x1, x2


def _align_inplace(x1, x2):
    """Validate x2 is broadcastable to x1's shape for in-place operations.

    Unlike `_align`, x1 is never replaced, since in-place operations must
    write into the original array. No host transfer happens; broadcasting is
    performed device-side by the CLIc backend. Raises ValueError if x2's
    shape cannot be broadcast to x1's shape.
    """
    ArrayCls = _get_array_class()
    if isinstance(x2, np.ndarray):
        x2 = ArrayCls.from_array(x2)
    if not isinstance(x2, ArrayCls):
        return x2
    shape = np.broadcast_shapes(x1.shape, x2.shape)
    if shape != x1.shape:
        raise ValueError(
            f"cannot broadcast shape {x2.shape} into in-place operand of shape {x1.shape}"
        )
    return x2


def __pos__(x1):
    """Unary plus, propagates the sign of the argument."""
    return x1.__mul__(1)


def __neg__(x1):
    """Unary minus, returns an array with the negative of the elements of the argument."""
    return x1.__mul__(-1)


def __add__(x1, x2):
    """Addition of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(x1, scalar=x2)
    return add_images_weighted(x1, x2, factor1=1, factor2=1)


def __iadd__(x1, x2):
    """Addition of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted, copy

    temp = copy(x1)
    x2 = _align_inplace(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(temp, output_image=x1, scalar=x2)
    return add_images_weighted(temp, x2, output_image=x1, factor1=1, factor2=1)


def __radd__(x1, x2):
    """Addition of two arrays."""
    return x1.__add__(x2)


def __sub__(x1, x2):
    """Subtraction of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(x1, scalar=-x2)
    return add_images_weighted(x1, x2, factor1=1, factor2=-1)


def __isub__(x1, x2):
    """Subtraction of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted, copy

    temp = copy(x1)
    x2 = _align_inplace(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(temp, output_image=x1, scalar=-x2)
    return add_images_weighted(temp, x2, output_image=x1, factor1=1, factor2=-1)


def __rsub__(x1, x2):
    """Subtraction of two arrays."""
    from ._tier1 import add_images_weighted, subtract_image_from_scalar

    if isinstance(x2, _supported_numeric_types):
        return subtract_image_from_scalar(x1, scalar=x2)
    return add_images_weighted(x1, x2, factor1=-1, factor2=1)


def __div__(x1, x2):
    """Division of two arrays (deprecated Python 2 alias for __truediv__)."""
    import warnings

    warnings.warn(
        "__div__ is deprecated, use __truediv__ instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return x1.__truediv__(x2)


def __truediv__(x1, x2):
    """Division of two arrays."""
    from ._tier1 import divide_images, multiply_image_and_scalar

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        if x2 == 0:
            import warnings

            warnings.warn(
                "divide by zero encountered in divide", RuntimeWarning, stacklevel=2
            )
            return multiply_image_and_scalar(x1, scalar=float("inf"))
        return multiply_image_and_scalar(x1, scalar=1.0 / x2)
    return divide_images(x1, x2)


def __idiv__(x1, x2):
    """Division of two arrays (deprecated Python 2 alias for __itruediv__)."""
    import warnings

    warnings.warn(
        "__idiv__ is deprecated, use __itruediv__ instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return x1.__itruediv__(x2)


def __itruediv__(x1, x2):
    """Division of two arrays."""
    from ._tier1 import copy, divide_images, multiply_image_and_scalar

    temp = copy(x1)
    x2 = _align_inplace(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        if x2 == 0:
            import warnings

            warnings.warn(
                "divide by zero encountered in divide", RuntimeWarning, stacklevel=2
            )
            return multiply_image_and_scalar(temp, x1, scalar=float("inf"))
        return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
    return divide_images(temp, x2, x1)


def __rdiv__(x1, x2):
    """Division of two arrays (deprecated Python 2 alias for __rtruediv__)."""
    import warnings

    warnings.warn(
        "__rdiv__ is deprecated, use __rtruediv__ instead",
        DeprecationWarning,
        stacklevel=2,
    )
    return x1.__rtruediv__(x2)


def __rtruediv__(x1, x2):
    """Division of two arrays."""
    from ._tier1 import divide_images, divide_scalar_by_image

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return divide_scalar_by_image(x1, scalar=x2)
    return divide_images(x2, x1)


def __mul__(x1, x2):
    """Multiplication of two arrays."""
    from ._tier1 import multiply_image_and_scalar, multiply_images

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return multiply_image_and_scalar(x1, scalar=x2)
    return multiply_images(x1, x2)


def __rmul__(x1, x2):
    """Multiplication of two arrays."""
    return x1.__mul__(x2)


def __imul__(x1, x2):
    """Multiplication of two arrays."""
    from ._tier1 import copy, multiply_image_and_scalar, multiply_images

    temp = copy(x1)
    x2 = _align_inplace(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return multiply_image_and_scalar(temp, x1, scalar=x2)
    return multiply_images(temp, x2, x1)


def _bool_out(x1):
    """Create a uint8 output array, the device stand-in for bool results."""
    from ._memory import create_like

    return create_like(x1, dtype=np.uint8)


def _unsupported_operand(x2):
    """Return True for operands that cannot be compared element-wise on device."""
    ArrayCls = _get_array_class()
    if isinstance(x2, (ArrayCls, np.ndarray)):
        return False
    return not isinstance(x2, _supported_numeric_types)


def maximum(x1, x2):
    """Element-wise maximum of an array and an array or scalar."""
    from ._tier1 import maximum_image_and_scalar, maximum_images

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return maximum_image_and_scalar(x1, scalar=x2)
    return maximum_images(x1, x2)


def minimum(x1, x2):
    """Element-wise minimum of an array and an array or scalar."""
    from ._tier1 import minimum_image_and_scalar, minimum_images

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return minimum_image_and_scalar(x1, scalar=x2)
    return minimum_images(x1, x2)


def logical_and(x1, x2):
    """Element-wise logical AND (truthiness: all non-zero values treated as True)."""
    from ._tier1 import binary_and

    x1, x2 = _align(x1, x2)
    return binary_and(x1, x2)


def logical_or(x1, x2):
    """Element-wise logical OR (truthiness: all non-zero values treated as True)."""
    from ._tier1 import binary_or

    x1, x2 = _align(x1, x2)
    return binary_or(x1, x2)


def logical_xor(x1, x2):
    """Element-wise logical XOR (truthiness: all non-zero values treated as True)."""
    from ._tier1 import binary_xor

    x1, x2 = _align(x1, x2)
    return binary_xor(x1, x2)


def rint(x1):
    """Element-wise round to nearest integer."""
    from ._execute import evaluate

    return evaluate("rint(a)", parameters={"a": x1})


def isnan(x1):
    """Element-wise check for NaN values."""
    from ._execute import evaluate

    return evaluate("isnan(a)", parameters={"a": x1})


def isfinite(x1):
    """Element-wise check for finite values."""
    from ._execute import evaluate

    return evaluate("isfinite(a)", parameters={"a": x1})


def atan2(x1, x2):
    """Element-wise arctangent of x1/x2, using the signs of both arguments to determine the quadrant."""
    from ._execute import evaluate

    x1, x2 = _align(x1, x2)
    return evaluate("atan2(a, b)", parameters={"a": x1, "b": x2})


def _atan2_reversed(x1, x2):
    """Element-wise arctan2(x2, x1), used to handle reflected `arctan2` ufunc dispatch."""
    return atan2(x2, x1)


def __gt__(x1, x2):
    """Greater than comparison of two arrays."""
    from ._tier1 import greater, greater_constant

    if _unsupported_operand(x2):
        return NotImplemented
    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return greater_constant(x1, _bool_out(x1), scalar=x2)
    return greater(x1, x2, _bool_out(x1))


def __ge__(x1, x2):
    """Greater than or equal comparison of two arrays."""
    from ._tier1 import greater_or_equal, greater_or_equal_constant

    if _unsupported_operand(x2):
        return NotImplemented
    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return greater_or_equal_constant(x1, _bool_out(x1), scalar=x2)
    return greater_or_equal(x1, x2, _bool_out(x1))


def __lt__(x1, x2):
    """Less than comparison of two arrays."""
    from ._tier1 import smaller, smaller_constant

    if _unsupported_operand(x2):
        return NotImplemented
    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return smaller_constant(x1, _bool_out(x1), scalar=x2)
    return smaller(x1, x2, _bool_out(x1))


def __le__(x1, x2):
    """Less than or equal comparison of two arrays."""
    from ._tier1 import smaller_or_equal, smaller_or_equal_constant

    if _unsupported_operand(x2):
        return NotImplemented
    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return smaller_or_equal_constant(x1, _bool_out(x1), scalar=x2)
    return smaller_or_equal(x1, x2, _bool_out(x1))


def __eq__(x1, x2):
    """Equal comparison of two arrays."""
    from ._tier1 import equal, equal_constant

    if _unsupported_operand(x2):
        return NotImplemented
    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return equal_constant(x1, _bool_out(x1), scalar=x2)
    return equal(x1, x2, _bool_out(x1))


def __ne__(x1, x2):
    """Not equal comparison of two arrays."""
    from ._tier1 import not_equal, not_equal_constant

    if _unsupported_operand(x2):
        return NotImplemented
    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return not_equal_constant(x1, _bool_out(x1), scalar=x2)
    return not_equal(x1, x2, _bool_out(x1))


def __pow__(x1, x2):
    """Power function of two arrays."""
    from ._tier1 import power, power_images

    x1, x2 = _align(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return power(x1, scalar=x2)
    return power_images(x1, x2)


def __ipow__(x1, x2):
    """Power function of two arrays."""
    from ._tier1 import copy, power, power_images

    temp = copy(x1)
    x2 = _align_inplace(x1, x2)
    if isinstance(x2, _supported_numeric_types):
        return power(temp, x1, scalar=x2)
    return power_images(temp, x2, x1)


def __rpow__(x1, x2):
    """Power function of two arrays (reflected)."""
    from ._execute import evaluate

    return evaluate("pow(b, a)", parameters={"b": x2, "a": x1})


def __abs__(x1):
    """Element-wise absolute value."""
    from ._tier1 import absolute

    return absolute(x1)


def __floordiv__(x1, x2):
    """Floor division of two arrays."""
    from ._tier1 import floor

    return floor(x1.__truediv__(x2))


def __rfloordiv__(x1, x2):
    """Floor division of two arrays (reflected)."""
    from ._tier1 import floor

    return floor(x1.__rtruediv__(x2))


def __ifloordiv__(x1, x2):
    """In-place floor division of two arrays."""
    from ._tier1 import copy

    return copy(x1.__floordiv__(x2), x1)


def __mod__(x1, x2):
    """Remainder of the floor division of two arrays."""
    from ._execute import evaluate

    return evaluate("a - floor(a/b)*b", parameters={"a": x1, "b": x2})


def __rmod__(x1, x2):
    """Remainder of the floor division of two arrays (reflected)."""
    from ._execute import evaluate

    return evaluate("b - floor(b/a)*a", parameters={"b": x2, "a": x1})


def __imod__(x1, x2):
    """In-place remainder of the floor division of two arrays."""
    from ._tier1 import copy

    return copy(x1.__mod__(x2), x1)


def _binarize(x1, value):
    """Return value as a device array matching x1 for bitwise/logical kernels."""
    ArrayCls = _get_array_class()
    if isinstance(value, ArrayCls):
        return _align(x1, value)[1]
    return ArrayCls.from_array(np.full(x1.shape, value, dtype=np.uint8))


def __and__(x1, x2):
    """Element-wise logical AND (mask arrays)."""
    from ._tier1 import binary_and

    return binary_and(x1, _binarize(x1, x2))


def __or__(x1, x2):
    """Element-wise logical OR (mask arrays)."""
    from ._tier1 import binary_or

    return binary_or(x1, _binarize(x1, x2))


def __xor__(x1, x2):
    """Element-wise logical XOR (mask arrays)."""
    from ._tier1 import binary_xor

    return binary_xor(x1, _binarize(x1, x2))


def __invert__(x1):
    """Element-wise logical NOT (mask arrays)."""
    from ._tier1 import binary_not

    return binary_not(x1)


def log1p(x):
    """Compute log(1 + x) element-wise."""
    from ._execute import evaluate

    return evaluate("log(a + 1)", parameters={"a": x})


def expm1(x):
    """Compute exp(x) - 1 element-wise."""
    from ._execute import evaluate

    return evaluate("exp(a) - 1", parameters={"a": x})


def hypot(x1, x2):
    """Compute sqrt(x1**2 + x2**2) element-wise."""
    from ._execute import evaluate

    x1, x2 = _align(x1, x2)
    return evaluate("sqrt(a*a + b*b)", parameters={"a": x1, "b": x2})


def __iter__(self):
    """Iterate over the first dimension of the array."""

    class MyIterator:
        def __init__(self, image):
            self.image = image
            self._iter_index = 0

        def __next__(self):
            if not hasattr(self, "_iter_index"):
                self._iter_index = 0
            if self._iter_index < self.image.shape[0]:
                result = self.image[self._iter_index]
                self._iter_index = self._iter_index + 1
                return result
            else:
                raise StopIteration

    return MyIterator(self)


# adapted from https://github.com/napari/napari/blob/d6bc683b019c4a3a3c6e936526e29bbd59cca2f4/napari/utils/notebook_display.py#L54-L73
def _figure_to_png(fig):
    """Standalone helper — convert a Figure to PNG bytes."""
    from io import BytesIO

    with BytesIO() as file_obj:
        fig.savefig(file_obj, format="png")
        file_obj.seek(0)
        return file_obj.read()


def _png_to_html(png):
    """Standalone helper — convert PNG bytes to an HTML img tag."""
    import base64

    url = "data:image/png;base64," + base64.b64encode(png).decode("utf-8")
    return f'<img src="{url}"></img>'


def __repr_html__(self):
    """HTML representation of the image object for IPython."""
    import matplotlib.pyplot as plt
    import numpy as np

    from ._functionalities import imshow

    size_in_pixels = np.prod(self.size)
    size_in_bytes = size_in_pixels * self.dtype.itemsize
    labels = self.dtype == np.uint32

    if len(self.shape) in (2, 3) and size_in_pixels >= 100:
        with plt.ioff():
            imshow(self, labels=labels, continue_drawing=True, colorbar=not labels)
            fig = plt.gcf()
            image = _png_to_html(_figure_to_png(fig))
            plt.close(fig)
    else:
        return "<pre>" + repr(self) + "</pre>"

    raw_size_in_bytes = size_in_bytes
    units = ["B", "kB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    while size_in_bytes > 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024
        unit_index += 1
    size = "{:.1f}".format(size_in_bytes) + " " + units[unit_index]

    histogram_html = ""
    if raw_size_in_bytes < 100 * 1024 * 1024:
        if not labels:

            from ._tier3 import histogram

            num_bins = 32
            h = np.asarray(
                histogram(
                    input_image=self,
                    num_bins=num_bins,
                    minimum_intensity=self.min(),
                    maximum_intensity=self.max(),
                )
            )
            with plt.ioff():
                plt.figure(figsize=(1.8, 1.2))
                plt.bar(range(0, len(h)), h)
                frame1 = plt.gca()
                frame1.axes.xaxis.set_ticklabels([])
                frame1.axes.yaxis.set_ticklabels([])
                plt.tick_params(left=False, bottom=False)
                hist_fig = plt.gcf()
                histogram_html = _png_to_html(_figure_to_png(hist_fig))
                plt.close(hist_fig)

        min_max = (
            "<tr><td>min</td><td>"
            + str(self.min())
            + "</td></tr>"
            + "<tr><td>max</td><td>"
            + str(self.max())
            + "</td></tr>"
        )
    else:
        min_max = ""

    all = [
        "<table>",
        "<tr>",
        "<td>",
        image,
        "</td>",
        '<td style="text-align: center; vertical-align: top;">',
        '<b><a href="https://github.com/clEsperanto/pyclesperanto" target="_blank">cle._</a> image</b><br/>',
        "<table>",
        "<tr><td>shape</td><td>"
        + str(self.shape).replace(" ", "&nbsp;")
        + "</td></tr>",
        "<tr><td>dtype</td><td>" + str(self.dtype) + "</td></tr>",
        "<tr><td>size</td><td>" + size + "</td></tr>",
        min_max,
        "</table>",
        histogram_html,
        "</td>",
        "</tr>",
        "</table>",
    ]
    return "\n".join(all)


def _is_fancy_index(index, ndim):
    """Return True if *index* is a sequence of coordinate arrays (fancy indexing)."""
    if not isinstance(index, (tuple, list, np.ndarray)):
        return False
    if len(index) != ndim:
        return False
    first = index[0]
    return first is not None and isinstance(first, (tuple, list, np.ndarray))


def _parse_index(index, shape):
    ndim = len(shape)

    if not isinstance(index, tuple):
        index = (index,)

    if len(index) > ndim:
        raise IndexError(
            f"too many indices for array: array is {ndim}-dimensional, "
            f"but {len(index)} were indexed"
        )

    # Expand ellipsis BEFORE determining which axes are scalar-indexed
    index = _process_ellipsis_into_slice(index, shape)
    index = _trim_index_to_shape(index, shape)

    squeeze_axes = [
        i for i, idx in enumerate(index) if isinstance(idx, (int, float, np.integer))
    ]

    slice_list = [[0, s, 1] for s in shape]
    for i, idx in enumerate(index):
        if isinstance(idx, slice):
            slice_list[i] = [idx.start, idx.stop, idx.step]
        elif isinstance(idx, _INTEGER_TYPES):
            slice_list[i] = [
                idx,
                idx + 1 if idx >= 0 else idx - 1,
                None,
            ]

    _, range_x, range_y, range_z = _compute_range(slice_list, shape)

    origin = [range_z[0], range_y[0], range_x[0]]
    region = [
        abs(range_z[1] - range_z[0]) or 1,
        abs(range_y[1] - range_y[0]) or 1,
        abs(range_x[1] - range_x[0]) or 1,
    ]
    steps = [range_z[2], range_y[2], range_x[2]]

    return origin, region, steps, squeeze_axes, range_x, range_y, range_z


def _compute_dst_shape(region, steps, squeeze_axes, ndim):
    """Compute the output shape after slicing, honouring squeezed (scalar-indexed) axes."""
    # Full 3-D stepped shape
    full = [-(-abs(r) // abs(s)) for r, s in zip(region, steps)]
    # Map back to the original ndim (region is always 3-D internally)
    offset = 3 - ndim
    out = full[offset:]
    # Drop axes that were scalar-indexed
    return [s for i, s in enumerate(out) if i not in squeeze_axes]


def _reshape_result(result, dst_shape, region):
    if result.shape == tuple(dst_shape):
        return result

    ndim = len(dst_shape)

    # Pad to 3D for the C++ reshape call
    while len(dst_shape) < 3:
        dst_shape.insert(0, 1)

    reshape = getattr(type(result), "_native_reshape", None) or type(result).reshape
    return reshape(
        result,
        width=int(dst_shape[-1]),
        height=int(dst_shape[-2]),
        depth=int(dst_shape[-3]),
        dimension=ndim,
    )


# ---------------------------------------------------------------------------
# Fancy-index helpers
# ---------------------------------------------------------------------------


def _swap_first_last(index):
    """Swap first and last coordinate arrays (X↔Z / X↔Y) for clesperanto's X-Y-Z order."""
    index = list(index)
    index[0], index[-1] = index[-1], index[0]
    return index


def _fancy_getitem(self, index):
    if len(index[0]) == 0:
        return []

    from ._memory import push
    from ._tier1 import read_values_from_positions

    positions = push(np.asarray(_swap_first_last(index)))
    return read_values_from_positions(self, positions)


def _fancy_setitem(self, index, value):
    if len(index[0]) == 0:
        return

    from ._memory import create, push
    from ._tier1 import write_values_to_positions
    from ._tier2 import concatenate_along_y

    positions = push(np.asarray(_swap_first_last(index)))
    num_positions = positions.shape[-1]

    if isinstance(value, (int, float)):
        scalar = value  # save before reassigning
        value_shape = [1] * len(self.shape)
        value_shape[-1] = num_positions
        value = create(value_shape)
        value.fill(scalar)

    values_and_positions = concatenate_along_y(positions, value)
    write_values_to_positions(values_and_positions, self)


# ---------------------------------------------------------------------------
# Public operators
# ---------------------------------------------------------------------------


def __getitem__(self, index):
    """Get a pixel value or a region of interest from the Array."""
    if (
        isinstance(index, list)
        and len(index) == self.ndim
        and all(isinstance(i, (int, np.integer)) for i in index)
    ):
        index = tuple(index)
    if _is_fancy_index(index, len(self.shape)):
        return _fancy_getitem(self, index)

    # Fast path: all-integer index → single pixel, skip all parsing
    if not isinstance(index, tuple):
        index = (index,)
    if len(index) == self.ndim and all(isinstance(i, (int, np.integer)) for i in index):
        # Reverse to x,y,z order for the C++ side
        origin = [0, 0, 0]
        offset = 3 - self.ndim
        for i, idx in enumerate(index):
            origin[offset + i] = int(idx) if idx >= 0 else self.shape[i] + int(idx)
        return self.get(origin, [1, 1, 1]).item()

    origin, region, steps, squeeze_axes, range_x, range_y, range_z = _parse_index(
        index, self.shape
    )

    total = region[0] * region[1] * region[2]
    if total == 1:
        return self.get(origin, region).item()

    from ._tier1 import gather

    result = gather(
        self,
        start_x=range_x[0],
        stop_x=range_x[1],
        step_x=range_x[2],
        start_y=range_y[0],
        stop_y=range_y[1],
        step_y=range_y[2],
        start_z=range_z[0],
        stop_z=range_z[1],
        step_z=range_z[2],
    )

    dst_shape = _compute_dst_shape(region, steps, squeeze_axes, self.ndim)
    return _reshape_result(result, dst_shape, region)


def __setitem__(self, index, value):
    """Set a pixel value or a region of interest in the Array."""
    if _is_fancy_index(index, len(self.shape)):
        _fancy_setitem(self, index, value)
        return

    if not isinstance(value, (_get_array_class(), np.ndarray)):
        value = np.asarray(value)

    origin, region, steps, squeeze_axes, range_x, range_y, range_z = _parse_index(
        index, self.shape
    )
    total = region[0] * region[1] * region[2]

    if any(s != 1 for s in steps):
        from ._memory import create, push
        from ._tier1 import scatter

        full = [-(-abs(r) // abs(s)) for r, s in zip(region, steps)]
        if value.size == 1:
            source = create(full, dtype=self.dtype, device=self.device)
            source.fill(float(np.asarray(value).ravel()[0]))
        else:
            data = (
                value.get()
                if isinstance(value, _get_array_class())
                else np.asarray(value)
            )
            data = np.broadcast_to(data, full).astype(self.dtype)
            source = push(data, device=self.device)
        scatter(
            source,
            self,
            start_x=range_x[0],
            stop_x=range_x[1],
            step_x=range_x[2],
            start_y=range_y[0],
            stop_y=range_y[1],
            step_y=range_y[2],
            start_z=range_z[0],
            stop_z=range_z[1],
            step_z=range_z[2],
        )
        return

    if value.size == 1:
        if total > 1:
            value = np.broadcast_to(np.asarray(value).ravel(), total)
            value = value.reshape(region)
        self.set(value, origin, region)
        return

    if isinstance(value, _get_array_class()):
        if self.dtype == value.dtype:
            value._copy_region(self, (0, 0, 0), origin, region)
        else:
            from ._tier1 import paste

            paste(
                value,
                self,
                index_x=origin[2],
                index_y=origin[1],
                index_z=origin[0],
            )
    else:
        self.set(value, origin, region)
