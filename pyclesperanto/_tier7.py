#
# This code is auto-generated from 'tier7.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function


@plugin_function
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
        target image
    output_image: Image = None
        translation along x axis in pixels
    translate_x: float = 0
        translation along y axis in pixels
    translate_y: float = 0
        translation along z axis in pixels
    translate_z: float = 0
        rotation around x axis in radians
    angle_x: float = 0
        rotation around y axis in radians
    angle_y: float = 0
        rotation around z axis in radians
    angle_z: float = 0
    centered: bool = True
    interpolate: bool = False
    resize: bool = False
        If true, bi/trilinear interpolation will be applied, if hardware allows.
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



@plugin_function
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
        target image
    output_image: Image = None
        rotation around x axis in degrees
    angle_x: float = 0
        rotation around y axis in degrees
    angle_y: float = 0
        rotation around z axis in degrees
    angle_z: float = 0
    centered: bool = True
    interpolate: bool = False
    resize: bool = False
        If true, bi/trilinear interpolation will be applied, if hardware supports it.
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



@plugin_function
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
        target image
    output_image: Image = None
        scaling along x
    factor_x: float = 1
        scaling along y
    factor_y: float = 1
        scaling along z
    factor_z: float = 1
        If true, the image will be scaled to the center of the image.
    centered: bool = True
        If true, bi/trilinear interplation will be applied.
    interpolate: bool = False
        Automatically determines output size image.
    resize: bool = False
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



@plugin_function
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
        image to be translated
    output_image: Image = None
        target image
    translate_x: float = 0
        translation along x axis in pixels
    translate_y: float = 0
        translation along y axis in pixels
    translate_z: float = 0
        translation along z axis in pixels
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



@plugin_function
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
    output_image: Image = None
    radius: int = 0
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



@plugin_function
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
    output_image: Image = None
    radius: int = 0
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



@plugin_function
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
        controls how close detected cells can be
    outline_sigma: float = 2
        controls how precise segmented objects are outlined.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    Links
    -----
    [1] https://clij.github.io/clij2docs/reference_voronoiOtsuLabeling
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

