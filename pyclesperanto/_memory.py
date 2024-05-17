import warnings
from typing import Optional, Tuple

import numpy as np

from ._array import Array, Image
from ._core import Device, get_device


def create(
    dim,
    dtype: Optional[type] = None,
    mtype: Optional[str] = None,
    device: Optional[Device] = None,
) -> Array:
    """Create a new image on the device.

    Parameters
    ----------
    shape : Tuple[int, ...]
        Shape of the image in (z,y,x)
    dtype : type, optional
        Data type of the image (np.int8, np.float32, etc.), np.float32 by default if None
    mtype : str, optional
        Memory type of the image (buffer, image), buffer by default if None
    device : Device, optional
        Device on which the image is created, current device by default if None

    Returns
    -------
    Array
        Created an empty Array on the device
    """
    if isinstance(dim, Array):
        device = device if device else dim.device
        mtype = mtype if mtype else dim.mtype
    if isinstance(dim, (np.ndarray, Array)):
        dtype = dtype if dtype else dim.dtype
        dim = dim.shape
    else:
        dim = tuple(dim)

    device = device if device else get_device()
    dtype = dtype if dtype else float
    mtype = mtype if mtype else "buffer"

    return Array.empty(dim, dtype=dtype, mtype=mtype, device=device)


def create_like(
    array: Image,
    dtype: Optional[type] = None,
    mtype: Optional[str] = None,
    device: Optional[Device] = None,
) -> Array:
    """Create a new image on the device with the same shape and dtype as the input image.

    Parameters
    ----------
    array : Image
        Input image
    dtype : type, optional
        Data type of the image (np.int8, np.float32, etc.), np.float32 by default if None
    mtype : str, optional
        Memory type of the image (buffer, image), buffer by default if None
    device : Device, optional
        Device on which the image is created, current device by default if None

    Returns
    -------
    Array
        Created an empty Array on the device
    """
    return create(array.shape, dtype, mtype, device)


def push(
    array: Image,
    dtype: Optional[type] = None,
    mtype: Optional[str] = None,
    device: Optional[Device] = None,
) -> Array:
    """Create a new image on the device and push the input image into it.

    Parameters
    ----------
    array : Image
        Input image
    dtype : type, optional
        If provided, the input image is cast to the given dtype before being
        pushed to the device. Examples are `np.int8`, `np.float32`, etc.
        By default, no casting is performed and the dtype of the pushed
        image will match the dtype of the input image.
    mtype : str, optional
        Memory type of the image (buffer, image), buffer by default if None
    device : Device, optional
        Device on which the image is created, current device by default if None

    Returns
    -------
    Array
        Created Array on the device with the input image data
    """
    if isinstance(array, Array):
        return array

    if not isinstance(array, np.ndarray):
        array = np.asarray(array)

    dtype = dtype if dtype else array.dtype
    return create(array.shape, dtype, mtype, device).set(array)


def pull(array: Image) -> np.ndarray:
    """Pull the input image from the device to the host.

    Parameters
    ----------
    array : Image
        Input image

    Returns
    -------
    np.ndarray
        Image data
    """
    if isinstance(array, Array):
        return array.get()
    return array
