#
# This code is auto-generated from CLIc 'cle::tier8.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional, List

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def smooth_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Apply a morphological opening operation to a label image and afterwards   fills
    gaps between the labels using voronoi-labeling. Finally, the result   label
    image is masked so that all background pixels remain background pixels.   Note:
    It is recommended to process isotropic label images.

    Parameters
    ----------
    input_image: Image 
        Input label image
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 0)
        Smoothing
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._smooth_labels(device, input_image, output_image, int(radius))

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def smooth_connected_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Apply a morphological erosion and dilation of the label image with respect to
    the connectivity of the labels.   Note: It is recommended to process isotropic
    label images.

    Parameters
    ----------
    input_image: Image 
        Input label image
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 0)
        Smoothing
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._smooth_connected_labels(device, input_image, output_image, int(radius))

@plugin_function
def fft(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Perform a 1D, 2D or 3D FFT (Fast Fourier Transform) on the input image

    Parameters
    ----------
    input_image: Image 
        Input image
    output_image: Optional[Image] (= None)
        Output image
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._fft(device, input_image, output_image)

@plugin_function
def ifft(
    input_image: Image,
    output_image: Image,
    device: Optional[Device] =None
) -> Image:
    """Perform a 1D, 2D or 3D IFFT (Inverse Fast Fourier Transform) on the input image.
    The input image must be hermitian and the output image must be provided as the
    second argument.

    Parameters
    ----------
    input_image: Image 
        Input image
    output_image: Image 
        Output image
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._ifft(device, input_image, output_image)

@plugin_function
def convolve_fft(
    input_image: Image,
    kernel: Image,
    output_image: Optional[Image] =None,
    correlate: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Perform a 1D, 2D or 3D convolution using FFT between an input image and a kernel
    Input image, psf kernel, and normalization image are expected to be in the
    spatial domain. The function will automatically pad the input image and psf
    kernel to the same size as the closest smooth size and will take care of the psf
    kernel centering.

    Parameters
    ----------
    input_image: Image 
        Input image
    kernel: Image 
        Kernel image
    output_image: Optional[Image] (= None)
        Output image
    correlate: bool (= False)
        If true, convolution with the PSF reversed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._convolve_fft(device, input_image, kernel, output_image, correlate)

@plugin_function
def deconvolve_fft(
    input_image: Image,
    psf: Image,
    normalization: Optional[Image] =None,
    output_image: Optional[Image] =None,
    iteration: int =100,
    regularization: float =0.0,
    device: Optional[Device] =None
) -> Image:
    """Perform a 1D, 2D or 3D deconvolution using FFT between an input image and a psf
    kernel. The deconvolution is performed using the Richardson-Lucy algorithm and
    will requires a maximum iteration number. User can specify a normalization image
    (optional) and a regularization parameter (optional) to apply a Total Variation
    regularization. Input image, psf kernel, and normalization image are expected to
    be in the spatial domain. The function will automatically pad the input image
    and psf kernel to the same size as the closest smooth size and will take care of
    the psf kernel centering.

    Parameters
    ----------
    input_image: Image 
        Input image
    psf: Image 
        Kernel image
    normalization: Optional[Image] (= None)
        Normalization image
    output_image: Optional[Image] (= None)
        Output image
    iteration: int (= 100)
        Maximum number of
    regularization: float (= 0.0)
        Regularization parameter
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._deconvolve_fft(device, input_image, psf, normalization, output_image, int(iteration), float(regularization))