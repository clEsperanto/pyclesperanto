import pyclesperanto as cle


def test_available_device_names():
    names = cle.available_device_names()

    assert len(names) > 0
