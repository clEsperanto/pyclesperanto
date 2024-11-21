def test_import():
    try:
        import pyclesperanto as cle
    except ImportError as e:
        print(f"ImportError: {e}")
