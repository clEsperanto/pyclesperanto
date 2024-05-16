import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_laplace_sphere():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, -1, 0, 0],
                [0, -1, 4, -1, 0],
                [0, 0, -1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.laplace(test1, result, connectivity="sphere")

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
