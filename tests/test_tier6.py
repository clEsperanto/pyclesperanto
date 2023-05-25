import pyclesperanto as cle
import numpy as np

data_3d = np.random.random((3,7,10))

def test_voronoi_otsu_labeling():
    cle.voronoi_otsu_labeling(input_image=data_3d, spot_sigma=1, outline_sigma=1)