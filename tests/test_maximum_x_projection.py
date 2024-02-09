import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_maximum_x_projection():
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
                [9, 8, 8, 8, 9],
                [8, 9, 10, 9, 7],
                [10, 10, 7, 7, 10],
                [7, 7, 9, 10, 8],
                [10, 10, 10, 10, 10],
            ]
        )
    )

    result = cle.create(reference)
    cle.maximum_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


def test_maximum_x_projection_of_pointlist():
    positions_and_values = cle.push(np.asarray([[0, 0, 2, 3, 5], [0, 1, 3, 2, 6]]))

    reference = cle.push(np.asarray([[5], [6]]))

    result = cle.maximum_x_projection(positions_and_values)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
