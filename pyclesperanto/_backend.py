"""Backend detection and management for pyclesperanto.

Discovers installed backend packages (pyclesperanto_opencl, pyclesperanto_cuda)
and provides a lazy accessor to the active compiled module.
"""

import platform
import sys
import warnings

_opencl_module = None
_cuda_module = None
_active_backend = None
_backends_detected = False


def _import_isolated(module_name):
    """Import a compiled backend module with symbol isolation.

    On Linux, both backend .so files statically link the CLIc C++ library,
    producing identical symbol names (e.g. cle::BackendManager::getInstance).
    Without isolation, the dynamic linker can resolve the second-loaded .so's
    internal CLIc calls to the first-loaded .so's symbols (interposition),
    causing the wrong C++ BackendManager singleton to be used.

    RTLD_DEEPBIND (Linux-only) forces each .so to resolve symbols from its
    own scope first, preventing this interposition.
    """
    if platform.system() == "Linux":
        RTLD_DEEPBIND = 0x00008
        old_flags = sys.getdlopenflags()
        try:
            sys.setdlopenflags(old_flags | RTLD_DEEPBIND)
            mod = __import__(module_name, fromlist=[module_name.rsplit(".", 1)[-1]])
        finally:
            sys.setdlopenflags(old_flags)
    else:
        mod = __import__(module_name, fromlist=[module_name.rsplit(".", 1)[-1]])
    return mod


def _detect_backends():
    """Try importing each backend package. Only runs once."""
    global _opencl_module, _cuda_module, _backends_detected
    if _backends_detected:
        return
    _backends_detected = True
    try:
        _opencl_module = _import_isolated("pyclesperanto_opencl._pyclesperanto")
    except ImportError as e:
        _warn_backend_failure("pyclesperanto-opencl", "opencl", e)
    try:
        _cuda_module = _import_isolated("pyclesperanto_cuda._pyclesperanto")
    except ImportError as e:
        _warn_backend_failure("pyclesperanto-cuda", "cuda", e)


def _warn_backend_failure(dist_name, backend_name, error):
    """Emit a warning if a backend package is installed but failed to load."""
    try:
        from importlib.metadata import distribution

        distribution(dist_name)
    except Exception:
        return  # not installed, nothing to warn about
    warnings.warn(
        f"'{backend_name}' backend package is installed but failed to load: {error}",
        RuntimeWarning,
        stacklevel=3,
    )


def _get_backend():
    """Return the active compiled backend module.

    On first call, auto-detects installed backends and selects the first available one.
    Raises RuntimeError if no backend is installed.
    """
    global _active_backend
    if _active_backend is None:
        _detect_backends()
        # Auto-select: prefer opencl, then cuda
        if _opencl_module is not None:
            _active_backend = _opencl_module
        elif _cuda_module is not None:
            _active_backend = _cuda_module
        else:
            raise RuntimeError(
                "No pyclesperanto backend installed.\n"
                "Install one with:\n"
                "  pip install pyclesperanto[opencl]   # for OpenCL\n"
                "  pip install pyclesperanto[cuda]     # for CUDA\n"
                "  pip install pyclesperanto[all]      # for both"
            )
    return _active_backend


def get_backend_name() -> str:
    """Return the name of the active backend ('opencl' or 'cuda'), or None."""
    if _active_backend is _opencl_module and _opencl_module is not None:
        return "opencl"
    if _active_backend is _cuda_module and _cuda_module is not None:
        return "cuda"
    return None


def select_backend(name: str):
    """Switch between 'opencl' and 'cuda' backends.

    Parameters
    ----------
    name : str
        Backend name: 'opencl' or 'cuda'.
    """
    global _active_backend
    _detect_backends()
    name = name.lower()
    if name == "opencl":
        if _opencl_module is None:
            raise ValueError(
                "'opencl' backend is not installed. Install with: pip install pyclesperanto[opencl]"
            )
        _active_backend = _opencl_module
    elif name == "cuda":
        if _cuda_module is None:
            raise ValueError(
                "'cuda' backend is not installed. Install with: pip install pyclesperanto[cuda]"
            )
        _active_backend = _cuda_module
    else:
        raise ValueError(f"'{name}' is not a valid backend. Use 'opencl' or 'cuda'.")
    # Tell CLIc's C++ BackendManager to switch and reset the current device
    _activate_clic_backend(name)


def _activate_clic_backend(name: str):
    """Tell CLIc's C++ BackendManager singleton to select the given backend,
    and reset the Python-side current device."""
    from ._core import _current_device

    try:
        _active_backend._BackendManager.set_backend(name)
    except RuntimeError as e:
        error_msg = str(e)
        # CLIc's setBackend() has a fallback path: if the requested backend's
        # runtime check fails (e.g. no CUDA GPU), it tries to create an
        # OpenCLBackend as fallback.  In the split-package model, the other
        # backend is compiled as a stub that throws "OpenCL/CUDA is not enabled".
        if "is not enabled" in error_msg:
            other = "opencl" if name == "cuda" else "cuda"
            raise RuntimeError(
                f"Failed to activate '{name}' backend.\n"
                f"The '{name}' runtime could not find a compatible device, and the "
                f"fallback to '{other}' is unavailable in this package.\n"
                "Make sure you have:\n"
                + (
                    "  1. An NVIDIA GPU available in this environment\n"
                    "  2. NVIDIA drivers installed (check with: nvidia-smi)\n"
                    "  3. A CUDA toolkit version compatible with the installed driver\n"
                    if name == "cuda"
                    else "  1. An OpenCL-compatible device available\n"
                    "  2. OpenCL ICD drivers installed\n"
                )
            ) from e
        raise RuntimeError(
            f"Failed to activate '{name}' backend: {e}\n"
            "This typically means the backend was not compiled into the CLIc C++ library.\n"
            f"Available backends: {list_available_backends()}\n"
            "Try reinstalling or using a different backend."
        ) from e

    _current_device._instance = None


def list_available_backends():
    """Return list of installed backend names."""
    _detect_backends()
    backends = []
    if _opencl_module is not None:
        backends.append("opencl")
    if _cuda_module is not None:
        backends.append("cuda")
    return backends
