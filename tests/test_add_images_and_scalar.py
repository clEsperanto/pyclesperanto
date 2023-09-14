import pyclesperanto as cle
import numpy as np


def test_add_image_and_scalar():
    data = np.arange(100).reshape(10, 10)
    # push an array to the GPU
    flip = cle.push(data)
    flop = cle.create_like(data)
    cle.add_image_and_scalar(flip, flop, 100.0)
    np.testing.assert_allclose(data + 100, flop.get())
