from ._core import Device
from ._array import Array, Image
from ._types import DataType, MemoryType

import numpy as np
from typing import Union, Tuple, Optional


def create(
    shape: Tuple[int, ...],
    dtype: Optional[type] = None,
    mtype: Optional[Union[str, MemoryType]] = None,
    device: Optional[Device] = None,
) -> Array:
    return Array.create(shape, dtype, mtype, device)


def create_like(
    array: Image,
    mtype: Optional[Union[str, DataType]] = None,
    device: Optional[Device] = None,
) -> Array:
    return create(array.shape, array.dtype, mtype, device)


def push(
    array: Image,
    dtype: Optional[type] = None,
    mtype: Optional[Union[str, DataType]] = None,
    device: Optional[Device] = None,
) -> Array:
    if isinstance(array, Array):
        return array
    return create(array.shape, dtype, mtype, device).set(array)


def pull(array: Image) -> np.ndarray:
    if isinstance(array, np.ndarray):
        return array
    return array.get()
