import pyclesperanto as cle
import pytest


@pytest.mark.backend
def test_cl_info(gpu_backend):
    print(cle.cl_info())
    assert True
