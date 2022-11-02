from ._types import Image
from ._types import plugin_function


@plugin_function
def absolute(self, input_image: Image, output_image: Image = None) -> Image:
    from ._pyclesperanto import _AbsoluteKernel_Call as op

    op(self.device, input_image, output_image)
    return output_image
