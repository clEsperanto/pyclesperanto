import pyclesperanto as cle
import numpy as np

data_3d = np.random.random((3,7,10))

def test_histogram():
    cle.histogram(input_image=data_3d, bins=255)