#
# This code is auto-generated from 'tier4.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function
def label_bounding_box(
    input_image: Image,
    label_id: int,
    device: Device = None
) -> list:
    """Determines the bounding box of the specified label from a label image. The
    positions are returned in  an array of 6 values as follows: minX, minY, minZ,
    maxX, maxY, maxZ.

    Parameters
    ----------
    input_image: Image
    label_id: int
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    list
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_boundingBox
    """

    from ._pyclesperanto import _label_bounding_box as op

    return op(
        device=device,
        src=input_image,
        label_id=int(label_id)
    )



@plugin_function(category=['in assistant', 'combine', 'bia-bob-suggestion'])
def mean_squared_error(
    input_image0: Image,
    input_image1: Image,
    device: Device = None
) -> float:
    """Determines the mean squared error (MSE) between two images. The MSE will be
    stored in a new row of ImageJs Results table in the column 'MSE'.

    Parameters
    ----------
    input_image0: Image
    input_image1: Image
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanSquaredError
    """

    from ._pyclesperanto import _mean_squared_error as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1
    )



@plugin_function
def spots_to_pointlist(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Transforms a spots image as resulting from maximum/minimum detection in an image
    where every column contains d pixels (with d = dimensionality of the original
    image) with the coordinates of the maxima/minima.

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
    [1] https://clij.github.io/clij2-docs/reference_spotsToPointList
    """

    from ._pyclesperanto import _spots_to_pointlist as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def relabel_sequential(
    input_image: Image,
    output_image: Image = None,
    blocksize: int = 4096,
    device: Device = None
) -> Image:
    """Analyses a label map and if there are gaps in the indexing (e.g. label 5 is not
    present) all subsequent labels will be relabelled. Thus, afterwards number of
    labels and maximum label index are equal. This operation is mostly performed on
    the CPU.

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    blocksize: int = 4096
        Renumbering is done in blocks for performance reasons.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_closeIndexGapsInLabelMap
    """

    from ._pyclesperanto import _relabel_sequential as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        blocksize=int(blocksize)
    )



@plugin_function(category=['binarize', 'in assistant', 'bia-bob-suggestion'])
def threshold_otsu(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Binarizes an image using Otsu's threshold method [3] implemented in
    scikit-image[2] using a histogram determined on the GPU to create binary images.

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
    [1] https://clij.github.io/clij2-docs/reference_thresholdOtsu
	[2] https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu
	[3] https://ieeexplore.ieee.org/document/4310076
    """

    from ._pyclesperanto import _threshold_otsu as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )

