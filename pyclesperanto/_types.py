from __future__ import annotations

from ._pyclesperanto import _MemoryType, _DataType

import numpy as np
from typing import Union


class DataType:
    np_dtype_mapping = {
        np.float32: _DataType.float32,
        np.int64: _DataType.int64,
        np.int32: _DataType.int32,
        np.int16: _DataType.int16,
        np.int8: _DataType.int8,
        np.uint64: _DataType.uint64,
        np.uint32: _DataType.uint32,
        np.uint16: _DataType.uint16,
        np.uint8: _DataType.uint8,
    }

    @classmethod
    def get_cle_dtype(cls, dtype):
        if isinstance(dtype, DataType):
            return dtype
        elif isinstance(dtype, np.dtype) and dtype.type in cls.np_dtype_mapping:
            return cls.np_dtype_mapping[dtype.type]
        elif isinstance(dtype, type) and dtype in cls.np_dtype_mapping:
            return cls.np_dtype_mapping[dtype]
        else:
            raise ValueError("Invalid value type. Expected dType or NumPy dtype.")

    @classmethod
    def get_np_dtype(cls, dtype):
        if dtype in cls.np_dtype_mapping.values():
            for numpy_dtype, dType in cls.np_dtype_mapping.items():
                if dType == dtype:
                    return numpy_dtype
        else:
            raise ValueError("No matching NumPy dtype found for the specified dType.")


class MemoryType:
    mtype_mapping = {  # type: ignore
        _MemoryType.buffer: "buffer",
        _MemoryType.image: "image",
    }

    def __init__(self, mtype: Union[MemoryType, _MemoryType] = None) -> None:
        if mtype is None:
            mtype = _MemoryType.buffer
        elif isinstance(mtype, MemoryType):
            self.type = mtype.type
            self.name = mtype.name
        elif isinstance(mtype, _MemoryType):
            self.type = mtype
            self.name = self.mtype_mapping[mtype]
        else:
            raise ValueError("Invalid argument for mtype")

    @classmethod
    def buffer(cls):
        return cls(_MemoryType.buffer)

    @classmethod
    def image(cls):
        return cls(_MemoryType.image)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"mtype({self.name})"
