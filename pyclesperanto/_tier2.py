#
# This code is auto-generated from 'tier2.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function(category=['combine', 'in assistant', 'bia-bob-suggestion'])
def absolute_difference(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the absolute difference pixel by pixel between two images. <pre>f(x,
    y) = |x y| </pre>

    Parameters
    ----------
    input_image0: Image
        The input image to be subtracted from.
    input_image1: Image
        The input image which is subtracted.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_absoluteDifference
    """

    from ._pyclesperanto import _absolute_difference as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['combine', 'in assistant'])
def add_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Calculates the sum of pairs of pixels x and y of two images X and Y. <pre>f(x,
    y) = x + y</pre>

    Parameters
    ----------
    input_image0: Image
        The first input image to added.
    input_image1: Image
        The second image to be added.
    output_image: Image = None
        The output image where results are written into.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_addImages
    """

    from ._pyclesperanto import _add_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'background removal', 'in assistant'])
def bottom_hat_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Apply a bottomhat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image
        The input image where the background is subtracted from.
    output_image: Image = None
        The output image where results are written into.
    radius_x: int = 1
        Radius of the background determination region in X.
    radius_y: int = 1
        Radius of the background determination region in Y.
    radius_z: int = 1
        Radius of the background determination region in Z.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_bottomHatBox
    """

    from ._pyclesperanto import _bottom_hat_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'background removal', 'in assistant', 'bia-bob-suggestion'])
def bottom_hat_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 1,
    radius_y: float = 1,
    radius_z: float = 1,
    device: Device = None
) -> Image:
    """Applies a bottomhat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image
        The input image where the background is subtracted from.
    output_image: Image = None
        The output image where results are written into.
    radius_x: float = 1
        Radius of the background determination region in X.
    radius_y: float = 1
        Radius of the background determination region in Y.
    radius_z: float = 1
        Radius of the background determination region in Z.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_bottomHatSphere
    """

    from ._pyclesperanto import _bottom_hat_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z)
    )



@plugin_function(category=['combine', 'in assistant'])
def clip(
    input_image: Image,
    output_image: Image = None,
    min_intensity: float = None,
    max_intensity: float = None,
    device: Device = None
) -> Image:
    """Limits the range of values in an image. This function is supposed to work
    similarly as its counter part in numpy [1].

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    min_intensity: float = None
        new, lower limit of the intensity range
    max_intensity: float = None
        new, upper limit of the intensity range
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.clip.html
    """

    from ._pyclesperanto import _clip as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        min_intensity=float(min_intensity),
        max_intensity=float(max_intensity)
    )



@plugin_function(category=['filter', 'in assistant'])
def closing_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None
) -> Image:
    """Closing operator, boxshaped Applies morphological closing to intensity images
    using a boxshaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 0
        Radius along the x axis.
    radius_y: int = 0
        Radius along the y axis.
    radius_z: int = 0
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _closing_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'in assistant', 'bia-bob-suggestion'])
def closing_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 0,
    device: Device = None
) -> Image:
    """Closing operator, sphereshaped Applies morphological closing to intensity images
    using a sphereshaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius along the x axis.
    radius_y: int = 1
        Radius along the y axis.
    radius_z: int = 0
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _closing_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['combine', 'transform', 'in assistant', 'bia-bob-suggestion'])
def concatenate_along_x(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Concatenate two images or stacks along the X axis.

    Parameters
    ----------
    input_image0: Image
        First input image.
    input_image1: Image
        Second input image.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_combineHorizontally
    """

    from ._pyclesperanto import _concatenate_along_x as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['combine', 'transform', 'in assistant', 'bia-bob-suggestion'])
def concatenate_along_y(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Concatenate two images or stacks along the Y axis.

    Parameters
    ----------
    input_image0: Image
        First input image.
    input_image1: Image
        Second input image.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_combineVertically
    """

    from ._pyclesperanto import _concatenate_along_y as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['combine', 'transform', 'in assistant', 'bia-bob-suggestion'])
def concatenate_along_z(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Concatenate two images or stacks along the Z axis.

    Parameters
    ----------
    input_image0: Image
        First input image.
    input_image1: Image
        Second input image.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_concatenateStacks
    """

    from ._pyclesperanto import _concatenate_along_z as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['bia-bob-suggestion'])
