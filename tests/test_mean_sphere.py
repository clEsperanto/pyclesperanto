import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_mean_sphere():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 9, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1.8, 0, 0],
                [0, 1.8, 1.8, 1.8, 0],
                [0, 0, 1.8, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1, dtype=float)
    cle.mean_sphere(test1, result, 1, 1, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.0001)
