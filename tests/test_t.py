import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_t_2d():
    image = np.random.random((3, 2))

    cle_image = cle.asarray(image)

    assert cle.array_equal(cle_image.T, image.T)


def test_t_3d():
    image = np.random.random((3, 2, 5))

    cle_image = cle.asarray(image)

    assert cle.array_equal(cle_image.T, image.T)
