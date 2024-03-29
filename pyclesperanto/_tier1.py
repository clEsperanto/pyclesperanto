#
# This code is auto-generated from 'tier1.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function(category=['filter', 'in assistant', 'bia-bob-suggestion'])
def absolute(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the absolute value of every individual pixel x in a given image.
    <pre>f(x) = |x| </pre>

    Parameters
    ----------
    input_image: Image
        The input image to be processed.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_absolute
    """

    from ._pyclesperanto import _absolute as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['combine', 'in assistant'])
def add_images_weighted(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    factor0: float = 1,
    factor1: float = 1,
    device: Device = None
) -> Image:
    """Calculates the sum of pairs of pixels x and y from images X and Y weighted with
    factors a and b. <pre>f(x, y, a, b) = x * a + y * b</pre>

    Parameters
    ----------
    input_image0: Image
        The first input image to added.
    input_image1: Image
        The second image to be added.
    output_image: Image = None
        The output image where results are written into.
    factor0: float = 1
        Multiplication factor of each pixel of src0 before adding it.
    factor1: float = 1
        Multiplication factor of each pixel of src1 before adding it.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_addImagesWeighted
    """

    from ._pyclesperanto import _add_images_weighted as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        factor0=float(factor0),
        factor1=float(factor1)
    )



@plugin_function(category=['filter', 'in assistant'])
def add_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 1,
    device: Device = None
) -> Image:
    """Adds a scalar value s to all pixels x of a given image X. <pre>f(x, s) = x +
    s</pre>

    Parameters
    ----------
    input_image: Image
        The input image where scalare should be added.
    output_image: Image = None
        The output image where results are written into.
    scalar: float = 1
        The constant number which will be added to all pixels.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_addImageAndScalar
    """

    from ._pyclesperanto import _add_image_and_scalar as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'binary processing', 'in assistant', 'combine labels', 'label processing', 'bia-bob-suggestion'])
def binary_and(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two images X and
    Y by connecting pairs of pixels x and y with the binary AND operator &. All
    pixel values except 0 in the input images are interpreted as 1. <pre>f(x, y) = x
    & y</pre>

    Parameters
    ----------
    input_image0: Image
        The first binary input image to be processed.
    input_image1: Image
        The second binary input image to be processed.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryAnd
    """

    from ._pyclesperanto import _binary_and as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binary processing', 'label processing', 'in assistant', 'bia-bob-suggestion'])
def binary_edge_detection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines pixels/voxels which are on the surface of binary objects and sets
    only them to 1 in the destination image. All other pixels are set to 0.

    Parameters
    ----------
    input_image: Image
        The binary input image where edges will be searched.
    output_image: Image = None
        The output image where edge pixels will be 1.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryEdgeDetection
    """

    from ._pyclesperanto import _binary_edge_detection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['binary processing', 'filter', 'label processing', 'in assistant', 'bia-bob-suggestion'])
def binary_not(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from an image X by
    negating its pixel values x using the binary NOT operator ! All pixel values
    except 0 in the input image are interpreted as 1. <pre>f(x) = !x</pre>

    Parameters
    ----------
    input_image: Image
        The binary input image to be inverted.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryNot
    """

    from ._pyclesperanto import _binary_not as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['combine', 'binary processing', 'in assistant', 'combine labels', 'label processing', 'bia-bob-suggestion'])
def binary_or(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two images X and
    Y by connecting pairs of pixels x and y with the binary OR operator |. All pixel
    values except 0 in the input images are interpreted as 1.<pre>f(x, y) = x |
    y</pre>

    Parameters
    ----------
    input_image0: Image
        The first binary input image to be processed.
    input_image1: Image
        The second binary input image to be processed.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryOr
    """

    from ._pyclesperanto import _binary_or as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['combine', 'binary processing', 'in assistant', 'combine labels', 'label processing', 'bia-bob-suggestion'])
def binary_subtract(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Subtracts one binary image from another.

    Parameters
    ----------
    input_image0: Image
        The first binary input image to be processed.
    input_image1: Image
        The second binary input image to be subtracted from the first.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binarySubtract
    """

    from ._pyclesperanto import _binary_subtract as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['combine', 'binary processing', 'in assistant', 'combine labels', 'label processing', 'bia-bob-suggestion'])
def binary_xor(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two images X and
    Y by connecting pairs of pixels x and y with the binary operators AND &, OR |
    and NOT ! implementing the XOR operator. All pixel values except 0 in the input
    images are interpreted as 1. <pre>f(x, y) = (x & !y) | (!x & y)</pre>

    Parameters
    ----------
    input_image0: Image
        The first binary input image to be processed.
    input_image1: Image
        The second binary input image to be processed.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryXOr
    """

    from ._pyclesperanto import _binary_xor as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function
def block_enumerate(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    blocksize: int = 256,
    device: Device = None
) -> Image:
    """Enumerates pixels with value 1 in a onedimensional image For example handing
    over the image [0, 1, 1, 0, 1, 0, 1, 1] would be processed to an image [0, 1, 2,
    0, 3, 0, 4, 5] This functionality is important in connected component neccessary
    (see also sum_reduction_x). In the above example, with blocksize 4, that would
    be the sum array: [2, 3] labeling. Processing is accelerated by paralellization
    in blocks. Therefore, handing over precomputed block sums is Note that the block
    size when calling this function and sum_reduction must be identical

    Parameters
    ----------
    input_image0: Image
        input binary vector image
    input_image1: Image
        precomputed sums of blocks
    output_image: Image = None
        output enumerated vector image
    blocksize: int = 256
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _block_enumerate as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        blocksize=int(blocksize)
    )



