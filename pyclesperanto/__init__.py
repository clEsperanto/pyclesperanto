
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
from ._tier6 import *
from ._tier7 import *

from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__

default_initialisation()

import pkgutil
import importlib
import inspect

def list_functions(module_name=None):
    package_name = __name__
    package = importlib.import_module(package_name)

    skip_modules = ["_decorators", "_operators", "_arrays", "_version"]

    print(f"Functions available in {package_name} package:")
    for importer, modname, ispkg in pkgutil.walk_packages(path=package.__path__, prefix=package.__name__ + '.'):
        module = importlib.import_module(modname)
        if module_name in skip_modules:
            continue  # Skip the specified modules
        module_functions = [attr for attr, value in inspect.getmembers(module) if inspect.isfunction(value)]
        if module_functions:
            print(f"Module: {modname}")
            print("Functions:")
            for function_name in module_functions:
                if not function_name.startswith('_'):
                    print(f"  {function_name}")
            print()


