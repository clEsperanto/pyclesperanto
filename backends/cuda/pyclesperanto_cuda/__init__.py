from ._pyclesperanto import *
from importlib.metadata import version

__version__ = version("pyclesperanto-cuda")
__backend__ = "cuda"

__all__ = [
    "__backend__",
]
