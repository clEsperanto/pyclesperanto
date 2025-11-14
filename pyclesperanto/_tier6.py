#
# This code is auto-generated from CLIc 'cle::tier6.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module("._pyclesperanto", package="pyclesperanto")


@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def dilate_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    radius: int = 2,
    device: Optional[Device] = None,
) -> Image:
    """Dilates labels to a larger size. No label overwrites another label. Similar to
    the implementation in scikit-image and MorphoLibJ. Note: This operation assumes
    input images are isotropic.

    Parameters
    ----------
    input_image: Image
        Input label image to dilate.
    output_image: Optional[Image] (= None)
        Output label image.
    radius: int (= 2)
        Dilation
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._dilate_labels(device, input_image, output_image, int(radius))


@plugin_function(categories=["label processing", "in assistant"])
def erode_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    relabel: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """Erodes labels to a smaller size. Note: Depending on the label image and the
    radius, labels may disappear and labels may split into multiple islands. Thus,
    overlapping labels of input and output may not have the same identifier. This
    operation assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    radius: int (= 1)
        Erosion
    relabel: bool (= False)
        Relabel the image, e.g., if objects disappear or split.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._erode_labels(device, input_image, output_image, int(radius), relabel)


@plugin_function(categories=["label", "in assistant"])
def gauss_otsu_labeling(
    input_image0: Image,
    output_image: Optional[Image] = None,
    outline_sigma: float = 0,
    device: Optional[Device] = None,
) -> Image:
    """Labels objects directly from gray-value images.  The outline_sigma parameter
    allows tuning the segmentation result. Under the hood,  this filter applies a
    Gaussian blur, Otsu thresholding, and connected component labeling. The
    thresholded binary image is flooded using the Voronoi tessellation approach
    starting from the found local maxima.

    Parameters
    ----------
    input_image0: Image
        Intensity image to segment.
    output_image: Optional[Image] (= None)
        Output label image.
    outline_sigma: float (= 0)
        Gaussian blur sigma along all axes.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://ieeexplore.ieee.org/document/4310076
    [2] https://en.wikipedia.org/wiki/Connected-component_labeling
    """
    return clic._gauss_otsu_labeling(
        device, input_image0, output_image, float(outline_sigma)
    )


@plugin_function(categories=["label"])
def masked_voronoi_labeling(
    input_image: Image,
    mask: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes a binary image, labels connected components, and dilates the regions using
    an octagon shape until they touch. The region growing is limited to a masked
    area. The resulting label map is written to the output.

    Parameters
    ----------
    input_image: Image
        Input binary image.
    mask: Image
        Input
    output_image: Optional[Image] (= None)
        Output label image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maskedVoronoiLabeling
    """
    return clic._masked_voronoi_labeling(device, input_image, mask, output_image)


@plugin_function(categories=["label", "in assistant", "bia-bob-suggestion"])
def voronoi_labeling(
    input_binary: Image,
    output_labels: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes a binary image, labels connected components, and dilates the regions using
    an octagon shape until they touch. The resulting label map is written to the
    output.

    Parameters
    ----------
    input_binary: Image
        Input binary image.
    output_labels: Optional[Image] (= None)
        Output label image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_voronoiLabeling
    """
    return clic._voronoi_labeling(device, input_binary, output_labels)


@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def remove_small_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    minimum_size: float = 100,
    device: Optional[Device] = None,
) -> Image:
    """Removes labelled objects smaller than a given size (in pixels) from a label map.

    Parameters
    ----------
    input_image: Image
        Label image to filter.
    output_image: Optional[Image] (= None)
        Filtered output label image.
    minimum_size: float (= 100)
        Smallest size object allowed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._remove_small_labels(
        device, input_image, output_image, float(minimum_size)
    )


@plugin_function(categories=["label processing", "in assistant"])
def exclude_small_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    maximum_size: float = 100,
    device: Optional[Device] = None,
) -> Image:
    """Removes labels from a label map that are below a given maximum size.

    Parameters
    ----------
    input_image: Image
        Label image to filter.
    output_image: Optional[Image] (= None)
        Filtered output label image.
    maximum_size: float (= 100)
        Largest size object to exclude.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._exclude_small_labels(
        device, input_image, output_image, float(maximum_size)
    )


@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def remove_large_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    maximum_size: float = 100,
    device: Optional[Device] = None,
) -> Image:
    """Removes labelled objects larger than a given size (in pixels) from a label map.

    Parameters
    ----------
    input_image: Image
        Label image to filter.
    output_image: Optional[Image] (= None)
        Filtered output label image.
    maximum_size: float (= 100)
        Largest size object allowed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._remove_large_labels(
        device, input_image, output_image, float(maximum_size)
    )


@plugin_function(categories=["label processing", "in assistant"])
def exclude_large_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    minimum_size: float = 100,
    device: Optional[Device] = None,
) -> Image:
    """Removes labels from a label map that are above a given minimum size.

    Parameters
    ----------
    input_image: Image
        Label image to filter.
    output_image: Optional[Image] (= None)
        Filtered output label image.
    minimum_size: float (= 100)
        Smallest size object to exclude.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._exclude_large_labels(
        device, input_image, output_image, float(minimum_size)
    )


@plugin_function(categories=["label measurement", "map", "in assistant"])
def proximal_neighbor_count_map(
    labels: Image,
    output_image: Optional[Image] = None,
    min_distance: float = -1,
    max_distance: float = -1,
    device: Optional[Device] = None,
) -> Image:
    """From a label map, generates a map where each label is replaced by the count of
    neighboring labels within a specified distance range.

    Parameters
    ----------
    labels: Image
        Input label image.
    output_image: Optional[Image] (= None)
        Output parametric image.
    min_distance: float (= -1)
        Minimum distance to consider a neighbor.
    max_distance: float (= -1)
        Maximum distance to consider a neighbor.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_proximalNeighborCountMap
    """
    return clic._proximal_neighbor_count_map(
        device, labels, output_image, float(min_distance), float(max_distance)
    )


__all__ = [
    "dilate_labels",
    "erode_labels",
    "gauss_otsu_labeling",
    "masked_voronoi_labeling",
    "voronoi_labeling",
    "remove_small_labels",
    "exclude_small_labels",
    "remove_large_labels",
    "exclude_large_labels",
    "proximal_neighbor_count_map",
]
