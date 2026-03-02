import numpy as np

import pyclesperanto as cle


def test_rotate():
    source = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
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
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                ]
            ]
        )
    )

    result = cle.rotate(source, angle_z=60.0, centered=False)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_rotate_around_center():
    source = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1],
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
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                ]
            ]
        )
    )

    result = cle.rotate(source, angle_z=90.0, centered=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_rotation_auto_size():
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
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    result = cle.rotate(source, angle_z=45, resize=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_scale_centered():
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
                    [0, 0, 1, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    result = cle.scale(source, factor_y=2)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_scale_not_centered():
    source = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
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
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    result = cle.scale(source, factor_y=2, centered=False)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_scale_auto_size():
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
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            ]
        )
    )

    result = cle.scale(source, factor_x=2, factor_y=2, resize=True)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_translate():
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

    result = cle.translate(source, translate_x=-1, translate_y=-1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)
