# This file is for code interroperability with other libraries. It is not expected to follow major
# conventions of pyclesperanto, instead it should be as simple as possible to use in order to make
# it easy to use pyclesperanto in other libraries and frameworks.
#
# The following code and behaviour is expected:
# Import aliases
# Function aliases or re-implementations
# Deprecated functions
# Deprecated aliases
#

from ._array import Image

# pyclesperanto_prototype aliases
from ._core import list_available_devices as available_device_names
from ._core import wait_for_kernel_to_finish as set_wait_for_kernel_to_finish
from ._core import gpu_info as cl_info


# scikit-image aliases
from ._tier5 import connected_components_labeling as label


# numpy operations aliases
from ._memory import push as asarray

from typing import Union


def clip(a: Image, a_min: float, a_max: float, out: Image = None) -> Image:
    from ._tier2 import clip

    a = asarray(a)
    if out:
        out = asarray(out)
    return clip(
        input_image=a,
        output_image=out,
        min_intensity=a_min,
        max_intensity=a_max,
        device=a.device,
    )


def mod(x1: Image, x2: Image, out: Image = None) -> Image:
    from ._tier1 import modulo_images

    x1 = asarray(x1)
    if out:
        out = asarray(out)
    return modulo_images(input_image0=x1, input_image1=x2, device=x1.device)


def sqrt(x: Image, out: Image = None) -> Image:
    from ._tier1 import square_root

    x = asarray(x)
    if out:
        out = asarray(out)
    return square_root(input_image=x, output_image=out, device=x.device)


def cbrt(x: Image, out: Image = None) -> Image:
    from ._tier1 import cubic_root

    x = asarray(x)
    if out:
        out = asarray(out)
    return cubic_root(input_image=x, output_image=out, device=x.device)


def power(x1: Image, x2: Union[float, int, Image], out: Image = None) -> Image:
    x1 = asarray(x1)
    if out:
        out = asarray(out)

    if x2 is Image:
        from ._tier1 import power_images

        x2 = asarray(x2)
        return power_images(
            input_image0=x1, input_image1=x2, output_image=out, device=x1.device
        )
    else:
        from ._tier1 import power

        return power(input_image=x1, scalar=x2, output_image=out, device=x1.device)


def fabs(x: Image, out: Image = None) -> Image:
    from ._tier1 import absolute
    from ._memory import create

    x = asarray(x)
    if out:
        out = asarray(out)
    else:
        out = create(x.shape, dtype=float, mtype=x.mtype, device=x.device)
    return absolute(input_image=x, output_image=out, device=x.device)
