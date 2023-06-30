from ._core import Device
from ._array import Image, Array
from ._decorators import plugin_function


@plugin_function
def absolute(
    input_image: Image,
    output_image: Array = None,
    device: Device = None,
) -> Array:
    from ._pyclesperanto import _absolute as op

    return op(
        device,
        src=input_image,
        dst=output_image,
    )


@plugin_function
def add_images_weighted(
    input_image0: Image,
    input_image1: Image,
    output_image: Array = None,
    factor0: float = 1,
    factor1: float = 1,
    device: Device = None,
) -> Array:
    from ._pyclesperanto import _add_images_weighted as op

    return op(
        device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image,
        factor0=float(factor0),
        factor1=float(factor1),
    )


@plugin_function
def gaussian_blur(
    input_image: Image,
    output_image: Array = None,
    sigma_x: float = 1,
    sigma_y: float = 1,
    sigma_z: float = 1,
    device: Device = None,
) -> Array:
    from ._pyclesperanto import _gaussian_blur as op

    return op(
        device,
        src=input_image,
        dst=output_image,
        sigma_x=float(sigma_x),
        sigma_y=float(sigma_y),
        sigma_z=float(sigma_z),
    )
