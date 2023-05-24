import pyclesperanto as cle
import numpy as np

def difference_of_gaussian():
    cle.difference_of_gaussian(np.random.rand(10, 10), sigma1_x = 3.0, sigma1_y = 3.0, sigma1_z = 3.0, sigma2_x = 1.0, sigma2_y = 1.0, sigma2_z = 1.0)


def detect_maxima_box():
    cle.detect_maxima_box(np.random.rand(20, 20), radius_x = 2, radius_y = 2, radius_z = 1)


def maximum_of_all_pixels():
    cle.maximum_of_all_pixels(np.random.rand(20, 20))


def minimum_of_all_pixels():
    cle.minimum_of_all_pixels(np.random.rand(10, 10))


def sum_of_all_pixels():
    cle.sum_of_all_pixels(np.random.rand(20, 20))


def extend_labeling_via_voronoi():
    cle.extend_labeling_via_voronoi(np.random.rand(10, 10))


def top_hat_box():
    cle.top_hat_box(np.random.rand(10, 10), radius_x = 2, radius_y = 2, radius_z = 1)