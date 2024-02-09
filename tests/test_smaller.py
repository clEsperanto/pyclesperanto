import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_smaller_2d():
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
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.smaller(test1, test2, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)

    print("ok smaller")


def test_smaller_3d():
    test1 = cle.push(
        np.asarray(
            [[[0, 1, 2, 3, 0], [0, 3, 3, 4, 0]], [[0, 4, 4, 5, 0], [0, 0, 0, 0, 0]]]
        )
    )
    test2 = cle.push(
        np.asarray(
            [[[0, 3, 3, 3, 0], [0, 3, 3, 3, 0]], [[0, 3, 3, 3, 0], [0, 0, 0, 0, 0]]]
        )
    )

    reference = cle.push(
        np.asarray(
            [[[0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
        )
    )

    result = cle.create(test1)
    cle.smaller(test1, test2, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)
