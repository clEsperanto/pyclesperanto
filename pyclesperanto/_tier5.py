#
# This code is auto-generated from CLIc 'cle::tier5.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

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
    """Compares if all pixels of two images are identical. If shape of the images or
    any pixel are different, returns False. True otherwise This function is supposed
    to work similarly like its counterpart in numpy [1].

    Parameters
    ----------
    input_image0: Image 
        First array to compare
    input_image1: Image 
        Second array to compare
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
    """Combines two label images by adding labels of a given label image to another.
    Labels in the second image overwrite labels in the first passed image.
    Afterwards, labels are relabeled sequentially.

    Parameters
    ----------
    input_image0: Image 
        label image to add labels to.
    input_image1: Image 
        label image to add labels from.
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
    """Performs connected components analysis inspecting the box neighborhood of every
    pixel to a binary image and generates a label map.

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
    """Performs connected components analysis inspecting the box neighborhood of every
    pixel to a binary image and generates a label map.

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
    """Take a label map and reduce each label to its centroid.

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
    """Filter labelled objects outside of the min/max size range value.

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
    """Filter labelled objects outside of the min/max size range value.

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