import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_push_np(gpu_backend):
    reference = np.asarray([[1, 2], [-3, 4]])

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)


@pytest.mark.backend
def test_push_list(gpu_backend):
    reference = [[1, 2], [-3, 4]]

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)


@pytest.mark.backend
def test_push_tuple(gpu_backend):
    reference = ([1, 2], [-3, 4])

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)
