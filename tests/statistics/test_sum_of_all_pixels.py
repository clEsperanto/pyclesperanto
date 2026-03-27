import numpy as np
import pytest

import pyclesperanto as cle



def test_sum_of_all_pixels_3d(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [
                    [0, 4, 0, 0, 2],
                    [0, 0, 0, 8, 0],
                    [3, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 2, 0, 0],
                ]
            ]
        )
    )

    s = cle.sum_of_all_pixels(test1)

    assert s == 20



def test_sum_of_all_pixels_2d(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [0, 4, 0, 0, 2],
                [0, 0, 0, 8, 0],
                [3, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 2, 0, 0],
            ]
        )
    )

    s = cle.sum_of_all_pixels(test1)

    assert s == 20



def test_sum_of_all_pixels_1d(gpu_backend):
    test1 = cle.push(np.asarray([0, 4, 0, 0, 2]))

    s = cle.sum_of_all_pixels(test1)

    assert s == 6



def test_sum_of_all_pixels_1d_y(gpu_backend):
    test1 = cle.push(np.asarray([[0], [4], [0], [0], [2]]))

    s = cle.sum_of_all_pixels(test1)

    assert s == 6



def test_sum_of_all_pixels_1d_z(gpu_backend):
    test1 = cle.push(np.asarray([[[0]], [[4]], [[0]], [[0]], [[2]]]))

    s = cle.sum_of_all_pixels(test1)

    assert s == 6
