"""NumPy-style creation functions (Phase 6 of the numpy compat plan)."""

import numpy as np
import pytest

import pyclesperanto as cle


def test_full_scalar(gpu_backend):
    arr = cle.full((2, 3), 7, dtype=np.float32)
    np.testing.assert_array_equal(np.asarray(arr), np.full((2, 3), 7, dtype=np.float32))


def test_full_like(gpu_backend):
    ref = cle.zeros((2, 4), dtype=np.float32)
    arr = cle.full_like(ref, 5)
    assert arr.shape == ref.shape
    np.testing.assert_array_equal(np.asarray(arr), np.full((2, 4), 5, dtype=np.float32))


def test_arange(gpu_backend):
    arr = cle.arange(0, 10, 2, dtype=np.float32)
    np.testing.assert_array_equal(
        np.asarray(arr), np.arange(0, 10, 2, dtype=np.float32)
    )


def test_arange_single_arg(gpu_backend):
    arr = cle.arange(5, dtype=np.float32)
    np.testing.assert_array_equal(np.asarray(arr), np.arange(5, dtype=np.float32))


def test_linspace(gpu_backend):
    arr = cle.linspace(0, 1, num=5, dtype=np.float32)
    np.testing.assert_allclose(
        np.asarray(arr), np.linspace(0, 1, num=5, dtype=np.float32)
    )


def test_eye(gpu_backend):
    arr = cle.eye(3, dtype=np.float32)
    np.testing.assert_array_equal(np.asarray(arr), np.eye(3, dtype=np.float32))


def test_eye_rectangular(gpu_backend):
    arr = cle.eye(2, 4, dtype=np.float32)
    np.testing.assert_array_equal(np.asarray(arr), np.eye(2, 4, dtype=np.float32))


def test_array_classmethods(gpu_backend):
    arr = cle.Array.full((2, 2), 3, dtype=np.float32)
    np.testing.assert_array_equal(np.asarray(arr), np.full((2, 2), 3, dtype=np.float32))
    assert cle.Array.arange(4, dtype=np.float32).shape == (4,)
    assert cle.Array.eye(2, dtype=np.float32).shape == (2, 2)


def test_mtype_keyword_only(gpu_backend):
    with pytest.raises(TypeError):
        cle.zeros((2, 2), np.float32, "buffer")
    with pytest.raises(TypeError):
        cle.ones((2, 2), np.float32, "buffer")
