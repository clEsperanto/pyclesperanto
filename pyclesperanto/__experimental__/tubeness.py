from typing import Optional

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute

from pyclesperanto._tier1 import absolute, power, maximum_images
from pyclesperanto._tier2 import minimum_of_all_pixels, hessian_gaussian_eigenvalues, clip

import numpy as np

@plugin_function
def sato(
    input_image: Image,
    output_image: Optional[Image] = None,
    sigma_min: float = 1.0,
    sigma_max: float = 5.0,
    sigma_step: float = 1.0,
    device: Optional[Device] = None,
) -> Image:

    input_image = Array.to_device(input_image)
    output_image = Array.empty_like(input_image)
    output_image.fill(0)

    is_3d = len(input_image.shape) == 3

    small_eigen = Array.empty_like(input_image)
    middle_eigen = Array.empty_like(input_image)

    for sigma in np.arange(sigma_min, sigma_max + 0.1, sigma_step):

        sigma_squared = sigma * sigma

        hessian_gaussian_eigenvalues(input_image, small_eigenvalue=small_eigen, middle_eigenvalue=middle_eigen, sigma=sigma)

        min = minimum_of_all_pixels(small_eigen)
        small_eigen = clip(small_eigen, min_intensity=min, max_intensity=0)

        if is_3d:
            min = minimum_of_all_pixels(middle_eigen)
            middle_eigen = clip(middle_eigen, min_intensity=min, max_intensity=0)

            temp = power(small_eigen * middle_eigen, scalar=0.5) * sigma_squared
        else:
            temp = absolute(small_eigen) * sigma_squared

        output_image = maximum_images(output_image, temp)

    return output_image
