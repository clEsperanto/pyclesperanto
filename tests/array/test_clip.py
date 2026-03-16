import numpy as np
import pytest

import pyclesperanto as cle


@pytest.mark.backend
def test_clip_min_max(gpu_backend):
    test = [[0, 1], [2, 3]]
    reference = [[1, 1], [2, 2]]

    result = cle.clip(test, min_intensity=1, max_intensity=2)

    assert np.array_equal(result, reference)


@pytest.mark.backend
def test_clip_max(gpu_backend):
    test = [[0, 1], [2, 3]]
    reference = [[0, 1], [2, 2]]

    result = cle.clip(test, min_intensity=0, max_intensity=2)

    assert np.array_equal(result, reference)


@pytest.mark.backend
def test_clip_min(gpu_backend):
    test = [[0, 1], [2, 3]]
    reference = [[1, 1], [2, 3]]

    result = cle.clip(test, min_intensity=1, max_intensity=3)

    assert np.array_equal(result, reference)
