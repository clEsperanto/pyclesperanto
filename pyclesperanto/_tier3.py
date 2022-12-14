from ._image import Image
from ._device import Device
from ._decorators import plugin_function
from ._memory_operations import create


@plugin_function
def histogram(input_image: Image, bins: int = 256, device: Device = None) -> Image:
    output_image = create((bins, 1, 1))
    from ._pyclesperanto import _HistogramKernel_Call as op
    import math

    op(
        device,
        src=input_image,
        dst=output_image,
        min_intensity=math.inf,
        max_intensity=math.inf,
        bins=int(bins),
    )
    return output_image
