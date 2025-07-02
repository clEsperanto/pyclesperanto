import functools
import math
from typing import Optional

import numpy as np
from scipy import ndimage as ndi

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute
from pyclesperanto._tier2 import maximum_of_all_pixels, minimum_of_all_pixels

from .gaussian_derivative import gaussian_derivative


@plugin_function
def hessian_gaussian_eigenvalues(
    input_image: Image,
    output_large: Optional[Image] = None,
    output_middle: Optional[Image] = None,
    output_small: Optional[Image] = None,
    sigma: int = 1,
    device: Optional[Device] = None,
) -> Image:

    if output_large is None:
        output_large = Array.zeros_like(input_image)
    if output_middle is None:
        output_middle = Array.zeros_like(input_image)
    if output_small is None:
        output_small = Array.zeros_like(input_image)

    truncate = 8  # truncate at 8 sigma
    sq1_2 = 1 / math.sqrt(2)
    sigma_scaled = sigma * sq1_2  # scale sigma for Gaussian derivative
    lw = int(truncate * sigma_scaled + 0.5)

    dirac = np.zeros((lw * 2 + 1, lw * 2 + 1)).astype(np.float32)
    dirac[lw, lw] = 1.0

    Ix = gaussian_derivative(
        dirac,
        sigma_x=sigma_scaled,
        sigma_y=sigma_scaled,
        sigma_z=sigma_scaled,
        order_x=1,
        order_y=0,
        order_z=0,
    )
    Ixy = gaussian_derivative(
        Ix,
        sigma_x=sigma_scaled,
        sigma_y=sigma_scaled,
        sigma_z=sigma_scaled,
        order_x=0,
        order_y=1,
        order_z=0,
    )
    Ixx = gaussian_derivative(
        Ix,
        sigma_x=sigma_scaled,
        sigma_y=sigma_scaled,
        sigma_z=sigma_scaled,
        order_x=1,
        order_y=0,
        order_z=0,
    )

    del Ix

    # Execute the OpenCL kernel
    params = {
        "src": input_image,
        "g_xx": Ixx,
        "g_xy": Ixy,
        "small_eigenvalue": output_small,
        "middle_eigenvalue": output_middle,
        "large_eigenvalue": output_large,
    }
    execute(
        anchor=__file__,
        kernel_source="hessian_gaussian_eigenvalues.cl",
        kernel_name="hessian_gaussian_eigenvalues",
        device=device,
        global_size=input_image.shape,
        parameters=params,
    )
    return [output_large, output_middle, output_small]
