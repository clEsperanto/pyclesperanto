# import numpy as np
# from ._types import Image, plugin_function

# class Clesperanto:

#     def __init__(self, device_name: str=""):
#         from ._pyclic import gpu
#         if device_name != "":
#             self._gpu = gpu(device_name, "all")
#         else:
#             self._gpu = gpu()

#     @property
#     def info(self) -> str:
#         """Return details about the current OpenCL device"""
#         return self._gpu.info()

#     @property
#     def name(self) -> str:
#         """Return the name of the current OpenCL device"""
#         return self._gpu.name()

#     @property
#     def score(self) -> int:
#         """Return the score of the current OpenCL device"""
#         return self._gpu.score()


#     def list_available_devices(self) -> list:
#         """Retrieve a list of names of available OpenCL-devices"""
#         return self._gpu.list_available_devices("all")

#     def select_device(self, device_name: str) -> str:
#         """Select an OpenCL device that contains `device_name` in its name."""
#         return self._gpu.select_device(device_name, "all")

#     def get_device(self) -> str:
#         """Return the name of the current OpenCL device."""
#         return self._gpu.name()

#     def set_wait_for_kernel_to_finish(self, flag: bool=True):
#         """Configure asyncronous execution of OpenCL kernels (False)"""
#         return self._gpu.set_wait_for_kernel_to_finish(flag)

#     def operations(self):
#         """Return all operations/filters pyclesperanto supports"""
#         all_operation_names = dir(self)
#         result = {}
#         for operation_name in [o for o in all_operation_names if not o.startswith("_")]:
#             potential_function = getattr(self, operation_name)
#             if callable(potential_function):
#                 result[operation_name] = potential_function
#         return result

#     def operation(self, operation_name:str):
#         """Return a function pyclesperanto supports specified by name"""
#         potential_function = getattr(self, operation_name)
#         if callable(potential_function):
#             return potential_function

#     def create(self, shape : list =(1,1,1), otype: str="buffer"):
#         """Create an OpenCL backed image/buffer with specified shape."""
#         return self._gpu.create(shape, otype)

#     def create_like(self, image):
#         """Create an OpenCL backed image/buffer with the same size and type like the given image."""
#         from ._pyclic import data
#         if isinstance(image, data):
#             return self.create(shape=image.shape(), otype=image.otype())
#         else:
#             return self.create(shape=image.shape)

#     def push(self, any_array, otype: str="buffer"):
#         """Transfer a numpy-compatible array to GPU memory."""
#         from ._pyclic import data
#         if isinstance(any_array, data):
#             return any_array
#         else:
#             return self._gpu.push(np.asarray(any_array), otype)

#     def pull(self, any_array):
#         """Return a OpenCL/GPU backed image from GPU memory as numpy array."""
#         return self._gpu.pull(any_array)

#     def imshow(self, image, title: str = None, labels: bool = False, min_display_intensity: float = None,
#                max_display_intensity: float = None, color_map=None, plot=None, colorbar: bool = False, colormap=None,
#                alpha: float = None, continue_drawing: bool = False):
#         """Visualize an image, e.g. in Jupyter notebooks.

#         Parameters
#         ----------
#         image: np.ndarray
#             numpy or OpenCL-backed image to visualize
#         title: str
#             Obsolete (kept for ImageJ-compatibility)
#         labels: bool
#             True: integer labels will be visualized with colors
#             False: Specified or default colormap will be used to display intensities.
#         min_display_intensity: float
#             lower limit for display range
#         max_display_intensity: float
#             upper limit for display range
#         color_map: str
#             deprecated, use colormap instead
#         plot: matplotlib axis
#             Plot object where the image should be shown. Useful for putting multiple images in subfigures.
#         colorbar: bool
#             True puts a colorbar next to the image. Will not work with label images and when visualizing multiple
#             images (continue_drawing=True).
#         colormap: str or matplotlib colormap
#         alpha: float
#             alpha blending value
#         continue_drawing: float
#             True: the next shown image can be visualized on top of the current one, e.g. with alpha = 0.5
#         """
#         import numpy as np

