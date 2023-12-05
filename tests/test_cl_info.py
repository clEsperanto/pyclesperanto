import pyclesperanto as cle


def test_cl_info():
    info = cle.cl_info()
    print(info)

    assert len(info) > 0
