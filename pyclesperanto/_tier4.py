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

clic = importlib.import_module("._pyclesperanto", package="pyclesperanto")


@plugin_function
def label_bounding_box(
    input_image: Image, label_id: int, device: Optional[Device] = None
) -> list:
    """Determines the bounding box of the specified label from a label image. The
    positions are returned in  an array of six values as follows: minX, minY, minZ,
    maxX, maxY, maxZ.

    Parameters
    ----------
    input_image: Image
        Label image.
    label_id: int
        Identifier of the label.
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
    input_image0: Image, input_image1: Image, device: Optional[Device] = None
) -> float:
    """Determines the mean squared error (MSE) between two images.

    Parameters
    ----------
    input_image0: Image
        First image to compare.
    input_image1: Image
        Second image to compare.
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
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Transforms a spots image (e.g., from maxima/minima detection) into an image
    where every column contains d entries (with d = dimensionality of the original
    image) holding the coordinates of the maxima/minima.

    Parameters
    ----------
    input_image: Image
        Input binary image of spots.
    output_image: Optional[Image] (= None)
        Output coordinate list of spots.
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
    output_image: Optional[Image] = None,
    blocksize: int = 4096,
    device: Optional[Device] = None,
) -> Image:
    """Analyzes a label map and if there are gaps in the indexing (e.g., label 5 is not
    present), all subsequent labels will be relabeled. Afterward, the number of
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
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Binarizes an image using Otsu's threshold method (Otsu et. al. 1979)

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


@plugin_function(categories=["binarize", "in assistant", "bia-bob-suggestion"])
def threshold_yen(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Binarizes an image using Yen's threshold method (Yen et. al. 1995)

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
    [1] https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_yen
    [2] https://ieeexplore.ieee.org/document/366472
    """
    return clic._threshold_yen(device, input_image, output_image)


