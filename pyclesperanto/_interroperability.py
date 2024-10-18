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

import warnings
from typing import Optional

import numpy as np

from ._array import Image

# pyclesperanto_prototype aliases
from ._core import info as cl_info
from ._core import list_available_devices as available_device_names
from ._core import wait_for_kernel_to_finish

# numpy operations aliases
from ._memory import push as asarray

# scikit-image aliases
from ._tier5 import connected_components_labeling as label
from ._tier7 import affine_transform as _tier7_affine_transform

# enforce deprecation warnings display
warnings.filterwarnings("always", category=DeprecationWarning, module=__name__)


def affine_transform(
    input_image: Image,
    output_image: Image = None,
    transform_matrix: Optional[list] = None,
    interpolate: bool = False,
    resize: bool = False,
    transform: Optional[np.ndarray] = None,
    linear_interpolation: Optional[bool] = None,
    auto_size: Optional[bool] = None,
) -> Image:

    if transform is not None:
        warnings.warn(
            "affine_transform : 'transform_matrix' parameter is deprecated. Please use 'transform' instead.",
            DeprecationWarning,
        )
        transform_matrix = transform.ravel().tolist()

    if linear_interpolation is not None:
        warnings.warn(
            "affine_transform : 'linear_interpolation' parameter is deprecated. Please use 'interpolate' instead.",
            DeprecationWarning,
        )
        interpolate = linear_interpolation

    if auto_size is not None:
        warnings.warn(
            "affine_transform : 'auto_size' parameter is deprecated. Please use 'resize' instead.",
            DeprecationWarning,
        )
        resize = auto_size

    if not isinstance(transform_matrix, list) and isinstance(
        transform_matrix, np.ndarray
    ):
        transform_matrix = transform_matrix.ravel().tolist()

    return _tier7_affine_transform(
        input_image=input_image,
        output_image=output_image,
        transform_matrix=transform_matrix,
        interpolate=interpolate,
        resize=resize,
    )


def set_wait_for_kernel_finish(wait: bool = True):
    warnings.warn(
        "set_wait_for_kernel_finish : This method is deprecated. Consider using wait_for_kernel_to_finish() instead.",
        DeprecationWarning,
    )
    wait_for_kernel_to_finish(wait)


# def clip(a, a_min, a_max, out=None):
#     from ._tier2 import clip

#     a = asarray(a)
#     if out:
#         out = asarray(out)
#     return clip(
#         input_image=a,
#         output_image=out,
#         min_intensity=a_min,
#         max_intensity=a_max,
#         device=a.device,
#     )


# def mod(x1, x2, out=None):
#     from ._tier1 import modulo_images

#     x1 = asarray(x1)
#     if out:
#         out = asarray(out)
#     return modulo_images(input_image0=x1, input_image1=x2, device=x1.device)


# def sqrt(x, out=None):
#     from ._tier1 import square_root

#     x = asarray(x)
#     if out:
#         out = asarray(out)
#     return square_root(input_image=x, output_image=out, device=x.device)


# def cbrt(x, out=None):
#     from ._tier1 import cubic_root

#     x = asarray(x)
#     if out:
#         out = asarray(out)
#     return cubic_root(input_image=x, output_image=out, device=x.device)


# def power(x1, x2, out=None):
#     x1 = asarray(x1)
#     if out:
#         out = asarray(out)

#     # test if x2 is a scalar
#     if np.isscalar(x2):
#         from ._tier1 import power

#         return power(input_image=x1, scalar=x2, output_image=out, device=x1.device)
#     else:
#         from ._tier1 import power_images

#         x2 = asarray(x2)
#         return power_images(
#             input_image0=x1, input_image1=x2, output_image=out, device=x1.device
#         )


# def fabs(x, out=None):
#     from ._memory import create
#     from ._tier1 import absolute

#     x = asarray(x)
#     if out:
#         out = asarray(out)
#     else:
#         out = create(x.shape, dtype=float, mtype=x.mtype, device=x.device)
#     return absolute(input_image=x, output_image=out, device=x.device)
