import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_multiply_image_and_scalar():
    test1 = cle.push(np.asarray([[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]))

    reference = cle.push(
        np.asarray([[0, 0, 0, 0, 0], [2, 2, 2, 2, 2], [4, 4, 4, 4, 4]])
    )

    result = cle.create(test1)
    cle.multiply_image_and_scalar(test1, result, 2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
