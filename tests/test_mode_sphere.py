import pyclesperanto as cle

cle.select_device("TX")


def test_mode_sphere_2d():
    image = cle.asarray(
        [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 3, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 1, 1, 1],
        ]
    )

    reference = cle.asarray(
        [
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 2, 1, 1],
            [0, 2, 2, 1, 1, 1],
        ]
    )

    result = cle.mode_sphere(image, None, 1, 1, 1)

    assert cle.array_equal(result, reference)


def test_mode_sphere_3d():
    image = cle.asarray(
        [
            [
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 3, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 1, 1, 1],
            ]
        ]
    )

    reference = cle.asarray(
        [
            [
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 2, 1, 1],
                [0, 2, 2, 1, 1, 1],
            ]
        ]
    )

    result = cle.mode_sphere(image, None, 1, 1, 1)

    assert cle.array_equal(result, reference)
