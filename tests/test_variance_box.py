import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_variance_box():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0.0987, 0.0987, 0.0987, 0],
                [0, 0.0987, 0.0987, 0.0987, 0],
                [0, 0.0987, 0.0987, 0.0987, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1, dtype=float)
    cle.variance_filter(test1, result, 1, 1, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.01)
