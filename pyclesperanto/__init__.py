# CLIc Import (is it usefull?)
# from ._pyclesperanto import _cleImage, _cleMemType, _cleDataType, _cleProcessor
# from ._pyclesperanto import _Create, _Push, _Pull
# from ._pyclesperanto import _ListAvailableDevices
# from ._pyclesperanto import _AbsoluteKernel_Call

# pyClEsperanto Import
from ._version import VERSION as __version__
from ._memory_operations import create, create_like, pull, push
from ._image import Image, mType
from ._device import get_device, select_device, list_available_devices, set_wait_for_kernel_to_finish, info
from ._tier1 import (
    absolute
)

# Generic Import
import os

# Supports for ocl-icd find shipped OpenCL ICDs, cf.
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

# Init pyclesperanto
print("pyclesperanto version:", __version__)

buffer = mType.buffer
image = mType.image

