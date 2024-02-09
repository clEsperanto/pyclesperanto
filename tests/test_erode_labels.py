import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_erode_labels_2d():
    gpu_input = cle.push(
        np.asarray(
            [
                [1, 1, 0, 0, 2, 2],
                [1, 1, 0, 0, 2, 2],
                [0, 0, 4, 4, 4, 0],
                [0, 0, 4, 4, 4, 0],
                [5, 5, 4, 4, 4, 3],
                [5, 5, 0, 0, 3, 3],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 0, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [5, 0, 0, 0, 0, 3],
            ]
        )
    )
    gpu_output = cle.erode_labels(gpu_input, radius=1, relabel=False)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_erode_labels_2d_1():
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
    )

    for r in range(5):
        print("r", r)
        gpu_reference = cle.minimum_box(gpu_input, radius_x=r, radius_y=r)
        gpu_output = cle.erode_labels(gpu_input, radius=r, relabel=False)

        print(gpu_output)
        print(gpu_reference)

        assert np.array_equal(gpu_output, gpu_reference)


def test_erode_labels_3d():
    gpu_input = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 2, 0],
                    [0, 1, 1, 4, 0, 0],
                    [0, 0, 4, 3, 3, 3],
                    [5, 5, 4, 3, 3, 3],
                    [5, 5, 0, 3, 3, 3],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 2, 0],
                    [0, 1, 1, 4, 0, 0],
                    [0, 0, 4, 3, 3, 3],
                    [5, 5, 4, 3, 3, 3],
                    [5, 5, 0, 3, 3, 3],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 2, 0],
                    [0, 1, 1, 4, 0, 0],
                    [0, 0, 4, 3, 3, 3],
                    [5, 5, 4, 3, 3, 3],
                    [5, 5, 0, 3, 3, 3],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1],
                    [2, 0, 0, 0, 1, 1],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
            ]
        )
    )

    gpu_output = cle.erode_labels(gpu_input, radius=1, relabel=False)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
