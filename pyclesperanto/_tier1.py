from ._image import Image
from ._device import cleDevice, get_device
from ._decorators import plugin_function

@plugin_function
def absolute(input_image: Image, output_image: Image = None, device: cleDevice =None) -> Image:
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

