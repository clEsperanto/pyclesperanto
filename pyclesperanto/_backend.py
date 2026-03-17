import warnings

_opencl_module = None
_cuda_module = None
_active_backend = None
_backends_detected = False

_BACKENDS = {
    "opencl": "pyclesperanto_opencl._pyclesperanto",
    "cuda": "pyclesperanto_cuda._pyclesperanto",
}

_DIST_NAMES = {
    "opencl": "pyclesperanto-opencl",
    "cuda": "pyclesperanto-cuda",
}


def _detect_backends():
    """Try importing each backend package. Only runs once."""
    global _opencl_module, _cuda_module, _backends_detected
    if _backends_detected:
        return
    _backends_detected = True

    for name, module_path in _BACKENDS.items():
        try:
            mod = __import__(module_path, fromlist=[module_path.rsplit(".", 1)[-1]])
            if name == "opencl":
                _opencl_module = mod
            else:
                _cuda_module = mod
        except ImportError as e:
            _warn_if_installed(name, e)


def _warn_if_installed(backend_name, error):
    """Warn if a backend package is installed but its native extension failed to load."""
    try:
        from importlib.metadata import distribution

        distribution(_DIST_NAMES[backend_name])
    except Exception:
        return  # not installed — nothing to warn about
    warnings.warn(
        f"'{backend_name}' backend is installed but failed to load: {error}",
        RuntimeWarning,
        stacklevel=3,
    )


def _get_backend():
    """Return the active compiled backend module.

    Auto-selects on first call (prefers OpenCL, then CUDA).
    Raises RuntimeError if no backend is available.
    """
    global _active_backend
    if _active_backend is None:
        _detect_backends()
        _active_backend = _opencl_module or _cuda_module
        if _active_backend is None:
            raise RuntimeError(
                "No pyclesperanto backend found.\n"
                "Install one with:\n"
                "  pip install pyclesperanto[opencl]\n"
                "  pip install pyclesperanto[cuda]\n"
                "  pip install pyclesperanto[all]"
            )
    return _active_backend


def get_backend_name() -> str:
    """Return the name of the active backend ('opencl' or 'cuda'), or None."""
    if _active_backend is not None:
        if _active_backend is _opencl_module:
            return "opencl"
        if _active_backend is _cuda_module:
            return "cuda"
    return None


def select_backend(name: str):
    """Switch the active backend.

    Parameters
    ----------
    name : str
        Backend name: 'opencl' or 'cuda'.
    """
    global _active_backend
    _detect_backends()
    name = name.lower()

    modules = {"opencl": _opencl_module, "cuda": _cuda_module}
    if name not in modules:
        raise ValueError(
            f"Unknown backend '{name}'. Choose from: {', '.join(modules)}."
        )
    if modules[name] is None:
        raise ValueError(
            f"'{name}' backend is not installed. "
            f"Install with: pip install pyclesperanto[{name}]"
        )

    _active_backend = modules[name]
    _activate_clic_backend(name)


def _activate_clic_backend(name: str):
    """Tell CLIc's C++ BackendManager to switch, and reset the current device."""
    from ._core import _current_device

    try:
        _active_backend._BackendManager.set_backend(name)
    except RuntimeError as e:
        raise RuntimeError(
            f"Failed to activate '{name}' backend: {e}\n"
            "Ensure your GPU drivers are installed and compatible."
        ) from e

    _current_device._instance = None


def list_available_backends():
    """Return list of installed backend names."""
    _detect_backends()
    available = []
    if _opencl_module is not None:
        available.append("opencl")
    if _cuda_module is not None:
        available.append("cuda")
    return available
