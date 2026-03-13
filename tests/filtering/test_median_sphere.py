import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_median_sphere(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [9, 9, 9, 0, 0],
                [9, 9, 9, 0, 0],
                [9, 9, 9, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [9, 9, 9, 0, 0],
                [9, 9, 9, 0, 0],
                [9, 9, 9, 0, 0],
            ]
        )
    )

    result = cle.create(test1)
    cle.median(test1, result, 1, 1, 0, "sphere")

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.0001)
