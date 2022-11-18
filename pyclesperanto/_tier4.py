from ._image import Image
from ._device import Device
from ._decorators import plugin_function


@plugin_function
def connected_components_labeling_box(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Performs connected components analysis inspecting the box neighborhood
    of every pixel to a binary image and generates a label map.

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _ConnectedComponentLabelingBoxKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image


@plugin_function
def threshold_otsu(
    input_image: Image, output_image: Image = None, device: Device = None
) -> Image:
    """Binarizes an image using Otsu's threshold method [1]
    using a histogram determined on the GPU to create binary images.

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional

    Returns
    -------
    output_image

    References
    ----------
    .. [1] https://ieeexplore.ieee.org/document/4310076
    """
    from ._pyclesperanto import _ThresholdOtsuKernel_Call as op

    op(device, src=input_image, dst=output_image)
    return output_image
