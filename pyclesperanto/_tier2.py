from ._core import Device
from ._array import Image, Array
from ._decorators import plugin_function


@plugin_function
def difference_of_gaussian(
    input_image: Image,
    output_image: Array = None,
    sigma1_x: float = 1,
    sigma1_y: float = 1,
    sigma1_z: float = 1,
    sigma2_x: float = 2,
    sigma2_y: float = 2,
    sigma2_z: float = 2,
    device: Device = None,
) -> Array:
    from ._pyclesperanto import _difference_of_gaussian as op

    return op(
        device,
        src=input_image,
        dst=output_image,
        sigma1_x=float(sigma1_x),
        sigma1_y=float(sigma1_y),
        sigma1_z=float(sigma1_z),
        sigma2_x=float(sigma2_x),
        sigma2_y=float(sigma2_y),
        sigma2_z=float(sigma2_z),
    )
