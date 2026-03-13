import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_set_plane(gpu_backend):
    result = cle.push(
        np.asarray(
            [
                [
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                ],
                [
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                    [3, 3, 3, 3, 3],
                ],
                [
                    [4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4],
                    [4, 4, 4, 4, 4],
                ],
            ]
        )
    )

    cle.set_plane(result, 1, 4)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.001)
