import pyclesperanto as cle
import numpy as np

def test_add_image_and_scalar():
    cle.add_image_and_scalar(np.random.rand(10, 10), scalar=1.0)