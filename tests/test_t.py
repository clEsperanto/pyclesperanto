def test_t_2d():
    import pyclesperanto as cle
    import numpy as np

    image = np.random.random((3, 2))

    cle_image = cle.asarray(image)

    assert cle.array_equal(cle_image.T, image.T)


def test_t_3d():
    import pyclesperanto as cle
    import numpy as np

    image = np.random.random((3, 2, 5))

    cle_image = cle.asarray(image)

    assert cle.array_equal(cle_image.T, image.T)
