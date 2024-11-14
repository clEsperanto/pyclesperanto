import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_erode_box_old():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test)
    cle.erode_box(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)


def test_erode_box():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test)
    cle.binary_erode(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)
