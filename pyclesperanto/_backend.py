"""Backend detection and management for pyclesperanto.

Discovers installed backend packages (pyclesperanto_opencl, pyclesperanto_cuda)
and provides a lazy accessor to the active compiled module.
"""

import warnings

_opencl_module = None
_cuda_module = None
_active_backend = None
_backends_detected = False


def _detect_backends():
    """Try importing each backend package. Only runs once."""
    global _opencl_module, _cuda_module, _backends_detected
    if _backends_detected:
        return
    _backends_detected = True
    try:
        import pyclesperanto_opencl._pyclesperanto as _ocl

        _opencl_module = _ocl
    except ImportError as e:
        _warn_backend_failure("pyclesperanto-opencl", "opencl", e)
    try:
        import pyclesperanto_cuda._pyclesperanto as _cu

        _cuda_module = _cu
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

    # Map backend name to the expected C++ BackendType enum value
    expected_types = {"opencl": "OpenCL", "cuda": "CUDA"}
    expected = expected_types.get(name)

    try:
        _active_backend._BackendManager.set_backend(name)
    except RuntimeError as e:
        raise RuntimeError(
            f"Failed to activate '{name}' backend: {e}\n"
            "This typically means the backend was not compiled into the CLIc C++ library.\n"
            f"Available backends: {list_available_backends()}\n"
            "Try reinstalling or using a different backend."
        ) from e

    # Verify the backend actually switched — catches C++ symbol interposition
    # where the other backend's BackendManager singleton is used instead.
    if expected is not None:
        try:
            actual_type = str(_active_backend._BackendManager.get_backend().type)
            if expected not in actual_type:
                raise RuntimeError(
                    f"Backend switch to '{name}' appeared to succeed but the active "
                    f"C++ backend is '{actual_type}' instead of '{expected}'.\n"
                    "This is caused by C++ symbol interposition between backend shared libraries.\n"
                    "Please upgrade pyclesperanto-opencl and pyclesperanto-cuda to the latest version:\n"
                    "  pip install --upgrade pyclesperanto-opencl pyclesperanto-cuda"
                )
        except RuntimeError:
            raise
        except Exception:
            pass  # If we can't verify, proceed anyway

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
