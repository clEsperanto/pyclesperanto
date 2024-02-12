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
                [0, 1, 8, 27, 0],
                [0, 8, 27, 64, 0],
                [0, 64, 64, 125, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.power(test1, 3)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, 0.001)
