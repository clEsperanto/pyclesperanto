import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_connected_components_labeling_diamond():
    gpu_input = cle.push(np.asarray([[0, 1, 0, 1], [0, 1, 0, 0], [1, 0, 0, 1]]))

    gpu_reference = cle.push(np.asarray([[0, 1, 0, 2], [0, 1, 0, 0], [3, 0, 0, 4]]))

    gpu_output = cle.connected_components_labeling(gpu_input, connectivity="diamond")

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(b)
    print(a)

    assert np.array_equal(a, b)
