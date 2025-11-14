#
# This code is auto-generated from CLIc 'cle::tier5.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional, List

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function(categories=["combine"])
def array_equal(
    input_image0: Image,
    input_image1: Image,
    device: Optional[Device] =None
) -> bool:
    """Compares if all pixels of two images are identical. If the shape of the images
    or any pixel are different, returns false; true otherwise. This function works
    similarly to its counterpart in NumPy.

    Parameters
    ----------
    input_image0: Image 
        First array to compare.
    input_image1: Image 
        Second array to compare.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    bool

    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
    """
    return clic._array_equal(device, input_image0, input_image1)

@plugin_function(categories=["label processing", "combine labels", "in assistant", "bia-bob-suggestion"])
def combine_labels(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Combines two label images by adding labels from one label image to another.
    Labels in the second image overwrite labels in the first image. Afterward,
    labels are relabeled sequentially.

    Parameters
    ----------
    input_image0: Image 
        Label image to add labels to.
    input_image1: Image 
        Label image to add labels from.
    output_image: Optional[Image] (= None)
        Output label image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._combine_labels(device, input_image0, input_image1, output_image)

@plugin_function(categories=["label", "in assistant"])
def connected_components_labeling(
    input_image: Image,
    output_image: Optional[Image] =None,
    connectivity: str ='box',
    device: Optional[Device] =None
) -> Image:
    """Performs connected components analysis by inspecting the neighborhood of every
    pixel in a binary image and generates a label map.

    Parameters
    ----------
    input_image: Image 
        Binary image to label.
    output_image: Optional[Image] (= None)
        Output label image.
    connectivity: str (= 'box')
        Defines pixel neighborhood relationship, "box" or "sphere".
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_connectedComponentsLabelingBox
    """
    return clic._connected_components_labeling(device, input_image, output_image, str(connectivity))

@plugin_function(categories=["label", "in assistant", "bia-bob-suggestion"])
def connected_component_labeling(
    input_image: Image,
    output_image: Optional[Image] =None,
    connectivity: str ='box',
    device: Optional[Device] =None
) -> Image:
    """Performs connected components analysis by inspecting the neighborhood of every
    pixel in a binary image and generates a label map.

    Parameters
    ----------
    input_image: Image 
        Binary image to label.
    output_image: Optional[Image] (= None)
        Output label image.
    connectivity: str (= 'box')
        Defines pixel neighborhood relationship, "box" or "sphere".
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_connectedComponentsLabelingBox
    """
    return clic._connected_component_labeling(device, input_image, output_image, str(connectivity))

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def reduce_labels_to_centroids(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a label map and reduces each label to its centroid.

    Parameters
    ----------
    input_image: Image 
        Label image to reduce.
    output_image: Optional[Image] (= None)
        Output label image with centroids.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_reduceLabelsToCentroids
    """
    return clic._reduce_labels_to_centroids(device, input_image, output_image)

@plugin_function(categories=["label processing", "in assistant"])
def filter_label_by_size(
    input_image: Image,
    output_image: Optional[Image] =None,
    minimum_size: float =0,
    maximum_size: float =100,
    device: Optional[Device] =None
) -> Image:
    """Filters labelled objects outside the min/max size range.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    minimum_size: float (= 0)
        Minimum size of labels to keep.
    maximum_size: float (= 100)
        Maximum size of labels to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._filter_label_by_size(device, input_image, output_image, float(minimum_size), float(maximum_size))

@plugin_function(categories=["label processing", "in assistant"])
def exclude_labels_outside_size_range(
    input_image: Image,
    output_image: Optional[Image] =None,
    minimum_size: float =0,
    maximum_size: float =100,
    device: Optional[Device] =None
) -> Image:
    """Filters labelled objects outside the min/max size range.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    minimum_size: float (= 0)
        Minimum size of labels to keep.
    maximum_size: float (= 100)
        Maximum size of labels to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._exclude_labels_outside_size_range(device, input_image, output_image, float(minimum_size), float(maximum_size))

@plugin_function(categories=["label processing", "in assistant"])
def merge_touching_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Merges touching labels of a label image and relabels the result sequentially.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._merge_touching_labels(device, input_image, output_image)

@plugin_function(categories=["label measurement"])
def proximal_neighbor_count(
    input_image: Image,
    output_image: Optional[Image] =None,
    min_distance: float =-1,
    max_distance: float =-1,
    device: Optional[Device] =None
) -> Image:
    """From a label map, determines which labels are whithin a given distance range of
    each other and returns the number of those in vector.

    Parameters
    ----------
    input_image: Image 
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
    """
    return clic._proximal_neighbor_count(device, input_image, output_image, float(min_distance), float(max_distance))

@plugin_function
def normalize(
    input_image: Image,
    output_image: Optional[Image] =None,
    low_percentile: float =-1,
    high_percentile: float =-1,
    device: Optional[Device] =None
) -> Image:
    """Normalizes the pixel values of an image to the range [0, 1]. This function
    normalize the pixel values between [0, 1] following the linear normalization
    formula: <pre>I_normalized = (I - I_min) * (new_max - new_min) / (I_max - I_min)
    + new_min</pre> where the I_min and I_max are determined by the low_percentile
    and high_percentile parameters, respectively. If not specified, the minimum and
    maximum pixel values of the image are used.

    Parameters
    ----------
    input_image: Image 
        Input image to normalize.
    output_image: Optional[Image] (= None)
        Output normalized image.
    low_percentile: float (= -1)
        Low percentile to determine the minimum pixel value.
    high_percentile: float (= -1)
        High percentile to determine the maximum pixel value.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._normalize(device, input_image, output_image, float(low_percentile), float(high_percentile))