@plugin_function(category=['filter', 'combine', 'in assistant'])
def convolve(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Convolve the image with a given kernel image. It is recommended that the kernel
    image has an odd size in X, Y and Z.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_convolve
    """

    from ._pyclesperanto import _convolve as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function
def copy(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Copies an image. <pre>f(x) = x</pre>

    Parameters
    ----------
    input_image: Image
        Input image to copy.
    output_image: Image = None
        Output copy image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copy
    """

    from ._pyclesperanto import _copy as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def copy_slice(
    input_image: Image,
    output_image: Image = None,
    slice: int = 0,
    device: Device = None
) -> Image:
    """This method has two purposes: It copies a 2D image to a given slice z position
    in a 3D image stack or It copies a given slice at position z in an image stack
    to a 2D image. The first case is only available via ImageJ macro. If you are
    using it, it is recommended that the target 3D image already preexists in GPU
    memory before calling this method. Otherwise, CLIJ create the image stack with z
    planes.

    Parameters
    ----------
    input_image: Image
        Input image to copy from.
    output_image: Image = None
        Output copy image slice.
    slice: int = 0
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copySlice
    """

    from ._pyclesperanto import _copy_slice as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        slice=int(slice)
    )



@plugin_function
def copy_horizontal_slice(
    input_image: Image,
    output_image: Image = None,
    slice: int = 0,
    device: Device = None
) -> Image:
    """This method has two purposes: It copies a 2D image to a given slice y position
    in a 3D image stack or It copies a given slice at position y in an image stack
    to a 2D image.

    Parameters
    ----------
    input_image: Image
        Input image to copy from.
    output_image: Image = None
        Output copy image slice.
    slice: int = 0
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copySlice
    """

    from ._pyclesperanto import _copy_horizontal_slice as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        slice=int(slice)
    )



@plugin_function
def copy_vertical_slice(
    input_image: Image,
    output_image: Image = None,
    slice: int = 0,
    device: Device = None
) -> Image:
    """This method has two purposes: It copies a 2D image to a given slice x position
    in a 3D image stack or It copies a given slice at position x in an image stack
    to a 2D image.

    Parameters
    ----------
    input_image: Image
        Input image to copy from.
    output_image: Image = None
        Output copy image slice.
    slice: int = 0
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copySlice
    """

    from ._pyclesperanto import _copy_vertical_slice as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        slice=int(slice)
    )



@plugin_function
def crop(
    input_image: Image,
    output_image: Image = None,
    start_x: int = 0,
    start_y: int = 0,
    start_z: int = 0,
    width: int = 1,
    height: int = 1,
    depth: int = 1,
    device: Device = None
) -> Image:
    """Crops a given substack out of a given image stack. Note: If the destination
    image preexists already, it will be overwritten and keep it's dimensions.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    start_x: int = 0
        Starting index coordicante x.
    start_y: int = 0
        Starting index coordicante y.
    start_z: int = 0
        Starting index coordicante z.
    width: int = 1
        Width size of the region to crop.
    height: int = 1
        Height size of the region to crop.
    depth: int = 1
        Depth size of the region to crop.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_crop3D
    """

    from ._pyclesperanto import _crop as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        start_x=int(start_x),
        start_y=int(start_y),
        start_z=int(start_z),
        width=int(width),
        height=int(height),
        depth=int(depth)
    )



@plugin_function(category=['filter', 'in assistant'])
def cubic_root(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the cubic root of each pixel.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _cubic_root as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['binarize', 'label processing', 'in assistant', 'bia-bob-suggestion'])
def detect_label_edges(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes a labelmap and returns an image where all pixels on label edges are set to
    1 and all other pixels to 0.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectLabelEdges
    """

    from ._pyclesperanto import _detect_label_edges as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['binary processing'])
def dilate_box(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary dilation
    of a given input image. The dilation takes the Mooreneighborhood (8 pixels in 2D
    and 26 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1. This method is comparable to the
    'Dilate' menu in ImageJ in case it is applied to a 2D image. The only difference
    is that the output image contains values 0 and 1 instead of 0 and 255.

    Parameters
    ----------
    input_image: Image
        Input image to process. Input image to process.
    output_image: Image = None
        Output result image. Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_dilateBox
    """

    from ._pyclesperanto import _dilate_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['binary processing', 'bia-bob-suggestion'])
def dilate_sphere(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary dilation
    of a given input image. The dilation takes the vonNeumannneighborhood (4 pixels
    in 2D and 6 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1.

    Parameters
    ----------
    input_image: Image
        Input image to process. Input image to process.
    output_image: Image = None
        Output result image. Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_dilateSphere
    """

    from ._pyclesperanto import _dilate_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['combine', 'in assistant'])
def divide_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Divides two images X and Y by each other pixel wise. <pre>f(x, y) = x / y</pre>

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_divideImages
    """

    from ._pyclesperanto import _divide_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def divide_scalar_by_image(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Divides a scalar by an image pixel by pixel. <pre>f(x, s) = s / x</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _divide_scalar_by_image as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'binarize', 'in assistant'])
def equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines if two images A and B equal pixel wise. <pre>f(a, b) = 1 if a == b; 0
    otherwise.</pre>

    Parameters
    ----------
    input_image0: Image
        The first image to be compared with.
    input_image1: Image
        The second image to be compared with the first.
    output_image: Image = None
        The resulting binary image where pixels will be 1 only if source1
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_equal
    """

    from ._pyclesperanto import _equal as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Determines if an image A and a constant b are equal. <pre>f(a, b) = 1 if a == b;
    0 otherwise.</pre>

    Parameters
    ----------
    input_image: Image
        The image where every pixel is compared to the constant.
    output_image: Image = None
        The resulting binary image where pixels will be 1 only if source1
    scalar: float = 0
        The constant where every pixel is compared to.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_equalConstant
    """

    from ._pyclesperanto import _equal_constant as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['binary processing'])