def count_touching_neighbors(
    input_image: Image,
    output_image: Image = None,
    ignore_background: bool = True,
    device: Device = None
) -> Image:
    """Takes a touch matrix as input and delivers a vector with number of touching
    neighbors per label as a vector. Note: Background is considered as something
    that can touch. To ignore touches with background, hand over a touch matrix
    where the first column (index = 0) has been set to 0. Use set_column for that.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    ignore_background: bool = True
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_countTouchingNeighbors
    """

    from ._pyclesperanto import _count_touching_neighbors as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        ignore_background=bool(ignore_background)
    )



@plugin_function
def crop_border(
    input_image: Image,
    output_image: Image = None,
    border_size: int = 1,
    device: Device = None
) -> Image:
    """Crops an image by removing the outer pixels, per default 1. Notes * To make sure
    the output image has the right size, provide destination_image=None.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    border_size: int = 1
        Border size to crop.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _crop_border as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        border_size=int(border_size)
    )



@plugin_function(category=['filter', 'background removal', 'in assistant', 'bia-bob-suggestion'])
def divide_by_gaussian_background(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 2,
    sigma_y: float = 2,
    sigma_z: float = 2,
    device: Device = None
) -> Image:
    """Applies Gaussian blur to the input image and divides the original by the result.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    sigma_x: float = 2
        Gaussian sigma value along x.
    sigma_y: float = 2
        Gaussian sigma value along y.
    sigma_z: float = 2
        Gaussian sigma value along z.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_divideByGaussianBackground
    """

    from ._pyclesperanto import _divide_by_gaussian_background as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        sigma_x=float(sigma_x),
        sigma_y=float(sigma_y),
        sigma_z=float(sigma_z)
    )



@plugin_function
def degrees_to_radians(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Converts radians to degrees.

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

    from ._pyclesperanto import _degrees_to_radians as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['binarize', 'in assistant'])
def detect_maxima_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood. Pixels in the
    resulting image are set to 1 if there is no other pixel in a given radius which
    has a higher intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 0
        Radius along the x axis.
    radius_y: int = 0
        Radius along the y axis.
    radius_z: int = 0
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    """

    from ._pyclesperanto import _detect_maxima_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['binarize', 'in assistant'])
def detect_minima_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None
) -> Image:
    """Detects local maxima in a given square/cubic neighborhood. Pixels in the
    resulting image are set to 1 if there is no other pixel in a given radius which
    has a lower intensity, and to 0 otherwise.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 0
        Radius along the x axis.
    radius_y: int = 0
        Radius along the y axis.
    radius_z: int = 0
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_detectMaximaBox
    """

    from ._pyclesperanto import _detect_minima_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'background removal', 'bia-bob-suggestion'])
def difference_of_gaussian(
    input_image: Image,
    output_image: Image = None,
    sigma1_x: float = 2,
    sigma1_y: float = 2,
    sigma1_z: float = 2,
    sigma2_x: float = 2,
    sigma2_y: float = 2,
    sigma2_z: float = 2,
    device: Device = None
) -> Image:
    """Applies Gaussian blur to the input image twice with different sigma values
    resulting in two images which are then subtracted from each other. It is
    recommended to apply this operation to images of type Float (32 bit) as results
    might be negative.

    Parameters
    ----------
    input_image: Image
        The input image to be processed.
    output_image: Image = None
        The output image where results are written into.
    sigma1_x: float = 2
        Sigma of the first Gaussian filter in x
    sigma1_y: float = 2
        Sigma of the first Gaussian filter in y
    sigma1_z: float = 2
        Sigma of the first Gaussian filter in z
    sigma2_x: float = 2
        Sigma of the second Gaussian filter in x
    sigma2_y: float = 2
        Sigma of the second Gaussian filter in y
    sigma2_z: float = 2
        Sigma of the second Gaussian filter in z
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_differenceOfGaussian3D
    """

    from ._pyclesperanto import _difference_of_gaussian as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        sigma1_x=float(sigma1_x),
        sigma1_y=float(sigma1_y),
        sigma1_z=float(sigma1_z),
        sigma2_x=float(sigma2_x),
        sigma2_y=float(sigma2_y),
        sigma2_z=float(sigma2_z)
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def extend_labeling_via_voronoi(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes a label map image and dilates the regions using a octagon shape until they
    touch. The resulting label map is written to the output.

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
    [1] https://clij.github.io/clij2-docs/reference_extendLabelingViaVoronoi
    """

    from ._pyclesperanto import _extend_labeling_via_voronoi as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter'])
def invert(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Computes the negative value of all pixels in a given image. It is recommended to
    convert images to 32bit float before applying this operation. <pre>f(x) =
    x</pre> For binary images, use binaryNot.

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
    [1] https://clij.github.io/clij2-docs/reference_invert
    """

    from ._pyclesperanto import _invert as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['label', 'in assistant', 'bia-bob-suggestion'])
