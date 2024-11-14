#
# This code is auto-generated from CLIc 'cle::tier4.hpp' file, do not edit manually.
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
def label_bounding_box(
    input_image: Image,
    label_id: int,
    device: Optional[Device] =None
) -> list:
    """Determines the bounding box of the specified label from a label image. The
    positions are returned in  an array of 6 values as follows: minX, minY, minZ,
    maxX, maxY, maxZ.

    Parameters
    ----------
    input_image: Image 
        Label image
    label_id: int 
        Identifier of label
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    list

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_boundingBox
    """
    return clic._label_bounding_box(device, input_image, int(label_id))

@plugin_function(categories=["in assistant", "combine", "bia-bob-suggestion"])
def mean_squared_error(
    input_image0: Image,
    input_image1: Image,
    device: Optional[Device] =None
) -> float:
    """Determines the mean squared error (MSE) between two images. The MSE will be
    stored in a new row of ImageJs Results table in the column 'MSE'.

    Parameters
    ----------
    input_image0: Image 
        First image to compare
    input_image1: Image 
        Second image to compare
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanSquaredError
    """
    return clic._mean_squared_error(device, input_image0, input_image1)

@plugin_function
def spots_to_pointlist(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Transforms a spots image as resulting from maximum/minimum detection in an image
    where every column contains d pixels (with d = dimensionality of the original
    image) with the coordinates of the maxima/minima.

    Parameters
    ----------
    input_image: Image 
        Input binary image of spots
    output_image: Optional[Image] (= None)
        Output coordinate list of spots
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_spotsToPointList
    """
    return clic._spots_to_pointlist(device, input_image, output_image)

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def relabel_sequential(
    input_image: Image,
    output_image: Optional[Image] =None,
    blocksize: int =4096,
    device: Optional[Device] =None
) -> Image:
    """Analyses a label map and if there are gaps in the indexing (e.g. label 5 is not
    present) all subsequent labels will be relabelled. Thus, afterwards number of
    labels and maximum label index are equal. This operation is mostly performed on
    the CPU.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    blocksize: int (= 4096)
        Renumbering is done in blocks for performance reasons.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_closeIndexGapsInLabelMap
    """
    return clic._relabel_sequential(device, input_image, output_image, int(blocksize))

@plugin_function(categories=["binarize", "in assistant", "bia-bob-suggestion"])
def threshold_otsu(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Binarizes an image using Otsu's threshold method [3] implemented in
    scikit-image[2] using a histogram determined on the GPU to create binary images.

    Parameters
    ----------
    input_image: Image 
        Input image to threshold.
    output_image: Optional[Image] (= None)
        Output binary image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_thresholdOtsu
    [2] https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu
    [3] https://ieeexplore.ieee.org/document/4310076
    """
    return clic._threshold_otsu(device, input_image, output_image)

@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def mean_intensity_map(
    input_image: Image,
    labels: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes an image and a corresponding label map, determines the mean   intensity
    per label and replaces every label with the that number. This results in a
    parametric image expressing mean object intensity.

    Parameters
    ----------
    input_image: Image 
        intensity image
    labels: Image 
        label image
    output_image: Optional[Image] (= None)
        Parametric image computed
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanIntensityMap
    """
    return clic._mean_intensity_map(device, input_image, labels, output_image)

@plugin_function(categories=["label measurement", "map", "in assistant"])
def pixel_count_map(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a label map, determines the number of pixels per label and replaces every
    label with the that number. This results in a parametric image expressing area
    or volume.

    Parameters
    ----------
    input_image: Image 
        Label image to measure
    output_image: Optional[Image] (= None)
        Parametric image computed
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_pixelCountMap
    """
    return clic._pixel_count_map(device, input_image, output_image)

@plugin_function(categories=["label measurement", "map", "in assistant"])
def label_pixel_count_map(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a label map, determines the number of pixels per label and replaces every
    label with the that number. This results in a parametric image expressing area
    or volume.

    Parameters
    ----------
    input_image: Image 
        Label image to measure
    output_image: Optional[Image] (= None)
        Parametric image computed
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_pixelCountMap
    """
    return clic._label_pixel_count_map(device, input_image, output_image)

@plugin_function
def centroids_of_labels(
    label_image: Image,
    centroids_coordinates: Image,
    include_background: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Determines the centroids of all labels in a label image or image stack. It
    writes the resulting coordinates in point list image of dimensions n * d where n
    is the number of labels and d=3 the dimensionality (x,y,z) of the original
    image.

    Parameters
    ----------
    label_image: Image 
        Label image where the centroids will be determined from.
    centroids_coordinates: Image 
        Output list of coordinates where the centroids will be written to.
    include_background: bool (= False)
        Determines if the background label should be included.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_centroidsOfLabels
    """
    return clic._centroids_of_labels(device, label_image, centroids_coordinates, include_background)

@plugin_function(categories=["label processing", "combine"])
def remove_labels_with_map_values_out_of_range(
    input_image: Image,
    values: Image,
    output_image: Optional[Image] =None,
    min_value: float =0,
    max_value: float =100,
    device: Optional[Device] =None
) -> Image:
    """Remove labels with values outside a given value range based on a vector of
    values associated with the labels.

    Parameters
    ----------
    input_image: Image 
        Input image where labels will be filtered.
    values: Image 
        Vector of
    output_image: Optional[Image] (= None)
        Output image where labels will be written to.
    min_value: float (= 0)
        Minimum value to keep.
    max_value: float (= 100)
        Maximum value to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesOutOfRange
    """
    return clic._remove_labels_with_map_values_out_of_range(device, input_image, values, output_image, float(min_value), float(max_value))

@plugin_function(categories=["label processing", "combine"])
def remove_labels_with_map_values_within_range(
    input_image: Image,
    values: Image,
    output_image: Optional[Image] =None,
    min_value: float =0,
    max_value: float =100,
    device: Optional[Device] =None
) -> Image:
    """Remove labels with values inside a given value range based on a vector of values
    associated with the labels.

    Parameters
    ----------
    input_image: Image 
        Input image where labels will be filtered.
    values: Image 
        Vector of
    output_image: Optional[Image] (= None)
        Output image where labels will be written to.
    min_value: float (= 0)
        Minimum value to keep.
    max_value: float (= 100)
        Maximum value to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesWithinRange
    """
    return clic._remove_labels_with_map_values_within_range(device, input_image, values, output_image, float(min_value), float(max_value))

@plugin_function(categories=["label processing", "combine"])
def exclude_labels_with_map_values_out_of_range(
    values_map: Image,
    label_map_input: Image,
    output_image: Optional[Image] =None,
    minimum_value_range: float =0,
    maximum_value_range: float =100,
    device: Optional[Device] =None
) -> Image:
    """Exclude labels with values outside a given value range based on a vector of
    values associated with the labels.

    Parameters
    ----------
    values_map: Image 
        Vector of values associated with the labels.
    label_map_input: Image 
        Input image where labels will be filtered.
    output_image: Optional[Image] (= None)
        Output image where labels will be written to.
    minimum_value_range: float (= 0)
        Minimum value to keep.
    maximum_value_range: float (= 100)
        Maximum value to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesOutOfRange
    """
    return clic._exclude_labels_with_map_values_out_of_range(device, values_map, label_map_input, output_image, float(minimum_value_range), float(maximum_value_range))

@plugin_function(categories=["label processing", "combine"])
def exclude_labels_with_map_values_within_range(
    values_map: Image,
    label_map_input: Image,
    output_image: Optional[Image] =None,
    minimum_value_range: float =0,
    maximum_value_range: float =100,
    device: Optional[Device] =None
) -> Image:
    """Exclude labels with values inside a given value range based on a vector of
    values associated with the labels.

    Parameters
    ----------
    values_map: Image 
        Vector of values associated with the labels.
    label_map_input: Image 
        Input image where labels will be filtered.
    output_image: Optional[Image] (= None)
        Output image where labels will be written to.
    minimum_value_range: float (= 0)
        Minimum value to keep.
    maximum_value_range: float (= 100)
        Maximum value to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsWithValuesWithinRange
    """
    return clic._exclude_labels_with_map_values_within_range(device, values_map, label_map_input, output_image, float(minimum_value_range), float(maximum_value_range))

@plugin_function(categories=["label processing", "in assistant", "map"])
def extension_ratio_map(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Determines the ratio of the extension for every label in a label map and returns
    it as a parametric map. The extension ration is defined as the maximum distance
    of any pixel in the label to the label's centroid divided by the average
    distance of all pixels in the label to the centroid.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_extensionRatioMap
    """
    return clic._extension_ratio_map(device, input_image, output_image)