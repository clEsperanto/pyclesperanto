import numpy as np
import pytest

import pyclesperanto as cle



def test_zeros_arrays(gpu_backend):
    gpu_arr = cle.zeros((10, 10))

    assert gpu_arr.shape == (10, 10)
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0



def test_empty_like(gpu_backend):
    arr = np.zeros((10, 10))
    gpu_arr = cle.empty_like(arr)

    assert gpu_arr.shape == arr.shape



def test_zeros_like(gpu_backend):
    arr = np.zeros((10, 10))
    gpu_arr = cle.zeros_like(arr)

    assert gpu_arr.shape == arr.shape
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0



def test_ones_like(gpu_backend):
    arr = np.zeros((10, 10))
    gpu_arr = cle.ones_like(arr)

    assert gpu_arr.shape == arr.shape
    assert gpu_arr.sum() == 100
    assert gpu_arr.max() == 1
    assert gpu_arr.min() == 1



def test_ones_arrays(gpu_backend):
    gpu_arr = cle.ones((10, 10))

    assert gpu_arr.shape == (10, 10)
    assert gpu_arr.sum() == 100
    assert gpu_arr.max() == 1
    assert gpu_arr.min() == 1



def test_from_array(gpu_backend):
    arr = np.zeros((10, 10))
    gpu_arr = cle.from_array(arr)

    assert gpu_arr.shape == arr.shape
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0



def test_array_ufunc_add(gpu_backend):
    array1 = cle.push(np.ones((10, 10)))
    array2 = cle.push(np.ones((10, 10)))
    result = np.add(array1, array2)  # This should call array1.__array_ufunc__

    res = cle.pull(result)
    assert np.all(res == 2)



def test_repr(gpu_backend):
    array = cle.zeros((10, 10))
    result = repr(array)

    assert len(result) > 0
