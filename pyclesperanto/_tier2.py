#
# This code is auto-generated from CLIc 'cle::tier2.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function(categories=["combine", "in assistant"])
def absolute_difference(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the absolute difference pixel by pixel between two images. <pre>f(x,
    y) = |x y| </pre>

    Parameters
    ----------
    input_image0: Image 
        The input image to be subtracted from.
    input_image1: Image 
        The input image which is subtracted.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_absoluteDifference
    """
    return clic._absolute_difference(device, input_image0, input_image1, output_image)

@plugin_function(categories=["combine", "in assistant"])
def add_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Calculates the sum of pairs of pixels x and y of two images X and Y. <pre>f(x,
    y) = x + y</pre>

    Parameters
    ----------
    input_image0: Image 
        The first input image to added.
    input_image1: Image 
        The second image to be added.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_addImages
    """
    return clic._add_images(device, input_image0, input_image1, output_image)

@plugin_function(categories=["filter", "background removal", "in assistant"])
def bottom_hat_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Apply a bottomhat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image 
        The input image where the background is subtracted from.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    radius_x: float (= 1)
        Radius of the background determination region in X.
    radius_y: float (= 1)
        Radius of the background determination region in Y.
    radius_z: float (= 1)
        Radius of the background determination region in Z.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_bottomHatBox
    """
    return clic._bottom_hat_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "background removal", "in assistant"])
def bottom_hat_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Applies a bottomhat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image 
        The input image where the background is subtracted from.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    radius_x: float (= 1)
        Radius of the background determination region in X.
    radius_y: float (= 1)
        Radius of the background determination region in Y.
    radius_z: float (= 1)
        Radius of the background determination region in Z.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_bottomHatSphere
    """
    return clic._bottom_hat_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "background removal", "in assistant"])
