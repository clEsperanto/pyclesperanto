import functools
import math
from typing import Optional

import numpy as np
from scipy import ndimage as ndi

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute, execute_separable
from pyclesperanto._tier1 import gaussian_blur


@plugin_function
def gaussian_derivative(
    input_image: Image,
    output: Optional[Image] = None,
    sigma_x: float = 0,
    sigma_y: float = 0,
    sigma_z: float = 0,
    order_x: int = 0,
    order_y: int = 0,
    order_z: int = 0,
    device: Optional[Device] = None,
) -> Image:
    """
    This function applies a Gaussian derivative filter to the input image.
    If all the orders are zero, it is the same as a Gaussian blur.

    Parameters
    ----------
    input_image : Image
        The input image to process.
    output : Optional[Image], optional
        The output image to store the result, by default None.
    sigma_x : float, optional
        The standard deviation for Gaussian kernel in the x direction, by default 0.
    sigma_y : float, optional
        The standard deviation for Gaussian kernel in the y direction, by default 0.
    sigma_z : float, optional
        The standard deviation for Gaussian kernel in the z direction, by default 0.
    order_x : int, optional
        The order of the derivative in the x direction, by default 0.
    order_y : int, optional
        The order of the derivative in the y direction, by default 0.
    order_z : int, optional
        The order of the derivative in the z direction, by default 0.
    device : Optional[Device], optional
        The device to run the operation on, by default None.

    Returns
    -------
    Image
        The output image with Gaussian derivative applied.
    """

    if output is None:
        output = Array.zeros_like(input_image)

    truncate = 8
    sigmas = [max(0, sigma_x), max(0, sigma_y), max(0, sigma_z)]
    radii = [int(truncate * sigma + 0.5) for sigma in sigmas]
    orders = [min(order, 2) for order in [order_x, order_y, order_z]]

    execute_separable(
        anchor=__file__,
        kernel_source="gaussian_derivative_separable.cl",
        kernel_name="gaussian_derivative_separable",
        src=input_image,
        dst=output,
        sigma=sigmas,
        radius=radii,
        orders=orders,
        device=device,
    )

    return output
