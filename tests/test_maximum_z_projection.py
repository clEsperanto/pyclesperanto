import pyclesperanto as cle
import numpy as np

cle.select_device("TX")

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
            [1, 2, 0, 8, 9],
            [3, 4, 1, 8, 10],
            [3, 4, 1, 7, 10],
            [3, 4, 1, 8, 10],
            [5, 0, 6, 0, 10],
        ]
    )
)


def test_maximum_z_projection():
    result = cle.create(reference)

    cle.maximum_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


def test_maximum_z_projection_creator():
    result = cle.maximum_z_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


def test_maximum_z_projection_creator_passing_none():
    result = cle.maximum_z_projection(test1, None)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
