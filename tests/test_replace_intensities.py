import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_replace_intensities():
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

    test2 = cle.push(np.asarray([[0, 9, 8, 7, 6, 5]]))

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 9, 8, 7, 0],
                [0, 8, 7, 6, 0],
                [0, 6, 6, 5, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.replace_values(test1, test2, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, 0.001)