def erode_box(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion
    of a given input image. The erosion takes the Mooreneighborhood (8 pixels in 2D
    and 26 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1. This method is comparable to the
    'Erode' menu in ImageJ in case it is applied to a 2D image. The only difference
    is that the output image contains values 0 and 1 instead of 0 and 255.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeBox
    """

    from ._pyclesperanto import _erode_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['binary processing', 'bia-bob-suggestion'])
def erode_sphere(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion
    of a given input image. The erosion takes the vonNeumannneighborhood (4 pixels
    in 2D and 6 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeSphere
    """

    from ._pyclesperanto import _erode_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def exponential(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes base exponential of all pixels values. f(x) = exp(x) Author(s): Peter
    Haub, Robert Haase

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_exponential
    """

    from ._pyclesperanto import _exponential as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def flip(
    input_image: Image,
    output_image: Image = None,
    flip_x: bool = True,
    flip_y: bool = True,
    flip_z: bool = True,
    device: Device = None
) -> Image:
    """Flips an image in X, Y and/or Z direction depending on boolean flags.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    flip_x: bool = True
        Flip along the x axis if true.
    flip_y: bool = True
        Flip along the y axis if true.
    flip_z: bool = True
        Flip along the z axis if true.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_flip3D
    """

    from ._pyclesperanto import _flip as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        flip_x=bool(flip_x),
        flip_y=bool(flip_y),
        flip_z=bool(flip_z)
    )



@plugin_function(category=['filter', 'denoise', 'in assistant', 'bia-bob-suggestion'])
def gaussian_blur(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 0,
    sigma_y: float = 0,
    sigma_z: float = 0,
    device: Device = None
) -> Image:
    """Computes the Gaussian blurred image of an image given sigma values in X, Y and
    Z. Thus, the filter kernel can have nonisotropic shape. The implementation is
    done separable. In case a sigma equals zero, the direction is not blurred.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    sigma_x: float = 0
        Sigma value along the x axis.
    sigma_y: float = 0
        Sigma value along the y axis.
    sigma_z: float = 0
        Sigma value along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gaussianBlur3D
    """

    from ._pyclesperanto import _gaussian_blur as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        sigma_x=float(sigma_x),
        sigma_y=float(sigma_y),
        sigma_z=float(sigma_z)
    )



@plugin_function(category=['bia-bob-suggestion'])
def generate_distance_matrix(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the distance between all point coordinates given in two point lists.
    Takes two images containing pointlists (dimensionality n * d, n: number of
    points and d: dimensionality) and builds up a matrix containing the distances
    between these points. Convention: Given two point lists with dimensionality n *
    d and m * d, the distance matrix will be of size(n + 1) * (m + 1). The first row
    and column contain zeros. They represent the distance of the (see
    generateTouchMatrix). Thus, one can threshold a distance matrix to generate a
    touch matrix out of it for drawing objects to a theoretical background object.
    In that way, distance matrices are of the same size as touch matrices meshes.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_generateDistanceMatrix
    """

    from ._pyclesperanto import _generate_distance_matrix as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant'])
def gradient_x(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the gradient of gray values along X. Assuming a, b and c are three
    adjacent pixels in X direction. In the target image will be saved as: <pre>b' =
    c a;</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gradientX
    """

    from ._pyclesperanto import _gradient_x as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant'])
def gradient_y(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the gradient of gray values along Y. Assuming a, b and c are three
    adjacent pixels in Y direction. In the target image will be saved as: <pre>b' =
    c a;</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gradientY
    """

    from ._pyclesperanto import _gradient_y as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant'])
def gradient_z(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the gradient of gray values along Z. Assuming a, b and c are three
    adjacent pixels in Z direction. In the target image will be saved as: <pre>b' =
    c a;</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gradientZ
    """

    from ._pyclesperanto import _gradient_z as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['combine', 'binarize', 'in assistant'])
def greater(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines if two images A and B greater pixel wise. f(a, b) = 1 if a > b; 0
    otherwise.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greater
    """

    from ._pyclesperanto import _greater as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def greater_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Determines if two images A and B greater pixel wise. f(a, b) = 1 if a > b; 0
    otherwise.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greaterConstant
    """

    from ._pyclesperanto import _greater_constant as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'binarize', 'in assistant'])
def greater_or_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines if two images A and B greater or equal pixel wise. f(a, b) = 1 if a
    >= b; 0 otherwise.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greaterOrEqual
    """

    from ._pyclesperanto import _greater_or_equal as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def greater_or_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Determines if two images A and B greater or equal pixel wise. f(a, b) = 1 if a
    >= b; 0 otherwise.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
        Scalar value used in the comparison.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greaterOrEqualConstant
    """

    from ._pyclesperanto import _greater_or_equal_constant as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function
def hessian_eigenvalues(
    input_image: Image,
    small_eigenvalue: Image = None,
    middle_eigenvalue: Image = None,
    large_eigenvalue: Image = None,
    device: Device = None
) -> list:
    """Computes the eigenvalues of the hessian matrix of a 2d or 3d image. Hessian
    matrix or 2D images: [Ixx, Ixy] [Ixy, Iyy] Hessian matrix for 3D images: [Ixx,
    Ixy, Ixz] [Ixy, Iyy, Iyz] [Ixz, Iyz, Izz] Ixx denotes the second derivative in
    x. Ixx and Iyy are calculated by convolving the image with the 1d kernel [1 2
    1]. Ixy is calculated by a convolution with the 2d kernel: [ 0.25 0 0.25] [ 0 0
    0] [0.25 0 0.25] Note: This is the only clesperanto function that returns
    multiple images. This API might be subject to change in the future. Consider
    using small_hessian_eigenvalue() and/or large_hessian_eigenvalue() instead which
    return only one image.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    small_eigenvalue: Image = None
        Output result image.
    middle_eigenvalue: Image = None
        Output result image, null if input is 2D.
    large_eigenvalue: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    list
    
    """

    from ._pyclesperanto import _hessian_eigenvalues as op

    return op(
        device=device,
        src=input_image,
        small_eigenvalue=small_eigenvalue,
        middle_eigenvalue=middle_eigenvalue,
        large_eigenvalue=large_eigenvalue
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant', 'bia-bob-suggestion'])
def laplace_box(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Applies the Laplace operator (Box neighborhood) to an image.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_laplaceBox
    """

    from ._pyclesperanto import _laplace_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'edge detection', 'bia-bob-suggestion'])
def laplace_diamond(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Applies the Laplace operator (Diamond neighborhood) to an image.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_laplaceDiamond
    """

    from ._pyclesperanto import _laplace_diamond as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'combine', 'in assistant'])
def local_cross_correlation(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Compute the cross correlation of an image to a given kernel.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _local_cross_correlation as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def logarithm(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes base e logarithm of all pixels values. f(x) = log(x) Author(s): Peter
    Haub, Robert Haase

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_logarithm
    """

    from ._pyclesperanto import _logarithm as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['bia-bob-suggestion'])
def mask(
    input_image: Image,
    mask: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes a masked image by applying a binary mask to an image. All pixel values
    x of image X will be copied to the destination image in case pixel value m at
    the same position in the mask image is not equal to zero. <pre>f(x,m) = (x if (m
    != 0); (0 otherwise))</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    mask: Image
        Mask image to apply.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mask
    """

    from ._pyclesperanto import _mask as op

    return op(
        device=device,
        src=input_image,
        mask=mask,
        dst=output_image
    )



@plugin_function(category=['bia-bob-suggestion'])
def mask_label(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    label: float = 1,
    device: Device = None
) -> Image:
    """Computes a masked image by applying a label mask to an image. All pixel values x
    of image X will be copied to the destination image in case pixel value m at the
    same position in the label_map image has the right index value i. f(x,m,i) = (x
    if (m == i); (0 otherwise))

    Parameters
    ----------
    input_image0: Image
        Input Intensity image.
    input_image1: Image
        Input Label image.
    output_image: Image = None
        Output result image.
    label: float = 1
        Label value to use.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maskLabel
    """

    from ._pyclesperanto import _mask_label as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        label=float(label)
    )



@plugin_function(category=['filter', 'in assistant', 'bia-bob-suggestion'])
def maximum_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Computes the maximum of a constant scalar s and each pixel value x in a given
    image X. <pre>f(x, s) = max(x, s)</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
        Scalar value used in the comparison.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumImageAndScalar
    """

    from ._pyclesperanto import _maximum_image_and_scalar as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'in assistant', 'bia-bob-suggestion'])
def maximum_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the maximum of a pair of pixel values x, y from two given images X and
    Y. <pre>f(x, y) = max(x, y)</pre>

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumImages
    """

    from ._pyclesperanto import _maximum_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def maximum_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local maximum of a pixels cube neighborhood. The cubes size is
    specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximum3DBox
    """

    from ._pyclesperanto import _maximum_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['projection'])
def maximum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the maximum intensity projection of an image along X.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumXProjection
    """

    from ._pyclesperanto import _maximum_x_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection'])
def maximum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the maximum intensity projection of an image along X.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumYProjection
    """

    from ._pyclesperanto import _maximum_y_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant', 'bia-bob-suggestion'])
def maximum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the maximum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumZProjection
    """

    from ._pyclesperanto import _maximum_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'denoise', 'in assistant'])
def mean_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local mean average of a pixels boxshaped neighborhood. The cubes
    size is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mean3DBox
    """

    from ._pyclesperanto import _mean_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'denoise', 'in assistant', 'bia-bob-suggestion'])
