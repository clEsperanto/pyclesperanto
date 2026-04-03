from importlib.metadata import version

from ._pyclesperanto import *

__version__ = version("pyclesperanto-metal")
__backend__ = "metal"

__all__ = [
    "__backend__",
]