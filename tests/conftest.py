"""Pytest configuration for pyclesperanto tests.

Provides fixtures for testing across multiple GPU backends (OpenCL, CUDA).

Usage:
    pytest -v              # run tests on ALL available backends
    pytest -k opencl -v    # run tests only on OpenCL
    pytest -k cuda -v      # run tests only on CUDA

Markers:
    @pytest.mark.skip_backend("cuda", reason="...")  — skip on specific backend
    @pytest.mark.only_backend("opencl")              — run only on specific backend
    @pytest.mark.skip_if_no_backend                  — skip if no backend available
"""

import pytest

import pyclesperanto as cle

_available_backends = None


def _get_available_backends():
    """Get and cache the list of available backends."""
    global _available_backends
    if _available_backends is not None:
        return _available_backends

    backends = cle.list_available_backends()

    if not backends:
        # Fallback: try importing backend modules directly
        for name, module in [
            ("opencl", "pyclesperanto_opencl"),
            ("cuda", "pyclesperanto_cuda"),
        ]:
            try:
                __import__(module)
                backends.append(name)
            except ImportError:
                pass

    _available_backends = backends
    return backends


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers",
        "skip_if_no_backend: skip test if no GPU backend is available",
    )
    config.addinivalue_line(
        "markers",
        "skip_backend(name, reason=''): skip test for a specific backend",
    )
    config.addinivalue_line(
        "markers",
        "only_backend(name): run test only on a specific backend",
    )


def pytest_generate_tests(metafunc):
    """Auto-parametrize any test that requests the `gpu_backend` fixture."""
    if "gpu_backend" not in metafunc.fixturenames:
        return

    backends = _get_available_backends()

    if backends:
        metafunc.parametrize("gpu_backend", backends, ids=backends)
    else:
        # Provide a single skip-marked param so the test shows as skipped, not missing
        metafunc.parametrize(
            "gpu_backend",
            [
                pytest.param(
                    "none",
                    marks=pytest.mark.skip(reason="No GPU backend available"),
                )
            ],
        )


# conftest.py


@pytest.fixture(scope="function")
def gpu_backend(request):
    """Parametrize backend, handle skip markers, and switch to the backend."""
    backend_name = request.param

    for marker in request.node.iter_markers("skip_backend"):
        if backend_name in marker.args:
            pytest.skip(f"Skipped on {backend_name}: {marker.kwargs.get('reason', '')}")

    for marker in request.node.iter_markers("only_backend"):
        if backend_name not in marker.args:
            pytest.skip(f"Only runs on {', '.join(marker.args)}")

    # ✅ Actually switch the backend here
    cle.select_backend(backend_name)
    cle.select_device()
    assert cle.get_backend_name() == backend_name, (
        f"Backend switch failed: wanted {backend_name}, got {cle.get_backend_name()}"
    )

    return backend_name


@pytest.fixture(scope="function")
def available_backends():
    """Fixture that returns list of available backends."""
    return _get_available_backends()
