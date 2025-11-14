#
# This code is auto-generated from CLIc 'cle::tier3.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function
def bounding_box(
    input_image: Image,
    device: Optional[Device] =None
) -> list:
    """Determines the bounding box of all non-zero pixels in a binary image. The
    positions are returned in  an array of six values as follows: minX, minY, minZ,
    maxX, maxY, maxZ.

    Parameters
    ----------
    input_image: Image 
        Input binary image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    list

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_boundingBox
    """
    return clic._bounding_box(device, input_image)

@plugin_function
def center_of_mass(
    input_image: Image,
    device: Optional[Device] =None
) -> list:
    """Determines the center of mass of an image or image stack. The result is written
    to the Results table in the columns MassX, MassY, and MassZ.

    Parameters
    ----------
    input_image: Image 
        Input image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    list

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_centerOfMass
    """
    return clic._center_of_mass(device, input_image)

@plugin_function
def clahe(
    input_image: Image,
    output_image: Optional[Image] =None,
    tile_size: int =8,
    clip_limit: float =0.01,
    minimum_intensity: float =float('nan'),
    maximum_intensity: float =float('nan'),
    device: Optional[Device] =None
) -> Image:
    """Applies CLAHE (Contrast Limited Adaptive Histogram Equalization) to the input
    image. The algorithm is adapted from the work of Hugo Raveton
    (https://github.com/HugoRaveton/pyopencl_clahe).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    tile_size: int (= 8)
        Size of the tiles used for CLAHE.
    clip_limit: float (= 0.01)
        Clip limit for CLAHE.
    minimum_intensity: float (= float('nan'))
        Minimum intensity value.
    maximum_intensity: float (= float('nan'))
        Maximum intensity value.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._clahe(device, input_image, output_image, int(tile_size), float(clip_limit), float(minimum_intensity), float(maximum_intensity))

@plugin_function
def remove_labels(
    input_image: Image,
    list: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Removes labels from a label map and renumbers the remaining labels. Provide a
    binary flag vector starting with a flag for the background, followed by label 1,
    label 2, … For example, if you pass 0, 1, 0, 0, 1: labels 1 and 4 will be
    removed (those with a 1 in the vector will be excluded). Labels 2 and 3 will be
    kept and renumbered to 1 and 2.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    list: Image 
        Vector of 0/1 flags indicating labels to remove.
    output_image: Optional[Image] (= None)
        Output label image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabels
    """
    return clic._remove_labels(device, input_image, list, output_image)

