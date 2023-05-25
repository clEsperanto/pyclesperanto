import pyclesperanto as cle
import numpy as np

data_3d=np.random.random((3,7,10))

def test_difference_of_gaussian():
    cle.difference_of_gaussian(input_image=data_3d, sigma1_x=3, sigma1_y=3, sigma1_z=3, sigma2_x=1, sigma2_y=1, sigma2_z=1)

def test_maximum_of_all_pixels():
    cle.maximum_of_all_pixels(input_image=data_3d)

def test_minimum_of_all_pixels():
    cle.minimum_of_all_pixels(input_image=data_3d)

def test_sum_of_all_pixels():
    cle.sum_of_all_pixels(input_image=data_3d)

def test_extend_labeling_via_voronoi():
    cle.extend_labeling_via_voronoi(input_image=data_3d)

def test_top_hat_box():
    cle.top_hat_box(input_image=data_3d, radius_x=2, radius_y=2, radius_z=1)