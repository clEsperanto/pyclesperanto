import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_array_equal():
    input1 = np.asarray([1, 2, 3])
    input2 = np.asarray([4, 5, 7])
    input3 = np.asarray([1, 2, 3, 3])
    input4 = np.asarray([1.0, 2.0, 3.0])

    assert not cle.array_equal(input1, input2)
    assert not cle.array_equal(input1, input3)
    assert cle.array_equal(input1, input4)
