import numpy as np
import pytest

import pyclesperanto as cle


def test_identity():
    transform = cle.transform.AffineTransform()
    assert np.allclose(transform.get_matrix(), np.eye(4))


def test_init_from_flat_list():
    flat = [1, 0, 0, 10, 0, 2, 0, 20, 0, 0, 3, 30, 0, 0, 0, 1]
    transform = cle.transform.AffineTransform(flat)
    expected = np.array(flat, dtype=np.float32).reshape(4, 4)
    assert np.allclose(transform.get_matrix(), expected)


def test_init_from_flat_tuple():
    flat = (1, 0, 0, 10, 0, 2, 0, 20, 0, 0, 3, 30, 0, 0, 0, 1)
    transform = cle.transform.AffineTransform(flat)
    expected = np.array(flat, dtype=np.float32).reshape(4, 4)
    assert np.allclose(transform.get_matrix(), expected)


def test_init_from_wrong_length_list_raises():
    with pytest.raises((ValueError, RuntimeError)):
        cle.transform.AffineTransform([1, 2, 3])


def test_init_from_4x4_numpy_array():
    matrix = np.array(
        [[1, 0, 0, 10], [0, 2, 0, 20], [0, 0, 3, 30], [0, 0, 0, 1]], dtype=np.float32
    )
    transform = cle.transform.AffineTransform(matrix)
    assert np.allclose(transform.get_matrix(), matrix)


def test_init_from_flat_numpy_array():
    matrix = np.array(
        [[1, 0, 0, 10], [0, 2, 0, 20], [0, 0, 3, 30], [0, 0, 0, 1]], dtype=np.float32
    )
    transform = cle.transform.AffineTransform(matrix.flatten())
    assert np.allclose(transform.get_matrix(), matrix)


def test_init_from_nested_list():
    matrix = [[1, 0, 0, 10], [0, 2, 0, 20], [0, 0, 3, 30], [0, 0, 0, 1]]
    transform = cle.transform.AffineTransform(matrix)
    assert np.allclose(transform.get_matrix(), np.array(matrix, dtype=np.float32))


def test_init_from_wrong_shape_array_raises():
    with pytest.raises((ValueError, RuntimeError, TypeError)):
        cle.transform.AffineTransform(np.eye(4, dtype=np.float32)[:2])


def test_init_from_3x3_numpy_array_embeds_into_4x4():
    matrix_2d = np.array([[1, 0, 10], [0, 2, 20], [0, 0, 1]], dtype=np.float32)
    transform = cle.transform.AffineTransform(matrix_2d)

    expected = np.eye(4, dtype=np.float32)
    expected[:2, :2] = matrix_2d[:2, :2]
    expected[:2, 3] = matrix_2d[:2, 2]

    assert np.allclose(transform.get_matrix(), expected)


def test_init_from_9_element_flat_list_embeds_into_4x4():
    flat = [1, 0, 10, 0, 2, 20, 0, 0, 1]
    transform = cle.transform.AffineTransform(flat)

    expected = np.eye(4, dtype=np.float32)
    expected[:2, :2] = [[1, 0], [0, 2]]
    expected[:2, 3] = [10, 20]

    assert np.allclose(transform.get_matrix(), expected)


def test_copy_constructor():
    original = cle.transform.AffineTransform()
    original.translate(1, 2, 3)

    copy = cle.transform.AffineTransform(original)
    assert np.allclose(copy.get_matrix(), original.get_matrix())

    # copy must be independent from the original
    copy.translate(10, 10, 10)
    assert not np.allclose(copy.get_matrix(), original.get_matrix())


def test_scale():
    transform = cle.transform.AffineTransform()
    transform.scale(2, 3, 4)
    assert np.allclose(np.diag(transform.get_matrix()), [2, 3, 4, 1])


def test_translate():
    transform = cle.transform.AffineTransform()
    transform.translate(10, 20, 30)
    assert np.allclose(transform.get_matrix()[:3, 3], [10, 20, 30])


def test_rotate_around_z_axis():
    transform = cle.transform.AffineTransform()
    transform.rotate_around_z_axis(90)
    assert np.allclose(transform.get_matrix()[:2, :2], [[0, -1], [1, 0]], atol=1e-6)


def test_rotate_around_x_axis():
    transform = cle.transform.AffineTransform()
    transform.rotate_around_x_axis(90)
    assert np.allclose(transform.get_matrix()[1:3, 1:3], [[0, -1], [1, 0]], atol=1e-6)


