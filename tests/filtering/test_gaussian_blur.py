import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_gaussian_blur(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test, dtype=float)
    cle.gaussian_blur(test, result, 1, 1, 0)

    print(result)

    a = cle.pull(result)
    assert np.min(a) > 0
    assert np.max(a) > 15.9
    assert np.max(a) < 16
