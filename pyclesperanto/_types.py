from ._pyclesperanto import _cleMemType, _cleDataType
import numpy as np
from typing import Union

class DataType:

    _string_to_type = {  # type: ignore
        'float32': _cleDataType.float32,
        'int8': _cleDataType.int8,
        'int16': _cleDataType.int16,
        'int32': _cleDataType.int32,
        'int64': _cleDataType.int64,
        'uint8': _cleDataType.uint8,
        'uint16': _cleDataType.uint16,
        'uint32': _cleDataType.uint32,
        'uint64': _cleDataType.uint64,
    }

    _type_to_string = {  # type: ignore
        _cleDataType.float32: 'float32',
        _cleDataType.int8: 'int8',
        _cleDataType.int16: 'int16',
        _cleDataType.int32: 'int32',
        _cleDataType.int64: 'int64',
        _cleDataType.uint8: 'uint8',
        _cleDataType.uint16: 'uint16',
        _cleDataType.uint32: 'uint32',
        _cleDataType.uint64: 'uint64',
    }

    def __init__(self, dtype: Union[str, np.dtype, _cleDataType, 'DataType'] = None) -> None:
        if dtype is None:
            dtype = _cleDataType.Float
        if isinstance(dtype, str):
            self.type = np.dtype(dtype)
            self.name = dtype
        elif isinstance(dtype, np.dtype):
            self.type = dtype
            self.name = dtype.name
        elif isinstance(dtype, DataType):
            self.type = dtype.type
            self.name = dtype.name
        elif isinstance(dtype, _cleDataType):
            self.type = np.dtype(self._type_to_string[dtype])
            self.name = self._type_to_string[dtype]
        else:
            raise ValueError("Invalid argument for dtype")

    @classmethod
    def float32(cls):
        return cls('float32')
    
    @classmethod
    def int8(cls):
        return cls('int8')
    
    @classmethod
    def int16(cls):
        return cls('int16')
    
    @classmethod
    def int32(cls):
        return cls('int32')
    
    @classmethod
    def int64(cls):
        return cls('int64')
    
    @classmethod
    def uint8(cls):
        return cls('uint8')
    
    @classmethod
    def uint16(cls):
        return cls('uint16')
    
    @classmethod
    def uint32(cls):
        return cls('uint32')
    
    @classmethod
    def uint64(cls):
        return cls('uint64')
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"dtype({self.name})"


class MemoryType:
    
    _string_to_type = {  # type: ignore
        'buffer': _cleMemType.buffer,
        'image': _cleMemType.image,
        'image1d': _cleMemType.image1d,
        'image2d': _cleMemType.image2d,
        'image3d': _cleMemType.image3d,
    }

    _type_to_string = {  # type: ignore
        _cleMemType.buffer: 'buffer',
        _cleMemType.image: 'image',
        _cleMemType.image1d: 'image1d',
        _cleMemType.image2d: 'image2d',
        _cleMemType.image3d: 'image3d',
    }

    def __init__(self, mtype: Union[str, _cleMemType, 'MemoryType'] = None) -> None:
        if mtype is None:
            mtype = _cleMemType.buffer
        if isinstance(mtype, str):
            self.type = self._string_to_type[mtype]
            self.name = mtype
        elif isinstance(mtype, MemoryType):
            self.type = mtype.type
            self.name = mtype.name
        elif isinstance(mtype, _cleMemType):
            self.type = mtype
            self.name = self._type_to_string[mtype]
        else:
            raise ValueError("Invalid argument for mtype")


    @classmethod
    def buffer(cls):
        return cls(_cleMemType.buffer)
    
    @classmethod
    def image(cls):
        return cls(_cleMemType.image)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"mtype({self.name})"