#         if not isinstance(image, np.ndarray):
#             # Todo: add self.pull here
#             image = self.pull(image)

#         if len(image.shape) == 3:
#             image = self.pull(self.maximum_z_projection(image))

#         if color_map is not None:
#             import warnings
#             warnings.warn("The imshow parameter color_map is deprecated. Use colormap instead.")
#             if colormap is None:
#                 colormap = color_map

#         if colormap is None:
#             colormap = "Greys_r"

#         cmap = colormap
#         if labels:
#             import matplotlib
#             import numpy as np

#             if not hasattr(self, "labels_cmap"):
#                 from numpy.random import MT19937
#                 from numpy.random import RandomState, SeedSequence
#                 rs = RandomState(MT19937(SeedSequence(3)))
#                 lut = rs.rand(65537, 3)
#                 lut[0, :] = 0
#                 self.labels_cmap = matplotlib.colors.ListedColormap(lut)
#             cmap = self.labels_cmap

#             if min_display_intensity is None:
#                 min_display_intensity = 0

#         if plot is None:
#             import matplotlib.pyplot as plt
#             plt.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity,
#                        interpolation='nearest', alpha=alpha)
#             if colorbar:
#                 plt.colorbar()
#             if not continue_drawing:
#                 plt.show()
#         else:
#             plot.imshow(image, cmap=cmap, vmin=min_display_intensity, vmax=max_display_intensity,
#                         interpolation='nearest', alpha=alpha)
#             if colorbar:
#                 plot.colorbar()


#     # Operation list

#     @plugin_function
#     def add_image_and_scalar(self, input_image: Image, output_image: Image = None, scalar: float = 0):
#         """Adds a scalar value s to all pixels x of a given image X.

#         <pre>f(x, s) = x + s</pre>

#         Parameters
#         ----------
#         input_image : Image
#             The input image where scalare should be added.
#         output_image : Image, optional
#             The output image where results are written into.
#         scalar : float, optional
#             The constant number which will be added to all pixels.


#         Returns
#         -------
#         output_image
#         """

#         from ._pyclic import add_image_and_scalar as op
#         op(self._gpu, input_image, output_image, scalar)
#         return output_image

#     @plugin_function
#     def add_images_weighted(self, input_image1: Image, input_image2: Image, output_image: Image = None, factor1: float = 1, factor2: float = 1):
#         """Calculates the sum of pairs of pixels x and y from images X and Y
#         weighted with factors a and b.

#         <pre>f(x, y, a, b) = x * a + y * b</pre>

#         Parameters
#         ----------
#         input_image1 : Image
#             The first input image to added.
#         input_image2 : Image
#             The second image to be added.
#         output_image : Image, optional
#             The output image where results are written into.
#         factor1 : float, optional
#             The constant number which will be multiplied with each pixel of summand1 before adding it.
#         factor2 : float, optional
#             The constant number which will be multiplied with each pixel of summand2 before adding it.


#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import add_images_weighted as op
#         op(self._gpu, input_image1, input_image2, output_image, factor1, factor2)
#         return output_image

#     @plugin_function
#     def gaussian_blur(self, input_image: Image, output_image: Image = None, sigma_x: float = 0, sigma_y: float = 0, sigma_z: float = 0):
#         """Computes the Gaussian blurred image of an image given sigma values
#         in X, Y and Z.

#         Thus, the filter kernel can have non-isotropic shape.

#         The implementation is done separable. In case a sigma equals zero, the
#         direction is not blurred.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional
#         sigma_x : Number, optional
#         sigma_y : Number, optional
#         sigma_z : Number, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import gaussian_blur as op
#         op(self._gpu, input_image, output_image, sigma_x=float(sigma_x), sigma_y=float(sigma_y), sigma_z=float(sigma_z))
#         return output_image

#     @plugin_function
#     def mean_box(self, input_image: Image, output_image: Image = None, radius_x: int = 0, radius_y: int = 0, radius_z: int = 0):
#         """Computes the local mean average of a pixels box-shaped neighborhood.

