import numpy as np
from skimage.segmentation.morphsnakes import inf_sup, sup_inf

import pyclesperanto as cle

cle.select_device("TX")


def test_superior_inferior_2d():
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
                [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ).astype(np.uint8)
    )

    result = cle.create(test)
    cle.binary_supinf(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)

    reference2 = sup_inf(test)
    assert cle.array_equal(result, reference2)


def test_superior_inferior_2d_compare_with_skimage_x():

    array = np.zeros((100, 85), dtype=np.uint8)
    array[15:85, 15:85] = 1
    array[35:65, 35:65] = 0

    result = cle.binary_supinf(cle.binary_infsup(array))
    reference = sup_inf(inf_sup(array))

    print("result", result)
    print("reference", reference)

    assert cle.array_equal(result, reference)


def test_superior_inferior_2d_compare_with_skimage_y():

    array = np.zeros((85, 100), dtype=np.uint8)
    array[15:85, 15:85] = 1
    array[35:65, 35:65] = 0

    result = cle.binary_supinf(cle.binary_infsup(array))
    reference = sup_inf(inf_sup(array))

    print("result", result)
    print("reference", reference)

    assert cle.array_equal(result, reference)


def test_superior_inferior_3d():
    test = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
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
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
            ]
        ).astype(np.uint8)
    )

    reference = inf_sup(test)

    result = cle.binary_infsup(test)

    print("result", result)
    print("reference", reference)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)


def test_superior_inferior_3d_compare_with_skimage_x():

    array = np.zeros((5, 5, 4), dtype=np.uint8)
    array[1:4, 1:4, 1:4] = 1
    array[2, 2, 2] = 0

    result = cle.binary_supinf(cle.binary_infsup(array))
    reference = sup_inf(inf_sup(array))

    print("result", result)
    print("reference", reference)

    assert cle.array_equal(result, reference)


def test_superior_inferior_3d_compare_with_skimage_y():

    array = np.zeros((5, 4, 5), dtype=np.uint8)
    array[1:4, 1:4, 1:4] = 1
    array[2, 2, 2] = 0

    result = cle.binary_supinf(cle.binary_infsup(array))
    reference = sup_inf(inf_sup(array))

    print("result", result)
    print("reference", reference)

    assert cle.array_equal(result, reference)


def test_superior_inferior_3d_compare_with_skimage_z():

    array = np.zeros((4, 5, 5), dtype=np.uint8)
    array[1:4, 1:4, 1:4] = 1
    array[2, 2, 2] = 0

    result = cle.binary_supinf(cle.binary_infsup(array))
    reference = sup_inf(inf_sup(array))

    print("result", result)
    print("reference", reference)

    assert cle.array_equal(result, reference)
