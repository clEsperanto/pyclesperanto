from ._image import Image
from ._device import Device
from ._decorators import plugin_function
from ._memory_operations import create


@plugin_function
def histogram(input_image: Image, bins: int = 255, device: Device = None) -> Image:
    output_image = create((bins))
    from ._pyclesperanto import _HistogramKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
        bins=int(bins),
        min_intensity=None,
        max_intensity=None,
    )
    return output_image
