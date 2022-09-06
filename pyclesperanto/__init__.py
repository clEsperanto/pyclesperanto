from pyclesperanto.version import VERSION, VERSION_STATUS, VERSION_TEXT 
from pyclesperanto._pyclesperanto import pygateway

# This supports ocl-icd find shipped OpenCL ICDs, cf. 
import os
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

print("clesperanto version:",VERSION)
cle = pygateway()
