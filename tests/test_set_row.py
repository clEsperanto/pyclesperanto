import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_set_row():
    result = cle.push(
        np.asarray(
            [
                [3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3],
                [3, 3, 3, 3, 3],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [3, 3, 3, 4, 3],
                [3, 3, 3, 4, 3],
                [3, 3, 3, 4, 3],
                [3, 3, 3, 4, 3],
                [3, 3, 3, 4, 3],
            ]
        ).T
    )

    cle.set_row(result, 3, 4)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert np.allclose(a, b, 0.001)
