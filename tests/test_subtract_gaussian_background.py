import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_subtract_gaussian_background():
    test1 = cle.push(np.asarray([[0, 0], [1, 1], [2, 2]]))

    reference = cle.difference_of_gaussian(
        test1, sigma1_x=0, sigma1_y=0, sigma1_z=0, sigma2_x=5, sigma2_y=5, sigma2_z=5
    )

    result = cle.create(test1, dtype=float)
    cle.subtract_gaussian_background(test1, result, 5, 5, 5)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
