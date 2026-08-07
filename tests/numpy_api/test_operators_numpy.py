"""Tests for Phase 5 operators, scalar conversion and limited broadcasting."""

import numpy as np
import pytest

import pyclesperanto as cle


def test_dunder_abs(gpu_backend):
    arr = cle.Array.from_array(np.asarray([-1.0, 2.0, -3.0], dtype=np.float32))
    result = abs(arr)
    np.testing.assert_allclose(np.asarray(result), [1.0, 2.0, 3.0])


def test_dunder_float(gpu_backend):
    arr = cle.Array.from_array(np.asarray([3.5], dtype=np.float32))
    assert float(arr) == 3.5


def test_dunder_int(gpu_backend):
    arr = cle.Array.from_array(np.asarray([[3.9]], dtype=np.float32))
    assert int(arr) == 3


def test_dunder_bool_true(gpu_backend):
    assert bool(cle.Array.from_array(np.asarray([2.0], dtype=np.float32))) is True
    assert bool(cle.Array.from_array(np.asarray([0.0], dtype=np.float32))) is False


def test_scalar_conversion_requires_size_one(gpu_backend):
    arr = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    with pytest.raises(TypeError):
        float(arr)
    with pytest.raises(TypeError):
        int(arr)
    with pytest.raises(ValueError):
        bool(arr)


