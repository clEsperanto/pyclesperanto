
from ._core import (
    select_backend,
    get_device,
    select_device,
    list_available_devices,
    list_available_backends,
    default_initialisation,
)
from ._array import Image, is_image
from ._memory import create, create_like, push, pull
from ._memory import push as asarray
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

default_initialisation()




