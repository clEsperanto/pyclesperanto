
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
from ._functionalities import imshow

from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *

# # Generic Import
# import os

# # Supports for ocl-icd find shipped OpenCL ICDs, cf.
# os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__

default_initialisation()