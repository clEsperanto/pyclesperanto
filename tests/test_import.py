"""Test that pyclesperanto can be imported successfully."""

import pytest

import pyclesperanto as cle


@pytest.mark.backend
def test_import(gpu_backend):
    """Test basic import of pyclesperanto."""
    assert hasattr(cle, "__version__")


@pytest.mark.backend
def test_backend_detection(gpu_backend):
    """Test that available backends are detected."""
    backends = cle.list_available_backends()
    assert isinstance(backends, list)
    assert len(backends) > 0, "At least one backend should be available"


@pytest.mark.backend
def test_backend_switching(gpu_backend):
    """Test switching between available backends."""
    # Test that we can get the active backend name
    active = cle.get_backend_name()
    assert active == gpu_backend
    assert active in cle.list_available_backends()
