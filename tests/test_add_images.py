import numpy as np

import pyclesperanto as cle

cle.select_device("TX")

input1 = np.asarray([1, 2, 3])
input2 = np.asarray([4, 5, 6])


def test_add_images():
    reference = np.asarray([5, 7, 9])
    output = cle.add_images(input1, input2, None)
    result = cle.pull(output)

    assert np.array_equal(result, reference)