#         The cubes size is specified by its half-width, half-height and
#         half-depth (radius).

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional
#         radius_x : Number, optional
#         radius_y : Number, optional
#         radius_z : Number, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import mean_box as op
#         op(self._gpu, input_image, output_image, radius_x=int(radius_x), radius_y=int(radius_y), radius_z=int(radius_z))
#         return output_image

#     @plugin_function
#     def maximum_box(self, input_image: Image, output_image: Image = None, radius_x: int = 0, radius_y: int = 0, radius_z: int = 0):
#         """Computes the local maximum of a pixels cube neighborhood.

#         The cubes size is specified by
#         its half-width, half-height and half-depth (radius).

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional
#         radius_x : Number, optional
#         radius_y : Number, optional
#         radius_z : Number, optional

#         Returns
#         -------
#         output_image
#         """

#         from ._pyclic import maximum_box as op
#         op(self._gpu, input_image, output_image, radius_x=int(radius_x), radius_y=int(radius_y), radius_z=int(radius_z))
#         return output_image

#     @plugin_function
#     def minimum_box(self, input_image: Image, output_image: Image = None, radius_x: int = 0, radius_y: int = 0, radius_z: int = 0):
#         """Computes the local minimum of a pixels cube neighborhood.

#         The cubes size is specified by
#         its half-width, half-height and half-depth (radius).

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional
#         radius_x : Number, optional
#         radius_y : Number, optional
#         radius_z : Number, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import minimum_box as op
#         op(self._gpu, input_image, output_image, radius_x=int(radius_x), radius_y=int(radius_y), radius_z=int(radius_z))
#         return output_image

#     @plugin_function
#     def maximum_of_all_pixels(self, input_image: Image):
#         """Determines the maximum of all pixels in a given image.

#         It will be stored in a new row of ImageJs
#         Results table in the column 'Max'.

#         Parameters
#         ----------
#         input_image : Image
#             The image of which the maximum of all pixels or voxels will be determined.

#         Returns
#         -------
#         float
#         """
#         output_image = self.create([1,1,1])
#         from ._pyclic import maximum_of_all_pixels as op
#         op(self._gpu, input_image, output_image)
#         return self.pull(output_image).item()

#     @plugin_function
#     def minimum_of_all_pixels(self, input_image: Image):
#         """Determines the minimum of all pixels in a given image.

#         It will be stored in a new row of ImageJs
#         Results table in the column 'Min'.

#         Parameters
#         ----------
#         input_image : Image
#             The image of which the minimum of all pixels or voxels will be determined.

#         Returns
#         -------
#         float
#         """
#         output_image = self.create([1,1,1])
#         from ._pyclic import minimum_of_all_pixels as op
#         op(self._gpu, input_image, output_image)
#         return self.pull(output_image).item()

#     @plugin_function
#     def sum_of_all_pixels(self, input_image: Image):
#         """Determines the sum of all pixels in a given image.

#         It will be stored in a new row of ImageJs
#         Results table in the column 'Sum'.

#         Parameters
#         ----------
#         input_image : Image
#             The image of which all pixels or voxels will be summed.

#         Returns
#         -------
#         float
#         """
#         output_image = self.create([1,1,1])
#         from ._pyclic import sum_of_all_pixels as op
#         op(self._gpu, input_image, output_image)
#         return self.pull(output_image).item()

#     @plugin_function
#     def copy(self, input_image: Image, output_image: Image = None):
#         """Copies an image."""
#         from ._pyclic import copy as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def connected_components_labeling_box(self, input_image: Image, output_image: Image = None):
#         """Performs connected components analysis inspecting the box neighborhood
#         of every pixel to a binary image and generates a label map.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import connected_components_labeling_box as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def threshold_otsu(self, input_image: Image, output_image: Image = None):
#         """Binarizes an image using Otsu's threshold method [1]
#         using a histogram determined on the GPU to create binary images.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image

