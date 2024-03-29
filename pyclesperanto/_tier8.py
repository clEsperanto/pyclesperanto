#
# This code is auto-generated from 'tier8.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def smooth_labels(
    input_image: Image,
    output_image: Image = None,
    radius: int = 0,
    device: Device = None
) -> Image:
    """Apply a morphological opening operation to a label image and afterwards   fills
    gaps between the labels using voronoi-labeling. Finally, the result   label
    image is masked so that all background pixels remain background pixels.   Note:
    It is recommended to process isotropic label images.

    Parameters
    ----------
    input_image: Image
        Input label image
    output_image: Image = None
        Output label image
    radius: int = 0
        Smoothing
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _smooth_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius=int(radius)
    )



@plugin_function
def smooth_connected_labels(
    input_image: Image,
    output_image: Image = None,
    radius: int = 0,
    device: Device = None
) -> Image:
    """Apply a morphological erosion and dilation of the label image with respect to
    the connectivity of the labels.   Note: It is recommended to process isotropic
    label images.

    Parameters
    ----------
    input_image: Image
        Input label image
    output_image: Image = None
        Output label image
    radius: int = 0
        Smoothing
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _smooth_connected_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius=int(radius)
    )

