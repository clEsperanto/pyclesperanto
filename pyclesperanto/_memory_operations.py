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
from ._image import Image, MemoryType


def create(
    shape: tuple, mtype: MemoryType = None, dtype: type = None, device: Device = None
):
    """create:

    Conventional method to create images on the GPU and return its handle

    Parameters
    ----------
    shape : tuple
        shape of the memory to create, using the zyx convention
    mtype : mType, optional
        buffer or image structure

    Returns
    -------
    Image
        Handle of the empty GPU image
    """
    from ._image import cleImage

    if mtype is None:
        mtype = MemoryType.buffer
    if dtype is None:
        dtype = np.float32
    if device is None:
        device = get_device()
    return cleImage(_Create(device, shape, dtype, mtype))


def create_like(image: Image) -> Image:
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

    if isinstance(image, cleImage):
        return create(
            shape=tuple(image.shape),
            dtype=image.dtype,
            mtype=image.mtype,
            device=image.device,
        )
    else:
        return create(
            shape=tuple(image.shape), dtype=image.dtype, mtype=MemoryType.buffer
        )


def push(array: Image, mtype: MemoryType = None, device: Device = None) -> Image:
    """push:

    Copy an host array to the GPU device and return its handle

    Parameters
    ----------
    array : Image (numpy array, etc.)
        Can be of other type compatible with numpy
    mtype : mType, optional
        buffer or image memory structure structure

    Returns
    -------
    Image
        Handle of the GPU image
    """
    from ._image import cleImage

    if isinstance(array, cleImage):
        return array
    else:
        if mtype is None:
            mtype = MemoryType.buffer
        if device is None:
            device = get_device()
        return cleImage(_Push(device, np.asarray(array), mtype))


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

    pull_dict = {
        np.float32: _PullFloat,
        np.uint8: _PullUint8,
        np.uint16: _PullUint16,
        np.uint32: _PullUint32,
        np.uint64: _PullUint64,
        np.int8: _PullInt8,
        np.int16: _PullInt16,
        np.int32: _PullInt32,
        np.int64: _PullInt64,
    }

    if isinstance(image, cleImage):
        # return _Pull(image, image.dtype)
        # if image.dtype == np.uint8:
        #     return _PullUint8(image)
        # elif image.dtype == np.uint16:
        #     return _PullUint16(image)
        # elif image.dtype == np.uint32:
        #     return _PullUint32(image)
        # elif image.dtype == np.uint64:
        #     return _PullUint64(image)
        # elif image.dtype == np.int8:
        #     return _PullInt8(image)
        # elif image.dtype == np.int16:
        #     return _PullInt16(image)
        # elif image.dtype == np.int32:
        #     return _PullInt32(image)
        # elif image.dtype == np.int64:
        #     return _PullInt64(image)
        # return _PullFloat(image)
        return pull_dict[image.dtype](image)
    else:
        return image
