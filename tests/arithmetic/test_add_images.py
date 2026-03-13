import numpy as np

import pyclesperanto as cle
import pytest
input1 = np.asarray([1, 2, 3])
input2 = np.asarray([4, 5, 6])


@pytest.mark.backend
def test_add_images(gpu_backend):
    reference = np.asarray([5, 7, 9])
    output = cle.add_images(input1, input2, None)
    result = cle.pull(output)

    assert np.array_equal(result, reference)