def bottom_hat(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Applies a bottomhat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image 
        The input image where the background is subtracted from.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    radius_x: float (= 1)
        Radius of the background determination region in X.
    radius_y: float (= 1)
        Radius of the background determination region in Y.
    radius_z: float (= 1)
        Radius of the background determination region in Z.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_bottomHatBox
    [2] https://clij.github.io/clij2-docs/reference_bottomHatSphere
    """
    return clic._bottom_hat(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["combine", "in assistant"])
def clip(
    input_image: Image,
    output_image: Optional[Image] =None,
    min_intensity: Optional[float] =None,
    max_intensity: Optional[float] =None,
    device: Optional[Device] =None
) -> Image:
    """Limits the range of values in an image. This function is supposed to work
    similarly as its counter part in numpy [1].

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    min_intensity: Optional[float] (= None)
        new, lower limit of the intensity range
    max_intensity: Optional[float] (= None)
        new, upper limit of the intensity range
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.clip.html
    """
    return clic._clip(device, input_image, output_image, min_intensity, max_intensity)

@plugin_function(categories=["filter", "in assistant"])
def closing_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: int =1,
    radius_y: int =1,
    radius_z: int =1,
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies grayscale morphological closing to intensity images
    using a box shaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: int (= 1)
        Radius along the x axis.
    radius_y: int (= 1)
        Radius along the y axis.
    radius_z: int (= 1)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._closing_box(device, input_image, output_image, int(radius_x), int(radius_y), int(radius_z))

@plugin_function(categories=["filter", "in assistant", "bia-bob-suggestion"])
def closing_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies grayscale morphological closing to intensity images
    using a sphere shaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._closing_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "in assistant"])
def grayscale_closing(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies grayscale morphological closing to intensity images
    using a sphere or box shaped footprint. This operator also works with binary
    images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._grayscale_closing(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def closing(
    input_image: Image,
    footprint: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies morphological closing to intensity images using a
    custom structuring element provided as input. This operator also works with
    binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    footprint: Image 
        Structuring element for the operation.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._closing(device, input_image, footprint, output_image)

@plugin_function(categories=["filter", "in assistant"])
def binary_closing(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies binary morphological closing to intensity images using
    a sphere or box shaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius of the sphere or box element along the x axis.
    radius_y: float (= 1)
        Radius of the sphere or box element along the y axis.
    radius_z: float (= 1)
        Radius of the sphere or box element along the z axis.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._binary_closing(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["combine", "transform", "in assistant", "bia-bob-suggestion"])
def concatenate_along_x(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Concatenate two images or stacks along the X axis.

    Parameters
    ----------
    input_image0: Image 
        First input image.
    input_image1: Image 
        Second input image.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_combineHorizontally
    """
    return clic._concatenate_along_x(device, input_image0, input_image1, output_image)

@plugin_function(categories=["combine", "transform", "in assistant", "bia-bob-suggestion"])
def concatenate_along_y(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Concatenate two images or stacks along the Y axis.

    Parameters
    ----------
    input_image0: Image 
        First input image.
    input_image1: Image 
        Second input image.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_combineVertically
    """
    return clic._concatenate_along_y(device, input_image0, input_image1, output_image)

@plugin_function(categories=["combine", "transform", "in assistant", "bia-bob-suggestion"])
def concatenate_along_z(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Concatenate two images or stacks along the Z axis.

    Parameters
    ----------
    input_image0: Image 
        First input image.
    input_image1: Image 
        Second input image.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_concatenateStacks
    """
    return clic._concatenate_along_z(device, input_image0, input_image1, output_image)

@plugin_function
def count_touching_neighbors(
    touch_matrix: Image,
    touching_neighbors_count_destination: Optional[Image] =None,
    ignore_background: bool =True,
    device: Optional[Device] =None
) -> Image:
    """Takes a touch matrix as input and delivers a vector with number of touching
    neighbors per label as a vector. Note: Background is considered as something
    that can touch. To ignore touches with background, hand over a touch matrix
    where the first column (index = 0) has been set to 0. Use set_column for that.

    Parameters
    ----------
    touch_matrix: Image 
        Input touch matrix to process.
    touching_neighbors_count_destination: Optional[Image] (= None)
        Output vector of touch count.
    ignore_background: bool (= True)
        
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_countTouchingNeighbors
    """
    return clic._count_touching_neighbors(device, touch_matrix, touching_neighbors_count_destination, ignore_background)

@plugin_function
def crop_border(
    input_image: Image,
    output_image: Optional[Image] =None,
    border_size: int =1,
    device: Optional[Device] =None
) -> Image:
    """Crops an image by removing the outer pixels, per default 1. Notes * To make sure
    the output image has the right size, provide destination_image=None.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    border_size: int (= 1)
        Border size to crop.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._crop_border(device, input_image, output_image, int(border_size))

@plugin_function(categories=["filter", "background removal", "in assistant"])
def divide_by_gaussian_background(
    input_image: Image,
    output_image: Optional[Image] =None,
    sigma_x: float =2,
    sigma_y: float =2,
    sigma_z: float =2,
    device: Optional[Device] =None
) -> Image:
    """Applies Gaussian blur to the input image and divides the original by the result.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    sigma_x: float (= 2)
        Gaussian sigma value along x.
    sigma_y: float (= 2)
        Gaussian sigma value along y.
    sigma_z: float (= 2)
        Gaussian sigma value along z.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_divideByGaussianBackground
    """
    return clic._divide_by_gaussian_background(device, input_image, output_image, float(sigma_x), float(sigma_y), float(sigma_z))

@plugin_function
def degrees_to_radians(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Converts radians to degrees.

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
    return clic._degrees_to_radians(device, input_image, output_image)

@plugin_function(categories=["binarize", "in assistant"])
def detect_maxima_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =0,
    radius_y: float =0,
    radius_z: float =0,
    device: Optional[Device] =None
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood. Pixels in the
    resulting image are set to 1 if there is no other pixel in a given radius which
    has a higher intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 0)
        Radius along the x axis.
    radius_y: float (= 0)
        Radius along the y axis.
    radius_z: float (= 0)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    """
    return clic._detect_maxima_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["binarize", "in assistant"])
def detect_maxima(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =0,
    radius_y: float =0,
    radius_z: float =0,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood. Pixels in the
    resulting image are set to 1 if there is no other pixel in a given radius which
    has a higher intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 0)
        Radius along the x axis.
    radius_y: float (= 0)
        Radius along the y axis.
    radius_z: float (= 0)
        Radius along the z axis.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    [2] https://clij.github.io/clij2-docs/reference_detectMaximaSphere
    """
    return clic._detect_maxima(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["binarize", "in assistant"])
def detect_minima_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =0,
    radius_y: float =0,
    radius_z: float =0,
    device: Optional[Device] =None
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood. Pixels in the
    resulting image are set to 1 if there is no other pixel in a given radius which
    has a lower intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 0)
        Radius along the x axis.
    radius_y: float (= 0)
        Radius along the y axis.
    radius_z: float (= 0)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectMinimaBox
    """
    return clic._detect_minima_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["binarize", "in assistant"])
