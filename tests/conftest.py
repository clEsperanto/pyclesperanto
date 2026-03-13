"""Pytest configuration for pyclesperanto tests.

Provides fixtures for testing across multiple GPU backends (OpenCL, CUDA).
"""

import pytest
import pyclesperanto as cle

# Store available backends for use in hooks
_available_backends = None


def _get_available_backends():
    """Get list of available backends, with fallback manual detection."""
    global _available_backends
    if _available_backends is not None:
        return _available_backends
    
    backends = cle.list_available_backends()
    
    if not backends:
        # Try manual detection if automatic detection failed
        backends = []
        try:
            import pyclesperanto_opencl
            backends.append("opencl")
        except ImportError:
            pass
        try:
            import pyclesperanto_cuda
            backends.append("cuda")
        except ImportError:
            pass
    
    _available_backends = backends
    return backends


def pytest_configure(config):
    """Register custom pytest markers and cache backends."""
    global _available_backends
    _available_backends = _get_available_backends()
    
    config.addinivalue_line(
        "markers",
        "skip_if_no_backend: skip test if no GPU backend is available",
    )
    config.addinivalue_line(
        "markers",
        "backend: parametrize test to run with each available backend",
    )


def pytest_generate_tests(metafunc):
    """Dynamically parametrize tests marked with @pytest.mark.backend."""
    if "gpu_backend" in metafunc.fixturenames:
        if metafunc.definition.get_closest_marker("backend"):
            backends = _get_available_backends()
            if backends:
                metafunc.parametrize("gpu_backend", backends, ids=backends)


@pytest.fixture(scope="function")
def gpu_backend(request):
    """Fixture that selects a GPU backend for the test.
    
    Use this fixture in test functions that need backend parametrization:
    
        @pytest.mark.backend
        def test_my_operation(gpu_backend):
            # Test will run once per available backend
            device = cle.select_device("TX")
            ...
    
    The fixture automatically switches backends before each test invocation.
    """
    # Tests are always parametrized via pytest_collection_modifyitems
    backend_name = request.param
    cle.select_backend(backend_name)
    yield backend_name
    # No cleanup needed, next test will select its own backend


@pytest.fixture(scope="function")
def available_backends():
    """Fixture that returns list of available backends."""
    return cle.list_available_backends()


@pytest.fixture(scope="function", autouse=True)
def ensure_gpu_backend_available(request):
    """Automatically skip tests if no GPU backend is available.
    
    Tests marked with @pytest.mark.skip_if_no_backend will be skipped
    if no GPU backend is available.
    """
    available_backends = cle.list_available_backends()
    
    if not available_backends:
        # Check if test is marked to skip if no backend
        if request.node.get_closest_marker("skip_if_no_backend"):
            pytest.skip("No GPU backend available")
        # Also warn on any test that tries to use cle operations
        if "cle" in request.node.name.lower() or "gpu" in request.node.name.lower():
            pytest.skip("No GPU backend available")


@pytest.fixture(scope="function", autouse=False)
def clear_gpu_cache(request):
    """Optional fixture to clear GPU cache between tests.
    
    Use with: @pytest.mark.usefixtures("clear_gpu_cache")
    """
    yield
    # GPU cache will be cleared if the backend supports it
    try:
        device = cle.get_device()
        if device:
            # Could add device.clear_cache() here if available
            pass
    except Exception:
        pass
