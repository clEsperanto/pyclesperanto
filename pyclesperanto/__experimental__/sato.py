from random import gauss
from typing import Optional

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute
from pyclesperanto._tier1 import (
    gaussian_blur,
    gradient_x,
    gradient_y,
    gradient_z,
    hessian_eigenvalues,
    maximum_images,
    multiply_images,
)
from pyclesperanto._tier2 import clip
from pyclesperanto._tier7 import scale

from .hessian_gaussian_eigenvalues import hessian_gaussian_eigenvalues


@plugin_function
def sato(
    input_image: Image,
    output_image: Optional[Image] = None,
    sigma_minimum: float = 1,
    sigma_maximum: float = 3,
    sigma_step: float = 1,
    device: Optional[Device] = None,
) -> Image:

    if output_image is None:
        output_image = Array.zeros_like(input_image)

    sigmas = range(int(sigma_minimum), int(sigma_maximum), int(sigma_step))

    for sigma in sigmas:

        # compute the hessian eigenvalues and keep only the largest and middle eigenvalues
        middle = Array.zeros_like(input_image)
        large = Array.zeros_like(input_image)
        hessian_gaussian_eigenvalues(
            input_image, sigma=sigma, output_large=large, output_middle=middle
        )
        # hessian_eigenvalues(blurred, middle_eigenvalue=middle, large_eigenvalue=large)

        # clip the eigenvalues to avoid negative values
        large = clip(large, min_intensity=0, max_intensity=large.max())
        middle = clip(middle, min_intensity=0, max_intensity=middle.max())

        # compute the mean eigenvalues
        mean_eigenvalues = large
        if input_image.ndim == 3:
            mean_eigenvalues = multiply_images(middle, large) ** (0.5)
        value = mean_eigenvalues * (sigma**2)

        output_image = maximum_images(output_image, value)

    return output_image
