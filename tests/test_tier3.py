import pyclesperanto as cle
import numpy as np

def histogram():
    cle.histogram(np.random.rand(30, 30).astype(int), bins = 250)