def mean_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local mean average of a pixels spherical neighborhood. The spheres
    size is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mean3DSphere
    """

    from ._pyclesperanto import _mean_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['projection'])
def mean_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the mean average intensity projection of an image along X.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanXProjection
    """

    from ._pyclesperanto import _mean_x_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection'])
def mean_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the mean average intensity projection of an image along Y.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanYProjection
    """

    from ._pyclesperanto import _mean_y_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant', 'bia-bob-suggestion'])
def mean_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the mean average intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanZProjection
    """

    from ._pyclesperanto import _mean_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'denoise', 'in assistant'])
def median_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local median of a pixels box shaped neighborhood. The box is
    specified by its halfwidth and halfheight (radius). For technical reasons, the
    area of the box must have less than 1000 pixels.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_median3DBox
    """

    from ._pyclesperanto import _median_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'denoise', 'in assistant'])
def median_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local median of a pixels sphere shaped neighborhood. The sphere is
    specified by its halfwidth and halfheight (radius). For technical reasons, the
    area of the box must have less than 1000 pixels.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_median3DSphere
    """

    from ._pyclesperanto import _median_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'in assistant'])
def minimum_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None
) -> Image:
    """Computes the local minimum of a pixels cube neighborhood. The cubes size is
    specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 0
        Radius size along x axis.
    radius_y: int = 0
        Radius size along y axis.
    radius_z: int = 0
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DBox
    """

    from ._pyclesperanto import _minimum_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'in assistant'])
def minimum_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Computes the minimum of a constant scalar s and each pixel value x in a given
    image X. <pre>f(x, s) = min(x, s)</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
        Scalar value used in the comparison.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumImageAndScalar
    """

    from ._pyclesperanto import _minimum_image_and_scalar as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'in assistant'])
def minimum_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the minimum of a pair of pixel values x, y from two given images X and
    Y. <pre>f(x, y) = min(x, y)</pre>

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumImages
    """

    from ._pyclesperanto import _minimum_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['projection'])
def minimum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the minimum intensity projection of an image along Y.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumXProjection
    """

    from ._pyclesperanto import _minimum_x_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection'])
def minimum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the minimum intensity projection of an image along Y.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumYProjection
    """

    from ._pyclesperanto import _minimum_y_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant', 'bia-bob-suggestion'])
