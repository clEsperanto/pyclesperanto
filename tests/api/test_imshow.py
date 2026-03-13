from unittest.mock import patch

import matplotlib.pyplot as plt
import numpy as np

import pyclesperanto as cle
import pytest


@pytest.mark.backend
@patch("matplotlib.pyplot.show")
def test_imshow(mock_show, gpu_backend):
    image = cle.push(np.random.random((512, 512)))
    cle.imshow(image)


@pytest.mark.backend
@patch("matplotlib.pyplot.show")
def test_imshow_3d(mock_show, gpu_backend):
    image = cle.push(np.random.random((10, 512, 512)))
    cle.imshow(image, colorbar=True)
    plt.show()
    plt.close()


@pytest.mark.backend
@patch("matplotlib.pyplot.show")
def test_imshow_label(mock_show, gpu_backend):
    image = cle.push(np.random.random((512, 512)))
    label = cle.connected_components_labeling(image > 0.8)
    cle.imshow(label, labels=True)
    plt.show()
