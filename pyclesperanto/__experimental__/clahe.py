from typing import Optional

from pyclesperanto._array import Array, Image
from pyclesperanto._core import Device
from pyclesperanto._decorators import plugin_function
from pyclesperanto._functionalities import execute
from pyclesperanto._tier2 import maximum_of_all_pixels, minimum_of_all_pixels


@plugin_function
def clahe(
    input_image: Image,
    output_image: Optional[Image] = None,
    tile_size: int = 8,
    clip_limit: float = 0.01,
    minimum_intensity: Optional[float] = None,
    maximum_intensity: Optional[float] = None,
    device: Optional[Device] = None,
) -> Image:
    """
    Contrast Limited Adaptive Histogram Equalization (CLAHE) is a method to enhance the contrast of images by
    normalizing the intensity values in small regions of the image. This implementation is based on the OpenCL
    implementation by Hugo Raveton (https://github.com/HugoRaveton/pyopencl_clahe).

    Parameters
    ----------
    input_image : Image
        The input image to be processed.
    output_image : Image, optional
        The output image where the result will be stored. If None, a new image will be created.
    tile_size : int, optional
        The width size of each tile (cube) in pixels.
    clip_limit : float, optional
        The clipping limit for histogram equalization (in ratio, e.g. 0.01).
    min_intensity : float, optional
        The minimum intensity value.
    max_intensity : float, optional
        The maximum intensity value.
    device : Device, optional
        The device on which to run the kernel.

    Returns
    -------
    Image
        The processed image.
    """

    input_image = Array.to_device(input_image)
    output_image = Array.empty_like(input_image)
    minimum_intensity = (
        minimum_of_all_pixels(input_image)
        if minimum_intensity is None
        else minimum_intensity
    )
    maximum_intensity = (
        maximum_of_all_pixels(input_image)
        if maximum_intensity is None
        else maximum_intensity
    )
    clip_limit = clip_limit * 255  # top 1% of the histogram for an 8-bit image

    # Execute the OpenCL kernel
    params = {
        "src": input_image,
        "dst": output_image,
        "tileSize": tile_size,
        "clipLimit": clip_limit,
        "minIntensity": minimum_intensity,
        "maxIntensity": maximum_intensity,
    }
    execute(
        anchor=__file__,
        kernel_source="clahe.cl",
        kernel_name="clahe",
        device=device,
        global_size=input_image.shape,
        parameters=params,
    )
    return output_image
