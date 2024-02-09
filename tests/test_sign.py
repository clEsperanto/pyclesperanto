import pytest
import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


# @pytest.mark.skip(reason="Fails on github CI but passes locally")
def test_sign():
    data = np.asarray([-np.inf, np.inf, 0, 1, -1, np.nan])

    print(np.sign(data))
    print(cle.sign(data))

    # we exclude nan from the test, because numpy cannot compare it
    assert np.allclose(np.sign(data)[0:4], cle.sign(data)[0:4])
