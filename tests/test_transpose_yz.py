import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_transpose_yz():
    test1 = cle.push(np.asarray([[[0, 1], [2, 3]], [[4, 5], [6, 7]]]))

    reference = cle.push(np.asarray([[[0, 1], [4, 5]], [[2, 3], [6, 7]]]))

    result = cle.create(test1)
    cle.transpose_yz(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_transpose_yz_3d_generate_output():
    test1 = cle.push(np.asarray([[[1, 2, 6], [3, 4, 5]]]))

    result = cle.transpose_yz(test1)

    a = cle.pull(result)

    assert np.min(a) == 1
    assert np.max(a) == 6
    assert np.mean(a) == 3.5


def test_transpose_yz_2d_generate_output():
    test1 = cle.push(np.asarray([[1, 2, 6], [3, 4, 5]]))

    result = cle.transpose_yz(test1)

    a = cle.pull(result)

    print(a)

    assert np.min(a) == 1
    assert np.max(a) == 6
    assert np.mean(a) == 3.5


def test_transpose_yz_1d_generate_output():
    test1 = cle.push(np.asarray([1, 2, 6, 3, 4, 5]))

    result = cle.transpose_yz(test1)

    a = cle.pull(result)

    print(a)

    assert np.min(a) == 1
    assert np.max(a) == 6
    assert np.mean(a) == 3.5
