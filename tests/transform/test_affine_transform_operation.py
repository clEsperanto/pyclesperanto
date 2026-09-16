import numpy as np
import pytest

import pyclesperanto as cle


def test_affine_transform_with_none_is_identity(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))

    result = cle.transform.affine_transform(source)

    assert result.shape == source.shape
    assert np.allclose(cle.pull(result), cle.pull(source), atol=1e-5)


def test_affine_transform_with_affine_transform_instance(gpu_backend):
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

    transform = cle.transform.AffineTransform()
    transform.translate(-1, -1, 0)

    result = cle.transform.affine_transform(source, transform_matrix=transform)

    assert np.array_equal(cle.pull(result), cle.pull(reference))


def test_affine_transform_with_4x4_numpy_array(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))
    matrix = np.eye(4, dtype=np.float32)
    matrix[0, 3] = 1  # translate x by 1

    result = cle.transform.affine_transform(source, transform_matrix=matrix)

    assert result.shape == source.shape


def test_affine_transform_with_flat_list(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))
    flat = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

    result = cle.transform.affine_transform(source, transform_matrix=flat)

    assert result.shape == source.shape


def test_affine_transform_combined_rotate_and_translate(gpu_backend):
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
        ).astype(np.float32)
    )

    transform = cle.transform.AffineTransform()
    transform.center(source.shape[::-1], undo=False)
    transform.rotate_around_z_axis(90)
    transform.center(source.shape[::-1], undo=True)

    result = cle.transform.affine_transform(source, transform_matrix=transform, interpolate=False)

    assert result.shape == source.shape
    # a 90 degree rotation around the center should preserve the number of foreground pixels
    assert np.sum(cle.pull(result) > 0) == np.sum(cle.pull(source) > 0)


def test_affine_transform_with_resize_grows_output(gpu_backend):
    source = cle.push(np.ones((1, 5, 5), dtype=np.float32))

    transform = cle.transform.AffineTransform()
    transform.rotate_around_z_axis(45)

    result = cle.transform.affine_transform(source, transform_matrix=transform, resize=True)

    assert result.shape[1] > source.shape[1] or result.shape[2] > source.shape[2]


def test_affine_transform_output_image_reused(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))
    destination = cle.create(source.shape, dtype=np.float32)

    transform = cle.transform.AffineTransform()
    transform.translate(1, 0, 0)

    result = cle.transform.affine_transform(source, output_image=destination, transform_matrix=transform)

    assert result is destination


def test_affine_transform_deprecated_transform_param_warns(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))
    matrix = np.eye(4, dtype=np.float32)

    with pytest.deprecated_call():
        cle.transform.affine_transform(source, transform=matrix)


@pytest.mark.skip_backend("metal", reason="known CLIc Metal kernel bug in the interpolate=True affine_transform path")
@pytest.mark.skip_backend("cuda", reason="known CLIc CUDA kernel bug in the interpolate=True affine_transform path")
def test_affine_transform_deprecated_linear_interpolation_param_warns(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))

    with pytest.deprecated_call():
        cle.transform.affine_transform(source, transform_matrix=None, linear_interpolation=True)


def test_affine_transform_deprecated_auto_size_param_warns(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))

    with pytest.deprecated_call():
        cle.transform.affine_transform(source, transform_matrix=None, auto_size=True)


def test_compute_output_shape(gpu_backend):
    source = cle.push(np.ones((1, 5, 5), dtype=np.float32))

    transform = cle.transform.AffineTransform()
    transform.rotate_around_z_axis(45)

    output_shape, updated_transform = cle.transform.compute_output_shape_from_transform(source.shape, transform)

    assert len(output_shape) == 3
    assert isinstance(updated_transform, cle.transform.AffineTransform)
    assert output_shape[1] > source.shape[1] or output_shape[2] > source.shape[2]


def test_compute_output_shape_requires_affine_transform_instance(gpu_backend):
    source = cle.push(np.ones((1, 5, 5), dtype=np.float32))

    with pytest.raises(TypeError):
        cle.transform.compute_output_shape_from_transform(source.shape, [1, 0, 0, 0])


def test_affine_transform_requires_affine_transform_instance(gpu_backend):
    source = cle.push(np.random.random((3, 5, 5)).astype(np.float32))

    with pytest.raises(TypeError):
        cle.transform.affine_transform(source, transform_matrix=[1, 0, 0, 0])


