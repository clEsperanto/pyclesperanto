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



@plugin_function(category=['label', 'in assistant', 'bia-bob-suggestion'])
def gauss_otsu_labeling(
    input_image0: Image,
    output_image: Image = None,
    outline_sigma: float = 0,
    device: Device = None
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
    output_image: Image = None
        Output label image.
    outline_sigma: float = 0
        Gaussian blur sigma along all axes
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://ieeexplore.ieee.org/document/4310076
	[2] https://en.wikipedia.org/wiki/Connected-component_labeling
    """

    from ._pyclesperanto import _gauss_otsu_labeling as op

    return op(
        device=device,
        src0=input_image0,
        dst=output_image,
        outline_sigma=float(outline_sigma)
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
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_maskedVoronoiLabeling
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
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_voronoiLabeling
    """

    from ._pyclesperanto import _voronoi_labeling as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )

