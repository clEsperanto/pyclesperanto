import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_mask_label():
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 3, 0],
                [0, 3, 3, 4, 0],
                [0, 4, 4, 5, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    test2 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 2, 1, 3, 0],
                [0, 2, 1, 3, 0],
                [0, 1, 1, 3, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0],
                [0, 0, 3, 0, 0],
                [0, 4, 4, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.mask_label(test1, test2, result, 1)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)
