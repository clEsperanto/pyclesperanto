from ._image import Image
from ._device import Device
from ._decorators import plugin_function
from ._memory_operations import create


@plugin_function
def histogram(input_image: Image, bins: int = 256, device: Device = None) -> Image:
    """Computes a histogram of an image.

    The histogram will be stored in a new row of ImageJs
    Results table in the column 'Histogram'.

    Parameters
    ----------
    input_image : Image
        The image of which the histogram will be determined.
    bins : int, default 256
        The number of bins used for the histogram.
    device: Device, optional
        The device to be used for computation.

    Returns
    -------
    histogram : Image 1d

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_histogram
    """
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
