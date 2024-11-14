#
# This code is auto-generated from CLIc 'cle::tier1.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function(categories=["filter", "in assistant"])
def absolute(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the absolute value of every individual pixel x in a given image.
    <pre>f(x) = |x| </pre>

    Parameters
    ----------
    input_image: Image 
        The input image to be processed.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_absolute
    """
    return clic._absolute(device, input_image, output_image)

@plugin_function(categories=["combine", "in assistant"])
def add_images_weighted(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    factor1: float =1,
    factor2: float =1,
    device: Optional[Device] =None
) -> Image:
    """Calculates the sum of pairs of pixels x and y from images X and Y weighted with
    factors a and b. <pre>f(x, y, a, b) = x * a + y * b</pre>

    Parameters
    ----------
    input_image0: Image 
        First input image to add.
    input_image1: Image 
        Second image to add.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    factor1: float (= 1)
        Multiplication factor of each pixel of src0 before adding it.
    factor2: float (= 1)
        Multiplication factor of each pixel of src1 before adding it.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_addImagesWeighted
    """
    return clic._add_images_weighted(device, input_image0, input_image1, output_image, float(factor1), float(factor2))

@plugin_function(categories=["filter", "in assistant"])
def add_image_and_scalar(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =1,
    device: Optional[Device] =None
) -> Image:
    """Adds a scalar value s to all pixels x of a given image X. <pre>f(x, s) = x +
    s</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output image.
    scalar: float (= 1)
        Scalar number to add to all pixels.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_addImageAndScalar
    """
    return clic._add_image_and_scalar(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "binary processing", "in assistant", "combine labels", "label processing"])
def binary_and(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two images X and
    Y by connecting pairs of pixels x and y with the binary AND operator &. All
    pixel values except 0 in the input images are interpreted as 1. <pre>f(x, y) = x
    & y</pre>

    Parameters
    ----------
    input_image0: Image 
        First binary input image to be processed.
    input_image1: Image 
        Second binary input image to be processed.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryAnd
    """
    return clic._binary_and(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binary processing", "label processing", "in assistant", "bia-bob-suggestion"])
def binary_edge_detection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines pixels/voxels which are on the surface of binary objects and sets
    only them to 1 in the destination image. All other pixels are set to 0.

    Parameters
    ----------
    input_image: Image 
        Binary input image where edges will be searched.
    output_image: Optional[Image] (= None)
        Output image where edge pixels will be 1.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryEdgeDetection
    """
    return clic._binary_edge_detection(device, input_image, output_image)

@plugin_function(categories=["binary processing", "filter", "label processing", "in assistant", "bia-bob-suggestion"])
def binary_not(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from an image X by
    negating its pixel values x using the binary NOT operator ! All pixel values
    except 0 in the input image are interpreted as 1. <pre>f(x) = !x</pre>

    Parameters
    ----------
    input_image: Image 
        Binary input image to be inverted.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryNot
    """
    return clic._binary_not(device, input_image, output_image)

@plugin_function(categories=["combine", "binary processing", "in assistant", "combine labels", "label processing"])
def binary_or(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two images X and
    Y by connecting pairs of pixels x and y with the binary OR operator |. All pixel
    values except 0 in the input images are interpreted as 1.<pre>f(x, y) = x |
    y</pre>

    Parameters
    ----------
    input_image0: Image 
        First binary input image to be processed.
    input_image1: Image 
        Second binary input image to be processed.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryOr
    """
    return clic._binary_or(device, input_image0, input_image1, output_image)

@plugin_function(categories=["combine", "binary processing", "in assistant", "combine labels", "label processing"])
def binary_subtract(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Subtracts one binary image from another.

    Parameters
    ----------
    input_image0: Image 
        First binary input image to be processed.
    input_image1: Image 
        Second binary input image to be subtracted from the first.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binarySubtract
    """
    return clic._binary_subtract(device, input_image0, input_image1, output_image)

@plugin_function(categories=["combine", "binary processing", "in assistant", "combine labels", "label processing"])
def binary_xor(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two images X and
    Y by connecting pairs of pixels x and y with the binary operators AND &, OR |
    and NOT ! implementing the XOR operator. All pixel values except 0 in the input
    images are interpreted as 1. <pre>f(x, y) = (x & !y) | (!x & y)</pre>

    Parameters
    ----------
    input_image0: Image 
        First binary input image to be processed.
    input_image1: Image 
        Second binary input image to be processed.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_binaryXOr
    """
    return clic._binary_xor(device, input_image0, input_image1, output_image)

@plugin_function(categories=["filter", "binary processing"])
def binary_supinf(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Compute the maximum of the erosion with plannar structuring elements. Warning:
    This operation is only supported BINARY data type images.

    Parameters
    ----------
    input_image: Image 
        The binary input image to be processed.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._binary_supinf(device, input_image, output_image)

@plugin_function(categories=["filter", "binary processing"])
def binary_infsup(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Compute the minimum of the dilation with plannar structuring elements. Warning:
    This operation is only supported BINARY data type images.

    Parameters
    ----------
    input_image: Image 
        The binary input image to be processed.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._binary_infsup(device, input_image, output_image)

@plugin_function
def block_enumerate(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    blocksize: int =256,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        output enumerated vector image
    blocksize: int (= 256)
        
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._block_enumerate(device, input_image0, input_image1, output_image, int(blocksize))

@plugin_function(categories=["filter", "combine", "in assistant"])
def convolve(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Convolve the image with a given kernel image. It is recommended that the kernel
    image has an odd size in X, Y and Z.

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_convolve
    """
    return clic._convolve(device, input_image0, input_image1, output_image)

@plugin_function
def copy(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Copies an image. <pre>f(x) = x</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to copy.
    output_image: Optional[Image] (= None)
        Output copy image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copy
    """
    return clic._copy(device, input_image, output_image)

@plugin_function
def copy_slice(
    input_image: Image,
    output_image: Optional[Image] =None,
    slice_index: int =0,
    device: Optional[Device] =None
) -> Image:
    """This method has two purposes: It copies a 2D image to a given slice_index z
    position in a 3D image stack or It copies a given slice_index at position z in
    an image stack to a 2D image. The first case is only available via ImageJ macro.
    If you are using it, it is recommended that the target 3D image already
    preexists in GPU memory before calling this method. Otherwise, CLIJ create the
    image stack with z planes.

    Parameters
    ----------
    input_image: Image 
        Input image to copy from.
    output_image: Optional[Image] (= None)
        Output copy image slice_index.
    slice_index: int (= 0)
        Index of the slice to copy.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copySlice
    """
    return clic._copy_slice(device, input_image, output_image, int(slice_index))

@plugin_function
def copy_horizontal_slice(
    input_image: Image,
    output_image: Optional[Image] =None,
    slice_index: int =0,
    device: Optional[Device] =None
) -> Image:
    """This method has two purposes: It copies a 2D image to a given slice_index y
    position in a 3D image stack or It copies a given slice_index at position y in
    an image stack to a 2D image.

    Parameters
    ----------
    input_image: Image 
        Input image to copy from.
    output_image: Optional[Image] (= None)
        Output copy image slice_index.
    slice_index: int (= 0)
        Index of the slice to copy.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copySlice
    """
    return clic._copy_horizontal_slice(device, input_image, output_image, int(slice_index))

@plugin_function
def copy_vertical_slice(
    input_image: Image,
    output_image: Optional[Image] =None,
    slice_index: int =0,
    device: Optional[Device] =None
) -> Image:
    """This method has two purposes: It copies a 2D image to a given slice_index x
    position in a 3D image stack or It copies a given slice_index at position x in
    an image stack to a 2D image.

    Parameters
    ----------
    input_image: Image 
        Input image to copy from.
    output_image: Optional[Image] (= None)
        Output copy image slice_index.
    slice_index: int (= 0)
        Index of the slice to copy.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_copySlice
    """
    return clic._copy_vertical_slice(device, input_image, output_image, int(slice_index))

@plugin_function
def crop(
    input_image: Image,
    output_image: Optional[Image] =None,
    start_x: int =0,
    start_y: int =0,
    start_z: int =0,
    width: int =1,
    height: int =1,
    depth: int =1,
    device: Optional[Device] =None
) -> Image:
    """Crops a given substack out of a given image stack. Note: If the destination
    image preexists already, it will be overwritten and keep it's dimensions.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    start_x: int (= 0)
        Starting index coordicante x.
    start_y: int (= 0)
        Starting index coordicante y.
    start_z: int (= 0)
        Starting index coordicante z.
    width: int (= 1)
        Width size of the region to crop.
    height: int (= 1)
        Height size of the region to crop.
    depth: int (= 1)
        Depth size of the region to crop.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_crop3D
    """
    return clic._crop(device, input_image, output_image, int(start_x), int(start_y), int(start_z), int(width), int(height), int(depth))

@plugin_function(categories=["filter", "in assistant"])
def cubic_root(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the cubic root of each pixel.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._cubic_root(device, input_image, output_image)

@plugin_function(categories=["binarize", "label processing", "in assistant", "bia-bob-suggestion"])
def detect_label_edges(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a labelmap and returns an image where all pixels on label edges are set to
    1 and all other pixels to 0.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectLabelEdges
    """
    return clic._detect_label_edges(device, input_image, output_image)

@plugin_function(categories=["binary processing" "filter"])
def dilation(
    input_image: Image,
    footprint: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the dilation operation between an image and a structuring element. The
    operation is applied in grayscale if the image is in grayscale. The structuring
    element is a binary image with pixel values 0 and 1, and must have the same
    dimensionality as the image (3D is the image is 3D, 2D if the image is 2D).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    footprint: Image 
        Structuring element to use for the operation.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeBox
    """
    return clic._dilation(device, input_image, footprint, output_image)

@plugin_function(categories=["binary processing"])
def dilate_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary dilation
    of a given input image. The dilation takes the Moore neighborhood (8 pixels in
    2D and 26 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1. This method is comparable to the
    'Dilate' menu in ImageJ in case it is applied to a 2D image. The only difference
    is that the output image contains values 0 and 1 instead of 0 and 255.

    Parameters
    ----------
    input_image: Image 
        Input image to process. Input image to process.
    output_image: Optional[Image] (= None)
        Output result image. Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_dilateBox
    """
    return clic._dilate_box(device, input_image, output_image)

@plugin_function(categories=["binary processing"])
def dilate_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary dilation
    of a given input image. The dilation takes the von Neumann neighborhood (4
    pixels in 2D and 6 pixels in 3d) into account. The pixels in the input image
    with pixel value not equal to 0 will be interpreted as 1.

    Parameters
    ----------
    input_image: Image 
        Input image to process. Input image to process.
    output_image: Optional[Image] (= None)
        Output result image. Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_dilateSphere
    """
    return clic._dilate_sphere(device, input_image, output_image)

@plugin_function(categories=["binary processing"])
def binary_dilate(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary dilation
    of a given input image. The dilation apply the Moore neighborhood (8 pixels in
    2D and 26 pixels in 3d) for the "box" connectivity and the von Neumann
    neighborhood (4 pixels in 2D and 6 pixels in 3d) for a "sphere" connectivity.
    The pixels in the input image with pixel value not equal to 0 will be
    interpreted as 1. For a more flexible dilation with arbitrary shapes, use
    dilation() instead.

    Parameters
    ----------
    input_image: Image 
        Input image to process. Input image to process.
    output_image: Optional[Image] (= None)
        Output result image. Output result image.
    radius_x: float (= 1)
        Radius of sphere or box structuring element in X.
    radius_y: float (= 1)
        Radius of sphere or box structuring element in Y.
    radius_z: float (= 1)
        Radius of sphere or box structuring element in Z.
    connectivity: str (= "box")
        Element shape, "box" or "sphere".
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_dilateBox
    [2] https://clij.github.io/clij2-docs/reference_dilateSphere
    """
    return clic._binary_dilate(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["combine", "in assistant"])
def divide_images(
    dividend: Image,
    divisor: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Divides two images X and Y by each other pixel wise. <pre>f(x, y) = x / y</pre>

    Parameters
    ----------
    dividend: Image 
        Input image to process.
    divisor: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_divideImages
    """
    return clic._divide_images(device, dividend, divisor, output_image)

@plugin_function(categories=["filter", "in assistant"])
def divide_scalar_by_image(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Divides a scalar by an image pixel by pixel. <pre>f(x, s) = s / x</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar value to divide the image with.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._divide_scalar_by_image(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "binarize", "in assistant"])
def equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B equal pixel wise. <pre>f(a, b) = 1 if a == b; 0
    otherwise.</pre>

    Parameters
    ----------
    input_image0: Image 
        First image to be compared with.
    input_image1: Image 
        Second image to be compared with the first.
    output_image: Optional[Image] (= None)
        Output binary image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_equal
    """
    return clic._equal(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def equal_constant(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Determines if an image A and a constant b are equal. <pre>f(a, b) = 1 if a == b;
    0 otherwise.</pre>

    Parameters
    ----------
    input_image: Image 
        Input omage where every pixel is compared to the constant.
    output_image: Optional[Image] (= None)
        Output binary image.
    scalar: float (= 0)
        Scalar value to compare pixel with.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_equalConstant
    """
    return clic._equal_constant(device, input_image, output_image, float(scalar))

@plugin_function(categories=["binary processing" "filter"])
def erosion(
    input_image: Image,
    footprint: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the erosion operation between an image and a structuring element. The
    operation is applied in grayscale if the image is in grayscale. The structuring
    element is a binary image with pixel values 0 and 1, and must have the same
    dimensionality as the image (3D is the image is 3D, 2D if the image is 2D).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    footprint: Image 
        Structuring element to use for the operation.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeBox
    """
    return clic._erosion(device, input_image, footprint, output_image)

@plugin_function(categories=["binary processing"])
def erode_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion
    of a given input image. The erosion takes the Moore neighborhood (8 pixels in 2D
    and 26 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1. This method is comparable to the
    'Erode' menu in ImageJ in case it is applied to a 2D image. The only difference
    is that the output image contains values 0 and 1 instead of 0 and 255.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeBox
    """
    return clic._erode_box(device, input_image, output_image)

@plugin_function(categories=["binary processing"])
def erode_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion
    of a given input image. The erosion takes the von Neumann neighborhood (4 pixels
    in 2D and 6 pixels in 3d) into account. The pixels in the input image with pixel
    value not equal to 0 will be interpreted as 1.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeSphere
    """
    return clic._erode_sphere(device, input_image, output_image)

@plugin_function(categories=["binary processing"])
def binary_erode(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes a binary image with pixel values 0 and 1 containing the binary erosion
    of a given input image. The erosion apply the Moore neighborhood (8 pixels in 2D
    and 26 pixels in 3d) for the "box" connectivity and the von Neumann neighborhood
    (4 pixels in 2D and 6 pixels in 3d) for a "sphere" connectivity. The pixels in
    the input image with pixel value not equal to 0 will be interpreted as 1. For a
    more flexible erosion with arbitrary shapes, use erosion() instead.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius of the eroding sphere or box structuring element in X.
    radius_y: float (= 1)
        Radius of the eroding sphere or box structuring element in Y.
    radius_z: float (= 1)
        Radius of the eroding sphere or box structuring element in Z.
    connectivity: str (= "box")
        Element shape, "box" or "sphere".
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_erodeBox
    [2] https://clij.github.io/clij2-docs/reference_erodeSphere
    """
    return clic._binary_erode(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def exponential(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes base exponential of all pixels values. f(x) = exp(x) Author(s): Peter
    Haub, Robert Haase

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_exponential
    """
    return clic._exponential(device, input_image, output_image)

@plugin_function
def flip(
    input_image: Image,
    output_image: Optional[Image] =None,
    flip_x: bool =True,
    flip_y: bool =True,
    flip_z: bool =True,
    device: Optional[Device] =None
) -> Image:
    """Flips an image in X, Y and/or Z direction depending on boolean flags.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    flip_x: bool (= True)
        Flip along the x axis if true.
    flip_y: bool (= True)
        Flip along the y axis if true.
    flip_z: bool (= True)
        Flip along the z axis if true.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_flip3D
    """
    return clic._flip(device, input_image, output_image, flip_x, flip_y, flip_z)

@plugin_function(categories=["filter", "denoise", "in assistant", "bia-bob-suggestion"])
def gaussian_blur(
    input_image: Image,
    output_image: Optional[Image] =None,
    sigma_x: float =0,
    sigma_y: float =0,
    sigma_z: float =0,
    device: Optional[Device] =None
) -> Image:
    """Computes the Gaussian blurred image of an image given sigma values in X, Y and
    Z. Thus, the filter kernel can have nonisotropic shape. The implementation is
    done separable. In case a sigma equals zero, the direction is not blurred.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    sigma_x: float (= 0)
        Sigma value along the x axis.
    sigma_y: float (= 0)
        Sigma value along the y axis.
    sigma_z: float (= 0)
        Sigma value along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gaussianBlur3D
    """
    return clic._gaussian_blur(device, input_image, output_image, float(sigma_x), float(sigma_y), float(sigma_z))

@plugin_function
def generate_distance_matrix(
    coordinate_list1: Image,
    coordinate_list2: Image,
    distance_matrix_destination: Optional[Image] =None,
    device: Optional[Device] =None
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
    coordinate_list1: Image 
        First coordinate list to process.
    coordinate_list2: Image 
        Second coordinate list to process.
    distance_matrix_destination: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_generateDistanceMatrix
    """
    return clic._generate_distance_matrix(device, coordinate_list1, coordinate_list2, distance_matrix_destination)

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def gradient_x(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the gradient of gray values along X. Assuming a, b and c are three
    adjacent pixels in X direction. In the target image will be saved as: <pre>b' =
    c a;</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gradientX
    """
    return clic._gradient_x(device, input_image, output_image)

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def gradient_y(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the gradient of gray values along Y. Assuming a, b and c are three
    adjacent pixels in Y direction. In the target image will be saved as: <pre>b' =
    c a;</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gradientY
    """
    return clic._gradient_y(device, input_image, output_image)

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def gradient_z(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the gradient of gray values along Z. Assuming a, b and c are three
    adjacent pixels in Z direction. In the target image will be saved as: <pre>b' =
    c a;</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gradientZ
    """
    return clic._gradient_z(device, input_image, output_image)

@plugin_function(categories=["combine", "binarize", "in assistant"])
def greater(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B greater pixel wise. f(a, b) = 1 if a > b; 0
    otherwise.

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greater
    """
    return clic._greater(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def greater_constant(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B greater pixel wise. f(a, b) = 1 if a > b; 0
    otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar value to compare pixel with.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greaterConstant
    """
    return clic._greater_constant(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "binarize", "in assistant"])
def greater_or_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B greater or equal pixel wise. f(a, b) = 1 if a
    >= b; 0 otherwise.

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greaterOrEqual
    """
    return clic._greater_or_equal(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def greater_or_equal_constant(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B greater or equal pixel wise. f(a, b) = 1 if a
    >= b; 0 otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar value to compare pixel with.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_greaterOrEqualConstant
    """
    return clic._greater_or_equal_constant(device, input_image, output_image, float(scalar))

@plugin_function
def hessian_eigenvalues(
    input_image: Image,
    small_eigenvalue: Optional[Image] =None,
    middle_eigenvalue: Optional[Image] =None,
    large_eigenvalue: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
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
    small_eigenvalue: Optional[Image] (= None)
        Output result image.
    middle_eigenvalue: Optional[Image] (= None)
        Output result image, null if input is 2D.
    large_eigenvalue: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._hessian_eigenvalues(device, input_image, small_eigenvalue, middle_eigenvalue, large_eigenvalue)

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def laplace_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Applies the Laplace operator (Box neighborhood) to an image.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_laplaceBox
    """
    return clic._laplace_box(device, input_image, output_image)

@plugin_function(categories=["filter", "edge detection"])
def laplace_diamond(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Applies the Laplace operator (Diamond neighborhood) to an image.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_laplaceDiamond
    """
    return clic._laplace_diamond(device, input_image, output_image)

@plugin_function(categories=["filter", "edge detection"])
def laplace(
    input_image: Image,
    output_image: Optional[Image] =None,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Applies the Laplace operator with a "box" or a "sphere" neighborhood to an
    image.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_laplaceDiamond
    """
    return clic._laplace(device, input_image, output_image, str(connectivity))

@plugin_function(categories=["filter", "combine", "in assistant"])
def local_cross_correlation(
    input_image: Image,
    kernel: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Compute the cross correlation of an image to a given kernel.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    kernel: Image 
        Input
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._local_cross_correlation(device, input_image, kernel, output_image)

@plugin_function(categories=["filter", "in assistant"])
def logarithm(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes base e logarithm of all pixels values. f(x) = log(x) Author(s): Peter
    Haub, Robert Haase

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_logarithm
    """
    return clic._logarithm(device, input_image, output_image)

@plugin_function
def mask(
    input_image: Image,
    mask: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mask
    """
    return clic._mask(device, input_image, mask, output_image)

@plugin_function
def mask_label(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    label: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes a masked image by applying a label mask to an image. All pixel values x
    of image X will be copied to the destination image in case pixel value m at the
    same position in the label_map image has the right index value i. <pre>f(x,m,i)
    = (x if (m == i); (0 otherwise))</pre>

    Parameters
    ----------
    input_image0: Image 
        Input Intensity image.
    input_image1: Image 
        Input Label image.
    output_image: Optional[Image] (= None)
        Output result image.
    label: float (= 1)
        Label value to use.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maskLabel
    """
    return clic._mask_label(device, input_image0, input_image1, output_image, float(label))

@plugin_function(categories=["filter", "in assistant"])
def maximum_image_and_scalar(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Computes the maximum of a constant scalar s and each pixel value x in a given
    image X. <pre>f(x, s) = max(x, s)</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar value used in the comparison.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumImageAndScalar
    """
    return clic._maximum_image_and_scalar(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "in assistant"])
def maximum_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the maximum of a pair of pixel values x, y from two given images X and
    Y. <pre>f(x, y) = max(x, y)</pre>

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumImages
    """
    return clic._maximum_images(device, input_image0, input_image1, output_image)

@plugin_function(categories=["filter", "in assistant"])
def maximum_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local maximum of a pixels cube neighborhood. The cubes size is
    specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximum3DBox
    """
    return clic._maximum_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "in assistant"])
def maximum_filter(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local maximum of a pixels neighborhood (box or sphere). The
    neighborhood size is specified by its halfwidth, halfheight and halfdepth
    (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximum3DBox
    [2] https://clij.github.io/clij2-docs/reference_maximum3DSphere
    """
    return clic._maximum_filter(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def grayscale_dilate(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes a grayscale image containing the grayscale dilation of a given input
    image. The erosion apply the Moore neighborhood (8 pixels in 2D and 26 pixels in
    3d) for the "box" connectivity and the von Neumann neighborhood (4 pixels in 2D
    and 6 pixels in 3d) for a "sphere" connectivity. The pixels in the input image
    with pixel value not equal to 0 will be interpreted as 1.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DBox
    [2] https://clij.github.io/clij2-docs/reference_minimum3DSphere
    """
    return clic._grayscale_dilate(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["projection"])
def maximum_x_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the maximum intensity projection of an image along X.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumXProjection
    """
    return clic._maximum_x_projection(device, input_image, output_image)

@plugin_function(categories=["projection"])
def maximum_y_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the maximum intensity projection of an image along X.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumYProjection
    """
    return clic._maximum_y_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant", "bia-bob-suggestion"])
def maximum_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the maximum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumZProjection
    """
    return clic._maximum_z_projection(device, input_image, output_image)

@plugin_function(categories=["filter", "denoise", "in assistant"])
def mean_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local mean average of a pixels boxshaped neighborhood. The cubes
    size is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mean3DBox
    """
    return clic._mean_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "denoise", "in assistant", "bia-bob-suggestion"])
def mean_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local mean average of a pixels spherical neighborhood. The spheres
    size is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mean3DSphere
    """
    return clic._mean_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "denoise", "in assistant"])
def mean_filter(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local mean average of a pixels neighborhood defined as a boxshaped
    or a sphereshaped. The shape size is specified by its halfwidth, halfheight and
    halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_mean3DSphere
    """
    return clic._mean_filter(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["projection"])
def mean_x_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the mean average intensity projection of an image along X.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanXProjection
    """
    return clic._mean_x_projection(device, input_image, output_image)

@plugin_function(categories=["projection"])
def mean_y_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the mean average intensity projection of an image along Y.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanYProjection
    """
    return clic._mean_y_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant", "bia-bob-suggestion"])
def mean_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the mean average intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanZProjection
    """
    return clic._mean_z_projection(device, input_image, output_image)

@plugin_function(categories=["filter", "denoise", "in assistant"])
def median_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local median of a pixels box shaped neighborhood. The box is
    specified by its halfwidth and halfheight (radius). For technical reasons, the
    area of the box must have less than 1000 pixels.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_median3DBox
    """
    return clic._median_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "denoise", "in assistant"])
def median_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local median of a pixels sphere shaped neighborhood. The sphere is
    specified by its halfwidth and halfheight (radius). For technical reasons, the
    area of the box must have less than 1000 pixels.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_median3DSphere
    """
    return clic._median_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "denoise", "in assistant"])
def median(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local median of a pixels neighborhood. The neighborhood is defined
    as a box or a sphere shape. Its size is specified by its halfwidth, halfheight,
    and halfdepth (radius). For technical reasons, the area of the shpae must have
    less than 1000 pixels.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_median3DSphere
    """
    return clic._median(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def minimum_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local minimum of a pixels cube neighborhood. The cubes size is
    specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DBox
    """
    return clic._minimum_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "in assistant"])
def minimum_filter(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local minimum of a pixels cube neighborhood. The cubes size is
    specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DBox
    [2] https://clij.github.io/clij2-docs/reference_minimum3DSphere
    """
    return clic._minimum_filter(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def grayscale_erode(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes a grayscale image containing the grayscale erosion of a given input
    image. The erosion apply the Mooreneighborhood (8 pixels in 2D and 26 pixels in
    3d) for the "box" connectivity and the vonNeumannneighborhood (4 pixels in 2D
    and 6 pixels in 3d) for a "sphere" connectivity. The pixels in the input image
    with pixel value not equal to 0 will be interpreted as 1.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DBox
    [2] https://clij.github.io/clij2-docs/reference_minimum3DSphere
    """
    return clic._grayscale_erode(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def minimum_image_and_scalar(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Computes the minimum of a constant scalar s and each pixel value x in a given
    image X. <pre>f(x, s) = min(x, s)</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar value used in the comparison.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumImageAndScalar
    """
    return clic._minimum_image_and_scalar(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "in assistant"])
def minimum_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the minimum of a pair of pixel values x, y from two given images X and
    Y. <pre>f(x, y) = min(x, y)</pre>

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumImages
    """
    return clic._minimum_images(device, input_image0, input_image1, output_image)

@plugin_function(categories=["projection"])
def minimum_x_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the minimum intensity projection of an image along Y.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumXProjection
    """
    return clic._minimum_x_projection(device, input_image, output_image)

@plugin_function(categories=["projection"])
def minimum_y_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the minimum intensity projection of an image along Y.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumYProjection
    """
    return clic._minimum_y_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant", "bia-bob-suggestion"])
def minimum_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the minimum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumZProjection
    """
    return clic._minimum_z_projection(device, input_image, output_image)

@plugin_function(categories=["label processing", "in assistant"])
def mode_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._mode_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def mode_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._mode_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["label processing", "in assistant"])
def mode(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local mode of a pixels neighborhood. This neighborhood can be
    shaped as a box or a sphere. This can be used to postprocess and locally correct
    semantic segmentation results. The shape size is specified by its halfwidth,
    halfheight, and halfdepth (radius). For technical reasons, the intensities must
    lie within a range from 0 to 255 (uint8). In case multiple values have maximum
    frequency, the smallest one is returned.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._mode(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["combine"])
def modulo_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the remainder of a division of pairwise pixel values in two images

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._modulo_images(device, input_image0, input_image1, output_image)

@plugin_function
def multiply_image_and_position(
    input_image: Image,
    output_image: Optional[Image] =None,
    dimension: int =0,
    device: Optional[Device] =None
) -> Image:
    """Multiplies all pixel intensities with the x, y or z coordinate, depending on
    specified dimension.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    dimension: int (= 0)
        Dimension (0,1,2) to use in the operation.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndCoordinate
    """
    return clic._multiply_image_and_position(device, input_image, output_image, int(dimension))

@plugin_function(categories=["filter", "in assistant"])
def multiply_image_and_scalar(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Multiplies all pixels value x in a given image X with a constant scalar s.
    <pre>f(x, s) = x * s</pre>

    Parameters
    ----------
    input_image: Image 
        The input image to be multiplied with a constant.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    scalar: float (= 0)
        The number with which every pixel will be multiplied with.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndScalar
    """
    return clic._multiply_image_and_scalar(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "in assistant"])
def multiply_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Multiplies all pairs of pixel values x and y from two image X and Y. <pre>f(x,
    y) = x * y</pre>

    Parameters
    ----------
    input_image0: Image 
        First input image to be multiplied.
    input_image1: Image 
        Second image to be multiplied.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyImages
    """
    return clic._multiply_images(device, input_image0, input_image1, output_image)

@plugin_function
def nan_to_num(
    input_image: Image,
    output_image: Optional[Image] =None,
    nan: float =0,
    posinf: float =np.nan_to_num(float('inf')),
    neginf: float =np.nan_to_num(float('-inf')),
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    nan: float (= 0)
        Value to replace
    posinf: float (= np.nan_to_num(float('inf')))
        Value to replace +inf with.
    neginf: float (= np.nan_to_num(float('-inf')))
        Value to replace -inf with.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html
    """
    return clic._nan_to_num(device, input_image, output_image, float(nan), float(posinf), float(neginf))

@plugin_function
def nonzero_maximum_box(
    input_image: Image,
    output_image0: Image,
    output_image1: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image1: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMaximumBox
    """
    return clic._nonzero_maximum_box(device, input_image, output_image0, output_image1)

@plugin_function
def nonzero_maximum_diamond(
    input_image: Image,
    output_image0: Image,
    output_image1: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image1: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMaximumDiamond
    """
    return clic._nonzero_maximum_diamond(device, input_image, output_image0, output_image1)

@plugin_function
def nonzero_maximum(
    input_image: Image,
    output_image0: Image,
    output_image1: Optional[Image] =None,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Apply a maximum filter of a neighborhood to the input image. The neighborhood
    shape can be a box or a sphere. The size is fixed to 1 and pixels with value 0
    are ignored. Note: Pixels with 0 value in the input image will not be
    overwritten in the output image. Thus, the result image should be initialized by
    copying the original image in advance.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image0: Image 
        Output flag (0 or 1).
    output_image1: Optional[Image] (= None)
        Output image where results are written into.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMaximumBox
    [2] https://clij.github.io/clij2-docs/reference_nonzeroMaximumDiamond
    """
    return clic._nonzero_maximum(device, input_image, output_image0, output_image1, str(connectivity))

@plugin_function
def nonzero_minimum_box(
    input_image: Image,
    output_image0: Image,
    output_image1: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image1: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumBox
    """
    return clic._nonzero_minimum_box(device, input_image, output_image0, output_image1)

@plugin_function
def nonzero_minimum_diamond(
    input_image: Image,
    output_image0: Image,
    output_image1: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image1: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumDiamond
    """
    return clic._nonzero_minimum_diamond(device, input_image, output_image0, output_image1)

@plugin_function
def nonzero_minimum(
    input_image: Image,
    output_image0: Image,
    output_image1: Optional[Image] =None,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Apply a minimum filter of a neighborhood to the input image. The neighborhood
    shape can be a box or a sphere. The radius is fixed to 1 and pixels with value 0
    are ignored.Note: Pixels with 0 value in the input image will not be overwritten
    in the output image. Thus, the result image should be initialized by copying the
    original image in advance.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image0: Image 
        Output flag (0 or 1).
    output_image1: Optional[Image] (= None)
        Output image where results are written into.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_nonzeroMinimumBox
    [2] https://clij.github.io/clij2-docs/reference_nonzeroMinimumDiamond
    """
    return clic._nonzero_minimum(device, input_image, output_image0, output_image1, str(connectivity))

@plugin_function(categories=["combine", "binarize", "in assistant"])
def not_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B equal pixel wise. f(a, b) = 1 if a != b; 0
    otherwise.

    Parameters
    ----------
    input_image0: Image 
        First image to be compared with.
    input_image1: Image 
        Second image to be compared with the first.
    output_image: Optional[Image] (= None)
        The resulting binary image where pixels will be 1 only if source1
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_notEqual
    """
    return clic._not_equal(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def not_equal_constant(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B equal pixel wise. f(a, b) = 1 if a != b; 0
    otherwise.

    Parameters
    ----------
    input_image: Image 
        The image where every pixel is compared to the constant.
    output_image: Optional[Image] (= None)
        The resulting binary image where pixels will be 1 only if source1
    scalar: float (= 0)
        The constant where every pixel is compared to.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_notEqualConstant
    """
    return clic._not_equal_constant(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "in assistant"])
def paste(
    input_image: Image,
    output_image: Optional[Image] =None,
    destination_x: int =0,
    destination_y: int =0,
    destination_z: int =0,
    device: Optional[Device] =None
) -> Image:
    """Pastes an image into another image at a given position.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    destination_x: int (= 0)
        Origin pixel coodinate in x to paste.
    destination_y: int (= 0)
        Origin pixel coodinate in y to paste.
    destination_z: int (= 0)
        Origin pixel coodinate in z to paste.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_paste3D
    """
    return clic._paste(device, input_image, output_image, int(destination_x), int(destination_y), int(destination_z))

@plugin_function
def onlyzero_overwrite_maximum_box(
    input_image: Image,
    flag: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Apply a local maximum filter to an image which only overwrites pixels with value
    0.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    flag: Image 
        Output
    output_image: Optional[Image] (= None)
        Output image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumBox
    """
    return clic._onlyzero_overwrite_maximum_box(device, input_image, flag, output_image)

@plugin_function
def onlyzero_overwrite_maximum_diamond(
    input_image: Image,
    flag: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Apply a local maximum filter to an image which only overwrites pixels with value
    0.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    flag: Image 
        Output
    output_image: Optional[Image] (= None)
        Output image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumDiamond
    """
    return clic._onlyzero_overwrite_maximum_diamond(device, input_image, flag, output_image)

@plugin_function
def onlyzero_overwrite_maximum(
    input_image: Image,
    flag: Image,
    output_image: Optional[Image] =None,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Apply a local maximum filter to an image which only overwrites pixels with value
    0.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    flag: Image 
        Output
    output_image: Optional[Image] (= None)
        Output image.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumBox
    [2] https://clij.github.io/clij2-docs/reference_onlyzeroOverwriteMaximumDiamond
    """
    return clic._onlyzero_overwrite_maximum(device, input_image, flag, output_image, str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def power(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes all pixels value x to the power of a given exponent a. <pre>f(x, a) = x
    ^ a</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 1)
        Power value.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_power
    """
    return clic._power(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "in assistant"])
def power_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Calculates x to the power of y pixel wise of two images X and Y.

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_powerImages
    """
    return clic._power_images(device, input_image0, input_image1, output_image)

@plugin_function(categories=["transform", "in assistant"])
def range(
    input_image: Image,
    output_image: Optional[Image] =None,
    start_x: Optional[int] =None,
    stop_x: Optional[int] =None,
    step_x: Optional[int] =None,
    start_y: Optional[int] =None,
    stop_y: Optional[int] =None,
    step_y: Optional[int] =None,
    start_z: Optional[int] =None,
    stop_z: Optional[int] =None,
    step_z: Optional[int] =None,
    device: Optional[Device] =None
) -> Image:
    """Crops an image according to a defined range and step size.

    Parameters
    ----------
    input_image: Image 
        First input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    start_x: Optional[int] (= None)
        Range starting value in x
    stop_x: Optional[int] (= None)
        Range stop value in x
    step_x: Optional[int] (= None)
        Range step value in x
    start_y: Optional[int] (= None)
        Range starting value in y
    stop_y: Optional[int] (= None)
        Range stop value in y
    step_y: Optional[int] (= None)
        Range step value in y
    start_z: Optional[int] (= None)
        Range starting value in z
    stop_z: Optional[int] (= None)
        Range stop value in z
    step_z: Optional[int] (= None)
        Range step value in z
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._range(device, input_image, output_image, start_x, stop_x, step_x, start_y, stop_y, step_y, start_z, stop_z, step_z)

@plugin_function
def read_values_from_positions(
    input_image: Image,
    list: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output vector image of intensities.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._read_values_from_positions(device, input_image, list, output_image)

@plugin_function(categories=["bia-bob-suggestion"])
def replace_values(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_replaceIntensities
    """
    return clic._replace_values(device, input_image0, input_image1, output_image)

@plugin_function
def replace_value(
    input_image: Image,
    output_image: Optional[Image] =None,
    value_to_replace: float =0,
    value_replacement: float =1,
    device: Optional[Device] =None
) -> Image:
    """Replaces a specific intensity in an image with a given new value.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    value_to_replace: float (= 0)
        Old value.
    value_replacement: float (= 1)
        New value.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_replaceIntensity
    """
    return clic._replace_value(device, input_image, output_image, float(value_to_replace), float(value_replacement))

@plugin_function
def replace_intensity(
    input_image: Image,
    output_image: Optional[Image] =None,
    value_to_replace: float =0,
    value_replacement: float =1,
    device: Optional[Device] =None
) -> Image:
    """Replaces a specific intensity in an image with a given new value.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    value_to_replace: float (= 0)
        Old value.
    value_replacement: float (= 1)
        New value.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_replaceIntensity
    """
    return clic._replace_intensity(device, input_image, output_image, float(value_to_replace), float(value_replacement))

@plugin_function
def replace_intensities(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
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
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_replaceIntensities
    """
    return clic._replace_intensities(device, input_image0, input_image1, output_image)

@plugin_function(categories=["filter", "in assistant", "bia-bob-suggestion"])
def maximum_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =0,
    device: Optional[Device] =None
) -> Image:
    """Computes the local maximum of a pixels spherical neighborhood. The spheres size
    is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 0)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximum3DSphere
    """
    return clic._maximum_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "in assistant", "bia-bob-suggestion"])
def minimum_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local minimum of a pixels spherical neighborhood. The spheres size
    is specified by its halfwidth, halfheight and halfdepth (radius).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimum3DSphere
    """
    return clic._minimum_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function
def multiply_matrix(
    matrix1: Image,
    matrix2: Image,
    matrix_destination: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Multiplies two matrices with each other. Shape of matrix1 should be equal to
    shape of matrix2 transposed.

    Parameters
    ----------
    matrix1: Image 
        First matrix to process.
    matrix2: Image 
        Second matrix to process.
    matrix_destination: Optional[Image] (= None)
        Output result matrix.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_multiplyMatrix
    """
    return clic._multiply_matrix(device, matrix1, matrix2, matrix_destination)

@plugin_function(categories=["filter", "in assistant"])
def reciprocal(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes 1/x for every pixel value This function is supposed to work similarly
    to its counter part in numpy [1]

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.reciprocal.html
    """
    return clic._reciprocal(device, input_image, output_image)

@plugin_function
def set(
    input_image: Image,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values x of a given image X to a constant value v. <pre>f(x) =
    v</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    scalar: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_set
    """
    return clic._set(device, input_image, float(scalar))

@plugin_function
def set_column(
    input_image: Image,
    column_index: int =0,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values x of a given column in X to a constant value v.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    column_index: int (= 0)
        Column index.
    value: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setColumn
    """
    return clic._set_column(device, input_image, int(column_index), float(value))

@plugin_function
def set_image_borders(
    input_image: Image,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values at the image border to a given value.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    value: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setImageBorders
    """
    return clic._set_image_borders(device, input_image, float(value))

@plugin_function
def set_plane(
    input_image: Image,
    plane_index: int =0,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values x of a given plane in X to a constant value v.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    plane_index: int (= 0)
        Plane index.
    value: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setPlane
    """
    return clic._set_plane(device, input_image, int(plane_index), float(value))

@plugin_function
def set_ramp_x(
    input_image: Image,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values to their X coordinate.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRampX
    """
    return clic._set_ramp_x(device, input_image)

@plugin_function
def set_ramp_y(
    input_image: Image,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values to their Y coordinate.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRampY
    """
    return clic._set_ramp_y(device, input_image)

@plugin_function
def set_ramp_z(
    input_image: Image,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values to their Z coordinate.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRampZ
    """
    return clic._set_ramp_z(device, input_image)

@plugin_function
def set_row(
    input_image: Image,
    row_index: int =0,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values x of a given row in X to a constant value v.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    row_index: int (= 0)
        
    value: float (= 0)
        
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setRow
    """
    return clic._set_row(device, input_image, int(row_index), float(value))

@plugin_function
def set_nonzero_pixels_to_pixelindex(
    input_image: Image,
    output_image: Optional[Image] =None,
    offset: int =1,
    device: Optional[Device] =None
) -> Image:
    """Replaces all 0 value pixels in an image with the index of a pixel.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output image.
    offset: int (= 1)
        Offset value to start the indexing.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._set_nonzero_pixels_to_pixelindex(device, input_image, output_image, int(offset))

@plugin_function
def set_where_x_equals_y(
    input_image: Image,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values a of a given image A to a constant value v in case its
    coordinates x == y. Otherwise the pixel is not overwritten. If you want to
    initialize an identity transfrom matrix, set all pixels to 0 first.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    value: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setWhereXequalsY
    """
    return clic._set_where_x_equals_y(device, input_image, float(value))

@plugin_function
def set_where_x_greater_than_y(
    input_image: Image,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values a of a given image A to a constant value v in case its
    coordinates x > y. Otherwise the pixel is not overwritten. If you want to
    initialize an identity transfrom matrix, set all pixels to 0 first.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    value: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setWhereXgreaterThanY
    """
    return clic._set_where_x_greater_than_y(device, input_image, float(value))

@plugin_function
def set_where_x_smaller_than_y(
    input_image: Image,
    value: float =0,
    device: Optional[Device] =None
) -> Image:
    """Sets all pixel values a of a given image A to a constant value v in case its
    coordinates x < y. Otherwise the pixel is not overwritten. If you want to
    initialize an identity transfrom matrix, set all pixels to 0 first.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    value: float (= 0)
        Value to set.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_setWhereXsmallerThanY
    """
    return clic._set_where_x_smaller_than_y(device, input_image, float(value))

@plugin_function
def sign(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Extracts the sign of pixels. If a pixel value < 0, resulting pixel value will be
    1. If it was > 0, it will be 1. Otherwise it will be 0. This function aims to
    work similarly as its counterpart in numpy [1].

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._sign(device, input_image, output_image)

@plugin_function(categories=["combine", "binarize", "in assistant"])
def smaller(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B smaller pixel wise. f(a, b) = 1 if a < b; 0
    otherwise.

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smaller
    """
    return clic._smaller(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def smaller_constant(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B smaller pixel wise. f(a, b) = 1 if a < b; 0
    otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar used in the comparison.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smallerConstant
    """
    return clic._smaller_constant(device, input_image, output_image, float(scalar))

@plugin_function(categories=["combine", "binarize", "in assistant"])
def smaller_or_equal(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B smaller or equal pixel wise. f(a, b) = 1 if a
    <= b; 0 otherwise.

    Parameters
    ----------
    input_image0: Image 
        First input image to process.
    input_image1: Image 
        Second input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smallerOrEqual
    """
    return clic._smaller_or_equal(device, input_image0, input_image1, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def smaller_or_equal_constant(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Determines if two images A and B smaller or equal pixel wise. f(a, b) = 1 if a
    <= b; 0 otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar used in the comparison.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_smallerOrEqualConstant
    """
    return clic._smaller_or_equal_constant(device, input_image, output_image, float(scalar))

@plugin_function(categories=["filter", "edge detection", "in assistant", "bia-bob-suggestion"])
def sobel(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Convolve the image with the Sobel kernel. Author(s): Ruth WhelanJeans, Robert
    Haase

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sobel
    """
    return clic._sobel(device, input_image, output_image)

@plugin_function(categories=["filter", "in assistant"])
def square_root(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the square root of each pixel.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._square_root(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant", "bia-bob-suggestion"])
def std_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the standard deviation intensity projection of an image stack along
    Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationZProjection
    """
    return clic._std_z_projection(device, input_image, output_image)

@plugin_function(categories=["filter", "in assistant"])
def subtract_image_from_scalar(
    input_image: Image,
    output_image: Optional[Image] =None,
    scalar: float =0,
    device: Optional[Device] =None
) -> Image:
    """Subtracts one image X from a scalar s pixel wise. <pre>f(x, s) = s x</pre>

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    scalar: float (= 0)
        Scalar used in the subtraction.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subtractImageFromScalar
    """
    return clic._subtract_image_from_scalar(device, input_image, output_image, float(scalar))

@plugin_function
def sum_reduction_x(
    input_image: Image,
    output_image: Optional[Image] =None,
    blocksize: int =256,
    device: Optional[Device] =None
) -> Image:
    """Takes an image and reduces it in width by factor blocksize. The new pixels
    contain the sum of the reduced pixels. For example, given the following image
    and block size 4: [0, 1, 1, 0, 1, 0, 1, 1] would lead to an image [2, 3]

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    blocksize: int (= 256)
        Blocksize value.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._sum_reduction_x(device, input_image, output_image, int(blocksize))

@plugin_function(categories=["projection"])
def sum_x_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumXProjection
    """
    return clic._sum_x_projection(device, input_image, output_image)

@plugin_function(categories=["projection"])
def sum_y_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumYProjection
    """
    return clic._sum_y_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant", "bia-bob-suggestion"])
def sum_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the sum intensity projection of an image along Z.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumZProjection
    """
    return clic._sum_z_projection(device, input_image, output_image)

@plugin_function(categories=["transform"])
def transpose_xy(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Transpose X and Y axes of an image.

    Parameters
    ----------
    input_image: Image 
        The input image.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_transposeXY
    """
    return clic._transpose_xy(device, input_image, output_image)

@plugin_function(categories=["transform"])
def transpose_xz(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Transpose X and Z axes of an image.

    Parameters
    ----------
    input_image: Image 
        The input image.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_transposeXZ
    """
    return clic._transpose_xz(device, input_image, output_image)

@plugin_function(categories=["transform"])
def transpose_yz(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Transpose Y and Z axes of an image.

    Parameters
    ----------
    input_image: Image 
        The input image.
    output_image: Optional[Image] (= None)
        Output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_transposeYZ
    """
    return clic._transpose_yz(device, input_image, output_image)

@plugin_function
def undefined_to_zero(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Copies all pixels instead those which are not a number (NaN) or infinity (inf),
    which are replaced by 0.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_undefinedToZero
    """
    return clic._undefined_to_zero(device, input_image, output_image)

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def variance_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local variance of a pixels box neighborhood. The box size is
    specified by its halfwidth, halfheight and halfdepth (radius). If 2D images are
    given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_varianceBox
    """
    return clic._variance_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def variance_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local variance of a pixels sphere neighborhood. The sphere size is
    specified by its halfwidth, halfheight and halfdepth (radius). If 2D images are
    given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_varianceSphere
    """
    return clic._variance_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def variance_filter(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local variance of a pixels neighborhood (box or sphere). The
    neighborhood size is specified by its halfwidth, halfheight and halfdepth
    (radius). If 2D images are given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius size along x axis.
    radius_y: float (= 1)
        Radius size along y axis.
    radius_z: float (= 1)
        Radius size along z axis.
    connectivity: str (= "box")
        Filter neigborhood
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_varianceBox
    [2] https://clij.github.io/clij2-docs/reference_varianceSphere
    """
    return clic._variance_filter(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function
def write_values_to_positions(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes an image with three/four rows (2D: height = 3; 3D: height = 4): x, y [, z]
    and v and target image. The value v will be written at position x/y[/z] in the
    target image.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_writeValuesToPositions
    """
    return clic._write_values_to_positions(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant"])
def x_position_of_maximum_x_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines an Xposition of the maximum intensity along X and writes it into the
    resulting image. If there are multiple xslices with the same value, the smallest
    X will be chosen.

    Parameters
    ----------
    input_image: Image 
        Input image stack
    output_image: Optional[Image] (= None)
        altitude map
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._x_position_of_maximum_x_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant"])
def x_position_of_minimum_x_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines an Xposition of the minimum intensity along X and writes it into the
    resulting image. If there are multiple xslices with the same value, the smallest
    X will be chosen.

    Parameters
    ----------
    input_image: Image 
        Input image stack
    output_image: Optional[Image] (= None)
        altitude map
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._x_position_of_minimum_x_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant"])
def y_position_of_maximum_y_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines an Yposition of the maximum intensity along Y and writes it into the
    resulting image. If there are multiple yslices with the same value, the smallest
    Y will be chosen.

    Parameters
    ----------
    input_image: Image 
        Input image stack
    output_image: Optional[Image] (= None)
        altitude map
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._y_position_of_maximum_y_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant"])
def y_position_of_minimum_y_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines an Yposition of the minimum intensity along Y and writes it into the
    resulting image. If there are multiple yslices with the same value, the smallest
    Y will be chosen.

    Parameters
    ----------
    input_image: Image 
        Input image stack
    output_image: Optional[Image] (= None)
        altitude map
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._y_position_of_minimum_y_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant"])
def z_position_of_maximum_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines a Zposition of the maximum intensity along Z and writes it into the
    resulting image. If there are multiple zslices with the same value, the smallest
    Z will be chosen.

    Parameters
    ----------
    input_image: Image 
        Input image stack
    output_image: Optional[Image] (= None)
        altitude map
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._z_position_of_maximum_z_projection(device, input_image, output_image)

@plugin_function(categories=["projection", "in assistant"])
def z_position_of_minimum_z_projection(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines a Zposition of the minimum intensity along Z and writes it into the
    resulting image. If there are multiple zslices with the same value, the smallest
    Z will be chosen.

    Parameters
    ----------
    input_image: Image 
        Input image stack
    output_image: Optional[Image] (= None)
        altitude map
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._z_position_of_minimum_z_projection(device, input_image, output_image)