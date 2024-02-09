import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_dilate_box():
    test = cle.push(
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
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test)
    cle.dilate_box(test, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.array_equal(a, b)
