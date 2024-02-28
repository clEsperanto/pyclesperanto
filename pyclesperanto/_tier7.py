#
# This code is auto-generated from 'tier7.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function(category=['label', 'in assistant', 'bia-bob-suggestion'])
def eroded_otsu_labeling(
    input_image: Image,
    output_image: Image = None,
    number_of_erosions: int = 5,
    outline_sigma: float = 2,
    device: Device = None
) -> Image:
    """Segments and labels an image using blurring, Otsu-thresholding, binary erosion
    and  masked Voronoi-labeling.  After bluring and Otsu-thresholding the image,
    iterative binary erosion is applied.  Objects in the eroded image are labeled
    and the labels are extended to fit again into  the initial binary image using
    masked-Voronoi labeling.  This function is similar to voronoi_otsu_labeling. It
    is intended to deal better in  case labels of objects swapping into each other
    if objects are dense. Like when using  Voronoi-Otsu-labeling, small objects may
    disappear when applying this operation.  This function is inspired by a similar
    implementation in Java by Jan Brocher (Biovoxxel) [0] [1]

    Parameters
    ----------
    input_image: Image
        Image to be transformed
    output_image: Image = None
        Output image
    number_of_erosions: int = 5
        Number of iteration of erosion
    outline_sigma: float = 2
        Gaussian blur sigma applied before Otsu thresholding
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] [0] https://github.com/biovoxxel/bv3dbox (BV_LabelSplitter.java#L83)
	[2] [1] https://zenodo.org/badge/latestdoi/434949702
    """

    from ._pyclesperanto import _eroded_otsu_labeling as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        number_of_erosions=int(number_of_erosions),
        outline_sigma=float(outline_sigma)
    )



@plugin_function(category=['transform', 'in assistant', 'bia-bob-suggestion'])
def rigid_transform(
    input_image: Image,
    output_image: Image = None,
    translate_x: float = 0,
    translate_y: float = 0,
    translate_z: float = 0,
    angle_x: float = 0,
    angle_y: float = 0,
    angle_z: float = 0,
    centered: bool = True,
    interpolate: bool = False,
    resize: bool = False,
    device: Device = None
) -> Image:
    """Translate the image by a given vector and rotate it by given angles. Angles are
    given in degrees. To convert radians to degrees, use this formula:
    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    input_image: Image
        Image to be transformed
    output_image: Image = None
        Output image
    translate_x: float = 0
        Translation along x axis in pixels
    translate_y: float = 0
        Translation along y axis in pixels
    translate_z: float = 0
        Translation along z axis in pixels
    angle_x: float = 0
        Rotation around x axis in radians
    angle_y: float = 0
        Rotation around y axis in radians
    angle_z: float = 0
        Rotation around z axis in radians
    centered: bool = True
        If true, rotate image around center, else around the origin
    interpolate: bool = False
        If true, bi/trilinear interpolation will be applied, if hardware allows.
    resize: bool = False
        Automatically determines the size of the output depending on the rotation angles.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _rigid_transform as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        translate_x=float(translate_x),
        translate_y=float(translate_y),
        translate_z=float(translate_z),
        angle_x=float(angle_x),
        angle_y=float(angle_y),
        angle_z=float(angle_z),
        centered=bool(centered),
        interpolate=bool(interpolate),
        resize=bool(resize)
    )



@plugin_function(category=['transform', 'in assistant'])
def rotate(
    input_image: Image,
    output_image: Image = None,
    angle_x: float = 0,
    angle_y: float = 0,
    angle_z: float = 0,
    centered: bool = True,
    interpolate: bool = False,
    resize: bool = False,
    device: Device = None
) -> Image:
    """Rotate the image by given angles. Angles are given in degrees. To convert
    radians to degrees, use this formula: angle_in_degrees = angle_in_radians /
    numpy.pi * 180.0

    Parameters
    ----------
    input_image: Image
        Image to be rotated
    output_image: Image = None
        Output image
    angle_x: float = 0
        Rotation around x axis in degrees
    angle_y: float = 0
        Rotation around y axis in degrees
    angle_z: float = 0
        Rotation around z axis in degrees
    centered: bool = True
        If true, rotate image around center, else around the origin
    interpolate: bool = False
        If true, bi/trilinear interpolation will be applied, if hardware allows.
    resize: bool = False
        Automatically determines the size of the output depending on the rotation angles.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _rotate as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        angle_x=float(angle_x),
        angle_y=float(angle_y),
        angle_z=float(angle_z),
        centered=bool(centered),
        interpolate=bool(interpolate),
        resize=bool(resize)
    )



