"""Test that pyclesperanto can be imported successfully."""


def test_import():
    """Test basic import of pyclesperanto."""
    import pyclesperanto as cle
    assert hasattr(cle, '__version__')
