import pyclesperanto as cle
import numpy as np

def voronoi_otsu_labeling():
    cle.voronoi_otsu_labeling(np.random.rand(10, 10), spot_sigma = 1.0, outline_sigma = 1.0)