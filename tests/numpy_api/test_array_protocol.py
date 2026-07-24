"""Tests for the NumPy conversion protocol (__array__) - NumPy >= 2.0 signature."""

import numpy as np
import pytest

import pyclesperanto as cle


def test_asarray_roundtrip(gpu_backend):
    data = np.asarray([[1, 2], [3, 4]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = np.asarray(arr)
    assert isinstance(result, np.ndarray)
    assert result.dtype == data.dtype
    assert np.array_equal(result, data)


def test_array_with_dtype(gpu_backend):
    data = np.asarray([[1.5, 2.5]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = np.asarray(arr, dtype=np.int32)
    assert result.dtype == np.int32
    assert np.array_equal(result, data.astype(np.int32))


def test_array_copy_true(gpu_backend):
    data = np.asarray([1, 2, 3], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = np.array(arr, copy=True)
    assert np.array_equal(result, data)


def test_array_copy_false_raises(gpu_backend):
    data = np.asarray([1, 2, 3], dtype=np.float32)
    arr = cle.Array.from_array(data)
    with pytest.raises(ValueError):
        arr.__array__(copy=False)
    with pytest.raises(ValueError):
        np.asarray(arr, copy=False)
