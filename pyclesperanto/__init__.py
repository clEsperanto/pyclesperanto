# CLIc Import (is it usefull?)
# from ._pyclesperanto import _cleImage, _cleMemType, _cleDataType, _cleProcessor
# from ._pyclesperanto import _Create, _Push, _Pull
# from ._pyclesperanto import _ListAvailableDevices
# from ._pyclesperanto import _AbsoluteKernel_Call

# pyClEsperanto Import
# from . import _gateway, _types, _version
from ._version import VERSION, VERSION_STATUS, VERSION_TEXT
from ._gateway import Clesperanto
from ._types import MemoryType, DataType, Image

# Generic Import
import os

# Supports for ocl-icd find shipped OpenCL ICDs, cf.
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

# Init pyclesperanto
print("pyclesperanto version:", VERSION_TEXT)
cle = Clesperanto()
