import numpy as np
import pytest

import pyclesperanto as cle

# ============================================================================
# DILATE BOX TESTS
# ============================================================================


def test_dilate(gpu_backend):
    test_simple = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    test_simple_box_expected = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test_simple)
    cle.binary_dilate(test_simple, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(test_simple_box_expected)
    assert np.array_equal(a, b)


# ============================================================================
# DILATE SPHERE TESTS
# ============================================================================


def test_dilate_sphere(gpu_backend):
    test_simple = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    test_simple_sphere_expected = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test_simple)
    cle.binary_dilate(test_simple, result, connectivity="sphere")

    print(result)

    a = cle.pull(result)
    b = cle.pull(test_simple_sphere_expected)
    assert np.array_equal(a, b)


# ============================================================================
# ERODE BOX TESTS
# ============================================================================


def test_erode_box(gpu_backend):

    test_square = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    test_square_eroded_expected = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    result = cle.create(test_square)
    cle.binary_erode(test_square, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(test_square_eroded_expected)
    assert np.array_equal(a, b)


# ============================================================================
# ERODE SPHERE TESTS
# ============================================================================


def test_erode_sphere(gpu_backend):

    test_square = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    test_square_eroded_expected = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    result = cle.create(test_square)
    cle.binary_erode(test_square, result, connectivity="sphere")

    print(result)

    a = cle.pull(result)
    b = cle.pull(test_square_eroded_expected)
    assert np.array_equal(a, b)


# ============================================================================
# OPENING TESTS
# ============================================================================


def test_opening_box_old(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.opening_box(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_opening_box_2d(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.grayscale_opening(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)


def test_opening_sphere_old(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.opening_sphere(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_opening_sphere(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.grayscale_opening(
        gpu_input, radius_x=1, radius_y=1, connectivity="sphere"
    )

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


# ============================================================================
# CLOSING TESTS
# ============================================================================


def test_close_box_old(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 2, 2],
                [1, 1, 1, 1, 2, 2],
                [1, 0, 0, 0, 2, 2],
                [3, 0, 0, 0, 2, 2],
            ]
        )
    )

    gpu_output = cle.closing_box(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_close_box_2d(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 2, 2],
                [1, 1, 1, 1, 2, 2],
                [1, 0, 0, 0, 2, 2],
                [3, 0, 0, 0, 2, 2],
            ]
        )
    )

    gpu_output = cle.grayscale_closing(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_closing_sphere_old(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 2, 0],
                [1, 1, 1, 1, 2, 2],
                [1, 1, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.closing_sphere(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_closing_sphere(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 2, 0],
                [1, 1, 1, 1, 2, 2],
                [1, 1, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.grayscale_closing(
        gpu_input, radius_x=1, radius_y=1, connectivity="sphere"
    )

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


# ============================================================================
# TOP HAT TESTS
# ============================================================================


def test_top_hat_box(gpu_backend):
    gpu_input = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 2, 0],
                [1, 1, 1, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [0, 0, 0, 0, 2, 0],
                [3, 0, 0, 0, 0, 0],
            ]
        )
    )

    gpu_output = cle.top_hat_box(gpu_input, radius_x=1, radius_y=1)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


def test_top_hat_sphere(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 50, 50, 50, 0],
                [0, 50, 100, 50, 0],
                [0, 50, 50, 50, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create(test)
    cle.top_hat(test, result, 1, 1, 0, connectivity="sphere")

    print(result)

    a = cle.pull(result)
    assert np.min(a) == 0
    assert np.max(a) == 50


# ============================================================================
# BOTTOM HAT TESTS
# ============================================================================


def test_bottom_hat_box(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 50, 50, 50, 0],
                [0, 50, 100, 50, 0],
                [0, 50, 50, 50, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create_like(test)
    cle.bottom_hat(test, result, 1, 1, 0)

    print(result)

    a = cle.pull(result)
    assert np.min(a) == 0
    assert np.max(a) == 50


def test_bottom_hat_sphere(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 50, 50, 50, 0],
                [0, 50, 100, 50, 0],
                [0, 50, 50, 50, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    result = cle.create_like(test)
    cle.bottom_hat(test, result, 1, 1, 0, "sphere")

    print(result)

    a = cle.pull(result)
    assert np.min(a) == 0
    assert np.max(a) == 50
