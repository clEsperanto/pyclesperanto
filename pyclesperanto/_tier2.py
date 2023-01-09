from ._image import Image
from ._device import Device
from ._decorators import plugin_function
from ._memory_operations import create, pull


@plugin_function
def difference_of_gaussian(
    input_image: Image,
    output_image: Image = None,
    sigma1_x: float = 0,
    sigma1_y: float = 0,
    sigma1_z: float = 0,
    sigma2_x: float = 0,
    sigma2_y: float = 0,
    sigma2_z: float = 0,
    device: Device = None,
) -> Image:
    """Applies Gaussian blur to the input image twice with different sigma
    values resulting in two images which are then subtracted from each other.

    It is recommended to apply this operation to images of type Float (32 bit)
    as results might be negative.

    Parameters
    ----------
    input_image : Image
        The input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    sigma1_x : float, default 0
        Sigma of the first Gaussian filter in x
    sigma1_y : float, default 0
        Sigma of the first Gaussian filter in y
    sigma1_z : float, default 0
        Sigma of the first Gaussian filter in z
    sigma2_x : float, default 0
        Sigma of the second Gaussian filter in x
    sigma2_y : float, default 0
        Sigma of the second Gaussian filter in y
    sigma2_z : float, default 0
        Sigma of the second Gaussian filter in z
    device : Device, optional
        The device to be used for computation.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_differenceOfGaussian
    """
    from ._pyclesperanto import _DifferenceOfGaussianKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
        sigma1_x=float(sigma1_x),
        sigma1_y=float(sigma1_y),
        sigma1_z=float(sigma1_z),
        sigma2_x=float(sigma2_x),
        sigma2_y=float(sigma2_y),
        sigma2_z=float(sigma2_z),
    )
    return output_image


@plugin_function
def detect_maxima_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood.

    Pixels in the resulting image are set to 1 if there is no other pixel in a
    given radius which has a
    higher intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image : Image
        The input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    radius_x : int, default 0
        Radius of the square/cubic neighborhood in x
    radius_y : int, default 0
        Radius of the square/cubic neighborhood in y
    radius_z : int, default 0
        Radius of the square/cubic neighborhood in z
    device : Device, optional
        The device to be used for computation.

    Returns
    -------
    output_image: Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    """
    from ._pyclesperanto import _DetectMaximaBoxKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )
    return output_image


@plugin_function
def maximum_of_all_pixels(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the maximum of all pixels in a given image.

    It will be stored in a new row of ImageJs
    Results table in the column 'Max'.

    Parameters
    ----------
    input_image : Image
        The image of which the maximum of all pixels or voxels will be determined.
    output_image : Image, optional
        The output image where results are written into.
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    maximum : scalar

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumOfAllPixels
    """
    output_image = create((1, 1, 1), dtype=input_image.dtype)
    from ._pyclesperanto import _MaximumOfAllPixelsKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return pull(output_image).item()


@plugin_function
def minimum_of_all_pixels(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the minimum of all pixels in a given image.

    It will be stored in a new row of ImageJs
    Results table in the column 'Min'.

    Parameters
    ----------
    input_image : Image
        The image of which the minimum of all pixels or voxels will be determined.
    output_image : Image, optional
        The output image where results are written into.
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    minimum : scalar

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumOfAllPixels
    """
    output_image = create((1, 1, 1), dtype=input_image.dtype)
    from ._pyclesperanto import _MinimumOfAllPixelsKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return pull(output_image).item()


@plugin_function
def sum_of_all_pixels(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the sum of all pixels in a given image.

    It will be stored in a new row of ImageJs
    Results table in the column 'Sum'.

    Parameters
    ----------
    input_image : Image
        The image of which all pixels or voxels will be summed.
    output_image : Image, optional
        The output image where results are written into.
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    sum : scalar

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sumOfAllPixels
    """
    output_image = create((1, 1, 1), dtype=input_image.dtype)
    from ._pyclesperanto import _SumOfAllPixelsKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return pull(output_image).item()


@plugin_function
def extend_labeling_via_voronoi(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Takes a label map image and dilates the regions using a octagon shape
    until they touch.

    The resulting label map is written to the output.

    Parameters
    ----------
    input_image : Image
        The input label map.
    output_image : Image, optional
        The output label map.
    device: Device, optional

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_extendLabelingViaVoronoi
    """
    from ._pyclesperanto import _ExtendLabelingViaVoronoiKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def top_hat_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    """Applies a top-hat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image : Image
        The input image where the background is subtracted from.
    output_image : Image, optional
        The output image where results are written into.
    radius_x : Image, default 0
        Radius of the background determination region in X.
    radius_y : Image, default 0
        Radius of the background determination region in Y.
    radius_z : Image, default 0
        Radius of the background determination region in Z.
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_topHatBox
    """
    from ._pyclesperanto import _TopHatBoxKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z),
    )
    return output_image
