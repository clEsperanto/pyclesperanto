"""NumPy-style reductions on device arrays (Phase 4 of the numpy compat plan)."""

import numpy as np
import pytest

import pyclesperanto as cle

REDUCTIONS = ["sum", "min", "max", "mean", "std", "var", "prod", "argmin", "argmax"]

MULTI_AXIS_REDUCTIONS = ["sum", "min", "max", "mean", "std", "var", "prod"]


@pytest.fixture
def data3d():
    return np.arange(24, dtype=np.float32).reshape(2, 3, 4)


@pytest.fixture
def data2d():
    return np.asarray([[1.0, 5.0, 2.0], [7.0, 3.0, 4.0]], dtype=np.float32)


@pytest.mark.parametrize("name", REDUCTIONS)
@pytest.mark.parametrize("axis", [0, 1, 2, -1, -2, -3])
@pytest.mark.parametrize("keepdims", [False, True])
def test_axis_reduction_3d(gpu_backend, data3d, name, axis, keepdims):
    arr = cle.Array.from_array(data3d)
    expected = getattr(np, name)(data3d, axis=axis, keepdims=keepdims)
    result = getattr(arr, name)(axis=axis, keepdims=keepdims)
    assert result.shape == expected.shape
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-4)


@pytest.mark.parametrize("name", REDUCTIONS)
@pytest.mark.parametrize("axis", [0, 1, -1, -2])
@pytest.mark.parametrize("keepdims", [False, True])
def test_axis_reduction_2d(gpu_backend, data2d, name, axis, keepdims):
    arr = cle.Array.from_array(data2d)
    expected = getattr(np, name)(data2d, axis=axis, keepdims=keepdims)
    result = getattr(arr, name)(axis=axis, keepdims=keepdims)
    assert result.shape == expected.shape
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-4)


@pytest.mark.parametrize("name", MULTI_AXIS_REDUCTIONS)
@pytest.mark.parametrize("axis", [(0, 1), (1, 2), (0, 2), (2, 1), (-1, -2)])
@pytest.mark.parametrize("keepdims", [False, True])
def test_multi_axis_reduction_3d(gpu_backend, data3d, name, axis, keepdims):
    arr = cle.Array.from_array(data3d)
    expected = getattr(np, name)(data3d, axis=axis, keepdims=keepdims)
    result = getattr(arr, name)(axis=axis, keepdims=keepdims)
    assert result.shape == expected.shape
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-4)


def test_multi_axis_accepts_list(gpu_backend, data3d):
    arr = cle.Array.from_array(data3d)
    expected = data3d.sum(axis=(0, 1))
    result = arr.sum(axis=[0, 1])
    assert result.shape == expected.shape
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-4)


def test_multi_axis_sum_projection(gpu_backend, data3d):
    arr = cle.Array.from_array(data3d)
    result = arr.sum(axis=(1, 2))
    expected = data3d.sum(axis=(1, 2))
    assert result.shape == expected.shape
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-4)


@pytest.mark.parametrize("name", ["argmin", "argmax"])
def test_multi_axis_argreduce_raises(gpu_backend, data3d, name):
    arr = cle.Array.from_array(data3d)
    with pytest.raises(TypeError):
        getattr(arr, name)(axis=(0, 1))


def test_multi_axis_duplicate_raises(gpu_backend, data3d):
    arr = cle.Array.from_array(data3d)
    with pytest.raises(ValueError):
        arr.sum(axis=(1, 1))


@pytest.mark.parametrize("name", REDUCTIONS)
def test_full_reduction_returns_scalar(gpu_backend, data3d, name):
    arr = cle.Array.from_array(data3d)
    expected = getattr(np, name)(data3d)
    result = getattr(arr, name)()
    assert np.isscalar(result)
    np.testing.assert_allclose(result, expected, rtol=1e-4)


@pytest.mark.parametrize("name", REDUCTIONS)
def test_full_reduction_keepdims(gpu_backend, data3d, name):
    arr = cle.Array.from_array(data3d)
    expected = getattr(np, name)(data3d, keepdims=True)
    result = getattr(arr, name)(keepdims=True)
    assert result.shape == expected.shape
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-4)


def test_full_min_max_keep_dtype(gpu_backend):
    data = np.asarray([[1, 5], [7, 3]], dtype=np.uint8)
    arr = cle.Array.from_array(data)
    assert arr.max() == 7
    assert arr.max().dtype == np.uint8
    assert arr.min() == 1
    assert arr.min().dtype == np.uint8


def test_mean(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    assert np.isclose(float(arr.mean()), data.mean())


def test_sum_keepdims(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = arr.sum(axis=0, keepdims=True)
    assert result.shape == (1, 2)


def test_argmax_dtype(gpu_backend, data2d):
    arr = cle.Array.from_array(data2d)
    assert arr.argmax(axis=0).dtype == np.uint32
    assert arr.argmax().dtype == np.uint32


def test_out_parameter(gpu_backend, data2d):
    arr = cle.Array.from_array(data2d)
    out = np.zeros(3, dtype=np.float32)
    arr.sum(axis=0, out=out)
    np.testing.assert_allclose(out, data2d.sum(axis=0))


def test_invalid_axis_raises(gpu_backend, data2d):
    arr = cle.Array.from_array(data2d)
    with pytest.raises(ValueError):
        arr.sum(axis=2)
    with pytest.raises(ValueError):
        arr.sum(axis=-3)
    with pytest.raises(TypeError):
        arr.sum(axis=1.5)


def test_empty_axis_tuple_is_noop(gpu_backend, data2d):
    arr = cle.Array.from_array(data2d)
    result = arr.sum(axis=())
    np.testing.assert_allclose(np.asarray(result), data2d.sum(axis=()))


@pytest.mark.parametrize("func", [np.sum, np.max, np.min, np.prod])
def test_numpy_free_function_dispatch(gpu_backend, data3d, func):
    arr = cle.Array.from_array(data3d)
    np.testing.assert_allclose(func(arr), func(data3d), rtol=1e-5)


@pytest.mark.parametrize("func", [np.sum, np.max, np.min])
def test_numpy_free_function_dispatch_axis(gpu_backend, data3d, func):
    arr = cle.Array.from_array(data3d)
    result = func(arr, axis=1)
    np.testing.assert_allclose(np.asarray(result), func(data3d, axis=1), rtol=1e-5)


def test_numpy_argmax_dispatch(gpu_backend, data2d):
    arr = cle.Array.from_array(data2d)
    assert int(np.argmax(arr)) == int(np.argmax(data2d))


def test_mean_of_comparison_mask(gpu_backend, data2d):
    arr = cle.Array.from_array(data2d)
    threshold = float(data2d.mean())
    result = (arr > threshold).mean()
    np.testing.assert_allclose(result, (data2d > threshold).mean(), rtol=1e-5)


@pytest.mark.parametrize("func", [np.mean, np.std])
def test_np_reduction_forwarding_dtype(gpu_backend, func):
    data = np.arange(12, dtype=np.float32).reshape(3, 4)
    arr = cle.Array.from_array(data)
    assert np.allclose(func(arr), func(data), rtol=1e-5)


def test_any_all(gpu_backend):
    data = np.asarray([[0.0, 1.0], [0.0, 0.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    assert bool(arr.any()) == data.any()
    assert bool(arr.all()) == data.all()
