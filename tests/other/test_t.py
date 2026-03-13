import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_t_2d(gpu_backend):
    image = np.random.random((3, 2))

    cle_image = cle.asarray(image)

    assert cle.array_equal(cle_image.T, image.T)


@pytest.mark.backend
def test_t_3d(gpu_backend):
    image = np.random.random((3, 2, 5))

    cle_image = cle.asarray(image)

    assert cle.array_equal(cle_image.T, image.T)
