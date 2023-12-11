import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


def test_setitem_single_value():
    image = cle.create([10, 20, 30])
    image[5, 10, 15] = 42

    result = cle.pull(image)
    assert result[5, 10, 15] == 42


def test_setitem_array():
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))
    image[2:7, 5:15, 10:25] = data

    result = cle.pull(image)
    assert np.array_equal(result[2:7, 5:15, 10:25], data)


def test_setitem_invalid_value():
    image = cle.create([10, 20, 30])
    invalid_value = "invalid"

    try:
        image[5, 10, 15] = invalid_value
    except ValueError:
        pass
    else:
        assert False, "Expected TypeError to be raised"


def test_setitem_invalid_region():
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))

    try:
        image[1, 5:6, 10:25] = data
    except IndexError:
        pass
    else:
        assert False, "Expected ValueError to be raised"


def test_setitem_out_of_bounds():
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))

    try:
        image[15, 25, 35] = data
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError to be raised"


def test_setitem_negative_indices():
    image = cle.create([10, 20, 30])
    data = np.ones((5, 10, 15))

    try:
        image[-5, -10, -15] = data
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError to be raised"


def test_setitem_every_2_rows():
    image = cle.create([10, 20, 30])
    data = np.ones((5, 20, 30))
    image[::2, :, :] = data

    result = cle.pull(image)
    assert np.array_equal(result[::2, :, :], data)


def test_setitem_negative_step():
    image = cle.create([10, 20, 30])
    data = np.ones((5, 20, 30))
    image[2:7:-1, :, :] = data

    result = cle.pull(image)
    assert np.array_equal(result[2:7, :, :], data)
