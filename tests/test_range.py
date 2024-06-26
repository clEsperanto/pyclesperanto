import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_range1():
    image = cle.push(np.asarray([[0, 1, 2], [2, 3, 4], [5, 6, 7]]))

    reference = cle.push(np.asarray([[3, 4], [6, 7]]))

    crop = image[1:, 1:]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)


def test_range2():
    image = cle.push(np.asarray([[0, 1, 2], [2, 3, 4], [5, 6, 7]]))

    reference = cle.push(np.asarray([[0, 1], [2, 3]]))

    crop = image[:2, :2]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)


def test_range3():
    image = cle.push(np.asarray([[[0, 1, 2], [2, 3, 4], [5, 6, 7]]]))

    reference = cle.push(np.asarray([[[3, 4], [6, 7]]]))

    crop = image[:, 1:, 1:]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)


def test_range4():
    image = cle.push(np.asarray([[[0, 1, 2], [2, 3, 4], [5, 6, 7]]]))

    reference = cle.push(np.asarray([[[0, 1], [2, 3]]]))

    crop = image[:, :2, :2]

    print(reference)
    print(crop)

    assert np.array_equal(crop, reference)


def test_range5():
    image = cle.push(np.random.random((10, 20, 30)))

    crop = image[:5]

    assert crop.shape[0] == 5
    assert crop.shape[1] == 20
    assert crop.shape[2] == 30


def test_range6():
    image = cle.push(np.random.random((10, 20, 30)))

    crop = image[5]

    assert crop.shape[0] == 20
    assert crop.shape[1] == 30
    assert len(crop.shape) == 2


def test_range7():
    image = cle.push(np.random.random((10, 20, 30)))

    crop = image[5, :]

    assert crop.shape[0] == 20
    assert crop.shape[1] == 30
    assert len(crop.shape) == 2


def test_range8():
    image = cle.push(np.random.random((10, 20, 30)))

    crop = image[:, :, 5]

    assert crop.shape[0] == 10
    assert crop.shape[1] == 20
    assert len(crop.shape) == 2


def test_range9():
    image = cle.push(np.random.random((10, 20, 30)))

    crop = image[:, 5]

    assert crop.shape[0] == 10
    assert crop.shape[1] == 30
    assert len(crop.shape) == 2


