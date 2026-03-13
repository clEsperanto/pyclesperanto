import warnings

from ._array import Array, Image, _patch_array_class, is_image
from ._backend import (
    get_backend_name,
    _get_backend,
    get_backend_name,
    list_available_backends,
    select_backend,
)
from ._categories import categories
from ._version import CLIC_VERSION as __clic_version__
from ._version import COMMON_ALIAS as __common_alias__
from ._version import VERSION as __version__


def _lazy_init():
    """Initialize the backend and patch the Array class.

    Called on first actual use. Safe to call multiple times.
    """
    try:
        _get_backend()
    except RuntimeError:
        warnings.warn(
            "No pyclesperanto backend installed.\n"
            "Install one with:\n"
            "  pip install pyclesperanto[opencl]   # for OpenCL\n"
            "  pip install pyclesperanto[cuda]     # for CUDA\n"
            "  pip install pyclesperanto[all]      # for both",
            RuntimeWarning,
        )
        return False
    _patch_array_class()
    return True


# Try initializing — if a backend is available, patch everything
_backend_available = _lazy_init()

if _backend_available:
    from . import __experimental__

    # Re-import Array/Image after patching so that cle.Array has the real class
    from ._array import Array, Image  # noqa: F811

    # Auto-select a default device
    from ._core import (
        Device,
        _default_initialisation,
        get_device,
        info,
        list_available_devices,
        select_device,
        wait_for_kernel_to_finish,
    )
    from ._execute import evaluate, execute, native_execute
    from ._functionalities import imshow, operation, operations
    from ._memory import create, create_like, pull, push
    from ._tier1 import *
    from ._tier2 import *
    from ._tier3 import *
    from ._tier4 import *
    from ._tier5 import *
    from ._tier6 import *
    from ._tier7 import *
    from ._tier8 import *
    from ._utils import fft_smooth_shape

    from ._interroperability import *  # isort:skip

    _default_initialisation()

__all__ = [
    "Array",
    "Image",
    "is_image",
    "select_backend",
    "list_available_backends",
    "get_backend_name",
    "__clic_version__",
    "__common_alias__",
    "__version__",
]

if _backend_available:
    import importlib as _importlib

    __all__ += [
        "Device",
        "get_device",
        "info",
        "list_available_devices",
        "select_device",
        "wait_for_kernel_to_finish",
        "execute",
        "imshow",
        "native_execute",
        "create",
        "create_like",
        "pull",
        "push",
        "evaluate",
        "fft_smooth_shape",
    ]

    for _tier_name in [
        "_tier1",
        "_tier2",
        "_tier3",
        "_tier4",
        "_tier5",
        "_tier6",
        "_tier7",
        "_tier8",
    ]:
        _tier_module = _importlib.import_module(
            f".{_tier_name}", package="pyclesperanto"
        )
        if hasattr(_tier_module, "__all__"):
            __all__ += _tier_module.__all__
    del _importlib, _tier_name, _tier_module
