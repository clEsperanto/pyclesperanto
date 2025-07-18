import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_gradient_x():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 0, 0],
                [0, 1, 2, 0, 0],
                [0, 1, 3, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 1.0, -0.5, -1.0, 0.0],
                [1.0, 1.0, -0.5, -1.0, 0.0],
                [1.0, 1.5, -0.5, -1.5, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0],
            ]
        )
    )

    result = cle.gradient_x(test)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)
