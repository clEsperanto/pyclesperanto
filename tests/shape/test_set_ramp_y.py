import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_set_ramp_y(gpu_backend):
    result = cle.push(
        np.asarray(
            [[[0, 0, 0], [3, 4, 3], [3, 4, 3]], [[3, 4, 3], [3, 4, 3], [3, 4, 3]]]
        )
    )

    reference = cle.push(
        np.asarray(
            [[[0, 0, 0], [1, 1, 1], [2, 2, 2]], [[0, 0, 0], [1, 1, 1], [2, 2, 2]]]
        )
    )

    cle.set_ramp_y(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.001)