def minimum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the minimum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumZProjection
    """

    from ._pyclesperanto import _minimum_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['label processing', 'in assistant'])
def mode_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local mode of a pixels box shaped neighborhood. This can be used to
    postprocess and locally correct semantic segmentation results. The box is
    specified by its halfwidth and halfheight (radius). For technical reasons, the
    intensities must lie within a range from 0 to 255. In case multiple values have
    maximum frequency, the smallest one is returned.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _mode_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def mode_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local mode of a pixels sphere shaped neighborhood. This can be used
    to postprocess and locally correct semantic segmentation results. The sphere is
    specified by its halfwidth and halfheight (radius). For technical reasons, the
    intensities must lie within a range from 0 to 255. In case multiple values have
    maximum frequency, the smallest one is returned.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _mode_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['combine', 'bia-bob-suggestion'])
def modulo_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the remainder of a division of pairwise pixel values in two images

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _modulo_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function
def multiply_image_and_position(
    input_image: Image,
    output_image: Image = None,
    dimension: int = 0,
    device: Device = None
) -> Image:
    """Multiplies all pixel intensities with the x, y or z coordinate, depending on
    specified dimension.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    dimension: int = 0
        Dimension (0,1,2) to use in the operation.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndCoordinate
    """

    from ._pyclesperanto import _multiply_image_and_position as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        dimension=int(dimension)
    )



@plugin_function(category=['filter', 'in assistant'])
def multiply_image_and_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Multiplies all pixels value x in a given image X with a constant scalar s.
    <pre>f(x, s) = x * s</pre>

    Parameters
    ----------
    input_image: Image
        The input image to be multiplied with a constant.
    output_image: Image = None
        The output image where results are written into.
    scalar: float = 0
        The number with which every pixel will be multiplied with.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndScalar
    """

    from ._pyclesperanto import _multiply_image_and_scalar as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'in assistant'])
def multiply_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Multiplies all pairs of pixel values x and y from two image X and Y. <pre>f(x,
    y) = x * y</pre>

    Parameters
    ----------
    input_image0: Image
        The first input image to be multiplied.
    input_image1: Image
        The second image to be multiplied.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyImages
    """

    from ._pyclesperanto import _multiply_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function
def nan_to_num(
    input_image: Image,
    output_image: Image = None,
    nan: float = 0,
    posinf: float = np.nan_to_num(float('inf')),
    neginf: float = np.nan_to_num(float('-inf')),
    device: Device = None
) -> Image:
    """Copies all pixels instead those which are not a number (NaN), or
    positive/negative infinity which are replaced by a defined new value, default 0.
    This function aims to work similarly as its counterpart in numpy [1]. Default
    values for posinf and neginf may differ from numpy and even differ depending on
    compute hardware. It is recommended to specify those values.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        The output image where results are written into.
    nan: float = 0
        Value to replace
    posinf: float = np.nan_to_num(float('inf'))
        Value to replace +inf with.
    neginf: float = np.nan_to_num(float('-inf'))
        Value to replace -inf with.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html
    """

    from ._pyclesperanto import _nan_to_num as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        nan=float(nan),
        posinf=float(posinf),
        neginf=float(neginf)
    )



@plugin_function
def nonzero_maximum_box(
    input_image: Image,
    output_image0: Image,
    output_image1: Image = None,
    device: Device = None
) -> Image:
    """Apply a maximum filter (box shape) to the input image. The radius is fixed to 1
    and pixels with value 0 are ignored. Note: Pixels with 0 value in the input
    image will not be overwritten in the output image. Thus, the result image should
    be initialized by copying the original image in advance.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image0: Image
        Output flag (0 or 1).
    output_image1: Image = None
        Output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMaximumBox
    """

    from ._pyclesperanto import _nonzero_maximum_box as op

    return op(
        device=device,
        src=input_image,
        dst0=output_image0,
        dst1=output_image1
    )



@plugin_function
def nonzero_maximum_diamond(
    input_image: Image,
    output_image0: Image,
    output_image1: Image = None,
    device: Device = None
) -> Image:
    """Apply a maximum filter (diamond shape) to the input image. The radius is fixed
    to 1 and pixels with value 0 are ignored. Note: Pixels with 0 value in the input
    image will not be overwritten in the output image. Thus, the result image should
    be initialized by copying the original image in advance.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image0: Image
        Output flag (0 or 1).
    output_image1: Image = None
        Output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMaximumDiamond
    """

    from ._pyclesperanto import _nonzero_maximum_diamond as op

    return op(
        device=device,
        src=input_image,
        dst0=output_image0,
        dst1=output_image1
    )



@plugin_function
def nonzero_minimum_box(
    input_image: Image,
    output_image0: Image,
    output_image1: Image = None,
    device: Device = None
) -> Image:
    """Apply a minimum filter (box shape) to the input image. The radius is fixed to 1
    and pixels with value 0 are ignored. Note: Pixels with 0 value in the input
    image will not be overwritten in the output image. Thus, the result image should
    be initialized by copying the original image in advance.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image0: Image
        Output flag (0 or 1).
    output_image1: Image = None
        Output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumBox
    """

    from ._pyclesperanto import _nonzero_minimum_box as op

    return op(
        device=device,
        src=input_image,
        dst0=output_image0,
        dst1=output_image1
    )



@plugin_function
def nonzero_minimum_diamond(
    input_image: Image,
    output_image0: Image,
    output_image1: Image = None,
    device: Device = None
) -> Image:
    """Apply a minimum filter (diamond shape) to the input image. The radius is fixed
    to 1 and pixels with value 0 are ignored.Note: Pixels with 0 value in the input
    image will not be overwritten in the output image. Thus, the result image should
    be initialized by copying the original image in advance.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image0: Image
        Output flag (0 or 1).
    output_image1: Image = None
        Output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumDiamond
    """

    from ._pyclesperanto import _nonzero_minimum_diamond as op

    return op(
        device=device,
        src=input_image,
        dst0=output_image0,
        dst1=output_image1
    )



@plugin_function(category=['combine', 'binarize', 'in assistant'])
def not_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines if two images A and B equal pixel wise. f(a, b) = 1 if a != b; 0
    otherwise.

    Parameters
    ----------
    input_image0: Image
        The first image to be compared with.
    input_image1: Image
        The second image to be compared with the first.
    output_image: Image = None
        The resulting binary image where pixels will be 1 only if source1
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_notEqual
    """

    from ._pyclesperanto import _not_equal as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def not_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Determines if two images A and B equal pixel wise. f(a, b) = 1 if a != b; 0
    otherwise.

    Parameters
    ----------
    input_image: Image
        The image where every pixel is compared to the constant.
    output_image: Image = None
        The resulting binary image where pixels will be 1 only if source1
    scalar: float = 0
        The constant where every pixel is compared to.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_notEqualConstant
    """

    from ._pyclesperanto import _not_equal_constant as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'in assistant'])
def paste(
    input_image: Image,
    output_image: Image = None,
    index_x: int = 0,
    index_y: int = 0,
    index_z: int = 0,
    device: Device = None
) -> Image:
    """Pastes an image into another image at a given position.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    index_x: int = 0
        Origin pixel coodinate in x to paste.
    index_y: int = 0
        Origin pixel coodinate in y to paste.
    index_z: int = 0
        Origin pixel coodinate in z to paste.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_paste3D
    """

    from ._pyclesperanto import _paste as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        index_x=int(index_x),
        index_y=int(index_y),
        index_z=int(index_z)
    )



@plugin_function
def onlyzero_overwrite_maximum_box(
    input_image: Image,
    output_image0: Image,
    output_image1: Image = None,
    device: Device = None
) -> Image:
    """Apply a local maximum filter to an image which only overwrites pixels with value
    0.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image0: Image
        Output flag value, 0 or 1.
    output_image1: Image = None
        Output image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumBox
    """

    from ._pyclesperanto import _onlyzero_overwrite_maximum_box as op

    return op(
        device=device,
        src=input_image,
        dst0=output_image0,
        dst1=output_image1
    )



@plugin_function
def onlyzero_overwrite_maximum_diamond(
    input_image: Image,
    output_image0: Image,
    output_image1: Image = None,
    device: Device = None
) -> Image:
    """Apply a local maximum filter to an image which only overwrites pixels with value
    0.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image0: Image
        Output flag value, 0 or 1.
    output_image1: Image = None
        Output image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumDiamond
    """

    from ._pyclesperanto import _onlyzero_overwrite_maximum_diamond as op

    return op(
        device=device,
        src=input_image,
        dst0=output_image0,
        dst1=output_image1
    )



@plugin_function(category=['filter', 'in assistant'])
def power(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 1,
    device: Device = None
) -> Image:
    """Computes all pixels value x to the power of a given exponent a. <pre>f(x, a) = x
    ^ a</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 1
        Power value.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_power
    """

    from ._pyclesperanto import _power as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'in assistant'])
def power_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Calculates x to the power of y pixel wise of two images X and Y.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_powerImages
    """

    from ._pyclesperanto import _power_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['transform', 'in assistant'])
