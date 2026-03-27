import pytest

import pyclesperanto as cle



def test_mode_box_2d(gpu_backend):
    image = cle.asarray(
        [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 3, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 1, 1, 1],
        ]
    )

    reference = cle.asarray(
        [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 2, 2, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 1, 1, 1],
        ]
    )

    result = cle.mode(image, None, 1, 1, 1)

    assert cle.array_equal(result, reference)



def test_mode_box_3d(gpu_backend):
    image = cle.asarray(
        [
            [
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 3, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 1, 1, 1],
            ]
        ]
    )

    reference = cle.asarray(
        [
            [
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 2, 2, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 1, 1, 1],
            ]
        ]
    )

    result = cle.mode(image, None, 1, 1, 1)

    assert cle.array_equal(result, reference)
