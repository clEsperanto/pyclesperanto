import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_crop_border_2d():
    test1 = cle.push(
        np.asarray([[0, 0, 0, 1], [0, 0, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]])
    )

    reference = cle.push(np.asarray([[0, 3], [0, 3]]))

    result = cle.crop_border(test1, border_size=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    assert np.array_equal(a, b)


def test_crop_3d():
    input_image = cle.push(
        np.asarray(
            [
                [[0, 0, 0, 1], [0, 0, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]],
                [[0, 0, 0, 1], [0, 1, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]],
                [[0, 0, 0, 1], [0, 0, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]],
                [[0, 0, 0, 1], [0, 0, 3, 1], [0, 0, 3, 1], [1, 1, 1, 1]],
            ]
        )
    )
    reference = cle.push(
        np.asarray(
            [
                [[1, 3], [0, 3]],
                [[0, 3], [0, 3]],
            ]
        )
    )

    result = cle.crop_border(input_image, border_size=1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    assert np.array_equal(a, b)
