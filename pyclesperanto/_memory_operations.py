import numpy as np
from ._pyclesperanto import (
    _Create,
    _PushFloat,
    _PullFloat,
    _PushInt32,
    _PullInt32,
    _PushInt16,
    _PullInt16,
    _PushInt8,
    _PullInt8,
    _PushUint32,
    _PullUint32,
    _PushUint16,
    _PullUint16,
    _PushUint8,
    _PullUint8,
)
from ._device import Device, get_device
from ._image import cleImage, Image, mType, dType


# def create(shape: tuple, mtype: mType = None, device: Device = None) -> Image:
#     """create:

#     Conventional method to create images on the GPU and return its handle

#     Parameters
#     ----------
#     shape : tuple
#         shape of the memory to create, using the zyx convention
#     mtype : mType, optional
#         buffer or image structure

#     Returns
#     -------
#     Image
#         Handle of the empty GPU image
#     """
#     if mtype is None:
#         mtype = mType.buffer
#     if device is None:
#         device = get_device()
#     return cleImage(_Create(device, shape, mtype))


def create(
    shape: tuple, dtype: dType = None, mtype: mType = None, device: Device = None
) -> Image:
    """create:

    Conventional method to create images on the GPU and return its handle

    Parameters
    ----------
    shape : tuple
        shape of the memory to create, using the zyx convention
    dtype : dType, optional
        data type of the memory to create (float, int, etc.)
    mtype : mType, optional
        memory structure of the memory to create (buffer or image)

    Returns
    -------
    Image
        Handle of the empty GPU image (buffer or image) with the specified data type
    """
    if dtype is None:
        dtype = dType.float
    if mtype is None:
        mtype = mType.buffer
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
    if isinstance(image, cleImage):
        return create(
            shape=tuple(image.shape),
            dtype=image.dtype,
            mtype=image.mtype,
            device=image.device,
        )
    else:
        # todo: get dtype from numpy array and convert to cle dType
        return create(shape=tuple(image.shape))


def push(array: Image, mtype: mType = None, device: Device = None) -> Image:
    """push:

    Copy an host array to the GPU device and return its handle

    Parameters
    ----------
    array : Image (numpy array, etc.)
        Can be of other type compatible with numpy
    mtype : mType, optional
        memory structure of the memory to create (buffer or image)

    Returns
    -------
    Image
        Handle of the GPU image (buffer or image) with the specified data type
    """
    if isinstance(array, cleImage):
        return array
    else:
        if device is None:
            device = get_device()
        if mtype is None:
            mtype = mType.buffer

        if array.dtype == np.float32:
            return cleImage(
                _PushFloat(device, np.asarray(array, dtype=np.float32), mtype)
            )
        elif array.dtype == np.int32:
            return cleImage(
                _PushInt32(device, np.asarray(array, dtype=np.int32), mtype)
            )
        elif array.dtype == np.int16:
            return cleImage(
                _PushInt16(device, np.asarray(array, dtype=np.int16), mtype)
            )
        elif array.dtype == np.int8:
            return cleImage(_PushInt8(device, np.asarray(array, dtype=np.int8), mtype))
        elif array.dtype == np.uint32:
            return cleImage(
                _PushUint32(device, np.asarray(array, dtype=np.uint32), mtype)
            )
        elif array.dtype == np.uint16:
            return cleImage(
                _PushUint16(device, np.asarray(array, dtype=np.uint16), mtype)
            )
        elif array.dtype == np.uint8:
            return cleImage(
                _PushUint8(device, np.asarray(array, dtype=np.uint8), mtype)
            )
        else:
            return cleImage(
                _PushFloat(device, np.asarray(array, dtype=np.float32), mtype)
            )


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
    if isinstance(image, cleImage):
        if image.dtype == dType.float:
            return _PullFloat(image)
        elif image.dtype == dType.int32:
            return _PullInt32(image)
        elif image.dtype == dType.int16:
            return _PullInt16(image)
        elif image.dtype == dType.int8:
            return _PullInt8(image)
        elif image.dtype == dType.uint32:
            return _PullUint32(image)
        elif image.dtype == dType.uint16:
            return _PullUint16(image)
        elif image.dtype == dType.uint8:
            return _PullUint8(image)
        else:
            return _PullFloat(image)
    else:
        return image
