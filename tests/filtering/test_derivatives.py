import numpy as np
import pytest

import pyclesperanto as cle

# ============================================================================
# GRADIENT TESTS
# ============================================================================



def test_gradient_x(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 0, 0],
                [0, 1, 2, 0, 0],
                [0, 1, 3, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0.0, 0.0, 0.0, 0.0, 0.0],
                [1.0, 1.0, -0.5, -1.0, 0.0],
                [1.0, 1.0, -0.5, -1.0, 0.0],
                [1.0, 1.5, -0.5, -1.5, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0],
            ]
        )
    )

    result = cle.gradient_x(test)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)



def test_gradient_y(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0],
                [0, 1, 2, 0, 0],
                [0, 1, 2, 0, 0],
                [0, 1, 3, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [0.0, 1.0, 2.0, 0.0, 0.0],
                [0.0, 0.5, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, -0.5, -1.0, 0.0, 0.0],
                [0.0, -1.0, -3.0, 0.0, 0.0],
            ]
        )
    )

    result = cle.gradient_y(test)

    a = cle.pull(result)
    b = cle.pull(reference)
    print(a)

    assert np.array_equal(a, b)



def test_gradient_z(gpu_backend):
    test = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
            ]
        )
    )

    reference = cle.push(
        np.asarray(
            [
                [
                    [0, 0, 0, 0, 0],
                    [1, 0, 0, -1, 0],
                    [1, 0, 0, -1, 0],
                    [1, 0, 0, -1, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                [
                    [0, 0, 0, 0, 0],
                    [-1, 0, 0, 1, 0],
                    [-1, 0, 0, 1, 0],
                    [-1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0],
                ],
            ]
        )
    )

    result = cle.gradient_z(test)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)

    assert np.array_equal(a, b)


# ============================================================================
# LAPLACE TESTS
# ============================================================================

test_laplace_input = cle.push(
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

laplace_box_reference = cle.push(
    np.asarray(
        [
            [0, 0, 0, 0, 0],
            [0, -1, -1, -1, 0],
            [0, -1, 8, -1, 0],
            [0, -1, -1, -1, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)

laplace_sphere_reference = cle.push(
    np.asarray(
        [
            [0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0],
            [0, -1, 4, -1, 0],
            [0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)



def test_laplace_box(gpu_backend):
    result = cle.create(test_laplace_input)
    cle.laplace(test_laplace_input, result)

    a = cle.pull(result)
    b = cle.pull(laplace_box_reference)

    print(a)

    assert np.array_equal(a, b)



def test_laplace_sphere(gpu_backend):
    result = cle.create(test_laplace_input)
    cle.laplace(test_laplace_input, result, connectivity="sphere")

    a = cle.pull(result)
    b = cle.pull(laplace_sphere_reference)

    print(a)

    assert np.array_equal(a, b)


# ============================================================================
# HESSIAN EIGENVALUES TESTS
# ============================================================================



def test_hessian_eigenvalues_2d(gpu_backend):
    test = np.asarray([[1, -1], [1, -1]])

    reference_small_hessian_eigenvalue = np.asarray([[-2, 0], [-2, 0]])

    reference_large_hessian_eigenvalue = np.asarray([[0, 2], [0, 2]])

    large_hessian_eigenvalue, small_hessian_eigenvalue = cle.hessian_eigenvalues(test)

    print(small_hessian_eigenvalue)
    print(large_hessian_eigenvalue)

    assert np.allclose(reference_small_hessian_eigenvalue, small_hessian_eigenvalue)
    assert np.allclose(reference_large_hessian_eigenvalue, large_hessian_eigenvalue)



def test_hessian_eigenvalues_3d(gpu_backend):
    test = np.asarray(
        [
            [[1, -1], [1, -1]],
            [[2, -2], [2, -2]],
        ]
    )

    reference_small_hessian_eigenvalue = np.asarray(
        [
            [[-2.1, -1.1], [-2.1, -1.1]],
            [[-4.1, 0], [-4.1, 0]],
        ]
    )

    reference_middle_hessian_eigenvalue = np.asarray(
        [
            [[0, 0], [0, 0]],
            [[-0.9, 0.9], [-0.9, 0.9]],
        ]
    )

    reference_large_hessian_eigenvalue = np.asarray(
        [
            [[1.1, 2.1], [1.1, 2.1]],
            [[0, 4.1], [0, 4.1]],
        ]
    )

    (
        large_hessian_eigenvalue,
        middle_hessian_eigenvalue,
        small_hessian_eigenvalue,
    ) = cle.hessian_eigenvalues(test)

    print(small_hessian_eigenvalue)
    print(reference_small_hessian_eigenvalue)
    print()
    print(middle_hessian_eigenvalue)
    print(reference_middle_hessian_eigenvalue)
    print()
    print(large_hessian_eigenvalue)
    print(reference_large_hessian_eigenvalue)

    assert np.allclose(
        reference_small_hessian_eigenvalue, small_hessian_eigenvalue, atol=0.1
    )
    assert np.allclose(
        reference_middle_hessian_eigenvalue, middle_hessian_eigenvalue, atol=0.1
    )
    assert np.allclose(
        reference_large_hessian_eigenvalue, large_hessian_eigenvalue, atol=0.1
    )


# ============================================================================
# LARGE HESSIAN EIGENVALUE TESTS
# ============================================================================



def test_large_hessian_eigenvalue_2d(gpu_backend):
    test = np.asarray([[1, -1], [1, -1]])

    reference_large_hessian_eigenvalue = np.asarray([[0, 2], [0, 2]])

    large_hessian_eigenvalue = cle.large_hessian_eigenvalue(test)

    print(large_hessian_eigenvalue)

    assert np.allclose(reference_large_hessian_eigenvalue, large_hessian_eigenvalue)



def test_large_hessian_eigenvalue_3d(gpu_backend):
    test = np.asarray(
        [
            [[1, -1], [1, -1]],
            [[2, -2], [2, -2]],
        ]
    )

    reference_large_hessian_eigenvalue = np.asarray(
        [
            [[1.1, 2.1], [1.1, 2.1]],
            [[0, 4.1], [0, 4.1]],
        ]
    )

    large_hessian_eigenvalue = cle.large_hessian_eigenvalue(test)

    print(large_hessian_eigenvalue)

    assert np.allclose(
        reference_large_hessian_eigenvalue, large_hessian_eigenvalue, atol=0.1
    )


# ============================================================================
# SMALL HESSIAN EIGENVALUE TESTS
# ============================================================================



def test_small_hessian_eigenvalue_2d(gpu_backend):
    test = np.asarray([[1, -1], [1, -1]])

    reference_small_hessian_eigenvalue = np.asarray([[-2, 0], [-2, 0]])

    small_hessian_eigenvalue = cle.small_hessian_eigenvalue(test)

    print(small_hessian_eigenvalue)

    assert np.allclose(reference_small_hessian_eigenvalue, small_hessian_eigenvalue)



def test_small_hessian_eigenvalue_3d(gpu_backend):
    test = np.asarray(
        [
            [[1, -1], [1, -1]],
            [[2, -2], [2, -2]],
        ]
    )

    reference_small_hessian_eigenvalue = np.asarray(
        [
            [[-2.1, -1.1], [-2.1, -1.1]],
            [[-4.1, 0], [-4.1, 0]],
        ]
    )

    small_hessian_eigenvalue = cle.small_hessian_eigenvalue(test)

    print(small_hessian_eigenvalue)

    assert np.allclose(
        reference_small_hessian_eigenvalue, small_hessian_eigenvalue, atol=0.1
    )
