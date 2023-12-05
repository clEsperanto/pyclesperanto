import pyclesperanto as cle

import numpy as np

cle.select_device("TX")


def test_power():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 3, 0],
                [0, 2, 3, 4, 0],
                [0, 4, 4, 5, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 4, 9, 0],
                [0, 4, 9, 16, 0],
                [0, 16, 16, 25, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.power(test1, 2)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, 0.001)
