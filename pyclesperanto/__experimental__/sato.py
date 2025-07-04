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
    multiply_image_and_scalar,
    multiply_images,
    power,
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

    is_3d = len(input_image.shape) == 3

    large = Array.zeros_like(input_image)
    middle = Array.zeros_like(input_image) if is_3d else None

    sigmas = range(int(sigma_minimum), int(sigma_maximum), int(sigma_step))
    for sigma in sigmas:

        # We compute the Hessian eigenvalues using a Gaussian derivative approach
        # We discard the smallest eigenvalue, which is not needed for Sato's method
        # and keep the largest and the middle eigenvalue (if 3D).
        hessian_gaussian_eigenvalues(
            input_image,
            sigma=sigma,
            output_small=None,
            output_large=large,
            output_middle=middle,
        )

        # We clip the largest eigenvalues to 0
        max = large.max()
        large = clip(large, min_intensity=0, max_intensity=max)
        mean_eigenvalues = large

        if is_3d:
            # We clip the middle eigenvalues to 0
            max = middle.max()
            middle = clip(middle, min_intensity=0, max_intensity=max)
            # We compute the mean eigenvalues between the large and middle eigenvalues
            mean_eigenvalues = power(multiply_images(middle, large), scalar=0.5)
        else:
            # For 2D images, we just use the large eigenvalues
            mean_eigenvalues = large

        # We multiply the mean eigenvalues by sigma^2 and add it to the output image
        # using maximum operation
        sigma_squared = sigma**2
        value = multiply_image_and_scalar(mean_eigenvalues, scalar=sigma_squared)
        output_image = maximum_images(output_image, value)

    return output_image
