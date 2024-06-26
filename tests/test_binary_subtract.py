import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_binary_subtract():
    test = cle.push(np.asarray([[1, 0], [1, 0]]))

    test1 = cle.push(np.asarray([[1, 1], [0, 0]]))

    test2 = cle.create(test)
    cle.binary_subtract(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.25
