import pyclesperanto as cle
import pytest


@pytest.mark.backend
def test_operations(gpu_backend):

    ops_list = cle.operations(must_have_categories=["filter"])
    assert len(ops_list) > 0
