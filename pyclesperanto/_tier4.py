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
    positions are returned in  an array of 6 values as follows: minX, minY, minZ,
    maxX, maxY, maxZ.

    Parameters
    ----------
    input_image: Image

    label_id: int

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


@plugin_function(category=["in assistant", "combine", "bia-bob-suggestion"])
def mean_squared_error(
    input_image0: Image, input_image1: Image, device: Optional[Device] = None
) -> float:
    """Determines the mean squared error (MSE) between two images. The MSE will be
    stored in a new row of ImageJs Results table in the column 'MSE'.

    Parameters
    ----------
    input_image0: Image

    input_image1: Image

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
    """Transforms a spots image as resulting from maximum/minimum detection in an image
    where every column contains d pixels (with d = dimensionality of the original
    image) with the coordinates of the maxima/minima.

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
    [1] https://clij.github.io/clij2-docs/reference_spotsToPointList
    """

    return clic._spots_to_pointlist(device, input_image, output_image)


@plugin_function(category=["label processing", "in assistant", "bia-bob-suggestion"])
def relabel_sequential(
    input_image: Image,
    output_image: Optional[Image] = None,
    blocksize: int = 4096,
    device: Optional[Device] = None,
) -> Image:
    """Analyses a label map and if there are gaps in the indexing (e.g. label 5 is not
    present) all subsequent labels will be relabelled. Thus, afterwards number of
    labels and maximum label index are equal. This operation is mostly performed on
    the CPU.

    Parameters
    ----------
    input_image: Image

    output_image: Optional[Image] (= None)

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


@plugin_function(category=["binarize", "in assistant", "bia-bob-suggestion"])
def threshold_otsu(
    input_image: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
) -> Image:
    """Binarizes an image using Otsu's threshold method [3] implemented in
    scikit-image[2] using a histogram determined on the GPU to create binary images.

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
    [1] https://clij.github.io/clij2-docs/reference_thresholdOtsu
    [2] https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu
    [3] https://ieeexplore.ieee.org/document/4310076
    """

    return clic._threshold_otsu(device, input_image, output_image)
