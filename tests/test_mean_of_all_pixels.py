import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_mean_of_all_pixels_3d():
    test1 = cle.push(
        np.asarray(
            [
                [
                    [0, 4, 0, 0, 2],
                    [0, 0, 0, 8, 0],
                    [3, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 5, 2, 0, 0],
                ]
            ]
        )
    )

    s = cle.mean_of_all_pixels(test1)

    assert s == 1


def test_mean_of_all_pixels_2d():
    test1 = cle.push(
        np.asarray(
            [
                [0, 4, 0, 0, 2],
                [0, 0, 0, 8, 0],
                [3, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 5, 2, 0, 0],
            ]
        )
    )

    s = cle.mean_of_all_pixels(test1)

    assert s == 1


def test_mean_of_all_pixels_1d():
    test1 = cle.push(np.asarray([0, 8, 0, 0, 2]))

    s = cle.mean_of_all_pixels(test1)

    assert s == 2


def test_mean_of_all_pixels_1d_y():
    test1 = cle.push(np.asarray([[0], [8], [0], [0], [2]]))

    s = cle.mean_of_all_pixels(test1)

    assert s == 2


def test_mean_of_all_pixels_1d_z():
    test1 = cle.push(np.asarray([[[0]], [[8]], [[0]], [[0]], [[2]]]))

    s = cle.mean_of_all_pixels(test1)

    assert s == 2
