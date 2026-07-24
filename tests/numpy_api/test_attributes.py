"""NumPy-style attributes on device arrays (Phase 3 of the numpy compat plan)."""

import numpy as np
import pytest

import pyclesperanto as cle


def test_nbytes(gpu_backend):
    data = np.zeros((2, 3, 4), dtype=np.float32)
    arr = cle.Array.from_array(data)
    assert arr.nbytes == data.nbytes


def test_T_2d(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.T), data.T)


def test_T_3d(gpu_backend):
    data = np.arange(24, dtype=np.float32).reshape(2, 3, 4)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.T), data.T)


def test_mT_2d(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.mT), data.mT)


def test_mT_3d(gpu_backend):
    data = np.arange(24, dtype=np.float32).reshape(2, 3, 4)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.mT), data.mT)


def test_mT_1d_raises(gpu_backend):
    arr = cle.Array.from_array(np.zeros(3, dtype=np.float32))
    with pytest.raises(ValueError):
        arr.mT


def test_real(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.real), data.real)


def test_imag(gpu_backend):
    data = np.arange(6, dtype=np.float32).reshape(2, 3)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr.imag), data.imag)


def test_flags(gpu_backend):
    arr = cle.Array.from_array(np.zeros((2, 3), dtype=np.float32))
    assert arr.flags.c_contiguous
    assert arr.flags.owndata
    assert arr.flags.writeable
    assert arr.flags["C_CONTIGUOUS"]
    assert arr.flags["WRITEABLE"]
