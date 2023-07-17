def test_import():
    import pyclesperanto as cle

    print(cle.list_available_backends())
    print(cle.list_available_devices())