#         References
#         ----------
#         .. [1] https://ieeexplore.ieee.org/document/4310076
#         """
#         from ._pyclic import threshold_otsu as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def detect_maxima_box(self, input_image: Image, output_image: Image = None, radius_x : int = 0, radius_y : int = 0, radius_z : int = 0):
#         """Detects local maxima in a given square/cubic neighborhood.

#         Pixels in the resulting image are set to 1 if there is no other pixel in a
#         given radius which has a
#         higher intensity, and to 0 otherwise.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import detect_maxima_box as op
#         op(self._gpu, input_image, output_image, int(radius_x), int(radius_y), int(radius_z))
#         return output_image

#     @plugin_function
#     def greater_or_equal_constant(self, input_image: Image, output_image: Image = None, scalar : float = 0):
#         """Determines if an images A is greater or equal a given scalar b.

#         f(a, b) = 1 if a >= b; 0 otherwise.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional
#         scalar : Number, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import greater_or_equal_constant as op
#         op(self._gpu, input_image, output_image, float(scalar))
#         return output_image

#     @plugin_function
#     def greater_or_equal(self, input_image1: Image, input_image2: Image, output_image: Image = None):
#         """Determines if two images A and B greater or equal pixel wise.

#         f(a, b) = 1 if a >= b; 0 otherwise.

#         Parameters
#         ----------
#         input_image1 : Image
#         input_image2 : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import greater_or_equal as op
#         op(self._gpu, input_image1, input_image2, output_image)
#         return output_image

#     @plugin_function
#     def binary_not(self, input_image: Image, output_image: Image = None):
#         """Computes a binary image (containing pixel values 0 and 1) from an image
#         X by negating its pixel values
#         x using the binary NOT operator !

#         All pixel values except 0 in the input image are interpreted as 1.

#         <pre>f(x) = !x</pre>

#         Parameters
#         ----------
#         input_image : Image
#             The binary input image to be inverted.
#         output_image : Image, optional
#             The output image where results are written into.

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import binary_not as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def binary_and(self, input_image1: Image, input_image2: Image, output_image: Image = None):
#         """Computes a binary image (containing pixel values 0 and 1) from two
#         images X and Y by connecting pairs of
#         pixels x and y with the binary AND operator &.
#         All pixel values except 0 in the input images are interpreted as 1.

#         <pre>f(x, y) = x & y</pre>

#         Parameters
#         ----------
#         input_image1 : Image
#             The first binary input image to be processed.
#         input_image2 : Image
#             The second binary input image to be processed.
#         output_image : Image, optional
#             The output image where results are written into.

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import binary_and as op
#         op(self._gpu, input_image1, input_image2, output_image)
#         return output_image

#     @plugin_function
#     def binary_or(self, input_image1: Image, input_image2: Image, output_image: Image = None):
#         """Computes a binary image (containing pixel values 0 and 1) from two
#         images X and Y by connecting pairs of
#         pixels x and y with the binary OR operator |.
#         All pixel values except 0 in the input images are interpreted as 1.

#         <pre>f(x, y) = x | y</pre>

#         Parameters
#         ----------
#         input_image1 : Image
#             The first binary input image to be processed.
#         input_image2 : Image
#             The second binary input image to be processed.
#         output_image : Image, optional
#             The output image where results are written into.

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import binary_or as op
#         op(self._gpu, input_image1, input_image2, output_image)
#         return output_image

#     @plugin_function
#     def binary_xor(self, input_image1: Image, input_image2: Image, output_image: Image = None):
#         """Computes a binary image (containing pixel values 0 and 1) from two
#         images X and Y by connecting pairs of
#         pixels x and y with the binary operators AND &, OR | and NOT ! implementing
#         the XOR operator.

#         All pixel values except 0 in the input images are interpreted as 1.

#         <pre>f(x, y) = (x & !y) | (!x & y)</pre>

#         Parameters
#         ----------
#         input_image1 : Image
#             The first binary input image to be processed.
#         input_image2 : Image
#             The second binary input image to be processed.
#         output_image : Image, optional
#             The output image where results are written into.

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import binary_xor as op
#         op(self._gpu, input_image1, input_image2, output_image)
#         return output_image

