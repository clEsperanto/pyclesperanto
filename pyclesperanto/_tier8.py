#
# This code is auto-generated from CLIc 'cle::tier8.hpp' file, do not edit manually.
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
def smooth_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Apply a morphological opening operation to a label image and afterwards   fills
    gaps between the labels using voronoi-labeling. Finally, the result   label
    image is masked so that all background pixels remain background pixels.   Note:
    It is recommended to process isotropic label images.

    Parameters
    ----------
    input_image: Image 
        Input label image
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 0)
        Smoothing
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._smooth_labels(device, input_image, output_image, int(radius))

@plugin_function(categories=["label processing", "in assistant", "bia-bob-suggestion"])
def smooth_connected_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Apply a morphological erosion and dilation of the label image with respect to
    the connectivity of the labels.   Note: It is recommended to process isotropic
    label images.

    Parameters
    ----------
    input_image: Image 
        Input label image
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 0)
        Smoothing
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._smooth_connected_labels(device, input_image, output_image, int(radius))