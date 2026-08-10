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

# enforce deprecation warnings display
warnings.filterwarnings("always", category=DeprecationWarning, module=__name__)


def label(
    input_image: Image, output_image: Image = None, connectivity: str = "box"
) -> Image:
    """
    Label connected components in an image.

    Parameters
    ----------
    input_image : Image
        The input image to be labeled.
    output_image : Image, optional
        The output image where the labeled components will be stored. If not provided, a new image
        will be created.
    connectivity : str, optional
        The connectivity criterion to use for labeling. Can be either 'box' or 'sphere'.
        Default is 'box'.

    Returns
    -------
    Image
        The labeled image.
    """
    from ._tier5 import connected_component_labeling

    return connected_component_labeling(
        input_image=input_image, output_image=output_image
    )


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

    from ._tier7 import affine_transform as _tier7_affine_transform

    if transform is not None:
        warnings.warn(
            "affine_transform : 'transform' parameter is deprecated. Please use 'transform_matrix' instead.",
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
