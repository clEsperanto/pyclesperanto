import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_subtract_image_from_scalar():
    test1 = cle.push(np.asarray([[0, 0], [1, 1], [2, 2]]))

    reference = cle.push(np.asarray([[5, 5], [4, 4], [3, 3]]))

    result = cle.create(test1)
    cle.subtract_image_from_scalar(test1, result, 5)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
