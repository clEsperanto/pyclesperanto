from ._core import (
    gpu_info,
    execute,
    select_backend,
    select_device,
    get_device,
    wait_for_kernel_to_finish,
    list_available_devices,
    list_available_backends,
    default_initialisation,
    Device,
)
from ._array import Array, Image, is_image
from ._memory import create, create_like, push, pull
from ._functionalities import imshow, list_operations

from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *
from ._tier6 import *
from ._tier7 import *
from ._tier8 import *
from ._interroperability import *

from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__


default_initialisation()
