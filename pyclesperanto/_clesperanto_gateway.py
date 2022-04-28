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

    def imshow(self, image, title: str = None, labels: bool = False, min_display_intensity: float = None,
               max_display_intensity: float = None, color_map=None, plot=None, colorbar: bool = False, colormap=None,
               alpha: float = None, continue_drawing: bool = False):
        import numpy as np

        if not isinstance(image, np.ndarray):
            # Todo: add self.pull here
            image = self.pull(image)

        if len(image.shape) == 3:
            image = self.pull(self.maximum_z_projection(image))

        if color_map is not None:
            import warnings
            warnings.warn("The imshow parameter color_map is deprecated. Use colormap instead.")
            if colormap is None:
                colormap = color_map

        if colormap is None:
            colormap = "Greys_r"

        cmap = colormap
        if labels:
            import matplotlib
            import numpy as np

            if not hasattr(self, "labels_cmap"):
                from numpy.random import MT19937
                from numpy.random import RandomState, SeedSequence
                rs = RandomState(MT19937(SeedSequence(3)))
                lut = rs.rand(65537, 3)
                lut[0, :] = 0
                self.labels_cmap = matplotlib.colors.ListedColormap(lut)
            cmap = self.labels_cmap

            if min_display_intensity is None:
                min_display_intensity = 0

        if plot is None:
            import matplotlib.pyplot as plt
            plt.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity,
                       interpolation='nearest', alpha=alpha)
            if colorbar:
                plt.colorbar()
            if not continue_drawing:
                plt.show()
        else:
            plot.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity,
                        interpolation='nearest', alpha=alpha)
            if colorbar:
                plot.colorbar()

    @plugin_function
    def add_image_and_scalar(self, input_image: Image, output_image: Image = None, scalar: float = 0):
        from ._pyclesperanto import add_image_and_scalar as op
        op(self._gpu, input_image, output_image, scalar)
        return output_image

    @plugin_function
    def add_images_weighted(self, input_image1: Image, input_image2: Image, output_image: Image = None, factor1: float = 1, factor2: float = 1):
        from ._pyclesperanto import add_images_weighted as op
        op(self._gpu, input_image1, input_image2, output_image, factor1, factor2)
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
    
    @plugin_function
    def histogram(self, input_image: Image, output_image: Image = None, bins : int = 256):
        from ._pyclesperanto import histogram as op
        op(self._gpu, input_image, output_image, bins)
        return output_image

    @plugin_function
    def maximum_z_projection(self, input_image: Image, output_image: Image = None):
        shape = input_image.shape()
        output_image = self.create([shape[1], shape[2]])
        from ._pyclesperanto import maximum_z_projection as op
        op(self._gpu, input_image, output_image)
        return output_image

    @plugin_function
    def maximum_y_projection(self, input_image: Image, output_image: Image = None):
        shape = input_image.shape()
        output_image = self.create([shape[0], shape[2]])
        from ._pyclesperanto import maximum_y_projection as op
        op(self._gpu, input_image, output_image)
        return output_image

    @plugin_function
    def maximum_x_projection(self, input_image: Image, output_image: Image = None):
        shape = input_image.shape()
        output_image = self.create([shape[1], shape[0]])
        from ._pyclesperanto import maximum_x_projection as op
        op(self._gpu, input_image, output_image)
        return output_image

    @plugin_function
    def difference_of_gaussian(self, input_image: Image, output_image: Image = None,
                               sigma1_x : float = 0,
                               sigma1_y : float = 0,
                               sigma1_z : float = 0,
                               sigma2_x : float = 0,
                               sigma2_y : float = 0,
                               sigma2_z : float = 0,
                               ):
        from ._pyclesperanto import difference_of_gaussian as op
        op(self._gpu, input_image, output_image,
           float(sigma1_x),
           float(sigma1_y),
           float(sigma1_z),
           float(sigma2_x),
           float(sigma2_y),
           float(sigma2_z),
           )
        return output_image