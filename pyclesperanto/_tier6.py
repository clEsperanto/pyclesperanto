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


@plugin_function(category=["label processing", "in assistant", "bia-bob-suggestion"])
def dilate_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    radius: int = 2,
    device: Optional[Device] = None,
) -> Image:
    """Dilates labels to a larger size. No label overwrites another label. Similar to
    the implementation in scikitimage [2] and MorpholibJ[3] Notes * This operation
    assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image
        label image to erode
    output_image: Optional[Image] (= None)
        result
    radius: int (= 2)

    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """

    return clic._dilate_labels(device, input_image, output_image, int(radius))


@plugin_function(category=["label processing", "in assistant"])
def erode_labels(
    input_image: Image,
    output_image: Optional[Image] = None,
    radius: int = 1,
    relabel: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """Erodes labels to a smaller size. Note: Depending on the label image and the
    radius, labels may disappear and labels may split into multiple islands. Thus,
    overlapping labels of input and output may not have the same identifier. Notes *
    This operation assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image
        result
    output_image: Optional[Image] (= None)

    radius: int (= 1)

    relabel: bool (= False)
        and all label indices exist.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """

    return clic._erode_labels(device, input_image, output_image, int(radius), relabel)


@plugin_function(category=["label", "in assistant", "bia-bob-suggestion"])
def gauss_otsu_labeling(
    input_image0: Image,
    output_image: Optional[Image] = None,
    outline_sigma: float = 0,
    device: Optional[Device] = None,
) -> Image:
    """Labels objects directly from grey-value images.  The outline_sigma parameter
    allows tuning the segmentation result. Under the hood,  this filter applies a
    Gaussian blur, Otsu-thresholding [1] and connected component labeling [2]. The
    thresholded binary image is flooded using the Voronoi tesselation approach
    starting from the found local maxima.

    Parameters
    ----------
    input_image0: Image
        intensity image to add labels
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

    return clic._gauss_otsu_labeling(
        device, input_image0, output_image, float(outline_sigma)
    )


@plugin_function(category=["label", "bia-bob-suggestion"])
def masked_voronoi_labeling(
    input_image: Image,
    mask: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes a binary image, labels connected components and dilates the regions using
    a octagon shape until they touch. The region growing is limited to a masked
    area. The resulting label map is written to the output.

    Parameters
    ----------
    input_image: Image

    mask: Image

    output_image: Optional[Image] (= None)

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


@plugin_function(category=["label", "in assistant", "bia-bob-suggestion"])
def voronoi_labeling(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Takes a binary image, labels connected components and dilates the regions using
    a octagon shape until they touch. The resulting label map is written to the
    output.

    Parameters
    ----------
    input_image: Image

    output_image: Optional[Image] (= None)

    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_voronoiLabeling
    """

    return clic._voronoi_labeling(device, input_image, output_image)
