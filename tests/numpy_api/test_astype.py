"""Tests for NumPy-aligned astype semantics (copy=True default, no-op casting=)."""

import numpy as np
import pytest

import pyclesperanto as cle


def test_astype_copies_by_default(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    result = arr.astype(np.float32)
    assert result is not arr
    assert result.dtype == arr.dtype
    np.testing.assert_array_equal(np.asarray(result), np.asarray(arr))


def test_astype_copy_is_independent(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    result = arr.astype(np.float32)
    result[0] = 5.0
    assert np.asarray(arr)[0] == 1.0


def test_astype_copy_false_same_dtype_returns_self(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    assert arr.astype(np.float32, copy=False) is arr


def test_astype_copy_false_different_dtype_converts(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    result = arr.astype(np.int32, copy=False)
    assert result is not arr
    assert result.dtype == np.int32


def test_astype_conversion_values(gpu_backend):
    data = np.asarray([[1.7, 2.2], [3.9, 4.5]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = arr.astype(np.uint8)
    assert result.dtype == np.uint8
    np.testing.assert_array_equal(np.asarray(result), data.astype(np.uint8))


def test_astype_accepts_casting_kwarg(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    result = arr.astype(np.int32, casting="same_kind")
    assert result.dtype == np.int32


def test_astype_unsupported_dtype_raises(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    with pytest.raises(ValueError):
        arr.astype(np.str_)
