import importlib
import warnings
from typing import Optional, Tuple

import numpy as np

from .._array import Image
from .._core import Device
from .._decorators import plugin_function

clic = importlib.import_module("._pyclesperanto", package="pyclesperanto")


def fft_smooth_shape(
    shape: list,
) -> tuple:
    """
    Computes the shape for FFT smoothing.

    Parameters
    ----------
    shape : tuple
        The shape of the image.

    Returns
    -------
    tuple
        The shape for FFT smoothing.
    """
    length = len(shape)

    if isinstance(shape, Tuple):
        shape = list(shape)

    if len(shape) > 3:
        shape = shape[:3]

    shape = [int(s) for s in shape]

    if len(shape) < 3:
        shape = shape + [0] * (3 - len(shape))

    return clic._fft_smooth_shape(shape)[:length]


@plugin_function
def pad(
    input_image: Image,
    output_image: Optional[Image] = None,
    size_x: int = 0,
    size_y: int = 0,
    size_z: int = 0,
    value: float = 0,
    center: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """
    Pads an image with zeros.

    Parameters
    ----------
    input_image : Image
        The input image to be padded.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    size_x : int, optional
        The new size with padding along x direction. Default is 0.
    size_y : int, optional
        The new size with padding along y direction. Default is 0.
    size_z : int, optional
        The new size with padding along z direction. Default is 0.
    value : float, optional
        The value to use for padding. Default is 0.
    center : bool, optional
        If True, the padding will be spread evenly around the image. Default is False.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The padded image.
    """

    return clic._pad(
        device, input_image, output_image, size_x, size_y, size_z, value, center
    )


@plugin_function
def unpad(
    input_image: Image,
    output_image: Optional[Image] = None,
    size_x: int = 0,
    size_y: int = 0,
    size_z: int = 0,
    center: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """
    Unpads an image by removing the padding.

    Parameters
    ----------
    input_image : Image
        The input image to be unpadded.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    size_x : int, optional
        The new size without padding along x direction. Default is 0.
    size_y : int, optional
        The new size without padding along y direction. Default is 0.
    size_z : int, optional
        The new size without padding along z direction. Default is 0.
    center : bool, optional
        If True, the padding will be cropped evenly around the image. Default is False.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The unpadded image.
    """

    return clic._unpad(
        device, input_image, output_image, size_x, size_y, size_z, center
    )


@plugin_function
def circular_shift(
    input_image: Image,
    output_image: Optional[Image] = None,
    x_shift: int = 0,
    y_shift: int = 0,
    z_shift: int = 0,
    device: Optional[Device] = None,
) -> Image:
    """
    Circularly shifts an image by the specified amounts.

    Parameters
    ----------
    input_image : Image
        The input image to be shifted.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    x_shift : int, optional
        The amount to shift in the x direction. Default is 0.
    y_shift : int, optional
        The amount to shift in the y direction. Default is 0.
    z_shift : int, optional
        The amount to shift in the z direction. Default is 0.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The shifted image.
    """

    return clic._circular_shift(
        device, input_image, output_image, x_shift, y_shift, z_shift
    )


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
def convolve_fft(
    input_image: Image,
    kernel: Image,
    output_image: Optional[Image] = None,
    correlate: bool = False,
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
    correlate : bool, optional
        If True, convolution with the PSF reversed. Default is False.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The convolved image.
    """

    return clic._convolve_fft(device, input_image, kernel, output_image, correlate)


@plugin_function
def deconvolve_fft(
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

    return clic._deconvolve_fft(
        device,
        input_image,
        kernel,
        normalization_image,
        output_image,
        iterations,
        regularization,
    )
