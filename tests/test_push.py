import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


def test_push_np():
    reference = np.asarray([[1, 2], [-3, 4]])

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)


def test_push_list():
    reference = [[1, 2], [-3, 4]]

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)


def test_push_tuple():
    reference = ([1, 2], [-3, 4])

    image = cle.push(reference)

    result = cle.pull(image)

    assert np.allclose(result, reference)
