# pyClEsperanto Import
from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__

from ._types import (
    MemoryType,
    DataType,
)
from ._core import (
    select_backend,
    get_device,
    select_device,
    list_available_devices,
)
from ._array import Array, Image, is_image
from ._memory import create, push, pull

from ._tier1 import absolute, add_images_weighted, gaussian_blur
from ._tier2 import difference_of_gaussian

# Generic Import
import os

# Supports for ocl-icd find shipped OpenCL ICDs, cf.
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

# redefine memory type for easy usage
buffer = MemoryType.buffer()
image = MemoryType.image()

__common_alias__ = "cle"
