import importlib
import warnings
from typing import Optional

import numpy as np

from .._array import Image
from .._core import Device
from .._decorators import plugin_function

clic = importlib.import_module("._pyclesperanto", package="pyclesperanto")

@plugin_function
def fft(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """
    Computes the Fast Fourier Transform (FFT) of an image.

    Parameters
    ----------
    input_image : Image
        The input image to be transformed.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The transformed image.
    """

    return clic._fft(device, input_image, output_image)

@plugin_function
def ifft(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """
    Computes the Inverse Fast Fourier Transform (IFFT) of an image.

    Parameters
    ----------
    input_image : Image
        The input image to be transformed.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The transformed image.
    """

    return clic._ifft(device, input_image, output_image)

@plugin_function
def fft_convolution(
    input_image: Image,
    kernel: Image,
    output_image: Optional[Image] = None,
    correlation: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """
    Computes the convolution of an image with a kernel using FFT.

    Parameters
    ----------
    input_image : Image
        The input image to be convolved.
    kernel : Image
        The kernel to convolve with.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The convolved image.
    """

    return clic._fft_convolution(device, input_image, kernel, output_image, correlation)

@plugin_function
def fft_deconvolution(
    input_image: Image,
    kernel: Image,
    normalization_image: Optional[Image] = None,
    output_image: Optional[Image] = None,
    iterations: int = 100,
    regularization: float = 0,
    device: Optional[Device] = None,
) -> Image:
    """
    Computes the deconvolution of an image with a kernel using FFT.

    Parameters
    ----------
    input_image : Image
        The input image to be deconvolved.
    kernel : Image
        The kernel to deconvolve with.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The deconvolved image.
    """

    return clic._fft_deconvolution(device, input_image, kernel, normalization_image, output_image, iterations, regularization)