def detect_minima(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =0,
    radius_y: float =0,
    radius_z: float =0,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood. Pixels in the
    resulting image are set to 1 if there is no other pixel in a given radius which
    has a lower intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 0)
        Radius along the x axis.
    radius_y: float (= 0)
        Radius along the y axis.
    radius_z: float (= 0)
        Radius along the z axis.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectMinimaBox
    [2] https://clij.github.io/clij2-docs/reference_detectMinimaSphere
    """
    return clic._detect_minima(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "background removal", "bia-bob-suggestion"])
def difference_of_gaussian(
    input_image: Image,
    output_image: Optional[Image] =None,
    sigma1_x: float =2,
    sigma1_y: float =2,
    sigma1_z: float =2,
    sigma2_x: float =2,
    sigma2_y: float =2,
    sigma2_z: float =2,
    device: Optional[Device] =None
) -> Image:
    """Applies Gaussian blur to the input image twice with different sigma values
    resulting in two images which are then subtracted from each other. It is
    recommended to apply this operation to images of type Float (32 bit) as results
    might be negative.

    Parameters
    ----------
    input_image: Image 
        The input image to be processed.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    sigma1_x: float (= 2)
        Sigma of the first Gaussian filter in x
    sigma1_y: float (= 2)
        Sigma of the first Gaussian filter in y
    sigma1_z: float (= 2)
        Sigma of the first Gaussian filter in z
    sigma2_x: float (= 2)
        Sigma of the second Gaussian filter in x
    sigma2_y: float (= 2)
        Sigma of the second Gaussian filter in y
    sigma2_z: float (= 2)
        Sigma of the second Gaussian filter in z
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_differenceOfGaussian3D
    """
    return clic._difference_of_gaussian(device, input_image, output_image, float(sigma1_x), float(sigma1_y), float(sigma1_z), float(sigma2_x), float(sigma2_y), float(sigma2_z))

@plugin_function(categories=["label processing", "in assistant"])
def extend_labeling_via_voronoi(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a label map image and dilates the regions using a octagon shape until they
    touch. The resulting label map is written to the output.

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
    [1] https://clij.github.io/clij2-docs/reference_extendLabelingViaVoronoi
    """
    return clic._extend_labeling_via_voronoi(device, input_image, output_image)

@plugin_function(categories=["filter"])
def invert(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Computes the negative value of all pixels in a given image. It is recommended to
    convert images to 32bit float before applying this operation. <pre>f(x) =
    x</pre> For binary images, use binaryNot.

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
    [1] https://clij.github.io/clij2-docs/reference_invert
    """
    return clic._invert(device, input_image, output_image)

@plugin_function(categories=["label", "in assistant"])
def label_spots(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Transforms a binary image with single pixles set to 1 to a labelled spots image.
    Transforms a spots image as resulting from maximum/minimum detection in an image
    of the same size where every spot has a number 1, 2,... n.

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
    [1] https://clij.github.io/clij2-docs/reference_labelSpots
    """
    return clic._label_spots(device, input_image, output_image)

@plugin_function(categories=["filter", "in assistant"])
def large_hessian_eigenvalue(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the Hessian eigenvalues and returns the large eigenvalue image.

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
    return clic._large_hessian_eigenvalue(device, input_image, output_image)

@plugin_function
def maximum_of_all_pixels(
    input_image: Image,
    device: Optional[Device] =None
) -> float:
    """Determines the maximum of all pixels in a given image. It will be stored in a
    new row of ImageJs Results table in the column 'Max'.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumOfAllPixels
    """
    return clic._maximum_of_all_pixels(device, input_image)

@plugin_function
def minimum_of_all_pixels(
    input_image: Image,
    device: Optional[Device] =None
) -> float:
    """Determines the minimum of all pixels in a given image. It will be stored in a
    new row of ImageJs Results table in the column 'Min'.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumOfAllPixels
    """
    return clic._minimum_of_all_pixels(device, input_image)

@plugin_function
def minimum_of_masked_pixels(
    input_image: Image,
    mask: Image,
    device: Optional[Device] =None
) -> float:
    """Determines the minimum intensity in a masked image. But only in pixels which
    have nonzero values in another mask image.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    mask: Image 
        Input
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumOfMaskedPixels
    """
    return clic._minimum_of_masked_pixels(device, input_image, mask)

@plugin_function(categories=["filter", "in assistant"])
def opening_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Opening operator, applies morphological opening to intensity images using a
    boxshaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._opening_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "in assistant"])
