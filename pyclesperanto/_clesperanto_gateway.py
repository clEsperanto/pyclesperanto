
class Clesperanto:
    def __init__(self):
        from ._pyclesperanto import gpu
        self._gpu = gpu()

    def create(self, shape):
        return self._gpu.create(shape)

    def push(self, np_array):
        return self._gpu.push(np_array)

    def pull(self, np_array):
        return self._gpu.pull(np_array)

    def info(self):
        return self._gpu.info()

    def set_wait_for_kernel_to_finish(self):
        return self._gpu.set_wait_for_kernel_to_finish()

    def add_image_and_scalar(self, input_image, output_image, scalar):
        from ._pyclesperanto import add_image_and_scalar as op
        op(self._gpu, input_image, output_image, scalar)
        return output_image

    def gaussian_blur(self, input_image, output_image, sigma_x, sigma_y, sigma_z):
        from ._pyclesperanto import gaussian_blur as op
        op(self._gpu, input_image, output_image, simga_x=float(sigma_x), simga_y=float(sigma_y), simga_z=float(sigma_z))
        return output_image

    def maximum_all_pixels(self, input_image, output_image):
        from ._pyclesperanto import maximum_all_pixels as op
        op(self._gpu, input_image, output_image)
        return output_image

    def copy(self, input_image, output_image):
        from ._pyclesperanto import copy as op
        op(self._gpu, input_image, output_image)
        return output_image

    def connected_component_labelling_box(self, input_image, output_image):
        from ._pyclesperanto import connected_component_labelling_box as op
        op(self._gpu, input_image, output_image)
        return output_image

