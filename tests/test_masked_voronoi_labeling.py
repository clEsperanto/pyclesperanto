import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_masked_voronoi_labeling():
    gpu_input = cle.push(
        np.asarray(
            [
                [1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1],
            ]
        )
    )

    gpu_mask = cle.push(
        np.asarray(
            [
                [1, 1, 1, 1, 0, 1],
                [1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 0, 1],
                [1, 0, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 1, 1, 0, 2],
                [1, 0, 0, 1, 0, 2],
                [1, 0, 1, 1, 0, 2],
                [3, 0, 1, 1, 0, 4],
                [3, 0, 0, 0, 0, 4],
                [3, 3, 3, 4, 4, 4],
            ]
        )
    )

    gpu_output = cle.masked_voronoi_labeling(gpu_input, gpu_mask)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
