import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_close_box_old():
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 2, 2],
                [1, 1, 1, 1, 2, 2],
                [1, 0, 0, 0, 2, 2],
                [3, 0, 0, 0, 2, 2],
            ]
        )
    )

    gpu_output = cle.closing_box(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_close_box_2d():
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 2, 2],
                [1, 1, 1, 1, 2, 2],
                [1, 0, 0, 0, 2, 2],
                [3, 0, 0, 0, 2, 2],
            ]
        )
    )

    gpu_output = cle.grayscale_closing(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_close_box_3d():
    gpu_input = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 2, 0],
                    [1, 1, 1, 0, 2, 0],
                    [0, 0, 0, 0, 2, 0],
                    [3, 0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 2, 0],
                    [1, 1, 1, 0, 2, 0],
                    [0, 0, 0, 0, 2, 0],
                    [3, 0, 0, 0, 0, 0],
                ],
            ]
        )
    )
    print(gpu_input.shape)

    gpu_reference = cle.push(
        np.asarray(
            [
                [
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 2, 2],
                    [1, 1, 1, 1, 2, 2],
                    [1, 0, 0, 0, 2, 2],
                    [3, 0, 0, 0, 2, 2],
                ],
                [
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 2, 2],
                    [1, 1, 1, 1, 2, 2],
                    [1, 0, 0, 0, 2, 2],
                    [3, 0, 0, 0, 2, 2],
                ],
            ]
        )
    )

    gpu_output = cle.grayscale_closing(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
