import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_grreater_or_equal(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, -6, 0, -3, 0],
                [0, 1, 2, 3, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 6, 0, 3, 0],
                [0, -1, -2, -3, 0],
            ]
        )
    )

    result = cle.create(test)
    cle.invert(test, result)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)
