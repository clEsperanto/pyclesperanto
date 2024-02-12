import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_square():
    test1 = cle.push(np.asarray([4, 6]))

    reference = cle.push(np.asarray([16, 36]))

    result = cle.square(test1)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.001)
