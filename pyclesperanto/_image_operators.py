import numpy as np
from ._pyclesperanto import _Pull

class ImageOperators:

    def abs(self, out=None):
        from ._tier1 import absolute
        result = absolute(self)
        if out is not None:
            np.copyto(out, _Pull(result).astype(out.dtype))
        return result
