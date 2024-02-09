import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_mean_x_projection():
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 0, 0, 0, 9],
                    [0, 2, 0, 8, 0],
                    [3, 0, 1, 0, 10],
                    [0, 4, 0, 7, 0],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [0, 2, 0, 8, 0],
                    [1, 0, 0, 0, 9],
                    [3, 0, 1, 0, 10],
                    [0, 4, 0, 7, 0],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [0, 2, 0, 8, 0],
                    [3, 0, 1, 0, 10],
                    [0, 4, 0, 7, 0],
                    [1, 0, 0, 0, 9],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [0, 2, 0, 8, 0],
                    [1, 0, 0, 0, 9],
                    [0, 4, 0, 7, 0],
                    [3, 0, 1, 0, 10],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [1, 0, 0, 0, 9],
                    [0, 4, 0, 7, 0],
                    [3, 0, 1, 0, 10],
                    [0, 2, 0, 8, 0],
                    [5, 0, 6, 0, 10],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [2, 2.0, 2.0, 2.0, 2.0],
                [2, 2.0, 2.8, 2.0, 2.2],
                [2.8, 2.8, 2.2, 2.2, 2.8],
                [2.2, 2.2, 2.0, 2.8, 2.0],
                [4.2, 4.2, 4.2, 4.2, 4.2],
            ]
        )
    )

    result = cle.create(reference)
    cle.mean_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert np.allclose(a, b, 0.001)
