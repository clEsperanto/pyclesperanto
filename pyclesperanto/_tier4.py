from ._image import Image
from ._device import Device
from ._decorators import plugin_function

@plugin_function
def threshold_otsu(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:

    from ._pyclesperanto import _ThresholdOtsuKernel_Call as op

    op(device, input_image, output_image)
    return output_image


@plugin_function
def connect_component_labeling_box(
    input_image: Image,
    output_image: Image = None,
    device: Device = None,
) -> Image:

    from ._pyclesperanto import _ConnectedComponentLabelingBoxKernel_Call as op

    op(device, input_image, output_image)
    return output_image
