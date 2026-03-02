import numpy as np
from skimage import morphology, segmentation

import pyclesperanto as cle

# def test_morphological_chan_vese():
#     image = generate_disk((25, 25), 5).astype(np.float32)
#     reference = cle.push(segmentation.morphological_chan_vese(image, num_iter=1, smoothing=1, lambda1=1, lambda2=1))
#     result = cle.morphological_chan_vese(image, num_iter=1, smoothing=, lambda1=1, lambda2=1)
#     a = cle.pull(result).astype(np.uint8)
#     b = cle.pull(reference).astype(np.uint8)
#     print(a)
#     print(b)
#     assert (np.array_equal(a, b))


# def test_morphological_chan_vese_on_membranes_2d():
#     from skimage.data import cells3d
#     from skimage.segmentation import morphological_chan_vese
#     import pyclesperanto as cle
#     image2d = cells3d()[30, 0, ...]
#     result_gpu = cle.morphological_chan_vese(image2d, num_iter=20, smoothing=10)
#     result_cpu = morphological_chan_vese(image2d, num_iter=20, smoothing=10)
#     assert cle.array_equal(result_cpu, result_gpu)

# def test_morphological_chan_vese_on_membranes_3d():
#     from skimage.data import cells3d
#     from skimage.segmentation import morphological_chan_vese
#     import pyclesperanto as cle
#     image3d = cells3d()[10:50:, 0, :40, :40]
#     result_gpu = cle.morphological_chan_vese(image3d, num_iter=20, smoothing=10)
#     result_cpu = morphological_chan_vese(image3d, num_iter=20, smoothing=10)
#     cle.array_equal(result_cpu, result_gpu)


def generate_disk(shape, radius):
    image = np.zeros(shape)
    image[
        image.shape[0] // 2 - radius : image.shape[0] // 2 + radius + 1,
        image.shape[1] // 2 - radius : image.shape[1] // 2 + radius + 1,
    ] = morphology.disk(radius)
    return image
