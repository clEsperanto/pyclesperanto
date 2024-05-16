from ._array import Array, Image, is_image
from ._core import (Device, default_initialisation, get_device, gpu_info,
                    list_available_backends, list_available_devices,
                    select_backend, select_device, wait_for_kernel_to_finish)
from ._functionalities import execute, imshow, list_operations, native_execute
from ._interroperability import *
from ._memory import create, create_like, pull, push
from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *
from ._tier6 import *
from ._tier7 import *
from ._tier8 import *
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__
from ._version import VERSION as __version__

default_initialisation()
