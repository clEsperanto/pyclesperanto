import numpy as np

import pyclesperanto as cle


def test_concate_along_x():
    test1 = cle.push(np.asarray([[1, 1], [1, 1]]))
    test2 = cle.push(np.asarray([[2, 2, 2], [2, 2, 2]]))

    reference = cle.push(np.asarray([[1, 1, 2, 2, 2], [1, 1, 2, 2, 2]]))

    result = cle.concatenate_along_x(test1, test2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.01)


def test_concate_along_y():
    test1 = cle.push(np.asarray([[1, 1], [1, 1]]))
    test2 = cle.push(np.asarray([[2, 2], [2, 2]]))

    reference = cle.push(np.asarray([[1, 1], [1, 1], [2, 2], [2, 2]]))

    result = cle.concatenate_along_y(test1, test2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.01)


def test_concate_along_z():
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 1],
                ],
                [[1, 1]],
            ]
        )
    )
    test2 = cle.push(np.asarray([[[2, 2]], [[2, 2]], [[2, 2]]]))

    reference = cle.push(
        np.asarray(
            [
                [
                    [1, 1],
                ],
                [
                    [1, 1],
                ],
                [
                    [2, 2],
                ],
                [[2, 2]],
                [[2, 2]],
            ]
        )
    )

    result = cle.concatenate_along_z(test1, test2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.01)
