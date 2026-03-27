import numpy as np
import pytest

import pyclesperanto as cle

input1 = np.asarray([1, 5, 3])
input2 = np.asarray([4, 2, 7])



def test_absolute_difference(gpu_backend):
    reference = np.asarray([3, 3, 4])
    output = cle.absolute_difference(input2, input1)
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)
