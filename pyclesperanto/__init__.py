# pyClEsperanto Import
from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__

# try:
# from . import _clesperanto as _cle
# except ImportError:
#     try:
# from . import _ocl_clesperanto as _cle
    # except ImportError:
    #     try:
# from . import _cuda_clesperanto as _cle
        # except ImportError:
        #     raise ImportError("Failed to import the backend")

from ._types import (
    MemoryType,
    DataType,
)
from ._core import (
    select_backend,
    get_device,
    select_device,
    list_available_devices,
    list_available_backends,
)
from ._array import Array, Image, is_image
from ._memory import create, create_like, push, pull
from ._functionalities import imshow

from ._tier1 import *
from ._tier2 import *

# Generic Import
import os

# Supports for ocl-icd find shipped OpenCL ICDs, cf.
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

# redefine memory type for easy usage
buffer = MemoryType.buffer()
image = MemoryType.image()

# default backend is opencl
__default_backend__ = select_backend(list_available_backends()[-1])
__common_alias__ = "cle"