def test_range_against_numpy_1():
    input = np.random.random((2, 3, 4))
    input_gpu = cle.push(input)

    reference = input[1, :, :]
    result = input_gpu[1, :, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_2():
    input = np.random.random((2, 3, 4))
    input_gpu = cle.push(input)

    reference = input[:, 1, :]
    result = input_gpu[:, 1, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_3():
    input = np.random.random((2, 3, 4))
    input_gpu = cle.push(input)

    reference = input[:, :, 1]
    result = input_gpu[:, :, 1]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_4():
    input = np.random.random((2, 3, 4))
    input_gpu = cle.push(input)

    reference = input[1, :]
    result = input_gpu[1, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_5():
    input = np.random.random((2, 3, 4))
    input_gpu = cle.push(input)

    reference = input[1]
    result = input_gpu[1]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_6():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[2:5, :, :]
    result = input_gpu[2:5, :, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_7():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, 10:15, :]
    result = input_gpu[:, 10:15, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_8():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, :, 10:15]
    result = input_gpu[:, :, 10:15]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_9():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:5, :, :]
    result = input_gpu[:5, :, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_10():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, :5, :]
    result = input_gpu[:, :5, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_11():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, :, :5]
    result = input_gpu[:, :, :5]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_12():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[5:, :, :]
    result = input_gpu[5:, :, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_14():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, 5:, :]
    result = input_gpu[:, 5:, :]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_15():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, :, 5:]
    result = input_gpu[:, :, 5:]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_range_against_numpy_16():
    input = np.random.random((10, 20, 30))
    input_gpu = cle.push(input)

    reference = input[:, :, np.int32(5)]
    result = input_gpu[:, :, np.int32(5)]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_type_1():
    input = np.random.random((10, 20, 30)).astype(np.uint16)
    input_gpu = cle.push(input).astype(np.uint16)

    reference = input[:, :, np.int32(5)]
    result = input_gpu[:, :, np.int32(5)]

    print(reference)
    print(result)

    assert reference.dtype == result.dtype


def test_types_2():
    input = np.random.random((10, 20, 30)).astype(np.uint16)
    input_gpu = cle.push(input).astype(np.uint16)

    reference = input[:, :, np.int64(5)]
    result = input_gpu[:, :, np.int64(5)]

    print(reference)
    print(result)

    assert np.allclose(reference, result, 0.0001)


def test_negative_step_2d():
    numbers = np.reshape(np.asarray([[i] for i in range(0, 20)]), (2, 10))

    cle_numbers = cle.asarray(numbers)

    assert cle.array_equal(numbers[::-1], cle_numbers[::-1])
    assert cle.array_equal(numbers[1::-1], cle_numbers[1::-1])
    # assert cle.array_equal(numbers[:5:-1], cle_numbers[:5:-1])
    # assert cle.array_equal(numbers[5:1:-1], cle_numbers[5:1:-1])
    # assert cle.array_equal(numbers[100:], cle_numbers[100:])
    assert cle.array_equal(numbers[100::-1], cle_numbers[100::-1])
    assert cle.array_equal(numbers[100:-50:-1], cle_numbers[100:-50:-1])

    assert cle.array_equal(numbers[::, ::-1], cle_numbers[::, ::-1])
    assert cle.array_equal(numbers[::, 1::-1], cle_numbers[::, 1::-1])
    # assert cle.array_equal(numbers[::, :5:-1], cle_numbers[::, :5:-1])
    # assert cle.array_equal(numbers[::, 5:1:-1], cle_numbers[::, 5:1:-1])
    # assert cle.array_equal(numbers[::, 100:], cle_numbers[::, 100:])
    assert cle.array_equal(numbers[::, 100::-1], cle_numbers[::, 100::-1])
    assert cle.array_equal(numbers[::, 100:-50:-1], cle_numbers[::, 100:-50:-1])


def test_negative_step_3d():
    numbers = np.reshape(np.asarray([[i] for i in range(0, 60)]), (3, 4, 5))

    cle_numbers = cle.asarray(numbers)

    assert cle.array_equal(numbers[::-1], cle_numbers[::-1])
    assert cle.array_equal(numbers[1::-1], cle_numbers[1::-1])
    # assert cle.array_equal(numbers[:5:-1], cle_numbers[:5:-1])
    # assert cle.array_equal(numbers[5:1:-1], cle_numbers[5:1:-1])
    # assert cle.array_equal(numbers[100:], cle_numbers[100:])
    assert cle.array_equal(numbers[100::-1], cle_numbers[100::-1])
    assert cle.array_equal(numbers[100:-50:-1], cle_numbers[100:-50:-1])

    assert cle.array_equal(numbers[::, ::-1], cle_numbers[::, ::-1])
    assert cle.array_equal(numbers[::, 1::-1], cle_numbers[::, 1::-1])
    # assert cle.array_equal(numbers[::, :5:-1], cle_numbers[::, :5:-1])
    # assert cle.array_equal(numbers[::, 5:1:-1], cle_numbers[::, 5:1:-1])
    # assert cle.array_equal(numbers[::, 100:], cle_numbers[::, 100:])
    assert cle.array_equal(numbers[::, 100::-1], cle_numbers[::, 100::-1])
    assert cle.array_equal(numbers[::, 100:-50:-1], cle_numbers[::, 100:-50:-1])

    assert cle.array_equal(numbers[::, ::, ::-1], cle_numbers[::, ::, ::-1])
    assert cle.array_equal(numbers[::, ::, 1::-1], cle_numbers[::, ::, 1::-1])
    # assert cle.array_equal(numbers[::, ::, :5:-1], cle_numbers[::, ::, :5:-1])
    # assert cle.array_equal(numbers[::, ::, 5:1:-1], cle_numbers[::, ::, 5:1:-1])
    # assert cle.array_equal(numbers[::, ::, 100:], cle_numbers[::, ::, 100:])
    assert cle.array_equal(numbers[::, ::, 100::-1], cle_numbers[::, ::, 100::-1])
    assert cle.array_equal(numbers[::, ::, 100:-50:-1], cle_numbers[::, ::, 100:-50:-1])
