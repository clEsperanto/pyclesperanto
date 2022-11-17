from ._image import Image
from ._device import cleDevice, get_device
from ._decorators import plugin_function


@plugin_function
def absolute(
    input_image: Image, output_image: Image = None, device: cleDevice = None
) -> Image:
    """absolute

    f(x) = |g(x)|

    Parameters
    ----------
    input_image : Image
    output_image : Image, optional

    Returns
    -------
    Image
    """
    from ._pyclesperanto import _AbsoluteKernel_Call as op

    if device is None:
        device = get_device()

    op(device, input_image, output_image)
    return output_image


@plugin_function
def gaussian_blur(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 0,
    sigma_y: float = 0,
    sigma_z: float = 0,
    device: cleDevice = None,
) -> Image:

    from ._pyclesperanto import _GaussianBlurKernel_Call as op

    if device is None:
        device = get_device()

    op(
        device,
        input_image,
        output_image,
        float(sigma_x),
        float(sigma_y),
        float(sigma_z),
    )
    return output_image


@plugin_function
def maximum_z_projection(
    input_image: Image,
    output_image: Image = None,
    device: cleDevice = None,
) -> Image:

    from ._pyclesperanto import _MaximumZProjectionKernel_Call as op

    if device is None:
        device = get_device()

    op(device, input_image, output_image)
    return output_image


@plugin_function
def maximum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: cleDevice = None,
) -> Image:

    from ._pyclesperanto import _MaximumYProjectionKernel_Call as op

    if device is None:
        device = get_device()

    op(device, input_image, output_image)
    return output_image


@plugin_function
def threshold_otsu(
    input_image: Image,
    output_image: Image = None,
    device: cleDevice = None,
) -> Image:

    from ._pyclesperanto import _ThresholdOtsuKernel_Call as op

    if device is None:
        device = get_device()

    op(device, input_image, output_image)
    return output_image


@plugin_function
def connect_component_labeling_box(
    input_image: Image,
    output_image: Image = None,
    device: cleDevice = None,
) -> Image:

    from ._pyclesperanto import _ConnectedComponentLabelingBoxKernel_Call as op

    if device is None:
        device = get_device()

    op(device, input_image, output_image)
    return output_image
