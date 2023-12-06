import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_replace_intensity():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 3, 0],
                [0, 2, 3, 4, 0],
                [0, 4, 4, 5, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 8, 3, 0],
                [0, 8, 3, 4, 0],
                [0, 4, 4, 5, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.replace_value(test1, result, 2, 8)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, 0.001)
