import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_exclude_labels_2d():
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 2, 0, 0, 0, 0],
                [0, 1, 2, 0, 7, 0, 0],
                [0, 1, 0, 0, 7, 5, 5],
                [8, 8, 8, 0, 0, 0, 0],
                [0, 4, 4, 0, 3, 0, 0],
                [0, 4, 4, 6, 0, 0, 0],
            ]
        ).astype(np.uint32)
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 2, 0, 0, 0, 0],
                [0, 1, 2, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 3, 3],
                [5, 5, 5, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 0, 0, 0],
            ]
        ).astype(np.uint32)
    )

    flaglist = cle.push(np.asarray([[0, 0, 0, 1, 1, 0, 0, 1, 0]]).astype(np.uint32))

    gpu_output = cle.exclude_labels(gpu_input, flaglist)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_exclude_labels_3d():
    gpu_input = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 2, 0, 0, 0, 0],
                    [0, 1, 2, 0, 7, 0, 0],
                    [0, 1, 0, 0, 7, 5, 5],
                ],
                [
                    [8, 8, 8, 0, 0, 0, 0],
                    [0, 4, 4, 0, 3, 0, 0],
                    [0, 4, 4, 6, 0, 0, 0],
                ],
            ]
        ).astype(np.uint32)
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 2, 0, 0, 0, 0],
                    [0, 1, 2, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 3, 3],
                ],
                [
                    [5, 5, 5, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 4, 0, 0, 0],
                ],
            ]
        ).astype(np.uint32)
    )

    flaglist = cle.push(np.asarray([[0, 0, 0, 1, 1, 0, 0, 1, 0]]).astype(np.uint32))

    gpu_output = cle.exclude_labels(gpu_input, flaglist)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
