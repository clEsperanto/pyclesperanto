import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_convolve():
    test = cle.push(np.asarray([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

    test1 = cle.push(np.asarray([[0, 1, 0], [1, 2, 1], [0, 1, 0]]))

    test2 = cle.create_like(test)
    cle.convolve(test, test1, test2)

    print(test2)

    a = cle.pull(test1)
    b = cle.pull(test2)

    assert np.allclose(np.min(a), np.min(b), atol=1e-6)
    assert np.allclose(np.max(a), np.max(b), atol=1e-6)
    assert np.allclose(np.mean(a), np.mean(b), atol=1e-6)
