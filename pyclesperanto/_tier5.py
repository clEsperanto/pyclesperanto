#
# This code is auto-generated from 'tier5.hpp' file, using 'gencle' script.
# Do not edit manually.
#

import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function


@plugin_function(category=["combine"])
def array_equal(
    input_image0: Image, input_image1: Image, device: Optional[Device] = None
) -> bool:
    """Compares if all pixels of two images are identical. If shape of the images or
    any pixel are different, returns False. True otherwise This function is supposed
    to work similarly like its counterpart in numpy [1].

    Parameters
    ----------
    input_image0: Image
    input_image1: Image
    device: Optional[Device] = None
        Device to perform the operation on.

    Returns
    -------
    bool

    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
    """

    from ._pyclesperanto import _array_equal as op

    return op(device=device, src0=input_image0, src1=input_image1)


@plugin_function(
    category=[
        "label processing",
        "combine labels",
        "in assistant",
        "bia-bob-suggestion",
    ]
)
def combine_labels(
    input_image0: Image,
    input_image1: Image,
    output_image: Optional[Image] = None,
    device: Optional[Device] = None,
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
    output_image: Optional[Image] = None
        Output label image.
    device: Optional[Device] = None
        Device to perform the operation on.

    Returns
    -------
    Image

    """

    from ._pyclesperanto import _combine_labels as op

    return op(device=device, src0=input_image0, src1=input_image1, dst=output_image)


@plugin_function(category=["label", "in assistant", "bia-bob-suggestion"])
def connected_components_labeling(
    input_image: Image,
    output_image: Optional[Image] = None,
    connectivity: str = "box",
    device: Optional[Device] = None,
) -> Image:
    """Performs connected components analysis inspecting the box neighborhood of every
    pixel to a binary image and generates a label map.

    Parameters
    ----------
    input_image: Image
        Binary image to label.
    output_image: Optional[Image] = None
        Output label image.
    connectivity: str = 'box'
        Defines pixel neighborhood relationship, "box" or "sphere".
    device: Optional[Device] = None
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_connectedComponentsLabelingBox
    """

    from ._pyclesperanto import _connected_components_labeling as op

    return op(
        device=device, src=input_image, dst=output_image, connectivity=connectivity
    )
