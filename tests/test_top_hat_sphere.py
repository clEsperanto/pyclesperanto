import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_top_hat_sphere():
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

    result = cle.create(test)
    cle.top_hat(test, result, 1, 1, 0, connectivity="sphere")

    print(result)

    a = cle.pull(result)
    assert np.min(a) == 0
    assert np.max(a) == 50
