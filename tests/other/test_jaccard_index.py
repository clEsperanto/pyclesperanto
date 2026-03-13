import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_jaccard_index_2d(gpu_backend):
    test1 = cle.push(np.asarray([[0, 0, 0, 0, 0], [0, 1, 1, 0, 0]]))

    test2 = cle.push(np.asarray([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]))

    j = cle.jaccard_index(test1, test2)

    assert j == 0.5


@pytest.mark.backend
def test_accard_index_3d(gpu_backend):
    test1 = cle.push(np.asarray([[[0, 0, 0], [0, 0, 0]], [[0, 1, 1], [0, 1, 0]]]))

    test2 = cle.push(np.asarray([[[0, 1, 1], [0, 1, 0]], [[0, 1, 1], [0, 1, 0]]]))

    j = cle.jaccard_index(test1, test2)

    assert j == 0.5
