import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_exponential():
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
                [1, 1, 1, 1, 1],
                [1, 2.7182817, 2.7182817, 7.389056, 1],
                [1, 7.389056, 7.389056, 20.085537, 1],
                [1, 20.085537, 20.085537, 54.59815, 1],
                [1, 1, 1, 1, 1],
            ]
        )
    )

    result = cle.create(test, dtype=float)
    cle.exponential(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    assert np.allclose(a, b, atol=0.00001)
