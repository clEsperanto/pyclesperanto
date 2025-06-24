from typing import Optional

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute
from pyclesperanto._tier1 import (
    gaussian_blur,
    hessian_eigenvalues,
    maximum_images,
    multiply_images,
)
from pyclesperanto._tier2 import clip
from pyclesperanto._tier7 import scale


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

        # prepare sigma values
        squared_sigma = sigma**2
        half_sigma = sigma / 2.0
        inverse_sigma = 1.0 / sigma

        # blur the image and downscale for approximate the hessian with gaussian derivatives
        blurred = gaussian_blur(
            input_image, sigma_x=half_sigma, sigma_y=half_sigma, sigma_z=half_sigma
        )
        downscale = scale(
            blurred,
            factor_x=inverse_sigma,
            factor_y=inverse_sigma,
            factor_z=inverse_sigma,
            centered=True,
            resize=True,
            interpolate=False,
        )

        # compute the hessian eigenvalues and keep only the largest and middle eigenvalues
        middle = Array.zeros_like(input_image)
        large = Array.zeros_like(input_image)
        hessian_eigenvalues(downscale, middle_eigenvalue=middle, large_eigenvalue=large)

        # clip the eigenvalues to avoid negative values
        large = clip(large, min_intensity=0, max_intensity=large.max())
        middle = clip(middle, min_intensity=0, max_intensity=middle.max())

        # compute the mean eigenvalues
        mean_eigenvalues = (
            multiply_images(middle, large) ** (1 / 2)
            if input_image.ndim == 3
            else large
        )
        value = mean_eigenvalues * squared_sigma

        # upscale the mean eigenvalues and add to the output image
        upscale = scale(
            value,
            factor_x=sigma,
            factor_y=sigma,
            factor_z=sigma,
            centered=True,
            resize=True,
            interpolate=False,
        )
        output_image = maximum_images(output_image, upscale)

    return output_image
