import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_clip_min_max():
    test = [[0, 1], [2, 3]]
    reference = [[1, 1], [2, 2]]

    result = cle.clip(test, min_intensity=1, max_intensity=2)

    assert np.array_equal(result, reference)


def test_clip_max():
    test = [[0, 1], [2, 3]]
    reference = [[0, 1], [2, 2]]

    result = cle.clip(test, min_intensity=0, max_intensity=2)

    assert np.array_equal(result, reference)


def test_clip_min():
    test = [[0, 1], [2, 3]]
    reference = [[1, 1], [2, 3]]

    result = cle.clip(test, min_intensity=1, max_intensity=3)

    assert np.array_equal(result, reference)
