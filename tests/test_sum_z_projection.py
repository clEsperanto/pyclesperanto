import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_sum_z_projection():
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 0, 0, 0, 9],
                    [0, 2, 0, 8, 0],
                    [3, 0, 1, 0, 10],
                    [0, 4, 0, 7, 0],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [0, 2, 0, 8, 0],
                    [1, 0, 0, 0, 9],
                    [3, 0, 1, 0, 10],
                    [0, 4, 0, 7, 0],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [0, 2, 0, 8, 0],
                    [3, 0, 1, 0, 10],
                    [0, 4, 0, 7, 0],
                    [1, 0, 0, 0, 9],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [0, 2, 0, 8, 0],
                    [1, 0, 0, 0, 9],
                    [0, 4, 0, 7, 0],
                    [3, 0, 1, 0, 10],
                    [5, 0, 6, 0, 10],
                ],
                [
                    [1, 0, 0, 0, 9],
                    [0, 4, 0, 7, 0],
                    [3, 0, 1, 0, 10],
                    [0, 2, 0, 8, 0],
                    [5, 0, 6, 0, 10],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [2.0, 6.0, 0.0, 24.0, 18.0],
                [5.0, 6.0, 1.0, 15.0, 28.0],
                [9.0, 8.0, 3.0, 14.0, 30.0],
                [4.0, 10.0, 1.0, 22.0, 19.0],
                [25.0, 0.0, 30.0, 0.0, 50.0],
            ]
        )
    )

    result = cle.create(reference)
    cle.sum_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert np.allclose(a, b, 0.01)


def test_sum_z_projection2():
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 0],
                ],
                [
                    [0, 2],
                ],
                [
                    [0, 2],
                ],
                [
                    [0, 2],
                ],
                [
                    [1, 0],
                ],
            ]
        )
    )

    reference = cle.push(np.asarray([[2, 6]]))

    result = cle.sum_z_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert np.allclose(a, b, 0.01)
