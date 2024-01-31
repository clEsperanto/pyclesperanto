#
# This code is auto-generated from 'tier6.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def dilate_labels(
    input_image: Image,
    output_image: Image = None,
    radius: int = 2,
    device: Device = None
) -> Image:
    """Dilates labels to a larger size. No label overwrites another label. Similar to
    the implementation in scikitimage [2] and MorpholibJ[3] Notes * This operation
    assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image
        label image to erode
    output_image: Image = None
        result
    radius: int = 2
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _dilate_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius=int(radius)
    )



@plugin_function(category=['label processing', 'in assistant'])
def erode_labels(
    input_image: Image,
    output_image: Image = None,
    radius: int = 1,
    relabel: bool = False,
    device: Device = None
) -> Image:
    """Erodes labels to a smaller size. Note: Depending on the label image and the
    radius, labels may disappear and labels may split into multiple islands. Thus,
    overlapping labels of input and output may not have the same identifier. Notes *
    This operation assumes input images are isotropic.

    Parameters
    ----------
    input_image: Image
        result
    output_image: Image = None
    radius: int = 1
    relabel: bool = False
        and all label indices exist.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _erode_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius=int(radius),
        relabel=bool(relabel)
    )



@plugin_function(category=['label', 'bia-bob-suggestion'])
def masked_voronoi_labeling(
    input_image: Image,
    mask: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes a binary image, labels connected components and dilates the regions using
    a octagon shape until they touch. The region growing is limited to a masked
    area. The resulting label map is written to the output.

    Parameters
    ----------
    input_image: Image
    mask: Image
    output_image: Image = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    Links
    -----
    [1] https://clij.github.io/clij2docs/reference_maskedVoronoiLabeling
    """

    from ._pyclesperanto import _masked_voronoi_labeling as op

    return op(
        device=device,
        src=input_image,
        mask=mask,
        dst=output_image
    )



@plugin_function(category=['label', 'in assistant', 'bia-bob-suggestion'])
def voronoi_labeling(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes a binary image, labels connected components and dilates the regions using
    a octagon shape until they touch. The resulting label map is written to the
    output.

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    Links
    -----
    [1] https://clij.github.io/clij2docs/reference_voronoiLabeling
    """

    from ._pyclesperanto import _voronoi_labeling as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )

