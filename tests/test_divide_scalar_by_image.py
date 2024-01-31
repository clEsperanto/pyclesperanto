import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_divide_scalar_by_image():
    test1 = cle.push(np.asarray([[5, 5], [1, 1], [2, 2]]))

    reference = cle.push(np.asarray([[2, 2], [10, 10], [5, 5]]))
    # reference = cle.push(np.asarray([[0.5, 0.5], [0.1, 0.1], [0.2, 0.2]]))

    result = cle.create(test1, dtype=float)
    cle.divide_scalar_by_image(test1, result, 10)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
