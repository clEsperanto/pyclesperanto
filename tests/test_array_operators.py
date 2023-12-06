import pyclesperanto as cle
import numpy as np

cle.select_device("TX")

arr1 = cle.push(np.asarray([1, 2, 3, 4, 5]))
arr2 = cle.push(np.asarray([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
arr3 = cle.push(
    np.asarray(
        [
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
            [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
        ]
    )
)


def test_max():
    assert arr1.max() == 5
    assert arr2.max() == 10
    assert arr3.max() == 20


def test_min():
    assert arr1.min() == 1
    assert arr2.min() == 1
    assert arr3.min() == 1


def test_sum():
    assert arr1.sum() == 15
    assert arr2.sum() == 55
    assert arr3.sum() == 210
