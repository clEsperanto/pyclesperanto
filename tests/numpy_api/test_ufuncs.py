"""Tests for __array_ufunc__ dispatch of NumPy ufuncs to device kernels."""

import numpy as np
import pytest

import pyclesperanto as cle

_UNARY = [
    np.sqrt,
    np.exp,
    np.log,
    np.abs,
    np.sin,
    np.cos,
    np.tan,
    np.arcsin,
    np.arccos,
    np.arctan,
    np.sinh,
    np.cosh,
    np.tanh,
    np.square,
    np.negative,
    np.positive,
]

_BINARY = [np.add, np.subtract, np.multiply, np.divide, np.maximum, np.minimum]

_UNARY_MAPPED = [
    np.floor,
    np.ceil,
    np.trunc,
    np.sign,
    np.rint,
    np.isnan,
    np.isfinite,
    np.log1p,
    np.expm1,
]

_BINARY_MAPPED = [
    np.logical_and,
    np.logical_or,
    np.logical_xor,
    np.hypot,
    np.arctan2,
]


@pytest.mark.parametrize("ufunc", _UNARY, ids=lambda u: u.__name__)
def test_unary_ufunc(gpu_backend, ufunc):
    data = np.asarray([[0.1, 0.2], [0.3, 0.4]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = ufunc(arr)
    assert isinstance(result, cle.Array)
    np.testing.assert_allclose(np.asarray(result), ufunc(data), rtol=1e-5)


@pytest.mark.parametrize("ufunc", _BINARY, ids=lambda u: u.__name__)
def test_binary_ufunc_array_array(gpu_backend, ufunc):
    d1 = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    d2 = np.asarray([[4.0, 3.0], [2.0, 1.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    result = ufunc(a1, a2)
    assert isinstance(result, cle.Array)
    np.testing.assert_allclose(np.asarray(result), ufunc(d1, d2), rtol=1e-5)


@pytest.mark.parametrize("ufunc", _BINARY, ids=lambda u: u.__name__)
def test_binary_ufunc_array_scalar(gpu_backend, ufunc):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = ufunc(arr, 2.0)
    np.testing.assert_allclose(np.asarray(result), ufunc(data, 2.0), rtol=1e-5)


@pytest.mark.parametrize("ufunc", _BINARY, ids=lambda u: u.__name__)
def test_binary_ufunc_scalar_array(gpu_backend, ufunc):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = ufunc(10.0, arr)
    np.testing.assert_allclose(np.asarray(result), ufunc(10.0, data), rtol=1e-5)


def test_binary_ufunc_numpy_array_operand(gpu_backend):
    d1 = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    d2 = np.asarray([[4.0, 3.0], [2.0, 1.0]], dtype=np.float32)
    arr = cle.Array.from_array(d1)
    result = np.add(d2, arr)
    assert isinstance(result, cle.Array)
    np.testing.assert_allclose(np.asarray(result), d1 + d2)


def test_power_ufunc(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = np.power(arr, 2)
    np.testing.assert_allclose(np.asarray(result), data**2)


def test_np_power_scalar_base(gpu_backend):
    data = np.asarray([1.0, 2.0, 3.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(np.power(2, arr)), np.power(2, data), rtol=1e-5)


@pytest.mark.parametrize("ufunc", _UNARY_MAPPED, ids=lambda u: u.__name__)
def test_unary_ufunc_mapped(gpu_backend, ufunc):
    data = np.asarray([0.5, 1.5, 2.5, 7.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = ufunc(arr)
    np.testing.assert_allclose(np.asarray(result), ufunc(data), rtol=1e-5)


@pytest.mark.parametrize("ufunc", _BINARY_MAPPED, ids=lambda u: u.__name__)
def test_binary_ufunc_mapped(gpu_backend, ufunc):
    d1 = np.asarray([0.0, 1.0, 3.0], dtype=np.float32)
    d2 = np.asarray([1.0, 0.0, 4.0], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    result = ufunc(a1, a2)
    np.testing.assert_allclose(np.asarray(result), ufunc(d1, d2), rtol=1e-5)


def test_ufunc_out_device_array(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    out = cle.Array.empty(data.shape, dtype=np.float32)
    result = np.multiply(arr, 2.0, out=out)
    assert result is out
    np.testing.assert_allclose(np.asarray(out), data * 2.0)


def test_ufunc_out_numpy_array(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    out = np.empty_like(data)
    result = np.add(arr, 1.0, out=out)
    assert result is out
    np.testing.assert_allclose(out, data + 1.0)


def test_unsupported_ufunc_raises_typeerror(gpu_backend):
    data = np.asarray([1.0, 2.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    with pytest.raises(TypeError):
        np.logaddexp(arr, 2)


@pytest.mark.parametrize("ufunc", [np.add, np.maximum, np.minimum, np.multiply])
def test_accumulate_supported(gpu_backend, ufunc):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = ufunc.accumulate(arr, axis=1)
    np.testing.assert_allclose(np.asarray(result), ufunc.accumulate(data, axis=1), rtol=1e-5)


def test_accumulate_supported_with_out_numpy(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    out = np.empty_like(data)
    result = np.add.accumulate(arr, axis=0, out=out)
    assert result is out
    np.testing.assert_allclose(out, np.add.accumulate(data, axis=0), rtol=1e-5)


def test_accumulate_supported_with_out_array(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    out = cle.Array.empty(data.shape, dtype=np.float32)
    result = np.add.accumulate(arr, axis=0, out=out)
    assert result is out
    np.testing.assert_allclose(np.asarray(out), np.add.accumulate(data, axis=0), rtol=1e-5)


def test_accumulate_supported_with_negative_axis(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = np.multiply.accumulate(arr, axis=-1)
    np.testing.assert_allclose(np.asarray(result), np.multiply.accumulate(data, axis=-1), rtol=1e-5)


def test_accumulate_dtype(gpu_backend):
    data = np.asarray([[1, 2], [3, 4]], dtype=np.int16)
    arr = cle.Array.from_array(data)
    result = np.add.accumulate(arr, axis=1, dtype=np.float32)
    expected = np.add.accumulate(data.astype(np.float32), axis=1)
    np.testing.assert_allclose(np.asarray(result), expected, rtol=1e-5)


def test_unsupported_accumulate_method_raises_typeerror(gpu_backend):
    data = np.asarray([1.0, 2.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    with pytest.raises(TypeError):
        np.logaddexp.accumulate(arr)
