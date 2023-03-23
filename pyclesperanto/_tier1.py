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
    scalar : float, default: 0
        The constant number which will be added to all pixels.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImageAndScalar
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
    factor1 : float, default: 1
        The constant number which will be multiplied with each pixel of summand1 before adding it.
    factor2 : float, default: 1
        The constant number which will be multiplied with each pixel of summand2 before adding it.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_addImagesWeighted
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
        image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    sigma_x : Number, default: 0
    sigma_y : Number, default: 0
    sigma_z : Number, default: 0
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gaussianBlur
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
        image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    radius_x : Number, default: 0
    radius_y : Number, default: 0
    radius_z : Number, default: 0
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_meanBox
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
        image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    radius_x : Number, default: 0
    radius_y : Number, default: 0
    radius_z : Number, default: 0
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumBox
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
        image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    radius_x : Number, default: 0
    radius_y : Number, default: 0
    radius_z : Number, default: 0
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumBox
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
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Copies an image into a new image.

    Parameters
    ----------
    input_image : Image
        image to be copied
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_copy
    """
    from ._pyclesperanto import _CopyKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def divide_images(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Divides two images pixel wise.

    Parameters
    ----------
    input_image1 : Image
        numerator image
    input_image2 : Image
        denominator image
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_divideImages
    """
    from ._pyclesperanto import _DivideImagesKernel_Call as op

    op(
        device,
        src1=input_image1,
        src2=input_image2,
        dst=output_image,
    )
    return output_image


@plugin_function
def gradient_x(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes the gradient of an image along X direction.

    Parameters
    ----------
    input_image : Image
        Image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image: Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientX
    """
    from ._pyclesperanto import _GradientXKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
    )
    return output_image


@plugin_function
def gradient_z(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes the gradient of an image along Z direction.

    Parameters
    ----------
    input_image : Image
        Image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image: Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientZ
    """
    from ._pyclesperanto import _GradientZKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
    )
    return output_image


