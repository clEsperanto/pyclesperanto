import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_square_root(gpu_backend):
    test = np.asarray([[25, 16]])
    reference = np.asarray([[5, 4]])

    result = cle.square_root(test)

    assert np.allclose(result, reference)
