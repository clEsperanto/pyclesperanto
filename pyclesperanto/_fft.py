from typing import Optional, Union

from ._array import Image
from ._backend import _get_backend
from ._core import Device
from ._decorators import plugin_function


def smooth_shape(
    shape: Union[tuple, list],
) -> tuple:
    """
    Computes the closest best shape for FFT.

    Parameters
    ----------
    shape : tuple
        The shape of the image (z, y, x).

    Returns
    -------
    tuple
        The shape for FFT (z, y, x).
    """
    length = len(shape)

    if isinstance(shape, tuple):
        shape = list(shape)

    if len(shape) > 3:
        shape = shape[:3]

    shape = [int(s) for s in shape]

    if len(shape) < 3:
        shape = shape + [0] * (3 - len(shape))

    return _get_backend()._smooth_shape(shape)[:length]


@plugin_function
def fft(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
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
    input_image: Image, output_image: Image, device: Optional[Device] = None
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
def convolve(
    input_image: Image,
    kernel: Image,
    output_image: Optional[Image] = None,
    correlate: bool = False,
    device: Optional[Device] = None,
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
    return _get_backend()._convolve(
        device, input_image, kernel, output_image, correlate
    )


@plugin_function
def deconvolve(
    input_image: Image,
    psf: Image,
    normalization: Optional[Image] = None,
    output_image: Optional[Image] = None,
    iteration: int = 100,
    regularization: float = 0.0,
    device: Optional[Device] = None,
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
        Maximum number of iterations.
    regularization: float (= 0.0)
        Regularization parameter.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return _get_backend()._deconvolve(
        device,
        input_image,
        psf,
        normalization,
        output_image,
        int(iteration),
        float(regularization),
    )


__all__ = ["fft", "ifft", "convolve", "deconvolve", "smooth_shape"]
