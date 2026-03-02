import numpy as np
from skimage.segmentation.morphsnakes import inf_sup, sup_inf

import pyclesperanto as cle

cle.select_device("TX")


def test_inferior_superior_2d():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ).astype(np.uint8)
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ).astype(np.uint8)
    )

    result = cle.create(test)
    cle.binary_infsup(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)


def test_inferior_superior_3d():
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
                    [0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 1, 1, 1, 0],
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
        ).astype(np.uint8)
    )

    reference = cle.push(
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
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
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
        ).astype(np.uint8)
    )

    result = cle.create(test)
    cle.binary_infsup(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)
