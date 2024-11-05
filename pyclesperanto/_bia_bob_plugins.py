def list_bia_bob_plugins():
    """List of function hints for bia_bob"""
    return """
    ## pyclesperanto
    pyclesperanto is a Python library for GPU-accelerated image processing and analysis.
    To use it, you need to import it:
    ```
    import pyclesperanto as cle
    ```

    * Compute the absolute value of each pixel in an input image, optionally specifying an output image and device for processing.
    cle.absolute(input_image: ndarray) -> ndarray

    * Calculate the pixel-by-pixel absolute difference between two images, optionally storing the result in an output image and selecting a device for operation.
    cle.absolute_difference(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Generate a binary image by applying the binary AND operator to corresponding pixels of two input images, considering all non-zero pixels as 1.
    cle.binary_and(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Identify and highlight edge pixels of binary objects, setting them to 1 in the output image on a specified device.
    cle.binary_edge_detection(input_image: ndarray) -> ndarray

    * Convert an image to a binary image by negating all non-zero pixels using the binary NOT operator.
    cle.binary_not(input_image: ndarray) -> ndarray

    * Combine two images pixel-wise using the binary OR operator, interpreting any non-zero pixel values as 1, with optional specification of output image and device.
    cle.binary_or(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Subtract one binary image from another, optionally specifying an output image and device.
    cle.binary_subtract(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Generate a binary image by applying the XOR operation on two input images, interpreting all non-zero pixels as 1.
    cle.binary_xor(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Perform background subtraction using a bottomhat filter on an image with customizable region radii, connectivity, and processing device options.
    cle.bottom_hat(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1, connectivity: str = 'box') -> ndarray

    * Perform background subtraction on an input image using a bottomhat filter with customizable radius parameters for X, Y, and Z dimensions.
    cle.bottom_hat_sphere(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray

    * calculate the centroids of all labels in a 3D label image and output the coordinates as a point list image, with optional control over background inclusion and device execution.
    cle.centroids_of_labels(input_image: ndarray, withBG: bool = False) -> ndarray

    * Apply spherical morphological closing to intensity or binary images with customizable radii and connectivity options, optionally specifying an output image and device.
    cle.closing(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 0, connectivity: str = 'box') -> ndarray

    * Perform a morphological closing operation on a label image using an octagonal structuring element with optional radius and device specifications.
    cle.closing_labels(input_image: ndarray, radius: int = 0) -> ndarray

    * Apply morphological closing to images using a spherical footprint, adjustable by x, y, z radii and optional output and device specifications.
    cle.closing_sphere(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 0) -> ndarray

    * Combine two label images by overwriting and sequentially relabeling, allowing specification of input images, output image, and device.
    cle.combine_labels(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Concatenate two images or image stacks along the X axis, with optional output image and device specifications.
    cle.concatenate_along_x(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Concatenate two images or stacks along the Y axis, specifying optional output and device parameters.
    cle.concatenate_along_y(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Concatenate two images or stacks along the Z axis to produce a combined output image, optionally specifying a device for the operation.
    cle.concatenate_along_z(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Generate a label map by performing connected components analysis on a binary image, considering either 'box' or 'sphere' pixel neighborhoods, with optional output image and device specification.
    cle.connected_component_labeling(input_image: ndarray, connectivity: str = 'box') -> ndarray

    * Analyze and label connected components in a binary image using specified neighborhood connectivity, with support for device-specific execution.
    cle.connected_components_labeling(input_image: ndarray, connectivity: str = 'box') -> ndarray

    * compute a vector indicating the number of touching neighbors for each label in a touch matrix, optionally ignoring background touches.
    cle.count_touching_neighbors(input_image: ndarray, ignore_background: bool = True) -> ndarray

    * Generate an image with pixel values of 1 on label edges and 0 elsewhere from an input labelmap.
    cle.detect_label_edges(input_image: ndarray) -> ndarray

    * Perform a Difference of Gaussian operation on a 3D image by applying two Gaussian blurs with specified sigmas and subtracting the results, suitable for 32-bit Float images.
    cle.difference_of_gaussian(input_image: ndarray, sigma1_x: float = 2, sigma1_y: float = 2, sigma1_z: float = 2, sigma2_x: float = 2, sigma2_y: float = 2, sigma2_z: float = 2) -> ndarray

    * Generate a binary image using dilation based on the specified 'box' or 'sphere' connectivity from an input image, with non-zero pixels treated as ones.
    cle.dilate(input_image: ndarray, connectivity: str = 'box') -> ndarray

    * Enlarge labels in an isotropic input image without overlap, optionally specifying output image, dilation radius, and device.
    cle.dilate_labels(input_image: ndarray, radius: int = 2) -> ndarray

    * Generate a binary image with pixel values 0 and 1 by applying binary dilation on the input image considering the von Neumann neighborhood.
    cle.dilate_sphere(input_image: ndarray) -> ndarray

    * apply Gaussian blur to an image, divide the original by the result, and optionally choose sigma values and device settings
    cle.divide_by_gaussian_background(input_image: ndarray, sigma_x: float = 2, sigma_y: float = 2, sigma_z: float = 2) -> ndarray

    * perform binary erosion on an input image using either 'box' or 'sphere' connectivity, with pixel interpretation for non-zero values as 1.
    cle.erode(input_image: ndarray, connectivity: str = 'box') -> ndarray

    * Perform binary erosion on an input image using the von Neumann neighborhood, outputting a binary image with pixel values 0 and 1.
    cle.erode_sphere(input_image: ndarray) -> ndarray

    * segment and label an image using blurring, thresholding, erosion, and masked Voronoi-labeling, suitable for dense objects but may remove small objects.
    cle.eroded_otsu_labeling(input_image: ndarray, number_of_erosions: int = 5, outline_sigma: float = 2) -> ndarray

    * Remove edge-touching labels from an image and renumber remaining labels, with options to exclude edges along x, y, z axes and specify a computing device.
    cle.exclude_labels_on_edges(input_image: ndarray, exclude_x: bool = True, exclude_y: bool = True, exclude_z: bool = True) -> ndarray

    * Filter a label image to remove labels smaller than a specified minimum size, optionally specifying an output image and processing device.
    cle.exclude_large_labels(input_image: ndarray, min_size: float = 100) -> ndarray

    * Filter out labels in an image that exceed a specified maximum size.
    cle.exclude_small_labels(input_image: ndarray, max_size: float = 100) -> ndarray

    * Dilate regions in a label map image using an octagon shape until they touch, with results output to a specified device or image.
    cle.extend_labeling_via_voronoi(input_image: ndarray) -> ndarray

    * Label objects in grey-value images using Gaussian blur, Otsu-thresholding, and connected component labeling, with adjustable segmentation via outline_sigma.
    cle.gauss_otsu_labeling(input_image0: ndarray, outline_sigma: float = 0) -> ndarray

    * Apply a Gaussian blur to an image with specified sigma values for the X, Y, and Z axes, allowing for non-isotropic filtering and skipping blur in any direction with a zero sigma.
    cle.gaussian_blur(input_image: ndarray, sigma_x: float = 0, sigma_y: float = 0, sigma_z: float = 0) -> ndarray

    * Calculate a matrix representing the distances between points from two n-dimensional pointlists extracted from input images, with the resulting matrix size being (n+1) x (m+1).
    cle.generate_distance_matrix(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * generate a matrix representing label adjacency by marking touching labels in an input image, while utilizing an optional output image and device parameter.
    cle.generate_touch_matrix(input_image: ndarray) -> ndarray

    * Convert a binary image with single pixels set to 1 into a labeled spots image, where each detected spot is assigned a unique number.
    cle.label_spots(input_image: ndarray) -> ndarray

    * Generate a list of coordinates for labelled points in an image based on a labelmap resulting from connected components analysis.
    cle.labelled_spots_to_pointlist(input_image: ndarray) -> ndarray

    * Apply the Laplace operator using 'box' or 'sphere' connectivity to process an input image, optionally specifying an output image and device.
    cle.laplace(input_image: ndarray, connectivity: str = 'box') -> ndarray

    * Apply the Laplace operator using a Box neighborhood to process an input image, with options to specify an output image and the device for computation.
    cle.laplace_box(input_image: ndarray) -> ndarray

    * Apply the Laplace operator using a Diamond neighborhood to process an input image, optionally specifying an output image and device.
    cle.laplace_diamond(input_image: ndarray) -> ndarray

    * Apply a binary mask to an image, copying pixels from the input image to the output where the mask is non-zero, resulting in a masked image.
    cle.mask(input_image: ndarray, mask: ndarray) -> ndarray

    * Generate a masked image by copying pixels from an intensity image where corresponding pixels in a label image match a specified label value, with optional output image and device parameters.
    cle.mask_label(input_image0: ndarray, input_image1: ndarray, label: float = 1) -> ndarray

    * Label connected components and dilate them using an octagon shape within a masked area to produce an output label map, with optional device specification.
    cle.masked_voronoi_labeling(input_image: ndarray, mask: ndarray) -> ndarray

    * Compare each pixel value in an image with a constant scalar and output the maximum between them.
    cle.maximum_image_and_scalar(input_image: ndarray, scalar: float = 0) -> ndarray

    * Determine the maximum pixel value between two images, optionally storing the result in a specified output and selecting the device for computation.
    cle.maximum_images(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Calculate the local maximum within a spherical neighborhood for each pixel in an image, with customizable radii along the x, y, and z axes, and optionally specify an output image and device for processing.
    cle.maximum_sphere(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 0) -> ndarray

    * calculate the maximum intensity projection of an image along the Z-axis, optionally specifying an output image and a processing device.
    cle.maximum_z_projection(input_image: ndarray) -> ndarray

    * Calculate the local mean average of pixels within a specified neighborhood shape (box or sphere) in an image, with adjustable radius for each dimension.
    cle.mean(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1, connectivity: str = 'box') -> ndarray

    * Calculate the local mean average of pixels within a spherical neighborhood defined by specified radii in an image.
    cle.mean_sphere(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray

    * Calculate and store the mean squared error (MSE) between two images in the ImageJs Results table.
    cle.mean_squared_error(input_image0: ndarray, input_image1: ndarray) -> float

    * compute the mean average intensity projection of an image along the Z-axis, with optional output image and device specifications
    cle.mean_z_projection(input_image: ndarray) -> ndarray

    * Determine the local minimum in a spherical neighborhood of each pixel with specified radii in the x, y, and z axes on a selected device.
    cle.minimum_sphere(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray

    * Compute the minimum intensity projection of an image along the Z-axis, specifying optional output and device parameters.
    cle.minimum_z_projection(input_image: ndarray) -> ndarray

    * compute the local mode of a pixel's neighborhood in an image with specified radius and shape, using values from 0 to 255.
    cle.mode(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1, connectivity: str = 'box') -> ndarray

    * calculate the local mode of pixel intensities within a spherical neighborhood for semantic segmentation correction, with intensity values ranging from 0 to 255, using specified radii and device options.
    cle.mode_sphere(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray

    * Compute the remainder of division for corresponding pixel values between two images, optionally specifying an output image and device.
    cle.modulo_images(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Apply morphological opening to intensity or binary images using a spherical or box-shaped footprint with configurable radii and device options.
    cle.opening(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 0, connectivity: str = 'box') -> ndarray

    * Perform a morphological opening on a label image using an octagonal structuring element, with optional output image and device specification.
    cle.opening_labels(input_image: ndarray, radius: int = 0) -> ndarray

    * Apply morphological opening to intensity or binary images using a spherical footprint, specifying radii along x, y, and z axes, with optional output and device parameters.
    cle.opening_sphere(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 0) -> ndarray

    * extract pixel intensities from specified (x,y,z) coordinates in an image and store them in a vector
    cle.read_values_from_positions(input_image: ndarray, list: ndarray) -> ndarray

    * Reduce a label map to its centroids in an optional output image using a specified device.
    cle.reduce_labels_to_centroids(input_image: ndarray) -> ndarray

    * Extracts label edges from a label map, preserving label IDs and setting the background to zero, with optional device specification for processing.
    cle.reduce_labels_to_label_edges(input_image: ndarray) -> ndarray

    * Renumber labels in an image to eliminate gaps, ensuring the number of labels equals the maximum label index, primarily processed on the CPU.
    cle.relabel_sequential(input_image: ndarray, blocksize: int = 4096) -> ndarray

    * Remove labels from the edges of an image and renumber remaining elements, with options to exclude specific axes and specify a device for operation.
    cle.remove_labels_on_edges(input_image: ndarray, exclude_x: bool = True, exclude_y: bool = True, exclude_z: bool = True) -> ndarray

    * Filter out objects larger than a specified size from a label map image.
    cle.remove_large_labels(input_image: ndarray, max_size: float = 100) -> ndarray

    * Remove labelled objects smaller than a specified pixel size from a label map image, with optional output image specification and device selection.
    cle.remove_small_labels(input_image: ndarray, min_size: float = 100) -> ndarray

    * Replace the intensities of an input image based on a vector mapping old to new intensity values, with optional specification of the output image and device for processing.
    cle.replace_intensities(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Replace pixel intensities in an image using a vector where the index corresponds to old intensities and the value to new ones, with optional output image and device specification.
    cle.replace_values(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Translate and rotate an image by specified vectors and angles (in degrees) optionally with interpolation and resizing, supporting operation on specified devices.
    cle.rigid_transform(input_image: ndarray, translate_x: float = 0, translate_y: float = 0, translate_z: float = 0, angle_x: float = 0, angle_y: float = 0, angle_z: float = 0, centered: bool = True, interpolate: bool = False, resize: bool = False) -> ndarray

    * Perform a morphological opening on a label image, fill gaps using Voronoi labeling, and retain the background, suitable for isotropic images.
    cle.smooth_labels(input_image: ndarray, radius: int = 0) -> ndarray

    * Apply the Sobel kernel to an input image for edge detection with optional device specification and output.
    cle.sobel(input_image: ndarray) -> ndarray

    * Calculate the squared pixel-by-pixel difference between two images, optionally specifying an output image and a device for processing.
    cle.squared_difference(input_image0: ndarray, input_image1: ndarray) -> ndarray

    * Calculate the local standard deviation of an image's pixel neighborhood with specified radii and optional output image, using either a box or sphere connectivity shape.
    cle.standard_deviation(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1, connectivity: str = 'box') -> ndarray

    * Calculate the local standard deviation in a pixel's spherical neighborhood based on specified radii along the x, y, and (optionally) z axes for either 2D or 3D images, with an optional device specification for processing.
    cle.standard_deviation_sphere(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray

    * compute the standard deviation intensity projection of an image stack along the Z-axis, with optional specification of output image and device.
    cle.std_z_projection(input_image: ndarray) -> ndarray

    * Subtracts a Gaussian-blurred version of an image from the original, with configurable blur radii and optional output image and device specification.
    cle.subtract_gaussian_background(input_image: ndarray, sigma_x: float = 2, sigma_y: float = 2, sigma_z: float = 2) -> ndarray

    * Calculate the sum intensity projection of an image along the Z-axis, optionally specifying an output image and device.
    cle.sum_z_projection(input_image: ndarray) -> ndarray

    * Convert an image to binary using Otsu's thresholding via a GPU-accelerated histogram.
    cle.threshold_otsu(input_image: ndarray) -> ndarray

    * perform background subtraction on an image using a tophat filter with customizable radii and connectivity options
    cle.top_hat(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1, connectivity: str = 'box') -> ndarray

    * Subtract the background from an input image using a tophat filter with customizable radii and device options.
    cle.top_hat_sphere(input_image: ndarray, radius_x: float = 1, radius_y: float = 1, radius_z: float = 1) -> ndarray

    * Calculate the local variance of a pixel's spherical neighborhood in an image, considering specified radii for each axis and optionally designating output and processing device.
    cle.variance_sphere(input_image: ndarray, radius_x: int = 1, radius_y: int = 1, radius_z: int = 1) -> ndarray

    * Label connected components in a binary image and dilate regions using an octagon shape until they touch, returning the resulting label map.
    cle.voronoi_labeling(input_image: ndarray) -> ndarray

    * Label objects in isotropic greyvalue images by applying Gaussian blurs, spot detection, Otsu thresholding, and Voronoi labeling with parameters for segmentation precision and cell proximity control.
    cle.voronoi_otsu_labeling(input_image: ndarray, spot_sigma: float = 2, outline_sigma: float = 2) -> ndarray

    """
