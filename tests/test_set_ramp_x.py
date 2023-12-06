import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_set_ramp_x():
    result = cle.push(
        np.asarray(
            [[[0, 0, 0], [3, 4, 3], [3, 4, 3]], [[3, 4, 3], [3, 4, 3], [3, 4, 3]]]
        )
    )

    reference = cle.push(
        np.asarray(
            [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
        )
    )

    cle.set_ramp_x(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.001)