@plugin_function(categories=["binarize", "in assistant", "bia-bob-suggestion"])
def threshold_mean(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Binarizes an image using the global average intensity in the image

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
    """
    return clic._threshold_mean(device, input_image, output_image)


@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def parametric_map(
    labels: Image,
    intensity: Optional[Image] = None,
    property: str = "label",
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes an image, a corresponding label map, and maps a specified property (e.g.,
    'mean_intensity') determined per label onto a new image where every label is
    replaced by the corresponding property value. The property name must be
    available from the statistics_labelled_pixels function.

    Parameters
    ----------
    labels: Image
        Label image.
    intensity: Optional[Image] (= None)
        Intensity image.
    property: str (= "label")
        Name of the
    output_image: Optional[Image] (= None)
        Parametric image computed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanIntensityMap
    [2] https://clij.github.io/clij2-docs/reference_pixelCountMap
    [3] https://clij.github.io/clij2-docs/reference_minimumIntensityMap
    [4] https://clij.github.io/clij2-docs/reference_maximumIntensityMap
    [5] https://clij.github.io/clij2-docs/reference_standardDeviationIntensityMap
    """
    return clic._parametric_map(device, labels, intensity, str(property), output_image)


@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def mean_intensity_map(
    input_image: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes an image and a corresponding label map, determines the mean   intensity
    per label, and replaces every label with that number. This results in a
    parametric image expressing mean object intensity.

    Parameters
    ----------
    input_image: Image
        Intensity image.
    labels: Image
        Label image.
    output_image: Optional[Image] (= None)
        Parametric image computed.
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


@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def label_mean_intensity_map(
    input_image: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes an image and a corresponding label map, determines the mean   intensity
    per label, and replaces every label with that number. This results in a
    parametric image expressing mean object intensity.

    Parameters
    ----------
    input_image: Image
        Intensity image.
    labels: Image
        Label image.
    output_image: Optional[Image] (= None)
        Parametric image computed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanIntensityMap
    """
    return clic._label_mean_intensity_map(device, input_image, labels, output_image)


@plugin_function(categories=["label measurement", "map", "in assistant"])
def pixel_count_map(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes a label map, determines the number of pixels per label, and replaces every
    label with that number. This results in a parametric image expressing area or
    volume.

    Parameters
    ----------
    input_image: Image
        Label image to measure.
    output_image: Optional[Image] (= None)
        Parametric image computed.
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
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes a label map, determines the number of pixels per label, and replaces every
    label with that number. This results in a parametric image expressing area or
    volume.

    Parameters
    ----------
    input_image: Image
        Label image to measure.
    output_image: Optional[Image] (= None)
        Parametric image computed.
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
    include_background: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """Determines the centroids of all labels in a label image or image stack. It
    writes the resulting coordinates into a point list image of dimensions n × d
    where n is the number of labels and d = 3 is the dimensionality (x, y, z) of the
    original image.

    Parameters
    ----------
    label_image: Image
        Label image from which the centroids will be determined.
    centroids_coordinates: Image
        Output list of coordinates where the centroids will be written.
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
    return clic._centroids_of_labels(
        device, label_image, centroids_coordinates, include_background
    )


@plugin_function(categories=["label processing", "combine"])
def remove_labels_with_map_values_out_of_range(
    input_image: Image,
    values: Image,
    output_image: Optional[Image] = None,
    min_value: float = 0,
    max_value: float = 100,
    device: Optional[Device] = None,
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
    return clic._remove_labels_with_map_values_out_of_range(
        device, input_image, values, output_image, float(min_value), float(max_value)
    )


@plugin_function(categories=["label processing", "combine"])
def remove_labels_with_map_values_within_range(
    input_image: Image,
    values: Image,
    output_image: Optional[Image] = None,
    min_value: float = 0,
    max_value: float = 100,
    device: Optional[Device] = None,
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
    return clic._remove_labels_with_map_values_within_range(
        device, input_image, values, output_image, float(min_value), float(max_value)
    )


@plugin_function(categories=["label processing", "combine"])
def exclude_labels_with_map_values_out_of_range(
    values_map: Image,
    label_map_input: Image,
    output_image: Optional[Image] = None,
    minimum_value_range: float = 0,
    maximum_value_range: float = 100,
    device: Optional[Device] = None,
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
    return clic._exclude_labels_with_map_values_out_of_range(
        device,
        values_map,
        label_map_input,
        output_image,
        float(minimum_value_range),
        float(maximum_value_range),
    )


@plugin_function(categories=["label processing", "combine"])
def exclude_labels_with_map_values_within_range(
    values_map: Image,
    label_map_input: Image,
    output_image: Optional[Image] = None,
    minimum_value_range: float = 0,
    maximum_value_range: float = 100,
    device: Optional[Device] = None,
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
    return clic._exclude_labels_with_map_values_within_range(
        device,
        values_map,
        label_map_input,
        output_image,
        float(minimum_value_range),
        float(maximum_value_range),
    )


@plugin_function(categories=["label processing", "in assistant", "map"])
def extension_ratio_map(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Determines the extension ratio for every label in a label map and returns it as
    a parametric map. The extension ratio is defined as the maximum distance of any
    pixel in the label to the label's centroid divided by the average distance of
    all pixels in the label to the centroid.

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


@plugin_function(categories=["label processing", "in assistant", "map"])
def mean_extension_map(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Determines, for every label, the mean distance of all pixels to the centroid in
    a label map and returns it as a parametric map.

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
    [1] https://clij.github.io/clij2-docs/reference_meanExtensionMap
    """
    return clic._mean_extension_map(device, input_image, output_image)


@plugin_function(categories=["label processing", "in assistant", "map"])
def maximum_extension_map(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Determines, for every label, the maximum distance of any pixel to the centroid
    in a label map and returns it as a parametric map.

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
    [1] https://clij.github.io/clij2-docs/reference_meanExtensionMap
    """
    return clic._maximum_extension_map(device, input_image, output_image)


@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def minimum_intensity_map(
    input_image: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes an image and a corresponding label map, determines the minimum   intensity
    per label, and replaces every label with that number. This results in a
    parametric image expressing minimum object intensity.

    Parameters
    ----------
    input_image: Image
        Intensity image.
    labels: Image
        Label image.
    output_image: Optional[Image] (= None)
        Parametric image computed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_minimumIntensityMap
    """
    return clic._minimum_intensity_map(device, input_image, labels, output_image)


@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def maximum_intensity_map(
    input_image: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes an image and a corresponding label map, determines the maximum   intensity
    per label, and replaces every label with that number. This results in a
    parametric image expressing maximum object intensity.

    Parameters
    ----------
    input_image: Image
        Intensity image.
    labels: Image
        Label image.
    output_image: Optional[Image] (= None)
        Parametric image computed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maximumIntensityMap
    """
    return clic._maximum_intensity_map(device, input_image, labels, output_image)


@plugin_function(categories=["label measurement", "map", "in assistant", "combine"])
def standard_deviation_intensity_map(
    input_image: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes an image and a corresponding label map, determines the standard deviation
    of the   intensity per label, and replaces every label with that number. This
    results in a parametric image expressing standard deviation of object intensity.

    Parameters
    ----------
    input_image: Image
        Intensity image.
    labels: Image
        Label image.
    output_image: Optional[Image] (= None)
        Parametric image computed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_standardDeviationIntensityMap
    """
    return clic._standard_deviation_intensity_map(
        device, input_image, labels, output_image
    )


@plugin_function(categories=["label processing", "in assistant", "map"])
def touching_neighbor_count_map(
    labels: Image, output_image: Optional[Image] = None, device: Optional[Device] = None
) -> Image:
    """For each label in a label map, determines how many other labels it is touching
    and creates a parametric map where each label is replaced by that number.

    Parameters
    ----------
    labels: Image
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
    [1] https://clij.github.io/clij2-docs/reference_touchingNeighborCountMap
    """
    return clic._touching_neighbor_count_map(device, labels, output_image)


@plugin_function
def percentile(
    input_image: Image, percentile: float = 50.0, device: Optional[Device] = None
) -> float:
    """Computes the percentile value of an image.

    Parameters
    ----------
    input_image: Image
        Input image.
    percentile: float (= 50.0)
        Percentile to compute.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float
    """
    return clic._percentile(device, input_image, float(percentile))


@plugin_function
def mean_of_touching_neighbors_map(
    map: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    ignore_background: bool = True,
    device: Optional[Device] = None,
) -> Image:
    """Compute the mean value of touching neighbors from a parametric map and a label
    image. Generates a new parametric map where each label is replaced by the mean
    value of its touching neighbors. The radius parameter allows considering
    neighbors of neighbors (e.g. radius 1 = direct neighbors, radius 2 = neighbors
    of neighbors, etc.).

    Parameters
    ----------
    map: Image
        Input parametric
    labels: Image
        Input vector image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    radius: int (= 1)
        Radius of touching neighbors to consider.
    ignore_background: bool (= True)
        Whether to ignore the background label.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._mean_of_touching_neighbors_map(
        device, map, labels, output_image, int(radius), ignore_background
    )


@plugin_function
def median_of_touching_neighbors_map(
    map: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    ignore_background: bool = True,
    device: Optional[Device] = None,
) -> Image:
    """Computes the median value of touching neighbors from a parametric map and a
    label image. Generates a new parametric map where each label is replaced by the
    mean value of its touching neighbors. The radius parameter allows considering
    neighbors of neighbors (e.g. radius 1 = direct neighbors, radius 2 = neighbors
    of neighbors, etc.).

    Parameters
    ----------
    map: Image
        Input parametric
    labels: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    radius: int (= 1)
        Radius of touching neighbors to consider.
    ignore_background: bool (= True)
        Whether to ignore the background label.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._median_of_touching_neighbors_map(
        device, map, labels, output_image, int(radius), ignore_background
    )


@plugin_function
def minimum_of_touching_neighbors_map(
    map: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    ignore_background: bool = True,
    device: Optional[Device] = None,
) -> Image:
    """Computes the minimum value of touching neighbors from a parametric map and a
    label image. Generates a new parametric map where each label is replaced by the
    mean value of its touching neighbors. The radius parameter allows considering
    neighbors of neighbors (e.g. radius 1 = direct neighbors, radius 2 = neighbors
    of neighbors, etc.).

    Parameters
    ----------
    map: Image
        Input parametric
    labels: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    radius: int (= 1)
        Radius of touching neighbors to consider.
    ignore_background: bool (= True)
        Whether to ignore the background label.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._minimum_of_touching_neighbors_map(
        device, map, labels, output_image, int(radius), ignore_background
    )


@plugin_function
def maximum_of_touching_neighbors_map(
    map: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    ignore_background: bool = True,
    device: Optional[Device] = None,
) -> Image:
    """Computes the maximum value of touching neighbors from a parametric map and a
    label image. Generates a new parametric map where each label is replaced by the
    mean value of its touching neighbors. The radius parameter allows considering
    neighbors of neighbors (e.g. radius 1 = direct neighbors, radius 2 = neighbors
    of neighbors, etc.).

    Parameters
    ----------
    map: Image
        Input parametric
    labels: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    radius: int (= 1)
        Radius of touching neighbors to consider.
    ignore_background: bool (= True)
        Whether to ignore the background label.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._maximum_of_touching_neighbors_map(
        device, map, labels, output_image, int(radius), ignore_background
    )


@plugin_function
def standard_deviation_of_touching_neighbors_map(
    map: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    ignore_background: bool = True,
    device: Optional[Device] = None,
) -> Image:
    """Computes the standard deviation of touching neighbors from a parametric map and
    a label image. Generates a new parametric map where each label is replaced by
    the mean value of its touching neighbors. The radius parameter allows
    considering neighbors of neighbors (e.g. radius 1 = direct neighbors, radius 2 =
    neighbors of neighbors, etc.).

    Parameters
    ----------
    map: Image
        Input parametric
    labels: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    radius: int (= 1)
        Radius of touching neighbors to consider.
    ignore_background: bool (= True)
        Whether to ignore the background label.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._standard_deviation_of_touching_neighbors_map(
        device, map, labels, output_image, int(radius), ignore_background
    )


@plugin_function
def mode_of_touching_neighbors_map(
    map: Image,
    labels: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    ignore_background: bool = True,
    device: Optional[Device] = None,
) -> Image:
    """Computes the mode value of touching neighbors from a parametric map and a label
    image. Generates a new parametric map where each label is replaced by the mean
    value of its touching neighbors. The radius parameter allows considering
    neighbors of neighbors (e.g. radius 1 = direct neighbors, radius 2 = neighbors
    of neighbors, etc.).

    Parameters
    ----------
    map: Image
        Input parametric
    labels: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    radius: int (= 1)
        Radius of touching neighbors to consider.
    ignore_background: bool (= True)
        Whether to ignore the background label.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._mode_of_touching_neighbors_map(
        device, map, labels, output_image, int(radius), ignore_background
    )


@plugin_function
def standard_deviation_of_all_pixels(
    input_image: Image, device: Optional[Device] = None
) -> float:
    """Computes the standard deviation of all pixel values in an image.

    Parameters
    ----------
    input_image: Image
        Input image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    float
    """
    return clic._standard_deviation_of_all_pixels(device, input_image)


__all__ = [
    "label_bounding_box",
    "mean_squared_error",
    "spots_to_pointlist",
    "relabel_sequential",
    "threshold_otsu",
    "threshold_yen",
    "threshold_mean",
    "parametric_map",
    "mean_intensity_map",
    "label_mean_intensity_map",
    "pixel_count_map",
    "label_pixel_count_map",
    "centroids_of_labels",
    "remove_labels_with_map_values_out_of_range",
    "remove_labels_with_map_values_within_range",
    "exclude_labels_with_map_values_out_of_range",
    "exclude_labels_with_map_values_within_range",
    "extension_ratio_map",
    "mean_extension_map",
    "maximum_extension_map",
    "minimum_intensity_map",
    "maximum_intensity_map",
    "standard_deviation_intensity_map",
    "touching_neighbor_count_map",
    "percentile",
    "mean_of_touching_neighbors_map",
    "median_of_touching_neighbors_map",
    "minimum_of_touching_neighbors_map",
    "maximum_of_touching_neighbors_map",
    "standard_deviation_of_touching_neighbors_map",
    "mode_of_touching_neighbors_map",
    "standard_deviation_of_all_pixels",
]
