import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_set_nonzero_pixels_to_pixelindex():
    test1 = cle.push(
        np.asarray([[0, 0, 0, 1], [0, 0, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]])
    )

    reference = cle.push(
        np.asarray([[0, 0, 0, 3], [0, 0, 6, 7], [0, 0, 10, 11], [12, 13, 14, 15]])
    )

    result = cle.create(test1)
    cle.set_nonzero_pixels_to_pixelindex(test1, result, offset=0)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)
    print(b)

    assert np.array_equal(a, b)
