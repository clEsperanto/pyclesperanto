import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_gamma_correction():
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 50, 0, 5, 0],
                [0, 0, 100, 0, 0],
                [0, 30, 0, 10, 0],
                [0, 0, 0, 0, 0],
            ]
        ).astype(float)
    )

    result = cle.create(test, dtype=float)
    cle.gamma_correction(test, result, 0.5)

    a = cle.pull(result)

    print(a)
    print(np.mean(a))

    print(np.abs(np.min(a)))
    print(np.abs(np.max(a) - 100))
    print(np.abs(np.mean(a) - 11.1786))

    assert np.abs(np.min(a)) < 0.001
    assert np.abs(np.max(a) - 100) < 0.001
    assert np.abs(np.mean(a) - 11.1786) < 0.001
