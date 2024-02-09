import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_gradient_z():
    test = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [-1, 0, 0, 1, 0],
                    [-1, 0, 0, 1, 0],
                    [-1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, -1, 0],
                    [1, 0, 0, -1, 0],
                    [1, 0, 0, -1, 0],
                    [0, 0, 0, 0, 0],
                ],
            ]
        )
    )

    result = cle.create(test)
    cle.gradient_z(test, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
