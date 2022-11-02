from ._types import Image, MemoryType


def create(self, shape: list = (1, 1, 1), mtype: MemoryType = None) -> Image:
    """Create an OpenCL backed image/buffer with specified shape."""
    from ._pyclesperanto import _Create
    from ._types import cleImage

    if mtype is None:
        mtype = self.buffer
    return cleImage(_Create(self.device, shape, mtype))


def create_like(self, image) -> Image:
    """Create an OpenCL backed image/buffer with the same size and type like the given image."""
    from ._types import cleImage

    if isinstance(image, cleImage):
        return self.create(shape=image.shape, mtype=image.mtype)
    else:
        return self.create(shape=image.shape)


def push(self, any_array, mtype: MemoryType = None) -> Image:
    """Transfer a numpy-compatible array to GPU memory."""
    from ._types import cleImage

    if mtype is None:
        mtype = self.buffer

    if isinstance(any_array, cleImage):
        return any_array
    else:
        import numpy as np
        from ._pyclesperanto import _Push

        return cleImage(_Push(self.device, np.asarray(any_array), mtype))


def pull(self, any_array) -> Image:
    """Return a OpenCL/GPU backed image from GPU memory as numpy array."""
    from ._types import cleImage

    if isinstance(any_array, cleImage):
        from ._pyclesperanto import _Pull

        return _Pull(any_array)
    else:
        return any_array
