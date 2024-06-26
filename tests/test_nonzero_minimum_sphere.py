import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_nonzero_minimum_sphere():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 2, 0],
                [0, 2, 2, 3, 0],
                [0, 3, 3, 4, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 2, 0],
                [0, 2, 2, 3, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test)
    flag = cle.create((1, 1, 1))

    # as nonzero filters don't touch zero values, we need to initialize the result in advance
    cle.set(result, 0)

    cle.nonzero_minimum(test, flag, result, connectivity="sphere")

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, atol=0.00001)
