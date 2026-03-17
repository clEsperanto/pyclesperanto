from importlib.metadata import version

from ._pyclesperanto import *

__version__ = version("pyclesperanto-cuda")
__backend__ = "cuda"

__all__ = [
    "__backend__",
]
