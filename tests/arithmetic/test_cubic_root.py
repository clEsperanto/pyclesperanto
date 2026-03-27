import numpy as np
import pytest

import pyclesperanto as cle


def test_cubic_root(gpu_backend):
    test = np.asarray([[125, 64]])
    reference = np.asarray([[5, 4]])

    result = cle.cubic_root(test)

    assert np.allclose(result, reference)
