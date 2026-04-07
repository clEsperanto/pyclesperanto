"""Test that pyclesperanto can be imported successfully."""

import pytest

import pyclesperanto as cle


def test_import():
    """Test basic import of pyclesperanto."""
    assert hasattr(cle, "__version__")


def test_backend_detection():
    """Test that available backends are detected."""
    backends = cle.list_available_backends()
    assert isinstance(backends, list)
    assert len(backends) > 0, "At least one backend should be available"
