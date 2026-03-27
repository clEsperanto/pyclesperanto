import numpy as np
import pytest

import pyclesperanto as cle



def test_affine_transform_translate(gpu_backend):
    source = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    transform = [1, 0, -1, 0, 1, -1, 0, 0, 1]
    result = cle.affine_transform(source, transform_matrix=transform)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
