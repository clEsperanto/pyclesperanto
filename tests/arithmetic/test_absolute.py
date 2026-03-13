import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_absolute(gpu_backend):
    """Test absolute operation across all available backends."""
    test = cle.push(np.asarray([[1, -1], [1, -1]]))

    test2 = cle.create(test)
    cle.absolute(test, test2)

    print(test2)

    a = cle.pull(test2)
    assert np.min(a) == 1
    assert np.max(a) == 1
    assert np.mean(a) == 1


@pytest.mark.backend
def test_absolute1(gpu_backend):
    """Test absolute operation (alternative implementation) across all available backends."""
    gpu_a = cle.push(np.asarray([[1, -1], [1, -1]]))
    gpu_b = cle.create(gpu_a)
    cle.absolute(gpu_a, gpu_b)
    assert np.all(cle.pull(gpu_b) == 1)