#     @plugin_function
#     def binary_subtract(self, input_image1: Image, input_image2: Image, output_image: Image = None):
#         """Subtracts one binary image from another.

#         Parameters
#         ----------
#         input_image1 : Image
#             The first binary input image to be processed.
#         input_image2 : Image
#             The second binary input image to be processed.
#         output_image : Image, optional
#             The output image where results are written into.

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import binary_subtract as op
#         op(self._gpu, input_image1, input_image2, output_image)
#         return output_image

#     @plugin_function
#     def dilate_sphere(self, input_image: Image, output_image: Image = None):
#         """Computes a binary image with pixel values 0 and 1 containing the binary
#         dilation of a given input image.

#         The dilation takes the von-Neumann-neighborhood (4 pixels in 2D and 6
#         pixels in 3d) into account.
#         The pixels in the input image with pixel value not equal to 0 will be
#         interpreted as 1.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import dilate_sphere as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def erode_sphere(self, input_image: Image, output_image: Image = None):
#         """Computes a binary image with pixel values 0 and 1 containing the binary
#         erosion of a given input image.

#         The erosion takes the von-Neumann-neighborhood (4 pixels in 2D and 6
#         pixels in 3d) into account.
#         The pixels in the input image with pixel value not equal to 0 will be
#         interpreted as 1.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import erode_sphere as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def extend_labeling_via_voronoi(self, input_image: Image, output_image: Image = None):
#         """Takes a label map image and dilates the regions using a octagon shape
#         until they touch.

#         The resulting label map is written to the output.

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import extend_labeling_via_voronoi as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def histogram(self, input_image: Image, bins : int = 256):
#         output_image = self.create([bins])
#         from ._pyclic import histogram as op
#         op(self._gpu, input_image, output_image, bins)
#         return output_image

#     @plugin_function
#     def maximum_z_projection(self, input_image: Image):
#         """Determines the maximum intensity projection of an image along Z.

#         Parameters
#         ----------
#         input_image : Image 3D

#         Returns
#         -------
#         Image 2D
#         """
#         shape = input_image.shape()
#         output_image = self.create([shape[1], shape[2]])
#         from ._pyclic import maximum_z_projection as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def maximum_y_projection(self, input_image: Image):
#         """Determines the maximum intensity projection of an image along Y.

#         Parameters
#         ----------
#         input_image : Image 3D

#         Returns
#         -------
#         Image 2D
#         """
#         shape = input_image.shape()
#         output_image = self.create([shape[0], shape[2]])
#         from ._pyclic import maximum_y_projection as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def maximum_x_projection(self, input_image: Image):
#         """Determines the maximum intensity projection of an image along X.

#         Parameters
#         ----------
#         input_image : Image 3D

#         Returns
#         -------
#         Image 2D
#         """
#         shape = input_image.shape()
#         output_image = self.create([shape[1], shape[0]])
#         from ._pyclic import maximum_x_projection as op
#         op(self._gpu, input_image, output_image)
#         return output_image

#     @plugin_function
#     def top_hat_box(self, input_image: Image, output_image: Image = None,
#                                radius_x : float = 0,
#                                radius_y : float = 0,
#                                radius_z : float = 0
#                                ):
#         """Applies a top-hat filter for background subtraction to the input image.

#         Parameters
#         ----------
#         input_image : Image
#             The input image where the background is subtracted from.
#         output_image : Image, optional
#             The output image where results are written into.
#         radius_x : Image, optional
#             Radius of the background determination region in X.
#         radius_y : Image, optional
#             Radius of the background determination region in Y.
#         radius_z : Image, optional
#             Radius of the background determination region in Z.

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import top_hat_box as op
#         op(self._gpu, input_image, output_image, float(radius_x), float(radius_y), float(radius_z))
#         return output_image

#     @plugin_function
#     def difference_of_gaussian(self, input_image: Image, output_image: Image = None,
#                                sigma1_x : float = 0,
#                                sigma1_y : float = 0,
#                                sigma1_z : float = 0,
#                                sigma2_x : float = 0,
#                                sigma2_y : float = 0,
#                                sigma2_z : float = 0,
#                                ):
#         """Applies Gaussian blur to the input image twice with different sigma
#         values resulting in two images which are then subtracted from each other.

