import pyclesperanto as cle
import numpy as np

cle.select_device("TX")

input1 = np.asarray([1, 2, 3])
input2 = np.asarray([4, 5, 6])


def test_add_images_weighted_missing_params():
    reference = np.asarray([5, 7, 9])
    output = cle.add_images_weighted(input1, input2, None, 1, 1)
    result = cle.pull(output)

    assert np.array_equal(result, reference)


reference = np.asarray([9, 12, 15])


def test_add_images_weighted_none_output():
    output = cle.add_images_weighted(input1, input2, None, 1, 2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


def test_add_images_weighted_named_params():
    output = cle.add_images_weighted(input1, input2, None, factor0=1, factor1=2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


def test_add_images_weighted_named_params_missing_params():
    output = cle.add_images_weighted(input1, input2, factor0=1, factor1=2)
    result = cle.pull(output)
    assert np.array_equal(result, reference)


def test_add_images_weighted_wrong_order_missing_params():
    reference = np.asarray([9, 12, 15])
    output = cle.add_images_weighted(input1, input2, factor1=2, factor0=1)
    result = cle.pull(output)
    assert np.array_equal(result, reference)
