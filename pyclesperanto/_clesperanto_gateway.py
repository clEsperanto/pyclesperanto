import numpy as np
from ._types import Image, plugin_function

class Clesperanto:
    def __init__(self):
        from ._pyclesperanto import gpu
        self._gpu = gpu()

    def create(self, shape):
        return self._gpu.create(shape)

    def create_like(self, image):
        from ._pyclesperanto import data
        if isinstance(image, data):
            return self.create(image.shape())
        else:
            return self.create(image.shape)

    def push(self, any_array):
        from ._pyclesperanto import data
        if isinstance(any_array, data):
            return any_array
        else:
            return self._gpu.push(np.asarray(any_array))

    def pull(self, np_array):
        return self._gpu.pull(np_array)

    def info(self):
        return self._gpu.info()

    def set_wait_for_kernel_to_finish(self):
        return self._gpu.set_wait_for_kernel_to_finish()

    @plugin_function
    def add_image_and_scalar(self, input_image: Image, output_image: Image = None, scalar: float = 0):
        from ._pyclesperanto import add_image_and_scalar as op
        op(self._gpu, input_image, output_image, scalar)
        return output_image

    @plugin_function
    def gaussian_blur(self, input_image: Image, output_image: Image = None, sigma_x: float = 0, sigma_y: float = 0, sigma_z: float = 0):
        from ._pyclesperanto import gaussian_blur as op
        op(self._gpu, input_image, output_image, sigma_x=float(sigma_x), sigma_y=float(sigma_y), sigma_z=float(sigma_z))
        return output_image

    @plugin_function
    def maximum_all_pixels(self, input_image: Image, output_image: Image = None):
        from ._pyclesperanto import maximum_all_pixels as op
        op(self._gpu, input_image, output_image)
        return output_image

    @plugin_function
    def copy(self, input_image: Image, output_image: Image = None):
        from ._pyclesperanto import copy as op
        op(self._gpu, input_image, output_image)
        return output_image

    @plugin_function
    def connected_components_labeling_box(self, input_image: Image, output_image: Image = None):
        from ._pyclesperanto import connected_components_labeling_box as op
        op(self._gpu, input_image, output_image)
        return output_image

