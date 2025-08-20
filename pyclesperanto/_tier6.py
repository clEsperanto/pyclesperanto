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

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def dilate_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =2,
    device: Optional[Device] =None
) -> Image:
    """Dilates labels to a larger size. No label overwrites another label. Similar to
    the implementation in scikitimage [2] and MorpholibJ[3] Notes * This operation
    assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image 
        Input label image to erode
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 2)
        
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
    output_image: Optional[Image] =None,
    radius: int =1,
    relabel: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Erodes labels to a smaller size. Note: Depending on the label image and the
    radius, labels may disappear and labels may split into multiple islands. Thus,
    overlapping labels of input and output may not have the same identifier. Notes *
    This operation assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image 
        Input label image
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 1)
        
    relabel: bool (= False)
        Relabel the image, e.g. if object disappear or split.
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
    output_image: Optional[Image] =None,
    outline_sigma: float =0,
    device: Optional[Device] =None
) -> Image:
    """Labels objects directly from grey-value images.  The outline_sigma parameter
    allows tuning the segmentation result. Under the hood,  this filter applies a
    Gaussian blur, Otsu-thresholding [1] and connected component labeling [2]. The
    thresholded binary image is flooded using the Voronoi tesselation approach
    starting from the found local maxima.

    Parameters
    ----------
    input_image0: Image 
        Intensity image to segment
    output_image: Optional[Image] (= None)
        Output label image.
    outline_sigma: float (= 0)
        Gaussian blur sigma along all axes
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
    return clic._gauss_otsu_labeling(device, input_image0, output_image, float(outline_sigma))

@plugin_function(categories=["label"])
def masked_voronoi_labeling(
    input_image: Image,
    mask: Image,
    output_image: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a binary image, labels connected components and dilates the regions using
    a octagon shape until they touch. The region growing is limited to a masked
    area. The resulting label map is written to the output.

    Parameters
    ----------
    input_image: Image 
        Input binary image
    mask: Image 
        Input
    output_image: Optional[Image] (= None)
        Output label image
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
    output_labels: Optional[Image] =None,
    device: Optional[Device] =None
) -> Image:
    """Takes a binary image, labels connected components and dilates the regions using
    a octagon shape until they touch. The resulting label map is written to the
    output.

    Parameters
    ----------
    input_binary: Image 
        Input binary image
    output_labels: Optional[Image] (= None)
        Output label image
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
    output_image: Optional[Image] =None,
    minimum_size: float =100,
    device: Optional[Device] =None
) -> Image:
    """Removes labelled objects small than a given size (in pixels) from a label map.

    Parameters
    ----------
    input_image: Image 
        Label image to filter.
    output_image: Optional[Image] (= None)
        Output label image filtered.
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
    return clic._remove_small_labels(device, input_image, output_image, float(minimum_size))

@plugin_function(categories=["label processing", "in assistant"])
def exclude_small_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    maximum_size: float =100,
    device: Optional[Device] =None
) -> Image:
    """Removes labels from a label map which are below a given maximum size.

    Parameters
    ----------
    input_image: Image 
        Label image to filter.
    output_image: Optional[Image] (= None)
        Output label image filtered.
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
    return clic._exclude_small_labels(device, input_image, output_image, float(maximum_size))

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def remove_large_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    maximum_size: float =100,
    device: Optional[Device] =None
) -> Image:
    """Removes labeled objects bigger than a given size (in pixels) from a label map.

    Parameters
    ----------
    input_image: Image 
        Label image to filter.
    output_image: Optional[Image] (= None)
        Output label image filtered.
    maximum_size: float (= 100)
        Biggest size object allowed.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._remove_large_labels(device, input_image, output_image, float(maximum_size))

@plugin_function(categories=["label processing", "in assistant"])
def exclude_large_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    minimum_size: float =100,
    device: Optional[Device] =None
) -> Image:
    """Removes labels from a label map which are higher a given minimum size.

    Parameters
    ----------
    input_image: Image 
        Label image to filter.
    output_image: Optional[Image] (= None)
        Output label image filtered.
    minimum_size: float (= 100)
        Smallest size object to keep.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOutsideSizeRange
    """
    return clic._exclude_large_labels(device, input_image, output_image, float(minimum_size))