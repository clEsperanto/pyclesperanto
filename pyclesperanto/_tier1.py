from ._image import Image
from ._device import Device
from ._memory_operations import create
from ._decorators import plugin_function


@plugin_function
def add_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    """Adds a scalar value s to all pixels x of a given image X.

    <pre>f(x, s) = x + s</pre>

    Parameters
    ----------
    input_image : Image
        The input image where scalare should be added.
    output_image : Image, optional
        The output image where results are written into.
    scalar : float, optional
        The constant number which will be added to all pixels.


    Returns
    -------
    output_image
    """

    from ._pyclesperanto import _AddImageAndScalarKernel_Call as op

    op(device, src=input_image, dst=output_image, scalar=float(scalar))
    return output_image


@plugin_function
def add_images_weighted(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    factor1: float = 1,
    factor2: float = 1,
    device: Device = None,
) -> Image:
    """Calculates the sum of pairs of pixels x and y from images X and Y
    weighted with factors a and b.

    <pre>f(x, y, a, b) = x * a + y * b</pre>

    Parameters
    ----------
    input_image1 : Image
        The first input image to added.
    input_image2 : Image
        The second image to be added.
    output_image : Image, optional
        The output image where results are written into.
    factor1 : float, optional
        The constant number which will be multiplied with each pixel of summand1 before adding it.
    factor2 : float, optional
        The constant number which will be multiplied with each pixel of summand2 before adding it.


    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _AddImagesWeightedKernel_Call as op

    op(
        device,
        src1=input_image1,
        src2=input_image2,
        dst=output_image,
        weight1=float(factor1),
        weight2=float(factor2),
    )
    return output_image


@plugin_function
def gaussian_blur(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 0,
    sigma_y: float = 0,
    sigma_z: float = 0,
    device: Device = None,
) -> Image:
    """Computes the Gaussian blurred image of an image given sigma values
    in X, Y and Z.

    Thus, the filter kernel can have non-isotropic shape.

    The implementation is done separable. In case a sigma equals zero, the
    direction is not blurred.

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional
    sigma_x : Number, optional
    sigma_y : Number, optional
    sigma_z : Number, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _GaussianBlurKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
        sigma_x=float(sigma_x),
        sigma_y=float(sigma_y),
        sigma_z=float(sigma_z),
    )
    return output_image


