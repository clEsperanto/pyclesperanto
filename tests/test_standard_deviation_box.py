import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_standard_deviation_box():
    test1 = cle.push(
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
                [0, 0.314, 0.314, 0.314, 0],
                [0, 0.314, 0.314, 0.314, 0],
                [0, 0.314, 0.314, 0.314, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test1, dtype=float)
    cle.standard_deviation(test1, result, 1, 1, 0)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.01)
