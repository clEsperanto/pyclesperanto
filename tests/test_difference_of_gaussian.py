import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_difference_of_gaussian():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test, dtype=float)
    cle.difference_of_gaussian(test, result, 1, 1, 0, 2, 2, 0)

    print(result)

    a = cle.pull(result)
    assert np.min(a) < -1.15
    assert np.min(a) > -1.18
    assert np.max(a) > 11.9
    assert np.max(a) < 12
