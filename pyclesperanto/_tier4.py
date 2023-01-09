from ._image import Image
from ._device import Device
from ._decorators import plugin_function
from typing import Optional


@plugin_function
def connected_components_labeling_box(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Performs connected components analysis inspecting the box neighborhood
    of every pixel to a binary image and generates a label map.

    Parameters
    ----------
    input_image : Image
        Input binary image
    output_image : Image, optional
        Output label map
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_connectedComponentsLabelingBox
    """
    from ._pyclesperanto import _ConnectedComponentLabelingBoxKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def threshold_otsu(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Binarizes an image using Otsu's threshold method [1]
    using a histogram determined on the GPU to create binary images.

    Parameters
    ----------
    input_image : Image
        The input image to be binarized.
    output_image : Image, optional
        The output image where results are written into.
    device: Device, optional

    Returns
    -------
    output_image : Image

    References
    ----------
    .. [1] https://ieeexplore.ieee.org/document/4310076
    .. [2] https://clij.github.io/clij2-docs/reference_thresholdOtsu
    """
    from ._pyclesperanto import _ThresholdOtsuKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image