def label_spots(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Transforms a binary image with single pixles set to 1 to a labelled spots image.
    Transforms a spots image as resulting from maximum/minimum detection in an image
    of the same size where every spot has a number 1, 2,... n.

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
    [1] https://clij.github.io/clij2-docs/reference_labelSpots
    """

    from ._pyclesperanto import _label_spots as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def large_hessian_eigenvalue(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the Hessian eigenvalues and returns the large eigenvalue image.

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

    from ._pyclesperanto import _large_hessian_eigenvalue as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def maximum_of_all_pixels(
    input_image: Image,
    device: Device = None
) -> float:
    """Determines the maximum of all pixels in a given image. It will be stored in a
    new row of ImageJs Results table in the column 'Max'.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumOfAllPixels
    """

    from ._pyclesperanto import _maximum_of_all_pixels as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def minimum_of_all_pixels(
    input_image: Image,
    device: Device = None
) -> float:
    """Determines the minimum of all pixels in a given image. It will be stored in a
    new row of ImageJs Results table in the column 'Min'.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumOfAllPixels
    """

    from ._pyclesperanto import _minimum_of_all_pixels as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def minimum_of_masked_pixels(
    input_image: Image,
    mask: Image,
    device: Device = None
) -> float:
    """Determines the minimum intensity in a masked image. But only in pixels which
    have nonzero values in another mask image.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    mask: Image
        Input
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumOfMaskedPixels
    """

    from ._pyclesperanto import _minimum_of_masked_pixels as op

    return op(
        device=device,
        src=input_image,
        mask=mask
    )



@plugin_function(category=['filter', 'in assistant'])
def opening_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 0,
    radius_y: int = 0,
    radius_z: int = 0,
    device: Device = None
) -> Image:
    """Opening operator, boxshaped Applies morphological opening to intensity images
    using a boxshaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 0
        Radius along the x axis.
    radius_y: int = 0
        Radius along the y axis.
    radius_z: int = 0
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _opening_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'in assistant', 'bia-bob-suggestion'])
def opening_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 1,
    radius_y: float = 1,
    radius_z: float = 0,
    device: Device = None
) -> Image:
    """Opening operator, sphereshaped Applies morphological opening to intensity images
    using a sphereshaped footprint. This operator also works with binary images.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: float = 1
        Radius along the x axis.
    radius_y: float = 1
        Radius along the y axis.
    radius_z: float = 0
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _opening_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z)
    )



@plugin_function
def radians_to_degrees(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Converts radians to degrees

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

    from ._pyclesperanto import _radians_to_degrees as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def reduce_labels_to_label_edges(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes a label map and reduces all labels to their edges. Label IDs stay and
    background will be zero.

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
    [1] https://clij.github.io/clij2-docs/reference_reduceLabelsToLabelEdges
    """

    from ._pyclesperanto import _reduce_labels_to_label_edges as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def small_hessian_eigenvalue(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the Hessian eigenvalues and returns the small eigenvalue image.

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

    from ._pyclesperanto import _small_hessian_eigenvalue as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter'])
def square(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Return the elementwise square of the input. This function is supposed to be
    similar to its counterpart in numpy [1]

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
    [1] https://numpy.org/doc/stable/reference/generated/numpy.square.html
    """

    from ._pyclesperanto import _square as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['combine', 'in assistant', 'bia-bob-suggestion'])
def squared_difference(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Determines the squared difference pixel by pixel between two images.

    Parameters
    ----------
    input_image0: Image
        First input image.
    input_image1: Image
        Second input image.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_squaredDifference
    """

    from ._pyclesperanto import _squared_difference as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant'])
def standard_deviation_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local standard deviation of a pixels box neighborhood. The box size
    is specified by its halfwidth, halfheight and halfdepth (radius). If 2D images
    are given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius along the x axis.
    radius_y: int = 1
        Radius along the y axis.
    radius_z: int = 1
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationBox
    """

    from ._pyclesperanto import _standard_deviation_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'edge detection', 'in assistant', 'bia-bob-suggestion'])
def standard_deviation_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Computes the local standard deviation of a pixels sphere neighborhood. The box
    size is specified by its halfwidth, halfheight and halfdepth (radius). If 2D
    images are given, radius_z will be ignored.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    radius_x: int = 1
        Radius along the x axis.
    radius_y: int = 1
        Radius along the y axis.
    radius_z: int = 1
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationSphere
    """

    from ._pyclesperanto import _standard_deviation_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'background removal', 'in assistant', 'bia-bob-suggestion'])
