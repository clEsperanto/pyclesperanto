#
# This code is auto-generated from 'tier5.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function(category=['combine'])
def array_equal(
    input_image0: Image,
    input_image1: Image,
    device: Device = None
) -> bool:
    """Compares if all pixels of two images are identical. If shape of the images or
    any pixel are different, returns False. True otherwise This function is supposed
    to work similarly like its counterpart in numpy [1].

    Parameters
    ----------
    input_image0: Image
    input_image1: Image
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    bool
    
    References
    ----------
    [1] https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html
    """

    from ._pyclesperanto import _array_equal as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1
    )



@plugin_function(category=['label processing', 'combine labels', 'in assistant', 'bia-bob-suggestion'])
def combine_labels(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
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
    output_image: Image = None
        Output label image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _combine_labels as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['label', 'in assistant', 'bia-bob-suggestion'])
def connected_components_labeling(
    input_image: Image,
    output_image: Image = None,
    connectivity: str = 'box',
    device: Device = None
) -> Image:
    """Performs connected components analysis inspecting the box neighborhood of every
    pixel to a binary image and generates a label map.

    Parameters
    ----------
    input_image: Image
        Binary image to label.
    output_image: Image = None
        Output label image.
    connectivity: str = 'box'
        Defines pixel neighborhood relationship.
    device: Device = None
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
        device=device,
        src=input_image,
        dst=output_image,
        connectivity=connectivity
    )

