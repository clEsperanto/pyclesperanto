import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


def test_undefined_to_zero():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        ).astype(float)
    )

    test2 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        ).astype(float)
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        ).astype(float)
    )

    divided = cle.divide_images(test1, test2)

    divided_no_nan = cle.undefined_to_zero(divided)

    print(divided)
    print(divided_no_nan)

    a = cle.pull(divided_no_nan)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
