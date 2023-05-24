import pyclesperanto as cle
import numpy as np

def connected_components_labeling_box():
    cle.connected_components_labeling_box(np.random.rand(40, 40))


def threshold_otsu():
    cle.threshold_otsu(np.random.rand(10, 10))