def test_floordiv_scalar(gpu_backend):
    data = np.asarray([1.0, 5.0, 7.0, 8.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(arr // 2), data // 2)


def test_floordiv_array(gpu_backend):
    d1 = np.asarray([10.0, 9.0, 8.0], dtype=np.float32)
    d2 = np.asarray([3.0, 2.0, 4.0], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_allclose(np.asarray(a1 // a2), d1 // d2)


def test_rfloordiv_scalar(gpu_backend):
    data = np.asarray([2.0, 3.0, 4.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(10 // arr), 10 // data)


def test_mod_scalar(gpu_backend):
    data = np.asarray([1.0, 5.0, 7.0, 8.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(arr % 3), data % 3, atol=1e-5)


def test_mod_array(gpu_backend):
    d1 = np.asarray([10.0, 9.0, 8.0], dtype=np.float32)
    d2 = np.asarray([3.0, 2.0, 5.0], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_allclose(np.asarray(a1 % a2), d1 % d2, atol=1e-5)


def test_rmod_scalar(gpu_backend):
    data = np.asarray([3.0, 4.0, 5.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(10 % arr), 10 % data, atol=1e-5)


def test_rmod_matches_numpy(gpu_backend):
    data = np.asarray([-7.0, -3.5, 2.5, 3.0, 7.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(7 % arr), 7 % data, atol=1e-5)


def test_bitwise_mask_ops(gpu_backend):
    m1 = np.asarray([0, 1, 0, 1], dtype=np.uint8)
    m2 = np.asarray([0, 0, 1, 1], dtype=np.uint8)
    a1 = cle.Array.from_array(m1)
    a2 = cle.Array.from_array(m2)
    np.testing.assert_array_equal(np.asarray(a1 & a2), m1 & m2)
    np.testing.assert_array_equal(np.asarray(a1 | a2), m1 | m2)
    np.testing.assert_array_equal(np.asarray(a1 ^ a2), m1 ^ m2)
    np.testing.assert_array_equal(np.asarray(~a1), (m1 == 0).astype(np.uint8))


def test_broadcast_singleton_dimension(gpu_backend):
    d1 = np.asarray([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype=np.float32)
    d2 = np.asarray([[10.0, 20.0, 30.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_allclose(np.asarray(a1 + a2), d1 + d2)


def test_broadcast_size_one_array(gpu_backend):
    d1 = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    d2 = np.asarray([[5.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_allclose(np.asarray(a1 * a2), d1 * d2)


def test_floor_divide_ufunc(gpu_backend):
    data = np.asarray([1.0, 5.0, 7.0, 8.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(np.floor_divide(arr, 2)), data // 2)


def test_div_deprecated(gpu_backend):
    data = np.asarray([2.0, 4.0, 6.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    with pytest.warns(DeprecationWarning):
        result = arr.__div__(2)
    np.testing.assert_allclose(np.asarray(result), data / 2)


def test_mod_negative_operands(gpu_backend):
    data = np.asarray([-7.0, -3.5, 2.5, 7.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    np.testing.assert_allclose(np.asarray(arr % 3), data % 3, atol=1e-5)
    np.testing.assert_allclose(np.asarray(arr % -3), data % -3, atol=1e-5)


def test_inplace_add_with_broadcast(gpu_backend):
    data = np.arange(24, dtype=np.float32).reshape(2, 3, 4)
    other = np.ones((1, 3, 1), dtype=np.float32)
    arr = cle.Array.from_array(data.copy())
    arr += other
    expected = data.copy()
    expected += other
    np.testing.assert_allclose(np.asarray(arr), expected)


def test_inplace_scalar_ops(gpu_backend):
    data = np.asarray([1.0, 2.0, 4.0], dtype=np.float32)
    arr = cle.Array.from_array(data.copy())
    arr *= 2
    arr -= 1
    arr /= 2
    np.testing.assert_allclose(np.asarray(arr), (data * 2 - 1) / 2)


def test_true_divide_by_zero_scalar(gpu_backend):
    data = np.asarray([1.0, -1.0], dtype=np.float32)
    arr = cle.Array.from_array(data)
    with np.errstate(divide="ignore"):
        expected = data / 0
    np.testing.assert_allclose(np.asarray(arr / 0), expected)


def test_comparison_with_numpy_operand(gpu_backend):
    d1 = np.asarray([1.0, 5.0, 3.0], dtype=np.float32)
    d2 = np.asarray([2.0, 5.0, 1.0], dtype=np.float32)
    arr = cle.Array.from_array(d1)
    np.testing.assert_array_equal(np.asarray(arr > d2).astype(bool), d1 > d2)
    np.testing.assert_array_equal(np.asarray(arr == d2).astype(bool), d1 == d2)


def test_maximum_with_broadcast(gpu_backend):
    d1 = np.asarray([[1.0, 5.0], [3.0, 2.0]], dtype=np.float32)
    d2 = np.asarray([[2.0, 4.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_allclose(np.asarray(np.maximum(a1, a2)), np.maximum(d1, d2))


def test_greater_than_with_broadcast(gpu_backend):
    d1 = np.asarray([[1.0, 5.0], [3.0, 2.0]], dtype=np.float32)
    d2 = np.asarray([[2.0, 4.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_array_equal(np.asarray(a1 > a2).astype(bool), d1 > d2)


def test_hypot_atan2_with_broadcast(gpu_backend):
    d1 = np.asarray([[3.0, 4.0], [1.0, 2.0]], dtype=np.float32)
    d2 = np.asarray([[4.0, 3.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    np.testing.assert_allclose(np.asarray(np.hypot(a1, a2)), np.hypot(d1, d2))
    np.testing.assert_allclose(
        np.asarray(np.arctan2(a1, a2)), np.arctan2(d1, d2), atol=1e-5
    )


def test_inplace_mul_div_pow_with_broadcast(gpu_backend):
    data = np.arange(1, 25, dtype=np.float32).reshape(2, 3, 4)
    other = np.full((1, 3, 1), 2.0, dtype=np.float32)

    arr = cle.Array.from_array(data.copy())
    arr *= other
    np.testing.assert_allclose(np.asarray(arr), data * other)

    arr = cle.Array.from_array(data.copy())
    arr /= other
    np.testing.assert_allclose(np.asarray(arr), data / other)

    arr = cle.Array.from_array(data.copy())
    arr **= other
    np.testing.assert_allclose(np.asarray(arr), data**other, rtol=1e-5)


def test_size_one_array_operand_stays_on_device(gpu_backend):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    scalar_like = np.asarray([[5.0]], dtype=np.float32)
    a1 = cle.Array.from_array(data)
    a2 = cle.Array.from_array(scalar_like)

    np.testing.assert_allclose(np.asarray(a1 + a2), data + scalar_like)
    np.testing.assert_array_equal(
        np.asarray(a1 > a2).astype(bool), data > scalar_like
    )

    arr = cle.Array.from_array(data.copy())
    arr += a2
    np.testing.assert_allclose(np.asarray(arr), data + scalar_like)


def test_incompatible_broadcast_raises(gpu_backend):
    a1 = cle.Array.from_array(np.ones((4, 3), dtype=np.float32))
    a2 = cle.Array.from_array(np.ones((5,), dtype=np.float32))
    with pytest.raises(ValueError):
        a1 + a2


def test_incompatible_inplace_broadcast_raises(gpu_backend):
    a1 = cle.Array.from_array(np.ones((1, 3), dtype=np.float32))
    a2 = cle.Array.from_array(np.ones((4, 3), dtype=np.float32))
    with pytest.raises(ValueError):
        a1 += a2
