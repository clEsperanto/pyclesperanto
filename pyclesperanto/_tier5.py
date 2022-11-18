from ._image import Image
from ._device import Device
from ._decorators import plugin_function


@plugin_function
def masked_voronoi_labeling(
    input_image: Image,
    mask_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:
    """Takes a binary image, labels connected components and dilates the
    regions using a octagon shape until they touch. The region growing is limited to a masked area.

    The resulting label map is written to the output.

    Parameters
    ----------
    input_image : Image
    mask_image : Image
    output_image : Image, optional

    Returns
    -------
    output_image
    """
    from ._pyclesperanto import _MaskedVoronoiLabelingKernel_Call as op

    op(device, src=input_image, mask=mask_image, dst=output_image)
    return output_image
