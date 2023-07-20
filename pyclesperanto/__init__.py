# pyClEsperanto Import
from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__

from ._core import (
    select_backend,
    get_device,
    select_device,
    list_available_devices,
    list_available_backends,
)
from ._array import _Array, Image, is_image
from ._memory import create, create_like, push, pull
from ._functionalities import imshow

from ._tier1 import *
from ._tier2 import *
from ._tier3 import *
from ._tier4 import *
from ._tier5 import *

# Generic Import
import os

# Supports for ocl-icd find shipped OpenCL ICDs, cf.
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

__backends__ = list_available_backends()
if __backends__:
    _ = select_backend(__backends__[-1])
else:
    print("No backends available, pyclesperanto is unlikely to run.")

__common_alias__ = "cle"