@plugin_function
def gradient_y(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes the gradient of an image along Y direction.

    Parameters
    ----------
    input_image : Image
        Image to be filtered
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image: Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gradientY
    """
    from ._pyclesperanto import _GradientYKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def greater(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines if an images A is greater than image B.

    f(a, b) = 1 if a > b; 0 otherwise.

    Parameters
    ----------
    input_image1 : Image
        image to be compared
    input_image2 : Image
        image to be compared
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greater
    """
    from ._pyclesperanto import _GreaterKernel_Call as op

    op(
        device,
        src1=input_image1,
        src2=input_image2,
        dst=output_image,
    )
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
        image to be compared
    output_image : Image, optional
        The output image where results are written into.
    scalar : Number, default 0
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greaterOrEqualConstant
    """
    from ._pyclesperanto import _GreaterOrEqualConstantKernel_Call as op

    op(device, src=input_image, dst=output_image, scalar=float(scalar))
    return output_image


@plugin_function
def greater_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    """Determines if an images A is greater a given scalar b.

    f(a, b) = 1 if a > b; 0 otherwise.

    Parameters
    ----------
    input_image : Image
        image to be compared
    output_image : Image, optional
        The output image where results are written into.
    scalar : Number, default 0
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greaterConstant
    """
    from ._pyclesperanto import _GreaterConstantKernel_Call as op

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
        image to be compared
    input_image2 : Image
        image to be compared
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_greaterOrEqual
    """
    from ._pyclesperanto import _GreaterOrEqualKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def binary_not(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
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
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryNot
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
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryAnd
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
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryOr
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
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryXor
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
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image
    """
    from ._pyclesperanto import _BinarySubtractKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def dilate_sphere(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
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
        The input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_dilateSphere
    """
    from ._pyclesperanto import _DilateSphereKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def equal_constant(
    input_image: Image,
    constant: float = 0,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the
    result of comparing each pixel value in a given input image
    to a constant value.

    <pre>f(x) = x == constant</pre>

    Parameters
    ----------
    input_image : Image
        The input image to be processed.
    constant : float, default 0
        The constant value to be compared to.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_equalConstant
    """
    from ._pyclesperanto import _EqualConstantKernel_Call as op

    op(device, src=input_image, dst=output_image, constant=constant)
    return output_image


@plugin_function
def equal(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the
    result of comparing each pixel value in two given input images.

    <pre>f(x, y) = x == y</pre>

    Parameters
    ----------
    input_image1 : Image
        The first input image to be processed.
    input_image2 : Image
        The second input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_equal
    """
    from ._pyclesperanto import _EqualKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def erode_sphere(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
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
        The input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_erodeSphere
    """
    from ._pyclesperanto import _ErodeSphereKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def maximum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the maximum intensity projection of an image along Z.

    Parameters
    ----------
    input_image : Image
        input image to be processed, must be 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 dimensions
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image of n-1 dimensions

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumZProjection
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[2]), dtype=input_image.dtype)
    from ._pyclesperanto import _MaximumZProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def maximum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the maximum intensity projection of an image along Y.

    Parameters
    ----------
    input_image : Image
        input image to be processed, must be 2d or 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image of n-1 dimensions

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumYProjection
    """
    shape = input_image.shape
    output_image = create((shape[0], shape[2]), dtype=input_image.dtype)
    from ._pyclesperanto import _MaximumYProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def maximum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the maximum intensity projection of an image along X.

    Parameters
    ----------
    input_image : Image
        Input image to be processed
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image of n-1 dimensions

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_maximumXProjection
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[0]), dtype=input_image.dtype)
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
        Image to be subtracted from the scalar
    output_image : Image, optional
        The output image where results are written into.
    scalar : Number, default 0

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_subtractImageFromScalar
    """
    from ._pyclesperanto import _SubtractImageFromScalarKernel_Call as op

    op(device, src=input_image, dst=output_image, scalar=float(scalar))
    return output_image


@plugin_function
def sobel(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Convolve the image with the Sobel kernel.

    Author( device: Device = Nones) -> Image: Ruth Whelan-Jeans, Robert Haase

    Parameters
    ----------
    input_image : Image
        The input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sobel
    """
    from ._pyclesperanto import _SobelKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def minimum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the minimum intensity projection of an image along Z.

    Parameters
    ----------
    input_image : Image
        Input image to be processed, must be 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image 2D

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumZProjection
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[2]), dtype=input_image.dtype)
    from ._pyclesperanto import _MinimumZProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def minimum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the minimum intensity projection of an image along Y.

    Parameters
    ----------
    input_image : Image
        Input image to be processed, must be 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image 2D

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumYProjection
    """
    shape = input_image.shape
    output_image = create((shape[0], shape[2]), dtype=input_image.dtype)
    from ._pyclesperanto import _MinimumYProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def minimum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the minimum intensity projection of an image along X.

    Parameters
    ----------
    input_image : Image
        Input image to be processed, must be 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image 2D

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumXProjection
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[0]), dtype=input_image.dtype)
    from ._pyclesperanto import _MinimumXProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def multiply_images(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Multiplies two images X and Y pixel wise.

    <pre>f(x, y) = x * y</pre>

    Parameters
    ----------
    input_image1 : Image
        First input image to be processed.
    input_image2 : Image
        Second input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyImages
    """
    from ._pyclesperanto import _MultiplyImagesKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def multiply_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None,
) -> Image:
    """Multiplies one image X with a scalar s pixel wise.

    <pre>f(x, s) = x * s</pre>

    Parameters
    ----------
    input_image : Image
        Input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    scalar : Number, default 0
        The scalar to multiply with.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndScalar
    """
    from ._pyclesperanto import _MultiplyImageAndScalarKernel_Call as op

    op(device, src=input_image, dst=output_image, scalar=float(scalar))
    return output_image


@plugin_function
def not_equal_constant(
    input_image: Image,
    output_image: Image = None,
    constant: float = 0,
    device: Device = None,
) -> Image:
    """Computes a binary image with pixel values 0 if the corresponding pixel in X is not equal to a given constant c and 1 otherwise.

    <pre>f(x, c) = (x != c ? 1 : 0)</pre>

    Parameters
    ----------
    input_image : Image
        Input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    constant : Number, default 0
        The constant to compare to.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_notEqualConstant
    """
    from ._pyclesperanto import _NotEqualConstantKernel_Call as op

    op(device, src=input_image, dst=output_image, constant=float(constant))
    return output_image


