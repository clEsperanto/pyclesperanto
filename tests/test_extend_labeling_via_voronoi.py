import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_extend_labeling_via_voronoi():
    gpu_input = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 3, 3],
                    [0, 4, 0, 0, 3, 3],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 2, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [
                    [4, 4, 4, 3, 3, 3],
                    [4, 4, 4, 3, 3, 3],
                    [4, 4, 4, 3, 3, 3],
                    [2, 2, 2, 1, 1, 1],
                    [2, 2, 2, 1, 1, 1],
                    [2, 2, 2, 1, 1, 1],
                ]
            ]
        )
    )

    gpu_output = cle.extend_labeling_via_voronoi(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
