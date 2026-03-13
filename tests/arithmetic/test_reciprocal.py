import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_reciprocal(gpu_backend):
    test = [[0.2, 0.1], [10, 20]]
    reference = [[5, 10], [0.1, 0.05]]

    result = cle.reciprocal(test)

    assert np.allclose(result, reference)