@plugin_function
def exclude_labels(
    input_image: Image,
    list: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Removes labels from a label map and renumbers the remaining labels. Provide a
    binary flag vector starting with a flag for the background, followed by label 1,
    label 2, … For example, if you pass 0, 1, 0, 0, 1: labels 1 and 4 will be
    removed (those with a 1 in the vector will be excluded). Labels 2 and 3 will be
    kept and renumbered to 1 and 2.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    list: Image 
        Vector of 0/1 flags indicating labels to remove.
    output_image: Optional[Image] (= None)
        Output label image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabels
    """
    return clic._exclude_labels(device, input_image, list, output_image)

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def remove_labels_on_edges(
    input_image: Image,
    output_image: Optional[Image] =None,
    exclude_x: bool =True,
    exclude_y: bool =True,
    exclude_z: bool =True,
    device: Optional[Device] =None
) -> Image:
    """Removes all labels from a label map that touch the edges of the image. Remaining
    label elements are renumbered afterwards.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    exclude_x: bool (= True)
        Exclude labels touching the min and max x boundaries.
    exclude_y: bool (= True)
        Exclude labels touching the min and max y boundaries.
    exclude_z: bool (= True)
        Exclude labels touching the min and max z boundaries.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOnEdges
    """
    return clic._remove_labels_on_edges(device, input_image, output_image, exclude_x, exclude_y, exclude_z)

@plugin_function(categories=["label processing", "in assistant"])
def exclude_labels_on_edges(
    input_image: Image,
    output_image: Optional[Image] =None,
    exclude_x: bool =True,
    exclude_y: bool =True,
    exclude_z: bool =True,
    device: Optional[Device] =None
) -> Image:
    """Removes all labels from a label map that touch the edges of the image. Remaining
    label elements are renumbered afterwards.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    exclude_x: bool (= True)
        Exclude labels touching the min and max x boundaries.
    exclude_y: bool (= True)
        Exclude labels touching the min and max y boundaries.
    exclude_z: bool (= True)
        Exclude labels touching the min and max z boundaries.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOnEdges
    """
    return clic._exclude_labels_on_edges(device, input_image, output_image, exclude_x, exclude_y, exclude_z)

@plugin_function
def flag_existing_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Given a label map, generates a binary vector whose entries are 1 if a label with
    the given x-coordinate exists. For example, a label image such as: ```0 1 3 5```
    will produce a flag_vector like: ```1 1 0 1 0 1```.

    Parameters
    ----------
    input_image: Image 
        Label image.
    output_image: Optional[Image] (= None)
        Binary vector; if provided, it should have size 1×n with n = maximum label + 1.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._flag_existing_labels(device, input_image, output_image)

@plugin_function(categories=["filter", "in assistant"])
def gamma_correction(
    input_image: Image,
    output_image: Optional[Image] =None,
    gamma: float =1,
    device: Optional[Device] =None
) -> Image:
    """Applies gamma correction to an image. All pixels x of the image X are
    normalized, raised to the power gamma g, and then de-normalized. Here, ^ denotes
    exponentiation: <pre>f(x) = (x / max(X))^gamma × max(X)</pre>

    Parameters
    ----------
    input_image: Image 
        Input image.
    output_image: Optional[Image] (= None)
        Output image.
    gamma: float (= 1)
        
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gammaCorrection
    """
    return clic._gamma_correction(device, input_image, output_image, float(gamma))

@plugin_function
def generate_binary_overlap_matrix(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes two label maps with n and m labels and generates an (n+1)×(m+1) matrix
    where all pixels are set to 0 except those where labels overlap between the
    label maps. For example, if label 3 in labelmap1 and label 4 in labelmap2 are
    touching, then the pixel (3, 4) in the matrix will be set to 1.

    Parameters
    ----------
    input_image0: Image 
        First input label image.
    input_image1: Image 
        Second input label image.
    output_image: Optional[Image] (= None)
        Output overlap matrix.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_generateBinaryOverlapMatrix
    """
    return clic._generate_binary_overlap_matrix(device, input_image0, input_image1, output_image)

@plugin_function
def generate_touch_matrix(
    input_image: Image,
    output_image_matrix: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a label map with n labels and generates an (n+1)×(n+1) matrix where all
    pixels are set to 0 except those where labels are touching. Only half of the
    matrix is filled (for x < y). For example, if labels 3 and 4 are touching, then
    the pixel (3, 4) in the matrix will be set to 1. The touch matrix is a
    representation of a region adjacency graph.

    Parameters
    ----------
    input_image: Image 
        Input label image
    output_image_matrix: Optional[Image] (= None)
        Output touch matrix
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_generateTouchMatrix
    """
    return clic._generate_touch_matrix(device, input_image, output_image_matrix)

@plugin_function
def histogram(
    input_image: Image,
    output_image: Optional[Image] =None,
    num_bins: int =256,
    minimum_intensity: float =float('nan'),
    maximum_intensity: float =float('nan'),
    device: Optional[Device] =None
) -> Image:
    """Determines the histogram of a given image. The histogram image has dimensions
    number_of_bins × 1 × 1 (a 3D image with height = 1 and depth = 1). Histogram
    bins contain the number of pixels with intensity in the corresponding bin. The
    bins are uniformly distributed between the given minimum and maximum gray-value
    intensities. If the flag determine_min_max is set, the minimum and maximum
    intensities will be determined. When calling this operation many times, it is
    recommended to determine minimum and maximum intensities once at the beginning
    and pass these values. Author(s): Robert Haase; adapted work from Aaftab Munshi,
    Benedict Gaster, Timothy Mattson, James Fung, Dan Ginsburg License: adapted code
    from
    https://github.com/bgaster/openclbooksamples/blob/master/src/Chapter_14/histogram/histogram_image.cl
    It was published under the BSD license according to
    https://code.google.com/archive/p/openclbooksamples/ Book: OpenCL(R) Programming
    Guide Authors: Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan
    Ginsburg ISBN10: 0321749642 ISBN13: 9780321749642 Publisher: AddisonWesley
    Professional URLs: http://safari.informit.com/9780132488006/
    http://www.openclprogrammingguide.com

    Parameters
    ----------
    input_image: Image 
        Input image from which to derive the histogram.
    output_image: Optional[Image] (= None)
        Output histogram.
    num_bins: int (= 256)
        Number of bins.
    minimum_intensity: float (= float('nan'))
        Minimum intensity.
    maximum_intensity: float (= float('nan'))
        Maximum intensity.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_histogram
    """
    return clic._histogram(device, input_image, output_image, int(num_bins), float(minimum_intensity), float(maximum_intensity))

@plugin_function
def jaccard_index(
    input_image0: Image,
    input_image1: Image,
    device: Optional[Device] =None
) -> float:
    """Determines the overlap of two binary images using the Jaccard index. A value of
    0 suggests no overlap, 1 means perfect overlap. The resulting Jaccard index is
    saved to the Results table in the 'Jaccard_Index' column. Note that the
    Sørensen–Dice coefficient can be calculated from the Jaccard index j using this
    formula: <pre>s = f(j) = 2 j / (j + 1)</pre>

    Parameters
    ----------
    input_image0: Image 
        First binary image to compare.
    input_image1: Image 
        Second binary image to compare.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_jaccardIndex
    """
    return clic._jaccard_index(device, input_image0, input_image1)

@plugin_function
def labelled_spots_to_pointlist(
    label: Image,
    dspointlistt: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Generates a coordinate list of points in a labelled spot image. Transforms a
    label map of spots (single pixels with values 1, 2, …, n for n spots), e.g. from
    connected components analysis, into an image where every column contains d
    entries (with d = dimensionality of the original image) holding the coordinates
    of maxima/minima.

    Parameters
    ----------
    label: Image 
        Input
    dspointlistt: Optional[Image] (= None)
        Output coordinate list.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_labelledSpotsToPointList
    """
    return clic._labelled_spots_to_pointlist(device, label, dspointlistt)

@plugin_function
def maximum_position(
    input_image: Image,
    device: Optional[Device] =None
) -> list:
    """Determines the position of the maximum of all pixels in a given image.

    Parameters
    ----------
    input_image: Image 
        The image of which the position of the maximum of all pixels will be determined.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    list
    """
    return clic._maximum_position(device, input_image)

@plugin_function
def mean_of_all_pixels(
    input_image: Image,
    device: Optional[Device] =None
) -> float:
    """Determines the mean of all pixels in a given image.

    Parameters
    ----------
    input_image: Image 
        The image of which the mean of all pixels will be determined.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanOfAllPixels
    """
    return clic._mean_of_all_pixels(device, input_image)

@plugin_function
def minimum_position(
    input_image: Image,
    device: Optional[Device] =None
) -> list:
    """Determines the position of the minimum of all pixels in a given image.

    Parameters
    ----------
    input_image: Image 
        The image of which the position of the minimum of all pixels will be determined.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    list
    """
    return clic._minimum_position(device, input_image)

@plugin_function
def morphological_chan_vese(
    input_image: Image,
    output_image: Optional[Image] =None,
    num_iter: int =100,
    smoothing: int =1,
    lambda1: float =1,
    lambda2: float =1,
    device: Optional[Device] =None
) -> Image:
    """Computes an active contour model using the Chan–Vese morphological algorithm.
    The output image (dst) should also be the initialization of the contour. If not
    provided (nullptr), the function uses a checkerboard pattern initialization.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output contour; can also be used to provide initialization.
    num_iter: int (= 100)
        Number of iterations.
    smoothing: int (= 1)
        Number of
    lambda1: float (= 1)
        Lambda1.
    lambda2: float (= 1)
        Lambda2.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._morphological_chan_vese(device, input_image, output_image, int(num_iter), int(smoothing), float(lambda1), float(lambda2))

@plugin_function
def statistics_of_labelled_pixels(
    intensity: Optional[Image] =None,
    label: Optional[Image] =None,
    device: Optional[Device] =None
) -> dict:
    """Computes the bounding box, area (in pixels/voxels), minimum intensity, maximum
    intensity, average intensity, standard deviation of the intensity, and shape
    descriptors of labelled objects in a label image and its corresponding intensity
    image. If not provided, the intensity image defaults to the label image. If not
    provided, the label image defaults to a single label covering the entire image.

    Parameters
    ----------
    intensity: Optional[Image] (= None)
        Intensity image.
    label: Optional[Image] (= None)
        Label image to compute the statistics.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    dict

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels
    """
    return clic._statistics_of_labelled_pixels(device, intensity, label)

@plugin_function
def statistics_of_background_and_labelled_pixels(
    intensity: Optional[Image] =None,
    label: Optional[Image] =None,
    device: Optional[Device] =None
) -> dict:
    """Computes, for the background and labels, the bounding box, area (in
    pixels/voxels), minimum intensity, maximum intensity, average intensity,
    standard deviation of the intensity, and shape descriptors of labelled objects
    in a label image and its corresponding intensity image. If not provided, the
    intensity image defaults to the label image. If not provided, the label image
    defaults to a single label covering the entire image.

    Parameters
    ----------
    intensity: Optional[Image] (= None)
        Intensity image.
    label: Optional[Image] (= None)
        Label image to compute the statistics.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    dict

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_statisticsOfBackgroundAndLabelledPixels
    """
    return clic._statistics_of_background_and_labelled_pixels(device, intensity, label)

@plugin_function(categories=["filter", "in assistant"])
def sato_filter(
    input_image: Image,
    output_image: Optional[Image] =None,
    sigma_minimum: float =1,
    sigma_maximum: float =3,
    sigma_step: float =1,
    device: Optional[Device] =None
) -> Image:
    """Applies the multi-scale ridge detection Sato filter. This filter is based on
    Sato et al., 1998 (https://doi.org/10.1016/S1361-8415(98)80009-1). The filter
    accumulates the maximum response over the range [sigma_minimum, sigma_maximum).

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    sigma_minimum: float (= 1)
        Minimum sigma value for the filter.
    sigma_maximum: float (= 3)
        Maximum sigma value for the filter.
    sigma_step: float (= 1)
        Step size for the sigma values.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://doi.org/10.1016/S1361-8415(98)80009-1
    """
    return clic._sato_filter(device, input_image, output_image, float(sigma_minimum), float(sigma_maximum), float(sigma_step))

@plugin_function(categories=["filter", "in assistant"])
def tubeness(
    input_image: Image,
    output_image: Optional[Image] =None,
    sigma: float =1,
    device: Optional[Device] =None
) -> Image:
    """Enhances filamentous structures of a specified thickness in 2D or 3D. This
    function is a reimplementation of the Tubeness filter from Fiji/ImageJ. It is
    based on the Sato filter (https://doi.org/10.1016/S1361-8415(98)80009-1). The
    sigma parameter defines the thickness of the structures to be enhanced.

    Parameters
    ----------
    input_image: Image 
        Input image to process.
    output_image: Optional[Image] (= None)
        Output result image.
    sigma: float (= 1)
        Standard deviation of the Gaussian kernel used in the filter.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://imagej.net/plugins/tubeness
    [2] https://doi.org/10.1016/S1361-8415(98)80009-1
    """
    return clic._tubeness(device, input_image, output_image, float(sigma))

@plugin_function
def artificial_tissue(
    width: int =256,
    height: int =256,
    depth: int =1,
    delta_x: float =1.0,
    delta_y: float =1.0,
    delta_z: float =1.0,
    sigma_x: float =1.0,
    sigma_y: float =1.0,
    sigma_z: float =1.0,
    device: Optional[Device] =None
) -> Image:
    """Generates 2D or 3D artificial tissue-like image by generating a regular grid
    point and introducing Gaussian noise.

    Parameters
    ----------
    width: int (= 256)
        Width of the generated image.
    height: int (= 256)
        Height of the generated image.
    depth: int (= 1)
        Depth of the generated image.
    delta_x: float (= 1.0)
        Spacing between pixels in x.
    delta_y: float (= 1.0)
        Spacing between pixels in y.
    delta_z: float (= 1.0)
        Spacing between pixels in z.
    sigma_x: float (= 1.0)
        Standard deviation of the Gaussian noise in x.
    sigma_y: float (= 1.0)
        Standard deviation of the Gaussian noise in y.
    sigma_z: float (= 1.0)
        Standard deviation of the Gaussian noise in z.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._artificial_tissue(device, int(width), int(height), int(depth), float(delta_x), float(delta_y), float(delta_z), float(sigma_x), float(sigma_y), float(sigma_z))

@plugin_function
def read_intensities_from_map(
    label: Image,
    map: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Reads values from a parametric map using its corresponding labels and return it
    as a vector of values.

    Parameters
    ----------
    label: Image 
        Input
    map: Image 
        Input
    output_image: Optional[Image] (= None)
        Output result image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._read_intensities_from_map(device, label, map, output_image)

__all__ = ["bounding_box", "center_of_mass", "clahe", "remove_labels", "exclude_labels", "remove_labels_on_edges", "exclude_labels_on_edges", "flag_existing_labels", "gamma_correction", "generate_binary_overlap_matrix", "generate_touch_matrix", "histogram", "jaccard_index", "labelled_spots_to_pointlist", "maximum_position", "mean_of_all_pixels", "minimum_position", "morphological_chan_vese", "statistics_of_labelled_pixels", "statistics_of_background_and_labelled_pixels", "sato_filter", "tubeness", "artificial_tissue", "read_intensities_from_map"]