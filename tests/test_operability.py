import numpy as np

import pyclesperanto as cle


def test_mod():
    a = np.array([1, 2, 3, 4, 5]).astype(float)
    b = np.array([2, 2, 2, 2, 2]).astype(float)
    c = cle.mod(a, b)

    res = cle.pull(c)

    assert (res == np.array([1, 0, 1, 0, 1])).all()


def test_sqrt():
    a = np.array([1, 9, 25]).astype(float)
    c = cle.sqrt(a)

    res = cle.pull(c)

    assert (res == np.array([1, 3, 5])).all()


def test_cbrt():
    a = np.array([1, 27, 125]).astype(float)
    c = cle.cbrt(a)

    res = cle.pull(c)

    assert (res == np.array([1, 3, 5])).all()


def test_fabs():
    a = np.array([-1, -2, -3, -4, -5]).astype(float)
    c = cle.fabs(a)

    res = cle.pull(c)

    assert (res == np.array([1, 2, 3, 4, 5])).all()


def test_power_scalar():
    a = np.array([1, 2, 3, 4, 5]).astype(float)
    c = cle.power(a, 3)

    res = cle.pull(c)

    assert (res == np.array([1, 8, 27, 64, 125])).all()


def test_power_images():
    a = np.array([1, 2, 3, 4, 5]).astype(float)
    b = np.array([3, 3, 3, 3, 3]).astype(float)

    c = cle.power(a, b)
    res = cle.pull(c)

    assert (res == np.array([1, 8, 27, 64, 125])).all()