def range(
    input_image: Image,
    output_image: Image = None,
    start_x: int = None,
    stop_x: int = None,
    step_x: int = None,
    start_y: int = None,
    stop_y: int = None,
    step_y: int = None,
    start_z: int = None,
    stop_z: int = None,
    step_z: int = None,
    device: Device = None
) -> Image:
    """Crops an image according to a defined range and step size.

    Parameters
    ----------
    input_image: Image
        First input image to process.
    output_image: Image = None
        Output result image.
    start_x: int = None
        Range starting value in x
    stop_x: int = None
        Range stop value in x
    step_x: int = None
        Range step value in x
    start_y: int = None
        Range starting value in y
    stop_y: int = None
        Range stop value in y
    step_y: int = None
        Range step value in y
    start_z: int = None
        Range starting value in z
    stop_z: int = None
        Range stop value in z
    step_z: int = None
        Range step value in z
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _range as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        start_x=int(start_x),
        stop_x=int(stop_x),
        step_x=int(step_x),
        start_y=int(start_y),
        stop_y=int(stop_y),
        step_y=int(step_y),
        start_z=int(start_z),
        stop_z=int(stop_z),
        step_z=int(step_z)
    )



@plugin_function(category=['bia-bob-suggestion'])
def read_values_from_positions(
    input_image: Image,
    list: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Go to positions in a given image specified by a pointlist and read intensities
    of those pixels. The intensities are stored in a new vector. The positions are
    passed as a (x,y,z) coordinate per column.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    list: Image
        List of coordinate, as a 2D matrix.
    output_image: Image = None
        Output vector image of intensities.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _read_values_from_positions as op

    return op(
        device=device,
        src=input_image,
        list=list,
        dst=output_image
    )



@plugin_function(category=['bia-bob-suggestion'])
def replace_values(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Replaces integer intensities specified in a vector image. The values are passed
    as a vector of values. The vector index represents the old intensity and the
    value at that position represents the new intensity.s

    Parameters
    ----------
    input_image0: Image
        Input image to process.
    input_image1: Image
        List of intensities to replace, as a vector of values.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_replaceIntensities
    """

    from ._pyclesperanto import _replace_values as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function
def replace_value(
    input_image: Image,
    output_image: Image = None,
    scalar0: float = 0,
    scalar1: float = 1,
    device: Device = None
) -> Image:
    """Replaces a specific intensity in an image with a given new value.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar0: float = 0
        Old value.
    scalar1: float = 1
        New value.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_replaceIntensity
    """

    from ._pyclesperanto import _replace_value as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar0=float(scalar0),
        scalar1=float(scalar1)
    )



@plugin_function(category=['filter', 'in assistant', 'bia-bob-suggestion'])
def maximum_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 1,
    radius_y: float = 1,
    radius_z: float = 0,
    device: Device = None
) -> Image:
    """Computes the local maximum of a pixels spherical neighborhood. The spheres size
    is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: float = 1
        Radius size along x axis.
    radius_y: float = 1
        Radius size along y axis.
    radius_z: float = 0
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximum3DSphere
    """

    from ._pyclesperanto import _maximum_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z)
    )



