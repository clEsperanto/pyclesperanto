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

    def make_gaussian(sigma, radius):
        x = np.arange(-radius, radius + 1)
        gaussian = np.exp(-0.5 * (x / sigma) ** 2)
        gaussian /= gaussian.sum()  # Normalize the kernel
        gaussian_derivative = -x * gaussian / (sigma**2)
        return gaussian, gaussian_derivative

    gaussian, gaussian_derivative = make_gaussian(sigma_scaled, lw)

    dirac = np.zeros((lw * 2 + 1, lw * 2 + 1)).astype(np.float32)
    dirac[lw, lw] = 1.0

    smoothed_rows = np.apply_along_axis(
        lambda row: np.convolve(row, gaussian, mode="same"), axis=0, arr=dirac
    )
    Ix = np.apply_along_axis(
        lambda col: np.convolve(col, gaussian_derivative, mode="same"),
        axis=1,
        arr=smoothed_rows,
    )

    smoothed_rows = np.apply_along_axis(
        lambda row: np.convolve(row, gaussian, mode="same"), axis=0, arr=Ix
    )
    Ixx = np.apply_along_axis(
        lambda col: np.convolve(col, gaussian_derivative, mode="same"),
        axis=1,
        arr=smoothed_rows,
    )

    smoothed_rows = np.apply_along_axis(
        lambda row: np.convolve(row, gaussian, mode="same"), axis=1, arr=Ix
    )
    Ixy = np.apply_along_axis(
        lambda col: np.convolve(col, gaussian_derivative, mode="same"),
        axis=0,
        arr=smoothed_rows,
    )

    gsd_xx_gpu = Array.from_array(Ixx)
    gsd_xy_gpu = Array.from_array(Ixy)

    # Execute the OpenCL kernel
    params = {
        "src": input_image,
        "gsd_xx": gsd_xx_gpu,
        "gsd_xy": gsd_xy_gpu,
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
