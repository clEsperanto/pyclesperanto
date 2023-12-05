import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


def test_add():
    input1 = cle.push(np.asarray([1, 2, 3]))
    input2 = cle.push(np.asarray([4, 5, 6]))
    reference = cle.push(np.asarray([5, 7, 9]))

    output = input1 + input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_add_with_scalar():
    input1 = cle.push(np.asarray([[1, 2, 3]]))
    input2 = 5
    reference = cle.push(np.asarray([[6, 7, 8]]))

    output = input1 + input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_add_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[6, 4, -6]]))

    output = input1 + input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_iadd():
    input1 = cle.push(np.asarray([[1, 2, 3]]))
    input2 = cle.push(np.asarray([[4, 5, 6]]))
    reference = cle.push(np.asarray([[5, 7, 9]]))

    input1 += input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_iadd_with_scalar():
    input1 = cle.push(np.asarray([[1, 2, 3]]))
    input2 = 5
    reference = cle.push(np.asarray([[6, 7, 8]]))

    input1 += input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_iadd_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[6, 4, -6]]))

    input1 += input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_subtract():
    input1 = cle.push(np.asarray([[4, 2, 3]]))
    input2 = cle.push(np.asarray([[1, 5, 6]]))
    reference = cle.push(np.asarray([[3, -3, -3]]))

    output = input1 - input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_subtract_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, 3]]))
    input2 = 5
    reference = cle.push(np.asarray([[-1, -3, -2]]))

    output = input1 - input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_subtract_with_np():
    input1 = cle.push(np.asarray([[4, 2, 3]]))
    input2 = np.asarray([[1, 5, 6]])
    reference = cle.push(np.asarray([[3, -3, -3]]))

    output = input1 - input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_isubtract():
    input1 = cle.push(np.asarray([[4, 2, 3]]))
    input2 = cle.push(np.asarray([[1, 5, 6]]))
    reference = cle.push(np.asarray([[3, -3, -3]]))

    input1 -= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_isubtract_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, 3]]))
    input2 = 5
    reference = cle.push(np.asarray([[-1, -3, -2]]))

    input1 -= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_isubtract_with_np():
    input1 = cle.push(np.asarray([[4, 2, 3]]))
    input2 = np.asarray([[1, 5, 6]])
    reference = cle.push(np.asarray([[3, -3, -3]]))

    input1 -= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_divide():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[2, 1, -4]]))

    output = input1 / input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_divide_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[2, 1, -4]]))

    output = input1 / input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_divide_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[2, 1, -4]]))

    output = input1 / input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_idivide():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[2, 1, -4]]))

    input1 /= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_idivide_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[2, 1, -4]]))

    input1 /= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_idivide_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[2, 1, -4]]))

    input1 /= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_multiply():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[8, 4, -16]]))

    output = input1 * input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_multiply_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[8, 4, -16]]))

    output = input1 * input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_multiply_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[8, 4, -16]]))

    output = input1 * input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_imultiply():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[8, 4, -16]]))

    input1 *= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_imultiply_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[8, 4, -16]]))

    input1 *= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_imultiply_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[8, 4, -16]]))

    input1 *= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_gt():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[1, 0, 0]]))

    output = input1 > input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_gt_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[1, 0, 0]]))

    output = input1 > input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_gt_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[1, 0, 0]]))

    output = input1 > input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ge():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[1, 1, 0]]))

    output = input1 >= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ge_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[1, 1, 0]]))

    output = input1 >= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ge_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[1, 1, 0]]))

    output = input1 >= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_lt():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[0, 0, 1]]))

    output = input1 < input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_lt_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[0, 0, 1]]))

    output = input1 < input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_lt_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[0, 0, 1]]))

    output = input1 < input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_le():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[0, 1, 1]]))

    output = input1 <= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_le_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[0, 1, 1]]))

    output = input1 <= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_le_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[0, 1, 1]]))

    output = input1 <= input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_eq():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[0, 1, 0]]))

    output = input1 == input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_eq_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[0, 1, 0]]))

    output = input1 == input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_eq_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[0, 1, 0]]))

    output = input1 == input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ne():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[1, 0, 1]]))

    output = input1 != input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ne_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[1, 0, 1]]))

    output = input1 != input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ne_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[1, 0, 1]]))

    output = input1 != input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_pos():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    reference = cle.push(np.asarray([[4, 2, -8]]))

    output = +input1
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_neg():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    reference = cle.push(np.asarray([[-4, -2, 8]]))

    output = -input1
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_power():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[16, 4, 64]]))

    output = input1**input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_power_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[16, 4, 64]]))

    output = input1**input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_power_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[16, 4, 64]]))

    output = input1**input2
    result = cle.pull(output)

    print(result)

    assert np.array_equal(result, reference)


def test_ipower():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = cle.push(np.asarray([[2, 2, 2]]))
    reference = cle.push(np.asarray([[16, 4, 64]]))

    input1 **= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_ipower_with_scalar():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = 2
    reference = cle.push(np.asarray([[16, 4, 64]]))

    input1 **= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_ipower_with_np():
    input1 = cle.push(np.asarray([[4, 2, -8]]))
    input2 = np.asarray([[2, 2, 2]])
    reference = cle.push(np.asarray([[16, 4, 64]]))

    input1 **= input2
    result = cle.pull(input1)

    print(result)

    assert np.array_equal(result, reference)


def test_ipow_with_types():
    scalars = [
        2,
        int(2),
        float(2),
        np.asarray([[2]]).astype(np.int8).max(),
        np.asarray([[2]]).astype(np.uint8).max(),
        np.asarray([[2]]).astype(np.int16).max(),
        np.asarray([[2]]).astype(np.uint16).max(),
        np.asarray([[2]]).astype(np.int32).max(),
        np.asarray([[2]]).astype(np.uint32).max(),
        np.asarray([[2]]).astype(np.int64).max(),
        np.asarray([[2]]).astype(np.uint64).max(),
        np.asarray([[2]]).astype(np.float32).max(),
        np.asarray([[2]]).astype(np.float64).max(),
        2,
    ]

    for input2 in scalars:
        print("Testing type", type(input2))

        input1 = cle.push(np.asarray([[4, 2, -8]]))
        reference = cle.push(np.asarray([[16, 4, 64]]))

        input1 **= input2
        result = cle.pull(input1)

        print(result)

        assert np.array_equal(result, reference)