def opening_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Opening operator, applies morphological opening to intensity images using a
    sphereshaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._opening_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "in assistant"])
def grayscale_opening(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Opening operator, Applies morphological opening to intensity images using a
    sphereshaped or boxshepd footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._grayscale_opening(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "in assistant"])
def opening(
    input_image: Image,
    footprint: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies morphological opening to intensity images using a
    custom structuring element provided as input. This operator also works with
    binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    footprint: Image 
        Structuring element for the operation.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._opening(device, input_image, footprint, output_image)

@plugin_function(categories=["filter", "in assistant"])
def binary_opening(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Closing operator, applies binary morphological opening to intensity images using
    a sphere or box shaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius of the sphere or box element along the x axis.
    radius_y: float (= 1)
        Radius of the sphere or box element along the y axis.
    radius_z: float (= 1)
        Radius of the sphere or box element along the z axis.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._binary_opening(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function
def radians_to_degrees(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Converts radians to degrees

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
    return clic._radians_to_degrees(device, input_image, output_image)

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def reduce_labels_to_label_edges(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a label map and reduces all labels to their edges. Label IDs stay and
    background will be zero.

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
    [1] https://clij.github.io/clij2-docs/reference_reduceLabelsToLabelEdges
    """
    return clic._reduce_labels_to_label_edges(device, input_image, output_image)

@plugin_function(categories=["filter", "in assistant"])
def small_hessian_eigenvalue(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the Hessian eigenvalues and returns the small eigenvalue image.

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
    return clic._small_hessian_eigenvalue(device, input_image, output_image)

@plugin_function(categories=["filter"])
def square(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Return the elementwise square of the input. This function is supposed to be
    similar to its counterpart in numpy [1]

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
    [1] https://numpy.org/doc/stable/reference/generated/numpy.square.html
    """
    return clic._square(device, input_image, output_image)

@plugin_function(categories=["combine", "in assistant"])
def squared_difference(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the squared difference pixel by pixel between two images.

    Parameters
    ----------
    input_image0: Image 
        First input image.
    input_image1: Image 
        Second input image.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_squaredDifference
    """
    return clic._squared_difference(device, input_image0, input_image1, output_image)

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def standard_deviation_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local standard deviation of a pixels box neighborhood. The box size
    is specified by its halfwidth, halfheight and halfdepth (radius). If 2D images
    are given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationBox
    """
    return clic._standard_deviation_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def standard_deviation_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes the local standard deviation of a pixels sphere neighborhood. The box
    size is specified by its halfwidth, halfheight and halfdepth (radius). If 2D
    images are given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationSphere
    """
    return clic._standard_deviation_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "edge detection", "in assistant"])
def standard_deviation(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Computes the local standard deviation of a pixels sphere neighborhood. The box
    size is specified by its halfwidth, halfheight and halfdepth (radius). If 2D
    images are given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    radius_x: float (= 1)
        Radius along the x axis.
    radius_y: float (= 1)
        Radius along the y axis.
    radius_z: float (= 1)
        Radius along the z axis.
    connectivity: str (= "box")
        Neigborhood shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationBox
    [2] https://clij.github.io/clij2-docs/reference_standardDeviationSphere
    """
    return clic._standard_deviation(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))

@plugin_function(categories=["filter", "background removal", "in assistant", "bia-bob-suggestion"])
def subtract_gaussian_background(
    input_image: Image,
    output_image: Optional[Image] =None,
    sigma_x: float =2,
    sigma_y: float =2,
    sigma_z: float =2,
    device: Optional[Device] =None
) -> Image:
    """Applies Gaussian blur to the input image and subtracts the result from the
    original.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    sigma_x: float (= 2)
        Radius along the x axis.
    sigma_y: float (= 2)
        Radius along the y axis.
    sigma_z: float (= 2)
        Radius along the z axis.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subtractGaussianBackground
    """
    return clic._subtract_gaussian_background(device, input_image, output_image, float(sigma_x), float(sigma_y), float(sigma_z))

@plugin_function(categories=["combine", "in assistant"])
def subtract_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Subtracts one image X from another image Y pixel wise. <pre>f(x, y) = x y</pre>

    Parameters
    ----------
    input_image0: Image 
        First input image.
    input_image1: Image 
        Second input image.
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subtractImages
    """
    return clic._subtract_images(device, input_image0, input_image1, output_image)

@plugin_function(categories=["transform", "in assistant"])
def sub_stack(
    input_image: Image,
    output_image: Optional[Image] =None,
    start_z: int =0,
    end_z: int =0,
    device: Optional[Device] =None
) -> Image:
    """Crop a volume into a new volume, along the z-axis.

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Optional[Image] (= None)
        Output image.
    start_z: int (= 0)
        Start z coordinate of the crop.
    end_z: int (= 0)
        End z coordinate of the crop.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subStack
    """
    return clic._sub_stack(device, input_image, output_image, int(start_z), int(end_z))

@plugin_function(categories=["transform", "in assistant"])
def reduce_stack(
    input_image: Image,
    output_image: Optional[Image] =None,
    reduction_factor: int =2,
    offset: int =0,
    device: Optional[Device] =None
) -> Image:
    """Reduces the number of z-slices in a stack by a given factor. With the offset you
    have control which slices stays: with a factor 3 and offset 0, slices 0,3,6,
    etc. are kept. with a factor 4 and offset 1, slices 1,5,9, etc. are kept.

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Optional[Image] (= None)
        Output image.
    reduction_factor: int (= 2)
        Reduction factor.
    offset: int (= 0)
        Offset.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_reduceStack
    """
    return clic._reduce_stack(device, input_image, output_image, int(reduction_factor), int(offset))

@plugin_function
def sum_of_all_pixels(
    input_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> float:
    """Determines the sum of all pixels in a given image. It will be stored in a new
    row of ImageJs Results table in the column 'Sum'.

    Parameters
    ----------
    input_image: Optional[Image] (= None)
        Input image to process.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumOfAllPixels
    """
    return clic._sum_of_all_pixels(device, input_image)

@plugin_function(categories=["filter", "background removal", "in assistant"])
def top_hat_box(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Applies a tophat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image 
        The input image where the background is subtracted from.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    radius_x: float (= 1)
        Radius of the background determination region in X.
    radius_y: float (= 1)
        Radius of the background determination region in Y.
    radius_z: float (= 1)
        Radius of the background determination region in Z.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_topHatBox
    """
    return clic._top_hat_box(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "background removal", "in assistant", "bia-bob-suggestion"])
def top_hat_sphere(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    device: Optional[Device] =None
) -> Image:
    """Applies a tophat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image 
        The input image where the background is subtracted from.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    radius_x: float (= 1)
        Radius of the background determination region in X.
    radius_y: float (= 1)
        Radius of the background determination region in Y.
    radius_z: float (= 1)
        Radius of the background determination region in Z.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_topHatSphere
    """
    return clic._top_hat_sphere(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))

@plugin_function(categories=["filter", "background removal", "in assistant"])
def top_hat(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius_x: float =1,
    radius_y: float =1,
    radius_z: float =1,
    connectivity: str ="box",
    device: Optional[Device] =None
) -> Image:
    """Applies a tophat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image 
        The input image where the background is subtracted from.
    output_image: Optional[Image] (= None)
        The output image where results are written into.
    radius_x: float (= 1)
        Radius of the background determination region in X.
    radius_y: float (= 1)
        Radius of the background determination region in Y.
    radius_z: float (= 1)
        Radius of the background determination region in Z.
    connectivity: str (= "box")
        Element shape, "box" or "sphere"
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_topHatBox
    [2] https://clij.github.io/clij2-docs/reference_topHatSphere
    """
    return clic._top_hat(device, input_image, output_image, float(radius_x), float(radius_y), float(radius_z), str(connectivity))