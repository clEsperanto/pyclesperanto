import pyclesperanto as cle


def test_operations():

    ops_list = cle.operations(must_have_categories=["filter"])
    assert len(ops_list) > 0
