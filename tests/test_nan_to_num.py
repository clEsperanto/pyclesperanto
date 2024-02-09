import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


def test_nan_to_num():
    data = np.asarray([[-np.inf], [np.inf], [np.nan], [0], [1]])

    print(np.nan_to_num(data, nan=3, posinf=4, neginf=5))
    print(cle.nan_to_num(data, nan=3, posinf=4, neginf=5))

    assert np.allclose(
        np.nan_to_num(data, nan=3, posinf=4, neginf=5),
        cle.nan_to_num(data, nan=3, posinf=4, neginf=5),
    )


def test_nan_to_num_defaults():
    data = np.asarray([[-np.inf], [np.inf], [np.nan], [0], [1]])

    print(np.nan_to_num(data))
    print(cle.nan_to_num(data, nan=0, posinf=np.inf, neginf=-np.inf))

    result = cle.nan_to_num(data, nan=0, posinf=np.inf, neginf=-np.inf)
    print(result)

    assert result[0, 0] < 0  # a very small number
    assert result[1, 0] > 0  # a very large number
    assert result[2, 0] == 0
    assert result[3, 0] == 0
    assert result[4, 0] == 1