@plugin_function(category=['filter', 'in assistant', 'bia-bob-suggestion'])
def minimum_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 1,
    radius_y: float = 1,
    radius_z: float = 1,
    device: Device = None
) -> Image:
    """Computes the local minimum of a pixels spherical neighborhood. The spheres size
    is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: float = 1
        Radius size along x axis.
    radius_y: float = 1
        Radius size along y axis.
    radius_z: float = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DSphere
    """

    from ._pyclesperanto import _minimum_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z)
    )



@plugin_function
def multiply_matrix(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Multiplies two matrices with each other. Shape of matrix1 should be equal to
    shape of matrix2 transposed.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyMatrix
    """

    from ._pyclesperanto import _multiply_matrix as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def reciprocal(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes 1/x for every pixel value This function is supposed to work similarly
    to its counter part in numpy [1]

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html
    """

    from ._pyclesperanto import _reciprocal as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def set(
    input_image: Image,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values x of a given image X to a constant value v. <pre>f(x) =
    v</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    scalar: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_set
    """

    from ._pyclesperanto import _set as op

    return op(
        device=device,
        src=input_image,
        scalar=float(scalar)
    )



@plugin_function
def set_column(
    input_image: Image,
    column: int = 0,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values x of a given column in X to a constant value v.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    column: int = 0
        Column index.
    value: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setColumn
    """

    from ._pyclesperanto import _set_column as op

    return op(
        device=device,
        src=input_image,
        column=int(column),
        value=float(value)
    )



@plugin_function
def set_image_borders(
    input_image: Image,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values at the image border to a given value.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    value: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setImageBorders
    """

    from ._pyclesperanto import _set_image_borders as op

    return op(
        device=device,
        src=input_image,
        value=float(value)
    )



@plugin_function
def set_plane(
    input_image: Image,
    plane: int = 0,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values x of a given plane in X to a constant value v.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    plane: int = 0
        Plane index.
    value: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setPlane
    """

    from ._pyclesperanto import _set_plane as op

    return op(
        device=device,
        src=input_image,
        plane=int(plane),
        value=float(value)
    )



@plugin_function
def set_ramp_x(
    input_image: Image,
    device: Device = None
) -> Image:
    """Sets all pixel values to their X coordinate.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRampX
    """

    from ._pyclesperanto import _set_ramp_x as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def set_ramp_y(
    input_image: Image,
    device: Device = None
) -> Image:
    """Sets all pixel values to their Y coordinate.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRampY
    """

    from ._pyclesperanto import _set_ramp_y as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def set_ramp_z(
    input_image: Image,
    device: Device = None
) -> Image:
    """Sets all pixel values to their Z coordinate.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRampZ
    """

    from ._pyclesperanto import _set_ramp_z as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def set_row(
    input_image: Image,
    row: int = 0,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values x of a given row in X to a constant value v.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    row: int = 0
    value: float = 0
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRow
    """

    from ._pyclesperanto import _set_row as op

    return op(
        device=device,
        src=input_image,
        row=int(row),
        value=float(value)
    )



@plugin_function
def set_nonzero_pixels_to_pixelindex(
    input_image: Image,
    output_image: Image = None,
    offset: int = 1,
    device: Device = None
) -> Image:
    """Replaces all 0 value pixels in an image with the index of a pixel.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output image.
    offset: int = 1
        Offset value to start the indexing.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _set_nonzero_pixels_to_pixelindex as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        offset=int(offset)
    )



@plugin_function
def set_where_x_equals_y(
    input_image: Image,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values a of a given image A to a constant value v in case its
    coordinates x == y. Otherwise the pixel is not overwritten. If you want to
    initialize an identity transfrom matrix, set all pixels to 0 first.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    value: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setWhereXequalsY
    """

    from ._pyclesperanto import _set_where_x_equals_y as op

    return op(
        device=device,
        src=input_image,
        value=float(value)
    )



@plugin_function
def set_where_x_greater_than_y(
    input_image: Image,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values a of a given image A to a constant value v in case its
    coordinates x > y. Otherwise the pixel is not overwritten. If you want to
    initialize an identity transfrom matrix, set all pixels to 0 first.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    value: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setWhereXgreaterThanY
    """

    from ._pyclesperanto import _set_where_x_greater_than_y as op

    return op(
        device=device,
        src=input_image,
        value=float(value)
    )



@plugin_function
def set_where_x_smaller_than_y(
    input_image: Image,
    value: float = 0,
    device: Device = None
) -> Image:
    """Sets all pixel values a of a given image A to a constant value v in case its
    coordinates x < y. Otherwise the pixel is not overwritten. If you want to
    initialize an identity transfrom matrix, set all pixels to 0 first.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    value: float = 0
        Value to set.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setWhereXsmallerThanY
    """

    from ._pyclesperanto import _set_where_x_smaller_than_y as op

    return op(
        device=device,
        src=input_image,
        value=float(value)
    )



@plugin_function
def sign(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Extracts the sign of pixels. If a pixel value < 0, resulting pixel value will be
    1. If it was > 0, it will be 1. Otherwise it will be 0. This function aims to
    work similarly as its counterpart in numpy [1].

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _sign as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['combine', 'binarize', 'in assistant'])
def smaller(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines if two images A and B smaller pixel wise. f(a, b) = 1 if a < b; 0
    otherwise.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smaller
    """

    from ._pyclesperanto import _smaller as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def smaller_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Determines if two images A and B smaller pixel wise. f(a, b) = 1 if a < b; 0
    otherwise.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
        Scalar used in the comparison.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smallerConstant
    """

    from ._pyclesperanto import _smaller_constant as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['combine', 'binarize', 'in assistant'])
def smaller_or_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines if two images A and B smaller or equal pixel wise. f(a, b) = 1 if a
    <= b; 0 otherwise.

    Parameters
    ----------
    input_image0: Image
        First input image to process.
    input_image1: Image
        Second input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smallerOrEqual
    """

    from ._pyclesperanto import _smaller_or_equal as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def smaller_or_equal_constant(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Determines if two images A and B smaller or equal pixel wise. f(a, b) = 1 if a
    <= b; 0 otherwise.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
        Scalar used in the comparison.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smallerOrEqualConstant
    """

    from ._pyclesperanto import _smaller_or_equal_constant as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant', 'bia-bob-suggestion'])
def sobel(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Convolve the image with the Sobel kernel. Author(s): Ruth WhelanJeans, Robert
    Haase

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sobel
    """

    from ._pyclesperanto import _sobel as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def square_root(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the square root of each pixel.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _square_root as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant', 'bia-bob-suggestion'])
def std_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the standard deviation intensity projection of an image stack along
    Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationZProjection
    """

    from ._pyclesperanto import _std_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def subtract_image_from_scalar(
    input_image: Image,
    output_image: Image = None,
    scalar: float = 0,
    device: Device = None
) -> Image:
    """Subtracts one image X from a scalar s pixel wise. <pre>f(x, s) = s x</pre>

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    scalar: float = 0
        Scalar used in the subtraction.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subtractImageFromScalar
    """

    from ._pyclesperanto import _subtract_image_from_scalar as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        scalar=float(scalar)
    )



@plugin_function
def sum_reduction_x(
    input_image: Image,
    output_image: Image = None,
    blocksize: int = 256,
    device: Device = None
) -> Image:
    """Takes an image and reduces it in width by factor blocksize. The new pixels
    contain the sum of the reduced pixels. For example, given the following image
    and block size 4: [0, 1, 1, 0, 1, 0, 1, 1] would lead to an image [2, 3]

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    blocksize: int = 256
        Blocksize value.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _sum_reduction_x as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        blocksize=int(blocksize)
    )



@plugin_function(category=['projection'])
def sum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumXProjection
    """

    from ._pyclesperanto import _sum_x_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection'])
def sum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumYProjection
    """

    from ._pyclesperanto import _sum_y_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant', 'bia-bob-suggestion'])
def sum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumZProjection
    """

    from ._pyclesperanto import _sum_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['transform'])
def transpose_xy(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Transpose X and Y axes of an image.

    Parameters
    ----------
    input_image: Image
        The input image.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_transposeXY
    """

    from ._pyclesperanto import _transpose_xy as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['transform'])
def transpose_xz(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Transpose X and Z axes of an image.

    Parameters
    ----------
    input_image: Image
        The input image.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_transposeXZ
    """

    from ._pyclesperanto import _transpose_xz as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['transform'])
def transpose_yz(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Transpose Y and Z axes of an image.

    Parameters
    ----------
    input_image: Image
        The input image.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_transposeYZ
    """

    from ._pyclesperanto import _transpose_yz as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def undefined_to_zero(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Copies all pixels instead those which are not a number (NaN) or infinity (inf),
    which are replaced by 0.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_undefinedToZero
    """

    from ._pyclesperanto import _undefined_to_zero as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant'])
def variance_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local variance of a pixels box neighborhood. The box size is
    specified by its halfwidth, halfheight and halfdepth (radius). If 2D images are
    given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_varianceBox
    """

    from ._pyclesperanto import _variance_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant', 'bia-bob-suggestion'])
def variance_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local variance of a pixels sphere neighborhood. The sphere size is
    specified by its halfwidth, halfheight and halfdepth (radius). If 2D images are
    given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius size along x axis.
    radius_y: int = 1
        Radius size along y axis.
    radius_z: int = 1
        Radius size along z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_varianceSphere
    """

    from ._pyclesperanto import _variance_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function
def write_values_to_positions(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes an image with three/four rows (2D: height = 3; 3D: height = 4): x, y [, z]
    and v and target image. The value v will be written at position x/y[/z] in the
    target image.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_writeValuesToPositions
    """

    from ._pyclesperanto import _write_values_to_positions as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant'])
def x_position_of_maximum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines an Xposition of the maximum intensity along X and writes it into the
    resulting image. If there are multiple xslices with the same value, the smallest
    X will be chosen.

    Parameters
    ----------
    input_image: Image
        Input image stack
    output_image: Image = None
        altitude map
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _x_position_of_maximum_x_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant'])
def x_position_of_minimum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines an Xposition of the minimum intensity along X and writes it into the
    resulting image. If there are multiple xslices with the same value, the smallest
    X will be chosen.

    Parameters
    ----------
    input_image: Image
        Input image stack
    output_image: Image = None
        altitude map
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _x_position_of_minimum_x_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant'])
def y_position_of_maximum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines an Yposition of the maximum intensity along Y and writes it into the
    resulting image. If there are multiple yslices with the same value, the smallest
    Y will be chosen.

    Parameters
    ----------
    input_image: Image
        Input image stack
    output_image: Image = None
        altitude map
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _y_position_of_maximum_y_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant'])
def y_position_of_minimum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines an Yposition of the minimum intensity along Y and writes it into the
    resulting image. If there are multiple yslices with the same value, the smallest
    Y will be chosen.

    Parameters
    ----------
    input_image: Image
        Input image stack
    output_image: Image = None
        altitude map
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _y_position_of_minimum_y_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant'])
def z_position_of_maximum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines a Zposition of the maximum intensity along Z and writes it into the
    resulting image. If there are multiple zslices with the same value, the smallest
    Z will be chosen.

    Parameters
    ----------
    input_image: Image
        Input image stack
    output_image: Image = None
        altitude map
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _z_position_of_maximum_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['projection', 'in assistant'])
def z_position_of_minimum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines a Zposition of the minimum intensity along Z and writes it into the
    resulting image. If there are multiple zslices with the same value, the smallest
    Z will be chosen.

    Parameters
    ----------
    input_image: Image
        Input image stack
    output_image: Image = None
        altitude map
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _z_position_of_minimum_z_projection as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )

