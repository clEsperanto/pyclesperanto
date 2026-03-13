import pytest

import pyclesperanto as cle


@pytest.mark.backend
def test_available_device_names(gpu_backend):
    names = cle.available_device_names()

    assert len(names) > 0
