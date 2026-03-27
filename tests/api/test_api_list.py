import pytest

import pyclesperanto as cle



def test_operations(gpu_backend):

    ops_list = cle.operations(must_have_categories=["filter"])
    assert len(ops_list) > 0