@plugin_function
def mean_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    """Computes the local mean average of a pixels box-shaped neighborhood.

    The cubes size is specified by its half-width, half-height and
    half-depth (radius).

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional
    radius_x : Number, optional
    radius_y : Number, optional
    radius_z : Number, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _MeanBoxKernel_Call as op

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
def maximum_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    """Computes the local maximum of a pixels cube neighborhood.

    The cubes size is specified by
    its half-width, half-height and half-depth (radius).

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional
    radius_x : Number, optional
    radius_y : Number, optional
    radius_z : Number, optional

    Returns
    -------
    output_image
    """

    from ._pyclesperanto import _MaximumBoxKernel_Call as op

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
def minimum_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None,
) -> Image:
    """Computes the local minimum of a pixels cube neighborhood.

    The cubes size is specified by
    its half-width, half-height and half-depth (radius).

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional
    radius_x : Number, optional
    radius_y : Number, optional
    radius_z : Number, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _MinimumBoxKernel_Call as op

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
def copy(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Copies an image."""
    from ._pyclesperanto import _CopyKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def greater_or_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    """Determines if an images A is greater or equal a given scalar b.

    f(a, b) = 1 if a >= b; 0 otherwise.

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional
    scalar : Number, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _GreaterOrEqualConstantKernel_Call as op

    op(device, src=input_image, dst=output_image, scalar=float(scalar))
    return output_image


@plugin_function
def greater_or_equal(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines if two images A and B greater or equal pixel wise.

    f(a, b) = 1 if a >= b; 0 otherwise.

    Parameters
    ----------
    input_image1 : Image
    input_image2 : Image
    output_image : Image, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _GreaterOrEqualKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def binary_not(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from an image
    X by negating its pixel values
    x using the binary NOT operator !

    All pixel values except 0 in the input image are interpreted as 1.

    <pre>f(x) = !x</pre>

    Parameters
    ----------
    input_image : Image
        The binary input image to be inverted.
    output_image : Image, optional
        The output image where results are written into.

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _BinaryNotKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def binary_and(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two
    images X and Y by connecting pairs of
    pixels x and y with the binary AND operator &.
    All pixel values except 0 in the input images are interpreted as 1.

    <pre>f(x, y) = x & y</pre>

    Parameters
    ----------
    input_image1 : Image
        The first binary input image to be processed.
    input_image2 : Image
        The second binary input image to be processed.
    output_image : Image, optional
        The output image where results are written into.

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _BinaryAndKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def binary_or(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two
    images X and Y by connecting pairs of
    pixels x and y with the binary OR operator |.
    All pixel values except 0 in the input images are interpreted as 1.

    <pre>f(x, y) = x | y</pre>

    Parameters
    ----------
    input_image1 : Image
        The first binary input image to be processed.
    input_image2 : Image
        The second binary input image to be processed.
    output_image : Image, optional
        The output image where results are written into.

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _BinaryOrKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def binary_xor(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two
    images X and Y by connecting pairs of
    pixels x and y with the binary operators AND &, OR | and NOT ! implementing
    the XOR operator.

    All pixel values except 0 in the input images are interpreted as 1.

    <pre>f(x, y) = (x & !y) | (!x & y)</pre>

    Parameters
    ----------
    input_image1 : Image
        The first binary input image to be processed.
    input_image2 : Image
        The second binary input image to be processed.
    output_image : Image, optional
        The output image where results are written into.

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _BinaryXorKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def binary_subtract(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Subtracts one binary image from another.

    Parameters
    ----------
    input_image1 : Image
        The first binary input image to be processed.
    input_image2 : Image
        The second binary input image to be processed.
    output_image : Image, optional
        The output image where results are written into.

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _BinarySubtractKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def dilate_sphere(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary
    dilation of a given input image.

    The dilation takes the von-Neumann-neighborhood (4 pixels in 2D and 6
    pixels in 3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be
    interpreted as 1.

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _DilateSphereKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def erode_sphere(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary
    erosion of a given input image.

    The erosion takes the von-Neumann-neighborhood (4 pixels in 2D and 6
    pixels in 3d) into account.
    The pixels in the input image with pixel value not equal to 0 will be
    interpreted as 1.

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _ErodeSphereKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def maximum_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the maximum intensity projection of an image along Z.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[2]))
    from ._pyclesperanto import _MaximumZProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def maximum_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the maximum intensity projection of an image along Y.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[0], shape[2]))
    from ._pyclesperanto import _MaximumYProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def maximum_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the maximum intensity projection of an image along X.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[0]))
    from ._pyclesperanto import _MaximumXProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def subtract_image_from_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    """Subtracts one image X from a scalar s pixel wise.

    <pre>f(x, s) = s - x</pre>

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional
    scalar : Number, optional

    Returns
    -------
    output_image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_subtractImageFromScalar
    """
    from ._pyclesperanto import _SubtractImageFromScalarKernel_Call as op

    op(device, src=input_image, dst=output_image, scalar=float(scalar))
    return output_image


@plugin_function
def sobel(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Convolve the image with the Sobel kernel.

    Author( device: Device = Nones) -> Image: Ruth Whelan-Jeans, Robert Haase

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional

    Returns
    -------
    output_image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sobel
    """
    from ._pyclesperanto import _SobelKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image

@plugin_function
def minimum_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the minimum intensity projection of an image along Z.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[2]))
    from ._pyclesperanto import _MinimumZProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def minimum_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the minimum intensity projection of an image along Y.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[0], shape[2]))
    from ._pyclesperanto import _MinimumYProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def minimum_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the minimum intensity projection of an image along X.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[0]))
    from ._pyclesperanto import _MinimumXProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image

@plugin_function
def sum_z_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[2]))
    from ._pyclesperanto import _SumZProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def sum_y_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the sum intensity projection of an image along Y.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[0], shape[2]))
    from ._pyclesperanto import _SumYProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def sum_x_projection(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Determines the sum intensity projection of an image along X.

    Parameters
    ----------
    input_image : Image 3D

    Returns
    -------
    Image 2D
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[0]))
    from ._pyclesperanto import _SumXProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image