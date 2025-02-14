import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_minimum_box():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
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

    result = cle.create(test1)
    cle.minimum_filter(test1, result, 1, 1, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)
