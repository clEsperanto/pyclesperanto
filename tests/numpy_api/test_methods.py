"""NumPy-style methods on device arrays (Phase 3 of the numpy compat plan)."""

import numpy as np
import pytest

import pyclesperanto as cle


def test_copy_returns_independent_array(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    dup = arr.copy()
    assert dup is not arr
    dup[0, 0] = -1
    np.testing.assert_array_equal(np.asarray(arr), data)
    assert np.asarray(dup)[0, 0] == -1


def test_copy_region_form_still_available(gpu_backend):
    dst = cle.Array.from_array(np.zeros((2, 3), dtype=np.float32))
    src = cle.Array.from_array(np.ones((1, 2), dtype=np.float32))
    dst[0:1, 0:2] = src
    result = np.asarray(dst)
    np.testing.assert_array_equal(result[0, :2], [1.0, 1.0])
    assert result[1, 0] == 0.0


def test_squeeze_all(gpu_backend):
    arr = cle.Array.empty((1, 3), dtype=np.float32)
    assert arr.squeeze().shape == (3,)


def test_squeeze_axis(gpu_backend):
    data = np.zeros((1, 2, 3), dtype=np.float32)
    arr = cle.Array.from_array(data)
    assert arr.squeeze(0).shape == (2, 3)
    assert arr.squeeze(axis=0).shape == (2, 3)


def test_squeeze_invalid_axis_raises(gpu_backend):
    arr = cle.Array.from_array(np.zeros((1, 2, 3), dtype=np.float32))
    with pytest.raises(ValueError):
        arr.squeeze(1)


def test_squeeze_noop(gpu_backend):
    arr = cle.Array.from_array(np.zeros((2, 3), dtype=np.float32))
    assert arr.squeeze() is arr


def test_ravel(gpu_backend):
    data = np.arange(24, dtype=np.float32).reshape(2, 3, 4)
    arr = cle.Array.from_array(data)
    result = arr.ravel()
    assert result.shape == (24,)
    np.testing.assert_array_equal(np.asarray(result), data.ravel())


def test_flatten_is_a_copy(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    flat = arr.flatten()
    assert flat.shape == (6,)
    flat[0] = -1
    np.testing.assert_array_equal(np.asarray(arr), data)


def test_item(gpu_backend):
    arr = cle.Array.from_array(np.asarray([[3.5]], dtype=np.float32))
    value = arr.item()
    assert value == 3.5
    assert isinstance(value, float)


def test_item_with_index(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    assert arr.item(4) == data.item(4)


def test_tolist(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    assert arr.tolist() == data.tolist()


def test_fill(gpu_backend):
    arr = cle.Array.empty((2, 3), dtype=np.float32)
    arr.fill(7)
    np.testing.assert_array_equal(np.asarray(arr), np.full((2, 3), 7, dtype=np.float32))


def test_clip(gpu_backend):
    data = np.arange(10, dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.clip(2, 7)), data.clip(2, 7))


def test_round(gpu_backend):
    data = np.asarray([1.4, 2.6, -1.4, 3.1], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.round()), np.rint(data))


def test_clip_min_only(gpu_backend):
    data = np.arange(10, dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.clip(min=4)), data.clip(min=4))
    np.testing.assert_array_equal(np.asarray(arr.clip(max=4)), data.clip(max=4))


def test_len_matches_first_dim(gpu_backend):
    data = np.zeros((4, 2, 3), dtype=np.float32)
    arr = cle.Array.from_array(data)
    assert len(arr) == len(data)


def test_iteration_yields_subarrays(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    rows = list(arr)
    assert len(rows) == 2
    for row, expected in zip(rows, data):
        np.testing.assert_array_equal(np.asarray(row), expected)


def test_asarray_with_dtype_conversion(gpu_backend):
    data = np.asarray([[1.7, 2.2], [3.9, 4.1]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = np.asarray(arr, dtype=np.int32)
    np.testing.assert_array_equal(result, np.asarray(data, dtype=np.int32))
    assert result.dtype == np.int32


def test_reshape_tuple(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    result = arr.reshape((3, 2))
    np.testing.assert_allclose(np.asarray(result), data.reshape((3, 2)))


def test_reshape_flatten(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    result = arr.reshape(-1)
    np.testing.assert_allclose(np.asarray(result), data.reshape(-1))


def test_reshape_varargs_shape_order(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    result = arr.reshape(3, 2)
    assert result.shape == (3, 2)
