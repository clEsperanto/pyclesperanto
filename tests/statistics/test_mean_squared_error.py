import numpy as np
import pytest

import pyclesperanto as cle

input1 = np.asarray([[1, 2, 3]])
input2 = np.asarray([[4, 5, 7]])



def test_mean_squared_error(gpu_backend):
    output = cle.mean_squared_error(input2, input1)
    assert abs(output - 11.333) < 0.001
