from . import __experimental__
from ._array import Array, Image, is_image
from ._categories import categories
from ._core import (
    Device,
    default_initialisation,
    get_device,
    info,
    list_available_backends,
    list_available_devices,
    select_backend,
    select_device,
    wait_for_kernel_to_finish,
)
from ._functionalities import execute, imshow, native_execute, operation, operations
from ._memory import create, create_like, pull, push
from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *
from ._tier6 import *
from ._tier7 import *
from ._tier8 import *
from ._utils import fft_smooth_shape
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__
from ._version import VERSION as __version__

from ._interroperability import *  # isort:skip

__all__ = [
    "Array",
    "Image",
    "is_image",
    "Device",
    "get_device",
    "info",
    "list_available_devices",
    "select_device",
    "wait_for_kernel_to_finish",
    "execute",
    "imshow",
    "native_execute",
    "create",
    "create_like",
    "pull",
    "push",
    "fft_smooth_shape",
    "__clic_version__",
    "__common_alias__",
    "__version__",
]

# Add all items from tier modules without polluting namespace
import importlib
for _tier_name in ['_tier1', '_tier2', '_tier3', '_tier4', '_tier5', '_tier6', '_tier7', '_tier8']:
    _tier_module = importlib.import_module(f'.{_tier_name}', package='pyclesperanto')
    if hasattr(_tier_module, '__all__'):
        __all__ += _tier_module.__all__
del importlib, _tier_name, _tier_module

default_initialisation()
