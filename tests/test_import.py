"""Test that pyclesperanto can be imported successfully."""

import pytest

import pyclesperanto as cle


def test_import(gpu_backend):
    """Test basic import of pyclesperanto."""
    assert hasattr(cle, "__version__")


def test_backend_detection(gpu_backend):
    """Test that available backends are detected."""
    backends = cle.list_available_backends()
    assert isinstance(backends, list)
    assert len(backends) > 0, "At least one backend should be available"


@pytest.fixture(scope="function")
def gpu_backend(request):
    """Select the GPU backend for this test."""
    backend_name = request.param
    cle.select_backend(backend_name)
    cle.select_device()  # force device (re)selection on the new backend

    # Verify the switch actually happened
    active = cle.get_backend_name()
    if active != backend_name:
        pytest.fail(
            f"Failed to switch backend to '{backend_name}', " f"still on '{active}'"
        )

    # Handle skip_backend marker
    for marker in request.node.iter_markers("skip_backend"):
        if backend_name in marker.args:
            pytest.skip(f"Skipped on {backend_name}: {marker.kwargs.get('reason', '')}")

    # Handle only_backend marker
    for marker in request.node.iter_markers("only_backend"):
        if backend_name not in marker.args:
            pytest.skip(f"Only runs on {', '.join(marker.args)}")

    yield backend_name
