import pytest

import pyclesperanto as cle


def test_available_device_names(gpu_backend):
    names = cle.list_available_devices()

    assert len(names) > 0
