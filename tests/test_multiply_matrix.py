import pytest
import numpy as np
import pyclesperanto as cle

cle.select_device("TX")



# @pytest.mark.parametrize("shape", 2 ** np.arange(9, 11), ids=lambda x: f"{x}x{x}")
# @pytest.mark.parametrize("target", ["cpu", "gpu"])
# def test_multiply_matrix(shape, benchmark, target):
#     @benchmark
#     def multiply():
#         a_np = np.random.rand(shape, shape).astype("float32")
#         b_np = np.random.rand(shape, shape).astype("float32")
#         if target == "gpu":
#             # push arrays to GPU
#             gpu_a = cle.push(a_np)
#             gpu_b = cle.push(b_np)
#             # allocate memory for result on GPU
#             gpu_c = cle.create((shape, shape), dtype=float)
#             cle.multiply_matrix(gpu_a, gpu_b, gpu_c)
#             _ = gpu_c.get()
#         else:
#             # multiply matrix on CPU
#             _ = np.dot(a_np.T, b_np.T)
#         # np.testing.assert_allclose(cle.pull(gpu_c), cpu_c, atol=1e-3)


# make a test for matrix multiplication
def test_multiply_matrix():
    matrix_a = np.random.rand(3,3).astype("float32")
    matrix_b = np.random.rand(3,3).astype("float32")

    valid = np.dot(matrix_a, matrix_b)
    matrix_c = cle.multiply_matrix(matrix_a, matrix_b)

    result = cle.pull(matrix_c)

    print(result)
    print(valid)

    assert np.allclose(result, valid, atol=0.001)
