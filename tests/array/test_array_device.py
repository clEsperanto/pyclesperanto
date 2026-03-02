import numpy as np

import pyclesperanto as cle


def test_zeros_arrays():
    gpu_arr = cle.Array.zeros((10, 10))

    assert gpu_arr.shape == (10, 10)
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0


def test_empty_like():
    arr = np.zeros((10, 10))
    gpu_arr = cle.Array.empty_like(arr)

    assert gpu_arr.shape == arr.shape


def test_zeros_like():
    arr = np.zeros((10, 10))
    gpu_arr = cle.Array.zeros_like(arr)

    assert gpu_arr.shape == arr.shape
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0


def test_to_device():
    arr = np.zeros((10, 10))
    gpu_arr = cle.Array.to_device(arr)

    assert gpu_arr.shape == arr.shape
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0


def test_from_array():
    arr = np.zeros((10, 10))
    gpu_arr = cle.Array.from_array(arr)

    assert gpu_arr.shape == arr.shape
    assert gpu_arr.sum() == 0
    assert gpu_arr.max() == 0
    assert gpu_arr.min() == 0


def test_array_ufunc_add():
    array1 = cle.push(np.ones((10, 10)))
    array2 = cle.push(np.ones((10, 10)))
    result = np.add(array1, array2)  # This should call array1.__array_ufunc__

    res = cle.pull(result)
    assert np.all(res == 2)


def test_repr():
    array = cle.Array.zeros((10, 10))
    result = repr(array)

    assert len(result) > 0
