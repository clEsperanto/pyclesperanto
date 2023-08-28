from ._core import (
    gpu_info,
    select_backend,
    select_device,
    get_device,
    wait_for_kernel_to_finish,
    list_available_devices,
    list_available_backends,
    default_initialisation,
    Device,
)
from ._array import Image, is_image
from ._memory import create, create_like, push, pull
from ._functionalities import imshow, list_operations

from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *
from ._tier6 import *
from ._tier7 import *

from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__

# Aliases - compatibility with prototype
from ._memory import push as asarray
from ._core import list_available_devices as available_device_names
from ._core import wait_for_kernel_to_finish as set_wait_for_kernel_to_finish
from ._core import gpu_info as cl_info
from ._tier5 import connected_components_labeling_box as label

default_initialisation()
