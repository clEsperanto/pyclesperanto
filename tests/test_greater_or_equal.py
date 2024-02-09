import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_greater_or_equal_2d():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 3, 0],
                [0, 3, 3, 4, 0],
                [0, 4, 4, 5, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    test2 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 3, 3, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ]
        )
    )

    result = cle.create(test1)
    cle.greater_or_equal(test1, test2, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)


def test_greater_or_equal_3d():
    test1 = cle.push(
        np.asarray(
            [
                [
                    [0, 1, 2, 3, 0],
                    [0, 3, 3, 4, 0],
                ],
                [[0, 4, 4, 5, 0], [0, 0, 0, 0, 0]],
            ]
        )
    )
    test2 = cle.push(
        np.asarray(
            [[[0, 3, 3, 3, 0], [0, 3, 3, 3, 0]], [[0, 3, 3, 3, 0], [0, 0, 0, 0, 0]]]
        )
    )

    reference = cle.push(
        np.asarray(
            [[[1, 0, 0, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]
        )
    )

    result = cle.create(test1)
    cle.greater_or_equal(test1, test2, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)
