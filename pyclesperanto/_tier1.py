from ._image import Image
from ._device import Device
from ._decorators import plugin_function


@plugin_function
def absolute(
    input_image: Image, output_image: Image = None, device: Device = None
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

    op(device, input_image, output_image)
    return output_image


@plugin_function
def gaussian_blur(
    input_image: Image,
    output_image: Image = None,
    sigma_x: float = 0,
    sigma_y: float = 0,
    sigma_z: float = 0,
    device: Device = None,
) -> Image:

    from ._pyclesperanto import _GaussianBlurKernel_Call as op

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
    device: Device = None,
) -> Image:

    from ._pyclesperanto import _MaximumZProjectionKernel_Call as op

    op(device, input_image, output_image)
    return output_image


@plugin_function
def maximum_y_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:

    from ._pyclesperanto import _MaximumYProjectionKernel_Call as op

    op(device, input_image, output_image)
    return output_image


@plugin_function
def maximum_x_projection(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:

    from ._pyclesperanto import _MaximumXProjectionKernel_Call as op

    op(device, input_image, output_image)
    return output_image
