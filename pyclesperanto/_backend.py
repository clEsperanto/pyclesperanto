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
    except ImportError:
        pass
    try:
        import pyclesperanto_cuda._pyclesperanto as _cu

        _cuda_module = _cu
    except ImportError:
        pass


def get_backend():
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


def select_backend(name):
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
        raise ValueError(
            f"'{name}' is not a valid backend. Use 'opencl' or 'cuda'."
        )


def list_available_backends():
    """Return list of installed backend names."""
    _detect_backends()
    backends = []
    if _opencl_module is not None:
        backends.append("opencl")
    if _cuda_module is not None:
        backends.append("cuda")
    return backends