@plugin_function(category=['transform', 'in assistant'])
def scale(
    input_image: Image,
    output_image: Image = None,
    factor_x: float = 1,
    factor_y: float = 1,
    factor_z: float = 1,
    centered: bool = True,
    interpolate: bool = False,
    resize: bool = False,
    device: Device = None
) -> Image:
    """Scale the image by given factors.

    Parameters
    ----------
    input_image: Image
        Image to be scaleded
    output_image: Image = None
        Output image
    factor_x: float = 1
        Scaling along x
    factor_y: float = 1
        Scaling along y
    factor_z: float = 1
        Scaling along z
    centered: bool = True
        If true, the image will be scaled to the center of the image.
    interpolate: bool = False
        If true, bi/trilinear interplation will be applied.
    resize: bool = False
        Automatically determines output size image.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _scale as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        factor_x=float(factor_x),
        factor_y=float(factor_y),
        factor_z=float(factor_z),
        centered=bool(centered),
        interpolate=bool(interpolate),
        resize=bool(resize)
    )



@plugin_function(category=['transform', 'in assistant'])
def translate(
    input_image: Image,
    output_image: Image = None,
    translate_x: float = 0,
    translate_y: float = 0,
    translate_z: float = 0,
    interpolate: bool = False,
    device: Device = None
) -> Image:
    """Translate the image by a given vector.

    Parameters
    ----------
    input_image: Image
        Image to be translated
    output_image: Image = None
        Output image
    translate_x: float = 0
        Translation along x axis in pixels
    translate_y: float = 0
        Translation along y axis in pixels
    translate_z: float = 0
        Translation along z axis in pixels
    interpolate: bool = False
        If true, bi/trilinear interplation will be applied.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _translate as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        translate_x=float(translate_x),
        translate_y=float(translate_y),
        translate_z=float(translate_z),
        interpolate=bool(interpolate)
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def closing_labels(
    input_image: Image,
    output_image: Image = None,
    radius: int = 0,
    device: Device = None
) -> Image:
    """Apply a morphological closing operation to a label image. The operation consists
    of iterative dilation and erosion of the labels. With every iteration, box and
    diamond/sphere structuring elements are used and thus, the operation has an
    octagon as structuring element. Notes * This operation assumes input images are
    isotropic.

    Parameters
    ----------
    input_image: Image
        Input label image
    output_image: Image = None
        Output label image
    radius: int = 0
        Radius size for the closing
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _closing_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius=int(radius)
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def opening_labels(
    input_image: Image,
    output_image: Image = None,
    radius: int = 0,
    device: Device = None
) -> Image:
    """Apply a morphological opening operation to a label image. The operation consists
    of iterative erosion and dilation of the labels. With every iteration, box and
    diamond/sphere structuring elements are used and thus, the operation has an
    octagon as structuring element. Notes * This operation assumes input images are
    isotropic.

    Parameters
    ----------
    input_image: Image
        Input label image
    output_image: Image = None
        Output label image
    radius: int = 0
        Radius size for the opening
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _opening_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        radius=int(radius)
    )



@plugin_function(category=['label', 'in assistant', 'bia-bob-suggestion'], priority=1)
def voronoi_otsu_labeling(
    input_image: Image,
    output_image: Image = None,
    spot_sigma: float = 2,
    outline_sigma: float = 2,
    device: Device = None
) -> Image:
    """Labels objects directly from greyvalue images. The two sigma parameters allow
    tuning the segmentation result. Under the hood, this filter applies two Gaussian
    blurs, spot detection, Otsuthresholding [2] and Voronoilabeling [3]. The
    thresholded binary image is flooded using the Voronoi tesselation approach
    starting from the found local maxima. Notes * This operation assumes input
    images are isotropic.

    Parameters
    ----------
    input_image: Image
        Input greyvalue image
    output_image: Image = None
        Output image
    spot_sigma: float = 2
        Controls how close detected cells can be
    outline_sigma: float = 2
        Controls how precise segmented objects are outlined.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_voronoiOtsuLabeling
	[2] https://ieeexplore.ieee.org/document/4310076
	[3] https://en.wikipedia.org/wiki/Voronoi_diagram
    """

    from ._pyclesperanto import _voronoi_otsu_labeling as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        spot_sigma=float(spot_sigma),
        outline_sigma=float(outline_sigma)
    )

