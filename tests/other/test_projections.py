import numpy as np

import pyclesperanto as cle
import pytest
# ============================================================================
# MAXIMUM PROJECTIONS
# ============================================================================


@pytest.mark.backend
def test_maximum_x_projection(gpu_backend):
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
                [9, 8, 8, 8, 9],
                [8, 9, 10, 9, 7],
                [10, 10, 7, 7, 10],
                [7, 7, 9, 10, 8],
                [10, 10, 10, 10, 10],
            ]
        )
    )

    result = cle.create(reference)
    cle.maximum_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


@pytest.mark.backend
def test_maximum_x_projection_of_pointlist(gpu_backend):
    positions_and_values = cle.push(np.asarray([[0, 0, 2, 3, 5], [0, 1, 3, 2, 6]]))

    reference = cle.push(np.asarray([[5], [6]]))

    result = cle.maximum_x_projection(positions_and_values)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.array_equal(a, b)


@pytest.mark.backend
def test_maximum_y_projection(gpu_backend):
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
                [5, 4, 6, 8, 10],
                [5, 4, 6, 8, 10],
                [5, 4, 6, 8, 10],
                [5, 4, 6, 8, 10],
                [5, 4, 6, 8, 10],
            ]
        )
    )

    result = cle.create(reference)
    cle.maximum_y_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


@pytest.mark.backend
def test_maximum_y_projection2(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [1, 0, 0, 0, 9],
                [0, 2, 0, 8, 0],
                [3, 0, 1, 0, 10],
            ]
        )
    )

    reference = cle.push(np.asarray([3, 2, 1, 8, 10]))

    result = cle.maximum_y_projection(test1)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


@pytest.mark.backend
def test_maximum_y_projection_against_numpy(gpu_backend):
    from skimage.data import camera

    image = camera()

    max_cle = cle.maximum_y_projection(image)
    max_np = image.max(axis=0)

    print(max_cle.get())
    print(max_np)

    assert np.array_equal(max_cle.get(), max_np)


@pytest.mark.backend
def test_maximum_y_projection_against_numpy_small(gpu_backend):
    from skimage.data import camera

    image = camera()[0:2, 0:10]

    max_cle = cle.maximum_y_projection(image)
    max_np = image.max(axis=0)

    print(max_cle.get())
    print(max_np)

    assert np.array_equal(max_cle.get(), max_np)


# Maximum Z Projection tests
test1_z = cle.push(
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

reference_z = cle.push(
    np.asarray(
        [
            [1, 2, 0, 8, 9],
            [3, 4, 1, 8, 10],
            [3, 4, 1, 7, 10],
            [3, 4, 1, 8, 10],
            [5, 0, 6, 0, 10],
        ]
    )
)


@pytest.mark.backend
def test_maximum_z_projection(gpu_backend):
    result = cle.create(reference_z)

    cle.maximum_z_projection(test1_z, result)

    a = cle.pull(result)
    b = cle.pull(reference_z)

    print(a)

    assert np.array_equal(a, b)


@pytest.mark.backend
def test_maximum_z_projection_creator(gpu_backend):
    result = cle.maximum_z_projection(test1_z)

    a = cle.pull(result)
    b = cle.pull(reference_z)

    print(a)

    assert np.array_equal(a, b)


@pytest.mark.backend
def test_maximum_z_projection_creator_passing_none(gpu_backend):
    result = cle.maximum_z_projection(test1_z, None)

    a = cle.pull(result)
    b = cle.pull(reference_z)

    print(a)

    assert np.array_equal(a, b)


# ============================================================================
# MEAN PROJECTIONS
# ============================================================================


@pytest.mark.backend
def test_mean_x_projection(gpu_backend):
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
                [2, 2.0, 2.0, 2.0, 2.0],
                [2, 2.0, 2.8, 2.0, 2.2],
                [2.8, 2.8, 2.2, 2.2, 2.8],
                [2.2, 2.2, 2.0, 2.8, 2.0],
                [4.2, 4.2, 4.2, 4.2, 4.2],
            ]
        )
    )

    result = cle.create(reference)
    cle.mean_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert np.allclose(a, b, 0.001)


