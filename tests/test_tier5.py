import pyclesperanto as cle
import numpy as np

def masked_voronoi_labeling():
    cle.masked_voronoi_labeling(np.random.rand(40, 40), np.random.rand(20, 20))