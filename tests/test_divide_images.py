import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_divide_images():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 4, 6, 8, 0],
                [0, 4, 6, 8, 0],
                [0, 4, 6, 8, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    test2 = cle.push(
        np.asarray(
            [
                [1, 1, 1, 1, 1],
                [1, 2, 3, 2, 1],
                [1, 2, 3, 2, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 2, 2, 4, 0],
                [0, 2, 2, 4, 0],
                [0, 4, 6, 8, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.divide_images(test1, test2, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, 0.0001)