#         It is recommended to apply this operation to images of type Float (32 bit)
#         as results might be negative.

#         Parameters
#         ----------
#         input_image : Image
#             The input image to be processed.
#         output_image : Image, optional
#             The output image where results are written into.
#         sigma1_x : float, optional
#             Sigma of the first Gaussian filter in x
#         sigma1_y : float, optional
#             Sigma of the first Gaussian filter in y
#         sigma1_z : float, optional
#             Sigma of the first Gaussian filter in z
#         sigma2_x : float, optional
#             Sigma of the second Gaussian filter in x
#         sigma2_y : float, optional
#             Sigma of the second Gaussian filter in y
#         sigma2_z : float, optional
#             Sigma of the second Gaussian filter in z

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import difference_of_gaussian as op
#         op(self._gpu, input_image, output_image,
#            float(sigma1_x),
#            float(sigma1_y),
#            float(sigma1_z),
#            float(sigma2_x),
#            float(sigma2_y),
#            float(sigma2_z),
#            )
#         return output_image

#     @plugin_function
#     def masked_voronoi_labeling(self, input_image: Image, mask_image: Image, output_image: Image = None):
#         """Takes a binary image, labels connected components and dilates the
#         regions using a octagon shape until they touch. The region growing is limited to a masked area.

#         The resulting label map is written to the output.

#         Parameters
#         ----------
#         input_image : Image
#         mask_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image
#         """
#         from ._pyclic import masked_voronoi_labeling as op
#         op(self._gpu, input_image, mask_image, output_image)
#         return output_image

#     @plugin_function
#     def voronoi_otsu_labeling(self, input_image: Image, output_image: Image = None, spot_sigma: float = 2, outline_sigma: float = 2):
#         """Labels objects directly from grey-value images.

#         The two sigma parameters allow tuning the segmentation result. Under the hood,
#         this filter applies two Gaussian blurs, spot detection, Otsu-thresholding [1] and Voronoi-labeling [2]. The
#         thresholded binary image is flooded using the Voronoi tesselation approach starting from the found local maxima.

#         Parameters
#         ----------
#         input_image : Image
#             Input grey-value image
#         output_image : Image, optional
#             Output image
#         spot_sigma : float, optional
#             controls how close detected cells can be
#         outline_sigma : float, optional
#             controls how precise segmented objects are outlined.

#         Returns
#         -------
#         output_image

#         References
#         ----------
#         .. [1] https://ieeexplore.ieee.org/document/4310076
#         .. [2] https://en.wikipedia.org/wiki/Voronoi_diagram
#         """
#         from ._pyclic import voronoi_otsu_labeling as op
#         op(self._gpu, input_image, output_image, float(spot_sigma), float(outline_sigma))
#         return output_image

#     @plugin_function
#     def subtract_image_from_scalar(self, input_image: Image, output_image: Image = None, scalar: float = 0):
#         """Subtracts one image X from a scalar s pixel wise.

#         <pre>f(x, s) = s - x</pre>

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional
#         scalar : Number, optional

#         Returns
#         -------
#         output_image

#         References
#         ----------
#         .. [1] https://clij.github.io/clij2-docs/reference_subtractImageFromScalar
#         """
#         from ._pyclic import subtract_image_from_scalar as op
#         op(self._gpu, input_image, output_image, float(scalar))
#         return output_image

#     @plugin_function
#     def sobel(self, input_image: Image, output_image: Image = None):
#         """Convolve the image with the Sobel kernel.

#         Author(s): Ruth Whelan-Jeans, Robert Haase

#         Parameters
#         ----------
#         input_image : Image
#         output_image : Image, optional

#         Returns
#         -------
#         output_image

#         References
#         ----------
#         .. [1] https://clij.github.io/clij2-docs/reference_sobel
#         """
#         from ._pyclic import sobel as op
#         op(self._gpu, input_image, output_image)
#         return output_image
