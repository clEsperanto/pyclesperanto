#
# This code is auto-generated from CLIc 'cle::tier8.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._backend import _get_backend
from ._core import Device
from ._decorators import plugin_function


@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def smooth_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Applies a morphological opening operation to a label image and afterward   fills
    gaps between the labels using Voronoi labeling. Finally, the result   label
    image is masked so that all background pixels remain background pixels.   Note:
    It is recommended to process isotropic label images.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    radius: int (= 0)
        Smoothing
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._smooth_labels(device, input_image, output_image, int(radius))

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def smooth_connected_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Applies a morphological erosion and dilation of the label image with respect to
    the connectivity of the labels.     Note: It is recommended to process isotropic
    label images.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    radius: int (= 0)
        Smoothing
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._smooth_connected_labels(device, input_image, output_image, int(radius))

@plugin_function
def fft(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Performs a 1D, 2D, or 3D FFT (Fast Fourier Transform) on the input image.

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Optional[Image] (= None)
        Output image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._fft(device, input_image, output_image)

@plugin_function
def ifft(
    input_image: Image,
    output_image: Image,
    device: Optional[Device] =None
) -> Image:
    """Performs a 1D, 2D, or 3D IFFT (Inverse Fast Fourier Transform) on the input
    image. The input image must be Hermitian, and the output image must be provided
    as the second argument.

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Image 
        Output image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._ifft(device, input_image, output_image)

@plugin_function
def convolve_fft(
    input_image: Image,
    kernel: Image,
    output_image: Optional[Image] =None,
    correlate: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Performs a 1D, 2D, or 3D convolution using FFT between an input image and a
    kernel. Input image, PSF kernel, and normalization image are expected to be in
    the spatial domain. The function will automatically pad the input image and PSF
    kernel to the same size as the closest smooth size and will take care of the PSF
    kernel centering.

    Parameters
    ----------
    input_image: Image 
        Input image.
    kernel: Image 
        Kernel image.
    output_image: Optional[Image] (= None)
        Output image.
    correlate: bool (= False)
        If true, convolution with the PSF reversed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._convolve_fft(device, input_image, kernel, output_image, correlate)

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
    """Performs a 1D, 2D, or 3D deconvolution using FFT between an input image and a
    PSF kernel. The deconvolution is performed using the Richardson-Lucy algorithm
    and requires a maximum iteration number. The user can specify a normalization
    image (optional) and a regularization parameter (optional) to apply Total
    Variation regularization. Input image, PSF kernel, and normalization image are
    expected to be in the spatial domain. The function will automatically pad the
    input image and PSF kernel to the same size as the closest smooth size and will
    take care of the PSF kernel centering.

    Parameters
    ----------
    input_image: Image 
        Input image.
    psf: Image 
        Kernel image.
    normalization: Optional[Image] (= None)
        Normalization image.
    output_image: Optional[Image] (= None)
        Output image.
    iteration: int (= 100)
        Maximum number of
    regularization: float (= 0.0)
        Regularization parameter.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._deconvolve_fft(device, input_image, psf, normalization, output_image, int(iteration), float(regularization))

@plugin_function
def make_isotropic(
    input_image: Image,
    output_image: Optional[Image] =None,
    current_spacing_x: float =1.0,
    current_spacing_y: float =1.0,
    current_spacing_z: float =1.0,
    target_spacing: float =-1.0,
    interpolate: bool =true,
    device: Optional[Device] =None
) -> Image:
    """Resamples an image to make it isotropic by rescaling the image to a target
    spacing. The current spacings of the image in x, y, and z dimensions must be
    provided and should be >= 0. If the target spacing is <= 0 or not provided, the
    function assumes the target spacing is the minimum of the current spacings.
    Finally, an interpolation option is provided to choose whether to interpolate
    the image during rescaling or not (default is true). For label images, it is
    recommended to set the interpolation option to false.

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Optional[Image] (= None)
        Output image.
    current_spacing_x: float (= 1.0)
        Original spacing in x dimension.
    current_spacing_y: float (= 1.0)
        Original spacing in y dimension.
    current_spacing_z: float (= 1.0)
        Original spacing in z dimension.
    target_spacing: float (= -1.0)
        Target isotropic spacing.
    interpolate: bool (= true)
        If true,
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._make_isotropic(device, input_image, output_image, float(current_spacing_x), float(current_spacing_y), float(current_spacing_z), float(target_spacing), interpolate)

@plugin_function
def make_anisotropic(
    input_image: Image,
    output_image: Optional[Image] =None,
    current_spacing: float =-1.0,
    target_spacing_x: float =-1.0,
    target_spacing_y: float =-1.0,
    target_spacing_z: float =-1.0,
    interpolate: bool =true,
    device: Optional[Device] =None
) -> Image:
    """Resamples an image to make it anisotropic by rescaling the image to target
    spacings in x, y, and z dimensions. The current isotropic spacing of the image
    in each dimension must be provided and should be >= 0. If the target spacings
    for x, y, and z shoudl be provided and >= 0. Finally, an interpolation option is
    provided to choose whether to interpolate the image during rescaling or not
    (default is true). For label images, it is recommended to set the interpolation
    option to false.

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Optional[Image] (= None)
        Output image.
    current_spacing: float (= -1.0)
        Current spacing of the image in each dimension.
    target_spacing_x: float (= -1.0)
        Target spacing in x dimension.
    target_spacing_y: float (= -1.0)
        Target spacing in y dimension.
    target_spacing_z: float (= -1.0)
        Target spacing in z dimension.
    interpolate: bool (= true)
        If true,
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._make_anisotropic(device, input_image, output_image, float(current_spacing), float(target_spacing_x), float(target_spacing_y), float(target_spacing_z), interpolate)

__all__ = ["smooth_labels", "smooth_connected_labels", "fft", "ifft", "convolve_fft", "deconvolve_fft", "make_isotropic", "make_anisotropic"]