def test_rotate_around_y_axis():
    transform = cle.transform.AffineTransform()
    transform.rotate_around_y_axis(90)
    assert abs(transform.get_matrix()[0, 2] - 1) < 1e-6


def test_rotate_generic_axis_matches_named_axis():
    transform_generic = cle.transform.AffineTransform()
    transform_generic.rotate(2, 45)

    transform_named = cle.transform.AffineTransform()
    transform_named.rotate_around_z_axis(45)

    assert np.allclose(transform_generic.get_matrix(), transform_named.get_matrix())


def test_rotate_invalid_axis_raises():
    transform = cle.transform.AffineTransform()
    with pytest.raises(RuntimeError):
        transform.rotate(7, 10)


def test_center():
    transform = cle.transform.AffineTransform()
    transform.center((50, 40, 30), False)
    assert np.allclose(transform.get_matrix()[:3, 3], [-25, -20, -15])


def test_center_undo():
    transform = cle.transform.AffineTransform()
    transform.center((50, 40, 30), True)
    assert np.allclose(transform.get_matrix()[:3, 3], [25, 20, 15])


def test_shear_in_z_plane():
    transform = cle.transform.AffineTransform()
    transform.shear_in_z_plane(45, 0)
    assert np.allclose(transform.get_matrix()[0, 1], 1.0, atol=1e-5)


def test_shear_in_y_plane():
    transform = cle.transform.AffineTransform()
    transform.shear_in_y_plane(45, 0)
    assert np.allclose(transform.get_matrix()[0, 2], 1.0, atol=1e-5)


def test_shear_in_x_plane():
    transform = cle.transform.AffineTransform()
    transform.shear_in_x_plane(45, 0)
    assert np.allclose(transform.get_matrix()[1, 2], 1.0, atol=1e-5)


def test_shear_out_of_range_raises():
    transform = cle.transform.AffineTransform()
    with pytest.raises(RuntimeError):
        transform.shear_in_z_plane(120, 0)


def test_deskew_x():
    transform = cle.transform.AffineTransform()
    transform.deskew_x(32, 0.5, 0.5, 0.5, 1.0)
    matrix = transform.get_matrix()
    assert matrix.shape == (4, 4)
    assert np.isfinite(matrix).all()


def test_deskew_y():
    transform = cle.transform.AffineTransform()
    transform.deskew_y(32, 0.5, 0.5, 0.5, 1.0)
    matrix = transform.get_matrix()
    assert matrix.shape == (4, 4)
    assert np.isfinite(matrix).all()


def test_get_inverse():
    transform = cle.transform.AffineTransform()
    transform.rotate_around_y_axis(30)
    transform.translate(3, 4, 5)

    matrix = transform.get_matrix()
    inverse = transform.get_inverse()

    assert np.allclose(matrix @ inverse, np.eye(4), atol=1e-5)


def test_get_transpose():
    transform = cle.transform.AffineTransform()
    transform.rotate_around_y_axis(30)
    transform.translate(3, 4, 5)

    matrix = transform.get_matrix()
    transpose = transform.get_transpose()

    assert np.allclose(transpose, matrix.T)


def test_get_inverse_transpose():
    transform = cle.transform.AffineTransform()
    transform.rotate_around_y_axis(30)
    transform.translate(3, 4, 5)

    matrix = transform.get_matrix()
    inverse_transpose = transform.get_inverse_transpose()

    assert np.allclose(inverse_transpose, np.linalg.inv(matrix).T, atol=1e-5)


def test_to_array_matches_flat_column_major_storage():
    matrix = np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        dtype=np.float32,
    )
    flat = cle.transform.AffineTransform.to_array(matrix)
    assert len(flat) == 16
    assert list(flat) == [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]


def test_to_array_wrong_shape_raises():
    with pytest.raises((ValueError, RuntimeError, TypeError)):
        cle.transform.AffineTransform.to_array(np.eye(3, dtype=np.float32))


def test_array_protocol():
    transform = cle.transform.AffineTransform()
    transform.translate(1, 2, 3)

    array = np.asarray(transform)
    assert array.shape == (4, 4)
    assert array.dtype == np.float32
    assert np.allclose(array, transform.get_matrix())

    array2 = np.array(transform)
    assert np.allclose(array2, transform.get_matrix())


def test_str_and_repr():
    transform = cle.transform.AffineTransform()
    assert "AffineTransform" in str(transform)
    assert "1" in repr(transform)