@plugin_function
def not_equal(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Computes a binary image with pixel values 0 if the corresponding pixel in X and Y are equal and 1 otherwise.

    <pre>f(x, y) = (x != y ? 1 : 0)</pre>

    Parameters
    ----------
    input_image1 : Image
        First input image to be processed.
    input_image2 : Image
        Second input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_notEqual
    """
    from ._pyclesperanto import _NotEqualKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def power(
    input_image: Image,
    output_image: Image = None,
    exponent: float = 1,
    device: Device = None,
) -> Image:
    """Computes all pixels value x to the power of a given exponent a.

    <pre>f(x, a) = x ^ a</pre>

    Parameters
    ----------
    input_image : Image
        Image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    exponent : Number, default 1
        The exponent to apply.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_power
    """
    from ._pyclesperanto import _PowerKernel_Call as op

    op(device, src=input_image, dst=output_image, exponent=float(exponent))
    return output_image


@plugin_function
def power_images(
    input_image1: Image,
    input_image2: Image,
    output_image: Image,
    device: Device = None,
) -> Image:
    """Computes all pairs of pixels x and y value x to the power of y.

    <pre>f(x, y) = x ^ y</pre>

    Parameters
    ----------
    input_image1 : Image
        First input image to be processed.
    input_image2 : Image
        Second input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_powerImages
    """
    from ._pyclesperanto import _PowerImagesKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def smaller_constant(
    input_image: Image,
    output_image: Image = None,
    constant: float = 0,
    device: Device = None,
) -> Image:
    """Determines if all pixels x smaller than a constant c.

    <pre>f(x, c) = x < c ? 1 : 0</pre>

    Parameters
    ----------
    input_image : Image
        Input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    constant : Number, default 0
        The constant to compare to.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_smallerConstant
    """
    from ._pyclesperanto import _SmallerConstantKernel_Call as op

    op(device, src=input_image, dst=output_image, constant=float(constant))
    return output_image


@plugin_function
def smaller(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines if all pairs of pixels x, y smaller.

    <pre>f(x, y) = x < y ? 1 : 0</pre>

    Parameters
    ----------
    input_image1 : Image
        First input image to be processed.
    input_image2 : Image
        Second input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_smaller
    """
    from ._pyclesperanto import _SmallerKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def smaller_or_equal_constant(
    input_image: Image,
    output_image: Image = None,
    constant: float = 0,
    device: Device = None,
) -> Image:
    """Determines if all pixels x smaller or equal to a constant c.

    <pre>f(x, c) = x <= c ? 1 : 0</pre>

    Parameters
    ----------
    input_image : Image
        Input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    constant : Number, optional
        The constant to compare to.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_smallerOrEqualConstant
    """
    from ._pyclesperanto import _SmallerOrEqualConstantKernel_Call as op

    op(device, src=input_image, dst=output_image, constant=float(constant))
    return output_image


@plugin_function
def smaller_or_equal(
    input_image1: Image,
    input_image2: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines if all pairs of pixels x, y smaller or equal.

    <pre>f(x, y) = x <= y ? 1 : 0</pre>

    Parameters
    ----------
    input_image1 : Image
        First input image to be processed.
    input_image2 : Image
        Second input image to be processed.
    output_image : Image, optional
        The output image where results are written into.
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_smallerOrEqual
    """
    from ._pyclesperanto import _SmallerOrEqualKernel_Call as op

    op(device, src1=input_image1, src2=input_image2, dst=output_image)
    return output_image


@plugin_function
def sum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image : Image
        Input image to be processed, must be 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image of n-1 d

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sumZProjection
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[2]), dtype=input_image.dtype)
    from ._pyclesperanto import _SumZProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def sum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the sum intensity projection of an image along Y.

    Parameters
    ----------
    input_image : Image
        Input image to be processed, must be 2d or 3d
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image of n-1 d

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sumYProjection
    """
    shape = input_image.shape
    output_image = create((shape[0], shape[2]), dtype=input_image.dtype)
    from ._pyclesperanto import _SumYProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def sum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Determines the sum intensity projection of an image along X.

    Parameters
    ----------
    input_image : Image
        Input image to be processed
    output_image : Image, optional
        The output image where results are written into, will be of n-1 d
    device : Device, optional
        The device where the operation should take place on.

    Returns
    -------
    output_image : Image of n-1 d

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_sumXProjection
    """
    shape = input_image.shape
    output_image = create((shape[1], shape[0]), dtype=input_image.dtype)
    from ._pyclesperanto import _SumXProjectionKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image
