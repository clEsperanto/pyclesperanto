import pyclesperanto as cle
import numpy as np

cle.select_device("TX")


def test_maximum_of_all_pixels():
    np_input = np.asarray(
        [
            [[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]],
            [[1, 2, 3, 13], [4, 5, 6, 14], [7, 8, 9, 15]],
        ]
    )

    gpu_input = cle.push(np_input)
    result = cle.maximum_of_all_pixels(gpu_input)
    print(result)
    assert result == 15

    gpu_input = cle.push(np_input)
    result = cle.maximum_of_all_pixels(gpu_input)
    print(result)
    assert result == 15


def test_maximum_of_all_pixels_against_numpy():
    from skimage.data import camera

    image = camera()

    max_cle = cle.maximum_of_all_pixels(image)
    max_np = image.max()

    assert max_cle == max_np
