import numpy as np
import pytest

import pyclesperanto as cle


def test_setitem_single_value(gpu_backend):
    image = cle.create([10, 20, 30])
    image[5, 10, 15] = 42

    result = cle.pull(image)
    assert result[5, 10, 15] == 42


def test_setitem_array(gpu_backend):
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))
    image[2:7, 5:15, 10:25] = data

    result = cle.pull(image)
    assert np.array_equal(result[2:7, 5:15, 10:25], data)


def test_setitem_invalid_value(gpu_backend):
    image = cle.create([10, 20, 30])
    invalid_value = "invalid"

    try:
        image[5, 10, 15] = invalid_value
    except ValueError:
        pass
    else:
        assert False, "Expected TypeError to be raised"


def test_setitem_invalid_region(gpu_backend):
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))

    try:
        image[1, 5:6, 10:25] = data
    except IndexError:
        pass
    else:
        assert False, "Expected ValueError to be raised"


def test_setitem_out_of_bounds(gpu_backend):
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))

    try:
        image[15, 25, 35] = data
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError to be raised"


def test_setitem_negative_indices(gpu_backend):
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))

    try:
        image[-5, -10, -15] = data
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError to be raised"


def test_setitem_every_2_rows(gpu_backend):
    image = cle.create([10, 20, 30])
    data = np.arange(5 * 20 * 30, dtype=np.float32).reshape(5, 20, 30)
    image[::2, :, :] = data

    result = cle.pull(image)
    assert np.array_equal(result[::2, :, :], data)


def test_setitem_strided_columns(gpu_backend):
    reference = np.arange(6 * 8, dtype=np.float32).reshape(6, 8)
    data = np.arange(6 * 4, dtype=np.float32).reshape(6, 4) + 100
    image = cle.push(reference.copy())
    image[:, ::2] = data
    reference[:, ::2] = data

    assert np.array_equal(cle.pull(image), reference)


def test_setitem_strided_scalar(gpu_backend):
    reference = np.arange(6 * 8, dtype=np.float32).reshape(6, 8)
    image = cle.push(reference.copy())
    image[::2, ::2] = -1
    reference[::2, ::2] = -1

    assert np.array_equal(cle.pull(image), reference)


def test_setitem_negative_step(gpu_backend):
    image = cle.create([10, 20, 30])
    data = np.arange(5 * 20 * 30, dtype=np.float32).reshape(5, 20, 30)
    image[7:2:-1, :, :] = data

    result = cle.pull(image)
    assert np.array_equal(result[3:8, :, :], data[::-1])