def subtract_gaussian_background(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 2,
    sigma_y: float = 2,
    sigma_z: float = 2,
    device: Device = None
) -> Image:
    """Applies Gaussian blur to the input image and subtracts the result from the
    original.

    Parameters
    ----------
    input_image: Image
        Input image to process.
    output_image: Image = None
        Output result image.
    sigma_x: float = 2
        Radius along the x axis.
    sigma_y: float = 2
        Radius along the y axis.
    sigma_z: float = 2
        Radius along the z axis.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subtractGaussianBackground
    """

    from ._pyclesperanto import _subtract_gaussian_background as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        sigma_x=float(sigma_x),
        sigma_y=float(sigma_y),
        sigma_z=float(sigma_z)
    )



@plugin_function(category=['combine', 'in assistant'])
def subtract_images(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Subtracts one image X from another image Y pixel wise. <pre>f(x, y) = x y</pre>

    Parameters
    ----------
    input_image0: Image
        First input image.
    input_image1: Image
        Second input image.
    output_image: Image = None
        Output result image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_subtractImages
    """

    from ._pyclesperanto import _subtract_images as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function
def sum_of_all_pixels(
    input_image: Image = None,
    device: Device = None
) -> float:
    """Determines the sum of all pixels in a given image. It will be stored in a new
    row of ImageJs Results table in the column 'Sum'.

    Parameters
    ----------
    input_image: Image = None
        Input image to process.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_sumOfAllPixels
    """

    from ._pyclesperanto import _sum_of_all_pixels as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function(category=['filter', 'background removal', 'in assistant'])
def top_hat_box(
    input_image: Image,
    output_image: Image = None,
    radius_x: int = 1,
    radius_y: int = 1,
    radius_z: int = 1,
    device: Device = None
) -> Image:
    """Applies a tophat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image
        The input image where the background is subtracted from.
    output_image: Image = None
        The output image where results are written into.
    radius_x: int = 1
        Radius of the background determination region in X.
    radius_y: int = 1
        Radius of the background determination region in Y.
    radius_z: int = 1
        Radius of the background determination region in Z.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_topHatBox
    """

    from ._pyclesperanto import _top_hat_box as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=int(radius_x),
        radius_y=int(radius_y),
        radius_z=int(radius_z)
    )



@plugin_function(category=['filter', 'background removal', 'in assistant', 'bia-bob-suggestion'])
def top_hat_sphere(
    input_image: Image,
    output_image: Image = None,
    radius_x: float = 1,
    radius_y: float = 1,
    radius_z: float = 1,
    device: Device = None
) -> Image:
    """Applies a tophat filter for background subtraction to the input image.

    Parameters
    ----------
    input_image: Image
        The input image where the background is subtracted from.
    output_image: Image = None
        The output image where results are written into.
    radius_x: float = 1
        Radius of the background determination region in X.
    radius_y: float = 1
        Radius of the background determination region in Y.
    radius_z: float = 1
        Radius of the background determination region in Z.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_topHatSphere
    """

    from ._pyclesperanto import _top_hat_sphere as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius_x=float(radius_x),
        radius_y=float(radius_y),
        radius_z=float(radius_z)
    )

