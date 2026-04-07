import numpy as np
import pytest

import pyclesperanto as cle


def test_copy(gpu_backend):
    test1 = cle.push(np.asarray([[1, 1], [1, 0]]))

    test2 = cle.create(test1)
    cle.copy(test1, test2)

    print(test2)
    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.75
