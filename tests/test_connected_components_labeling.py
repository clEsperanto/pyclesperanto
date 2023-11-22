import pyclesperanto as cle
import numpy as np


def test_connected_components_labeling_box():
    gpu_input = cle.push(np.asarray([[1, 0, 1], [1, 0, 0], [0, 0, 1]]))
    gpu_reference = cle.push(np.asarray([[1, 0, 2], [1, 0, 0], [0, 0, 3]]))
    gpu_output = cle.connected_components_labeling(gpu_input)
    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)
    assert np.array_equal(a, b)
