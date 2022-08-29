
from pyclesperanto._pyclesperanto import __version__
from pyclesperanto._pyclesperanto import pygateway

# This supports ocl-icd find shipped OpenCL ICDs, cf. 
import os
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

print("clesperanto version:",__version__)
cle = pygateway()
