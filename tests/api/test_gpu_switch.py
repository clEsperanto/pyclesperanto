import numpy as np
import pytest

import pyclesperanto as cle


# this test may only work on a machine with multiple GPUs
@pytest.mark.backend
def test_gpu_switch(gpu_backend):
    image = np.random.random((100, 100))

    # select NVidia
    print(cle.select_device("RTX"))
    cle.gaussian_blur(image, sigma_x=1, sigma_y=1)

    # select AMD
    print(cle.select_device("gfx"))
    cle.gaussian_blur(image, sigma_x=1, sigma_y=1)

    # select Intel
    print(cle.select_device("Intel"))
    cle.gaussian_blur(image, sigma_x=1, sigma_y=1)