@pytest.mark.backend
def test_mean_y_projection(gpu_backend):
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
                [1.8, 1.2, 1.4, 3, 5.8],
                [1.8, 1.2, 1.4, 3, 5.8],
                [1.8, 1.2, 1.4, 3, 5.8],
                [1.8, 1.2, 1.4, 3, 5.8],
                [1.8, 1.2, 1.4, 3, 5.8],
            ]
        )
    )

    result = cle.create(reference)
    cle.mean_y_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.001)


@pytest.mark.backend
def test_mean_z_projection(gpu_backend):
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
                [0.4, 1.2, 0, 4.8, 3.6],
                [1, 1.2, 0.2, 3, 5.6],
                [1.8, 1.6, 0.6, 2.8, 6],
                [0.8, 2, 0.2, 4.4, 3.8],
                [5, 0, 6, 0, 10],
            ]
        )
    )

    result = cle.create(reference)
    cle.mean_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.001)


# ============================================================================
# MINIMUM PROJECTIONS
# ============================================================================


@pytest.mark.backend
def test_minimum_x_projection(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 0, 0, 0, 1],
                    [0, 2, 0, 8, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [1, 0, 0, 0, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [1, 0, 0, 0, 1],
                    [0, 4, 0, 7, 1],
                    [3, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [1, 0, 0, 0, 1],
                    [0, 4, 0, 7, 1],
                    [3, 0, 1, 0, 1],
                    [0, 2, 0, 8, 1],
                    [1, 1, 1, 1, 1],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ]
        )
    )

    result = cle.create(reference)
    cle.minimum_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.001)


@pytest.mark.backend
def test_minimum_y_projection(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 0, 0, 0, 1],
                    [0, 2, 0, 8, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [1, 0, 0, 0, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [1, 0, 0, 0, 1],
                    [0, 4, 0, 7, 1],
                    [3, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [1, 0, 0, 0, 1],
                    [0, 4, 0, 7, 1],
                    [3, 0, 1, 0, 1],
                    [0, 2, 0, 8, 1],
                    [1, 1, 1, 1, 1],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
            ]
        )
    )

    result = cle.create(reference)
    cle.minimum_y_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.001)


@pytest.mark.backend
def test_minimum_z_projection(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [
                    [1, 0, 0, 0, 1],
                    [0, 2, 0, 8, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [1, 0, 0, 0, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [3, 0, 1, 0, 1],
                    [0, 4, 0, 7, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [0, 2, 0, 8, 1],
                    [1, 0, 0, 0, 1],
                    [0, 4, 0, 7, 1],
                    [3, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                [
                    [1, 0, 0, 0, 1],
                    [0, 4, 0, 7, 1],
                    [3, 0, 1, 0, 1],
                    [0, 2, 0, 8, 1],
                    [1, 1, 1, 1, 1],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ]
        )
    )

    result = cle.create(reference)
    cle.minimum_z_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(b)
    print(a)

    assert np.allclose(a, b, 0.001)


# ============================================================================
# SUM PROJECTIONS
# ============================================================================


@pytest.mark.backend
def test_sum_x_projection(gpu_backend):
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
                [10.0, 10.0, 10.0, 10.0, 10.0],
                [10.0, 10.0, 14.0, 10.0, 11.0],
                [14.0, 14.0, 11.0, 11.0, 14.0],
                [11.0, 11.0, 10.0, 14.0, 10.0],
                [21.0, 21.0, 21.0, 21.0, 21.0],
            ]
        )
    )

    result = cle.create(reference)
    cle.sum_x_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.01)


@pytest.mark.backend
def test_sum_y_projection(gpu_backend):
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
                [9, 6, 7, 15, 29],
                [9, 6, 7, 15, 29],
                [9, 6, 7, 15, 29],
                [9, 6, 7, 15, 29],
                [9, 6, 7, 15, 29],
            ]
        )
    )

    result = cle.create(reference)
    cle.sum_y_projection(test1, result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.allclose(a, b, 0.01)


@pytest.mark.backend
def test_sum_z_projection(gpu_backend):
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


@pytest.mark.backend
def test_sum_z_projection2(gpu_backend):
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

    result = cle.sum_z_projection(test1)

    a = cle.pull(result)

    # Expected values (note: may be different shape due to projection)
    expected = np.asarray([2, 6])

    print(a)
    print(expected)

    assert np.allclose(a, expected)
