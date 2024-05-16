from unittest.mock import patch

import matplotlib.pyplot as plt
import numpy as np

import pyclesperanto as cle


@patch("matplotlib.pyplot.show")
def test_imshow(mock_show):
    image = cle.push(np.random.random((512, 512)))
    cle.imshow(image)


@patch("matplotlib.pyplot.show")
def test_imshow_3d(mock_show):
    image = cle.push(np.random.random((10, 512, 512)))
    cle.imshow(image, colorbar=True)
    plt.show()
    plt.close()


@patch("matplotlib.pyplot.show")
def test_imshow_label(mock_show):
    image = cle.push(np.random.random((512, 512)))
    label = cle.connected_components_labeling(image > 0.8)
    cle.imshow(label, labels=True)
    plt.show()
