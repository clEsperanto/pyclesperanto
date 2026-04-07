import warnings

_opencl_module = None
_cuda_module = None
_metal_module = None
_active_backend = None
_backends_detected = False

_BACKENDS = {
    "opencl": "pyclesperanto_opencl._pyclesperanto",
    "cuda": "pyclesperanto_cuda._pyclesperanto",
    "metal": "pyclesperanto_metal._pyclesperanto",
}

_DIST_NAMES = {
    "opencl": "pyclesperanto-opencl",
    "cuda": "pyclesperanto-cuda",
    "metal": "pyclesperanto-metal",
}

_MODULES = {
    "opencl": "_opencl_module",
    "cuda": "_cuda_module",
    "metal": "_metal_module",
}


def _detect_backends():
    """Try importing each backend package. Only runs once."""
    global _opencl_module, _cuda_module, _metal_module, _backends_detected
    if _backends_detected:
        return
    _backends_detected = True

    for name, module_path in _BACKENDS.items():
        try:
            mod = __import__(module_path, fromlist=[module_path.rsplit(".", 1)[-1]])
            if name == "opencl":
                _opencl_module = mod
            elif name == "cuda":
                _cuda_module = mod
            elif name == "metal":
                _metal_module = mod
        except ImportError as e:
            _warn_if_installed(name, e)


def _warn_if_installed(backend_name, error):
    """Warn if a backend package is installed but its native extension failed to load."""
    try:
        from importlib.metadata import distribution

        distribution(_DIST_NAMES[backend_name])
    except Exception:
        return
    warnings.warn(
        f"'{backend_name}' backend is installed but failed to load: {error}",
        RuntimeWarning,
        stacklevel=3,
    )


def _get_module(name):
    """Return the module for a given backend name, or None."""
    if name == "opencl":
        return _opencl_module
    if name == "cuda":
        return _cuda_module
    if name == "metal":
        return _metal_module
    return None


def _get_backend():
    """Return the active compiled backend module.

    Auto-selects on first call (prefers OpenCL, then CUDA, then Metal).
    Raises RuntimeError if no backend is available.
    """
    global _active_backend
    if _active_backend is None:
        _detect_backends()
        _active_backend = _opencl_module or _cuda_module or _metal_module
        if _active_backend is None:
            raise RuntimeError(
                "No pyclesperanto backend found.\n"
                "Install one with:\n"
                "  pip install pyclesperanto[opencl]\n"
                "  pip install pyclesperanto[cuda]\n"
                "  pip install pyclesperanto[metal]\n"
                "  pip install pyclesperanto[all]"
            )
        # Activate the C++ side and patch Array for the auto-selected backend
        _activate_clic_backend(get_backend_name())
        from ._array import _patch_array_class

        _patch_array_class()
    return _active_backend


def get_backend_name() -> str:
    """Return the name of the active backend ('opencl' or 'cuda' or 'metal'), or None."""
    if _active_backend is _opencl_module and _opencl_module is not None:
        return "opencl"
    if _active_backend is _cuda_module and _cuda_module is not None:
        return "cuda"
    if _active_backend is _metal_module and _metal_module is not None:
        return "metal"
    return None


def select_backend(name: str):
    """Switch the active backend. No-op if already active."""
    global _active_backend
    _detect_backends()
    name = name.lower()

    if name not in _BACKENDS:
        raise ValueError(
            f"Unknown backend '{name}'. Choose from: {', '.join(_BACKENDS)}."
        )

    mod = _get_module(name)
    if mod is None:
        raise ValueError(
            f"'{name}' backend is not installed. "
            f"Install with: pip install pyclesperanto[{name}]"
        )

    # Already active — nothing to do
    if _active_backend is mod:
        return

    _active_backend = mod
    _activate_clic_backend(name)

    from ._array import _patch_array_class

    _patch_array_class()


def _activate_clic_backend(name: str):
    """Tell CLIc's C++ BackendManager in the target backend module to activate,
    then reset the current device."""
    from ._core import _current_device

    target_mod = _get_module(name)
    if target_mod is None:
        raise RuntimeError(
            f"'{name}' backend module is not loaded. "
            f"Install with: pip install pyclesperanto[{name}]"
        )

    try:
        target_mod._BackendManager.set_backend(name)
    except RuntimeError as e:
        raise RuntimeError(
            f"Failed to activate '{name}' backend in {target_mod.__name__}: {e}\n"
            "Ensure your GPU drivers are installed and compatible."
        ) from e

    _current_device._instance = None


def list_available_backends():
    """Return list of installed backend names."""
    _detect_backends()
    return [name for name in _BACKENDS if _get_module(name) is not None]
