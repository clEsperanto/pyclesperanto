from pyclesperanto.version import VERSION, VERSION_STATUS, VERSION_TEXT 

from ._pyclesperanto import cleImage, cleMemType, cleDataType, cleGateway, cleProcessor
from ._pyclesperanto import ListAvailableDevices

# This supports ocl-icd find shipped OpenCL ICDs, cf. 
import os
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

print("clesperanto version:",VERSION)