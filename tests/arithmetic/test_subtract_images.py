import numpy as np

import pyclesperanto as cle
import pytest
input1 = np.asarray([1, 2, 3])
input2 = np.asarray([4, 5, 7])


@pytest.mark.backend
def test_subtract_images(gpu_backend):
    reference = np.asarray([3, 3, 4])
    output = cle.subtract_images(input2, input1)
    result = cle.pull(output)

    print(output)
    print(result)

    assert np.array_equal(result, reference)
