import numpy as np
from skimage.data import camera
from skimage.filters import threshold_otsu

import pyclesperanto as cle

cle.select_device("TX")


def test_threshold_otsu_against_scikit_image():
    image = camera()
    thresh = threshold_otsu(image)
    binary = image > thresh

    print(thresh)

    # from skimage import exposure
    # counts, bin_centers = exposure.histogram(image.ravel(), 256, source_range='image')

    # print(str(counts))
    # print(str(bin_centers))

    # threshold in GPU

    gpu_image = cle.push(image)
    gpu_binary = cle.threshold_otsu(gpu_image)

    print(str(binary))
    print(str(cle.pull(gpu_binary)))

    # compare
    assert np.allclose(binary, (cle.pull(gpu_binary) > 0))


def test_threshold_otsu_low_values():
    input = np.asarray([[0, 0, 0], [0, 0.003, 0], [0, 0, 0]])

    reference = np.asarray([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    result = cle.threshold_otsu(input)

    assert np.allclose(reference, cle.pull(result) > 0)
