import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_bottom_hat_box():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 50, 50, 50, 0],
                [0, 50, 100, 50, 0],
                [0, 50, 50, 50, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create_like(test)
    cle.bottom_hat(test, result, 1, 1, 0)

    print(result)

    a = cle.pull(result)
    assert np.min(a) == 0
    assert np.max(a) == 50
