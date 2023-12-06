import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_set_where_x_greater_than_y():
    result = cle.push(
        np.asarray([[0, 0, 0, 1], [0, 0, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]])
    )

    reference = cle.push(
        np.asarray([[0, 3, 3, 3], [0, 0, 3, 3], [0, 0, 3, 3], [1, 1, 1, 1]])
    )

    cle.set_where_x_greater_than_y(result, 3)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)
