import numpy as np
import pyclesperanto as cle

cle.select_device("TX")


def test_setitem_3d():
    data = np.asarray([[[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]]).astype(np.float32)
    ref = np.asarray([[[4.0, 2.0, 3.0], [4.0, 4.0, 3.0]]]).astype(np.float32)

    cl_data = cle.push(data)

    positions = (np.asarray([0, 0, 0]), np.asarray([0, 1, 1]), np.asarray([0, 1, 0]))

    cl_data[positions] = 4

    assert np.allclose(cl_data, ref)


def test_setitem_2d():
    data = np.asarray([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]).astype(np.float32)
    ref = np.asarray([[4.0, 2.0, 3.0], [4.0, 4.0, 3.0]]).astype(np.float32)

    cl_data = cle.push(data)

    positions = (np.asarray([0, 1, 1]), np.asarray([0, 1, 0]))

    cl_data[positions] = 4

    assert np.allclose(cl_data, ref)
