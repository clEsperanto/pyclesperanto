def test_init():
    import pyclesperanto as cle

    print("pyclesperanto version:", cle.__version__)
    print("relying on CLIc version:", cle.__clic_version__)

    print(cle.list_available_devices())
