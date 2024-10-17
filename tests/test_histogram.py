import numpy as np

import pyclesperanto as cle

cle.select_device("TX")


def test_histogram():
    test = cle.push(np.asarray([[1, 2, 4, 4, 2, 3], [3, 3, 4, 4, 5, 5]]))

    ref_histogram = [1, 2, 3, 4, 2]

    my_histogram = cle.histogram(
        test, num_bins=5, minimum_intensity=1, maximum_intensity=5
    )

    print(my_histogram)

    a = cle.pull(my_histogram)
    assert np.allclose(a, ref_histogram)


def test_histogram_3d():
    test = cle.push(np.asarray([[1, 2, 4, 4, 2, 3], [3, 3, 4, 4, 5, 5]]))

    ref_histogram = [1, 2, 3, 4, 2]

    my_histogram = cle.histogram(
        test, num_bins=5, minimum_intensity=1, maximum_intensity=5
    )

    print(my_histogram)

    a = cle.pull(my_histogram)
    assert np.allclose(a, ref_histogram)


def test_histogram_3d_2():
    test = cle.push(np.asarray([[[1, 2, 4], [4, 2, 3]], [[3, 3, 4], [4, 5, 5]]]))

    ref_histogram = [1, 2, 3, 4, 2]

    my_histogram = cle.histogram(
        test, num_bins=5, minimum_intensity=1, maximum_intensity=5
    )

    print(my_histogram)

    a = cle.pull(my_histogram)
    assert np.allclose(a, ref_histogram)


# def test_histogram_against_scikit_image():
#     from skimage.data import camera
#     image = camera()
#     from skimage import exposure
#     hist, bc = exposure.histogram(image.ravel(), 256, source_range="image")
#     print(hist)
#     gpu_image = cle.push(image.astype(int))
#     gpu_hist = cle.histogram(gpu_image, num_bins=256, minimum_intensity=0, maximum_intensity=gpu_image.max())
#     print(cle.pull(gpu_hist))
#     assert np.allclose(hist, cle.pull(gpu_hist))
