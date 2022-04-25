import numpy as np
from ._types import Image, plugin_function

class Clesperanto:
    
    def __init__(self, device_name: str=""):
        from ._pyclesperanto import gpu
        if device_name != "": 
            self._gpu = gpu(device_name, "all")
        else:
            self._gpu = gpu()
    
    
    
    @property
    def info(self) -> str:
        return print(self._gpu.info())
    
    @property
    def name(self) -> str:
        return print(self._gpu.name())
    
    @property
    def score(self) -> int:
        return print(self._gpu.score())
    
    
    
    def list_available_devices(self) -> list:
        return self._gpu.list_available_devices("all")
    
    def select_device(self, device_name: str) -> str:
        return self._gpu.select_device(device_name, "all")
    
    def set_wait_for_kernel_to_finish(self, flag: bool=True):
        return self._gpu.set_wait_for_kernel_to_finish(flag)




    def create(self, shape : list =(1,1,1), otype: str="buffer"):
        return self._gpu.create(shape, otype)

    def create_like(self, image):
        from ._pyclesperanto import data
        if isinstance(image, data):
            return self.create(shape=image.shape(), otype=image.otype())
        else:
            return self.create(shape=image.shape)

    def push(self, any_array, otype: str="buffer"):
        from ._pyclesperanto import data
        if isinstance(any_array, data):
            return any_array
        else:
            return self._gpu.push(np.asarray(any_array), otype)

    def pull(self, np_array):
        return self._gpu.pull(np_array)



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

    @plugin_function
    def threshold_otsu(self, input_image: Image, output_image: Image = None):
        from ._pyclesperanto import threshold_otsu as op
        op(self._gpu, input_image, output_image)
        return output_image
    
    @plugin_function
    def greater_or_equal_constant(self, input_image: Image, output_image: Image = None, scalar : float = 0):
        from ._pyclesperanto import greater_or_equal_constant as op
        op(self._gpu, input_image, output_image, float(scalar))
        return output_image
    
    @plugin_function
    def binary_not(self, input_image: Image, output_image: Image = None):
        from ._pyclesperanto import binary_not as op
        op(self._gpu, input_image, output_image)
        return output_image
    
    @plugin_function
    def threshold_otsu(self, input_image: Image, output_image: Image = None):
        from ._pyclesperanto import threshold_otsu as op
        op(self._gpu, input_image, output_image)
        return output_image
