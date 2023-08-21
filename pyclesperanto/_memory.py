import warnings

from ._array import Array, Image
from ._core import Device, get_device

import numpy as np
from typing import Tuple, Optional


def create(
    shape: Tuple[int, ...],
    dtype: Optional[type] = None,
    mtype: Optional[str] = None,
    device: Optional[Device] = None,
) -> Image:
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
    Image
        Created an empty image on the device
    """
    if not isinstance(shape, tuple):
        shape = tuple(shape)
    if dtype is None:
        dtype = np.float32
    if dtype in [float, np.float64]:
        dtype = np.float32
        warnings.warn(
            "Warning: float64 type is not a supported in GPUs. Casting data to float32 type.",
            UserWarning,
        )
    if mtype is None:
        mtype = "buffer"
    if device is None:
        device = get_device()
    return Array.create(shape, dtype, mtype, device)


def create_like(
    array: Image,
    dtype: Optional[type] = None,
    mtype: Optional[str] = None,
    device: Optional[Device] = None,
) -> Image:
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
    Image
        Created an empty image on the device
    """
    if dtype is None:
        dtype = array.dtype
    if dtype in [float, np.float64]:
        dtype = np.float32
        warnings.warn(
            "Warning: float64 type is not a supported in GPUs. Casting data to float32 type.",
            UserWarning,
        )
    return create(array.shape, dtype, mtype, device)


def push(
    array: Image,
    dtype: Optional[type] = None,
    mtype: Optional[str] = None,
    device: Optional[Device] = None,
) -> Image:
    """Create a new image on the device and push the input image into it.

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
    Image
        Created image on the device with the input image data
    """
    if isinstance(array, Array):
        return array
    if array.dtype in [float, np.float64]:
        array = array.astype(np.float32)
    if dtype is None:
        dtype = array.dtype
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
    if isinstance(array, np.ndarray):
        return array
    return array.get()
