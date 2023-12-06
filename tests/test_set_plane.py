import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_set_plane():
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
