import numpy as np

import pyclesperanto as cle
import pytest
# ============================================================================
# BINARY AND
# ============================================================================


@pytest.mark.backend
def test_binary_and_1(gpu_backend):
    test = cle.push(np.asarray([[1, 0], [1, 0]]))

    test1 = cle.push(np.asarray([[1, 1], [0, 0]]))

    test2 = cle.create(test)
    cle.binary_and(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.25


@pytest.mark.backend
def test_binary_and_2(gpu_backend):
    a = np.asarray([[1, 0], [1, 0]])
    b = np.asarray([[1, 1], [0, 0]])
    gpu_a = cle.push(a)
    gpu_b = cle.push(b)
    gpu_c = cle.create(gpu_a)
    cle.binary_and(gpu_a, gpu_b, gpu_c)

    result = cle.pull(gpu_c)
    assert np.allclose(result, a & b)


# ============================================================================
# BINARY OR
# ============================================================================


@pytest.mark.backend
def test_binary_or(gpu_backend):
    test = cle.push(np.asarray([[1, 0], [1, 0]]))

    test1 = cle.push(np.asarray([[1, 1], [0, 0]]))

    test2 = cle.create(test)
    cle.binary_or(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.75


# ============================================================================
# BINARY XOR
# ============================================================================


@pytest.mark.backend
def test_binary_xor(gpu_backend):
    test = cle.push(np.asarray([[1, 0], [1, 0]]))

    test1 = cle.push(np.asarray([[1, 1], [0, 0]]))

    test2 = cle.create(test)
    cle.binary_xor(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.5


# ============================================================================
# BINARY NOT
# ============================================================================


@pytest.mark.backend
def test_binary_not(gpu_backend):
    test1 = cle.push(np.asarray([[1, 1], [1, 0]]))

    test2 = cle.create(test1)
    cle.binary_not(test1, test2)

    print(test2)
    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.25


# ============================================================================
# BINARY SUBTRACT
# ============================================================================


@pytest.mark.backend
def test_binary_subtract(gpu_backend):
    test = cle.push(np.asarray([[1, 0], [1, 0]]))

    test1 = cle.push(np.asarray([[1, 1], [0, 0]]))

    test2 = cle.create(test)
    cle.binary_subtract(test, test1, test2)

    print(test2)

    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) == 0.25


# ============================================================================
# BINARY EDGE DETECTION
# ============================================================================


@pytest.mark.backend
def test_binary_edge_detection(gpu_backend):
    test1 = cle.push(
        np.asarray(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
            ]
        )
    )

    test2 = cle.create_like(test1)
    cle.binary_edge_detection(test1, test2)

    print(test2)
    a = cle.pull(test2)
    assert np.min(a) == 0
    assert np.max(a) == 1
    assert np.mean(a) - 12 / 36 < 0.001
