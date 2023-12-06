import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_detect_maxima_box():
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [1, 0, 0, 2, 0],
                [1, 2, 1, 3, 2],
                [0, 1, 0, 2, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    gpu_output = cle.create_like(gpu_input)

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    cle.detect_maxima_box(gpu_input, gpu_output)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
