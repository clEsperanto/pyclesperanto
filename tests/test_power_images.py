import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_power_images():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 3, 0],
                [0, 4, 5, 6, 0],
                [0, 7, 8, 9, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    test2 = cle.push(
        np.asarray(
            [
                [1, 0, 0, 0, 0],
                [1, 1, 2, 3, 0],
                [1, 1, 3, 3, 0],
                [1, 1, 2, 3, 0],
                [1, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 1, 1, 1, 1],
                [0, 1, 4, 27, 1],
                [0, 4, 125, 216, 1],
                [0, 7, 64, 729, 1],
                [0, 1, 1, 1, 1],
            ]
        )
    )

    result = cle.create(test1)
    cle.power_images(test1, test2, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.allclose(a, b, 0.0001)
