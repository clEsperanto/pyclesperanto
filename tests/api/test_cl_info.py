import pytest

import pyclesperanto as cle


def test_cl_info(gpu_backend):
    print(cle.cl_info())
    assert True


def test_device_info(gpu_backend):
    print(cle.get_device().info)
    assert True
