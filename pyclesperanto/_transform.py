import warnings
from typing import Optional, Union

import numpy as np

from ._array import Image
from ._backend import _get_backend
from ._core import Device
from ._decorators import plugin_function


def _get_affine_transform_class():
    """Get the _AffineTransform class from the active backend (lazy)."""
    return _get_backend()._AffineTransform


class _AffineTransformMeta(type):
    """Metaclass that makes isinstance/issubclass/calls always use the *current* backend."""

    def __instancecheck__(cls, instance):
        try:
            return isinstance(instance, _get_affine_transform_class())
        except RuntimeError:
            return False

    def __subclasscheck__(cls, subclass):
        try:
            return issubclass(subclass, _get_affine_transform_class())
        except RuntimeError:
            return False

    def __call__(cls, *args, **kwargs):
        return _get_affine_transform_class()(*args, **kwargs)

    def __getattr__(cls, name):
        return getattr(_get_affine_transform_class(), name)


class AffineTransform(metaclass=_AffineTransformMeta):
    """Lazy proxy for the backend AffineTransform class.

    Instantiation and attribute access are forwarded to the *currently active*
    backend _AffineTransform, so switching backends with select_backend() is
    fully transparent.
    """


def compute_output_shape_from_transform(
    input_shape: tuple[int, int, int], transform_matrix: AffineTransform
) -> tuple[tuple[int, int, int], AffineTransform]:
    """
    Computes the output shape of an image after applying an affine transformation.

    Arguments:
    ----------
    input_shape : tuple[int, int, int]
        The shape of the input image (z, y, x).
    transform_matrix : AffineTransform
        The affine transformation matrix.

    Returns:
    --------
    tuple[tuple[int, int, int], AffineTransform]
        A tuple containing the output shape (z, y, x) and the transformed affine matrix as AffineTransform.
    """
    if not isinstance(transform_matrix, AffineTransform):
        raise TypeError(
            f"compute_output_shape : 'transform_matrix' must be an AffineTransform, {type(transform_matrix)} given."
        )

    # get width, height, depth from input_shape
    if len(input_shape) == 1:
        depth = 1
        height = 1
        width = input_shape[0]
    elif len(input_shape) == 2:
        depth = 1
        height = input_shape[0]
        width = input_shape[1]
    elif len(input_shape) == 3:
        depth = input_shape[0]
        height = input_shape[1]
        width = input_shape[2]
    else:
        raise ValueError(
            f"compute_output_shape : 'input_shape' must be a tuple of length 1, 2 or 3, {len(input_shape)} given."
        )

    x, y, z, transform = _get_backend()._prepare_output_shape_and_transform(width, height, depth, transform_matrix)
    output_shape = (z, y, x)

    return output_shape, transform

@plugin_function
def affine_transform(
    input_image: Image,
    output_image: Optional[Image] = None,
    transform_matrix: Optional[Union[list, np.ndarray, AffineTransform]] = None,
    interpolate: bool = False,
    resize: bool = False,
    transform: Optional[np.ndarray] = None,
    linear_interpolation: Optional[bool] = None,
    auto_size: Optional[bool] = None,
    device: Optional[Device] = None,
) -> Image:
    """
    Applies an affine transformation matrix to an image.

    Arguments:
    ----------
    input_image : Image
        The input image to be transformed.
    output_image : Image, optional
        The output image to store the result. If None, a new image will be created.
    transform_matrix : list, np.ndarray, or AffineTransform, optional
        The affine transformation matrix (4x4, or a flat row-major list of 16 values).
        If None, the identity transformation is applied.
    interpolate : bool, optional
        Whether to use interpolation when transforming the image. Default is False.
    resize : bool, optional
        Whether to resize the output image to fit the transformed content. Default is False.
    transform : np.ndarray, optional
        Deprecated. Use 'transform_matrix' instead.
    linear_interpolation : bool, optional
        Deprecated. Use 'interpolate' instead.
    auto_size : bool, optional
        Deprecated. Use 'resize' instead.

    Returns:
    --------
    Image
        The transformed image.
    """
    if transform is not None:
        warnings.warn(
            "affine_transform : 'transform' parameter is deprecated. Please use 'transform_matrix' instead.",
            DeprecationWarning,
        )
        transform_matrix = transform

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

    if transform_matrix is None:
        transform_matrix = AffineTransform()
    if not isinstance(transform_matrix, AffineTransform):
        try:
            transform_matrix = AffineTransform(transform_matrix)
        except (ValueError, RuntimeError) as error:
            raise TypeError(
                f"affine_transform : 'transform_matrix' must be an AffineTransform, a 4x4/3x3 matrix, "
                f"or a flat list/array of 16 or 9 floats, {transform_matrix!r} given."
            ) from error


    return _get_backend()._affine_transform(input_image, output_image, transform_matrix, interpolate, resize)


@plugin_function
def affine_transform_deskew(
    input_image: Image,
    output_image: Optional[Image] = None,
    transform_matrix: Optional[Union[list, np.ndarray, AffineTransform]] = None,
    deskew_angle: float = 0.0,
    voxel_size: tuple = (1.0, 1.0, 1.0),
    deskew_direction: str = "x",
    resize: bool = False,
    device: Optional[Device] = None,
) -> Image:
    """
    Applies a deskewing transformation matrix to an image with software interpolation.

    Arguments:
    ----------
    input_image : Image
        The input image to be transformed.
    output_image : Image, optional
        The output image to store the result. If None, a new image will be created.
    transform_matrix : list, np.ndarray, or AffineTransform, optional
        The affine transformation matrix (4x4, or a flat row-major list of 16 values).
        If None, the identity transformation is applied.
    deskew_angle : float, optional
        The angle in degrees for deskewing. Default is 0.0.
    voxel_size : tuple, optional
        The voxel size (z, y, x) directions. Default is (1.0, 1.0, 1.0).
    deskew_direction : str, optional
        The direction of deskewing ('x' or 'y'). Default is 'x'.
    resize : bool, optional
        Whether to resize the output image to fit the transformed content. Default is False.

    Returns:
    --------
    Image
        The transformed image.
    """
    if transform_matrix is None:
        transform_matrix = AffineTransform()
    if not isinstance(transform_matrix, AffineTransform):
        transform_matrix = AffineTransform(transform_matrix)

    if not isinstance(voxel_size, (tuple, list)) or len(voxel_size) != 3:
        raise ValueError("voxel_size must be a tuple or list of length 3 as (z, y, x).")

    return _get_backend()._affine_transform_deskew(input_image, output_image, transform_matrix, deskew_angle, voxel_size[-1], voxel_size[-2], voxel_size[-3], deskew_direction, resize)


__all__ = [
    "AffineTransform",
    "compute_output_shape_from_transform",
    "affine_transform",
    "affine_transform_deskew",
]