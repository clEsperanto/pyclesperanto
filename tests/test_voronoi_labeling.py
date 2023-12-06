import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_voronoi_labeling():
    gpu_input = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [
                    [1, 1, 1, 2, 2, 2],
                    [1, 1, 1, 2, 2, 2],
                    [1, 1, 1, 2, 2, 2],
                    [3, 3, 3, 4, 4, 4],
                    [3, 3, 3, 4, 4, 4],
                    [3, 3, 3, 4, 4, 4],
                ]
            ]
        )
    )

    gpu_output = cle.voronoi_labeling(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
