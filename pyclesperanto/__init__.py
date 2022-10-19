from pyclesperanto.version import VERSION, VERSION_STATUS, VERSION_TEXT

from ._pyclesperanto import _cleImage, _cleMemType, _cleDataType, _cleProcessor
from ._pyclesperanto import _Create, _Push, _Pull
from ._pyclesperanto import _ListAvailableDevices
from ._pyclesperanto import _AbsoluteKernel_Call

from pyclesperanto import _gateway, _types
from _gateway import Clesperanto


# This supports ocl-icd find shipped OpenCL ICDs, cf.
import os

os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

print("clesperanto version:", VERSION)
cle = Clesperanto()
