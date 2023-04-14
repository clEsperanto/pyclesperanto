import numpy as np
from ._pyclesperanto import (
    _Create,
    _Push,
    _PullFloat,
    _PullInt64,
    _PullInt32,
    _PullInt16,
    _PullInt8,
    _PullUint64,
    _PullUint32,
    _PullUint16,
    _PullUint8,
)
from ._device import Device, get_device
from ._image import Image
from ._types import MemoryType 
from typing import Optional, Union


def create(
    shape: tuple,
    mtype: Optional[MemoryType] = None,
    dtype: Optional[type] = None,
    device: Optional[Device] = None,
):
    """create:

    Conventional method to create images on the GPU and return its handle

    Parameters
    ----------
    shape : tuple
        shape of the memory to create, using the zyx convention
    mtype : MemoryType, optional
        buffer or image structure
    dtype : type, optional
        data type of the memory to create
    device : Device, optional
        Device to create the memory on

    Returns
    -------
    Image
        Handle of the empty GPU image
    """
    from ._image import cleImage

    if dtype is None:
        dtype = np.float32
    if device is None:
        device = get_device()
    return cleImage(_Create(device, shape, np.dtype(dtype), MemoryType(mtype).type))


def create_like(
    image: Image,
    mtype: Optional[MemoryType] = None,
    dtype: Optional[type] = None,
    device: Optional[Device] = None,
) -> Image:
    """create_like:

    Create an empty copy of the provided image on the GPU and return its handle

    Parameters
    ----------
    image : Image
        A GPU image or any other Image alternative compatible with pyclesperanto.
        If the source image is not a GPU image, the newly create image will be a buffer type.

    Returns
    -------
    Image
        Handle of the empty GPU image
    """
    from ._image import cleImage

    if dtype is None:
        dtype = image.dtype
    if mtype is None:
        mtype = image.mtype if isinstance(image, cleImage) else MemoryType.buffer
    if device is None:
        device = image.device if isinstance(image, cleImage) else get_device()
    return create(shape=tuple(image.shape), dtype=dtype, mtype=mtype, device=device)


def push(
    array: Image, mtype: Optional[MemoryType] = None, device: Optional[Device] = None
) -> Image:
    """push:

    Copy an host array to the GPU device and return its handle

    Parameters
    ----------
    array : Image (numpy array, etc.)
        Can be of other type compatible with numpy
    mtype : MemoryType, optional
        buffer or image memory structure structure
    device : Device, optional
        Device to create the memory on

    Returns
    -------
    Image
        Handle of the GPU image
    """
    from ._image import cleImage

    if isinstance(array, cleImage):
        return array
    else:
        if device is None:
            device = get_device()
        return cleImage(_Push(device, np.asarray(array), MemoryType(mtype).type))


def pull(image: Image) -> Image:
    """pull:

    Returns an image from the GPU device to the host memory as a numpy compatible array

    Parameters
    ----------
    image : Image
        A GPU image handle

    Returns
    -------
    Image
        numpy compatible array
    """
    from ._image import cleImage

    # TODO: should this dict be moved in the cleImage class?
    pull_dict = {
        'float32': _PullFloat,
        'uint8': _PullUint8,
        'uint16': _PullUint16,
        'uint32': _PullUint32,
        'uint64': _PullUint64,
        'int8': _PullInt8,
        'int16': _PullInt16,
        'int32': _PullInt32,
        'int64': _PullInt64,
    }
    if isinstance(image, cleImage):
        return pull_dict[image.dtype.name](image)
    else:
        return image
