#
# This code is auto-generated from CLIc 'cle::tier7.hpp' file, do not edit manually.
#

import importlib
import warnings
from typing import Optional

import numpy as np

from ._array import Image
from ._core import Device
from ._decorators import plugin_function

clic = importlib.import_module('._pyclesperanto', package='pyclesperanto')

@plugin_function
def affine_transform(
    input_image: Image,
    output_image: Optional[Image] =None,
    transform_matrix: Optional[list] =None,
    interpolate: bool =False,
    resize: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Apply an affine transformation matrix to an array and return the result.  The
    transformation matrix must be 3x3 or 4x4 stored as a 1D array.  The matrix
    should be row-major, i.e. the first 3 elements are the first row of the matrix.
    If no matrix is given, the identity matrix will be used.

    Parameters
    ----------
    input_image: Image 
        Input image to be transformed.
    output_image: Optional[Image] (= None)
        Output image.
    transform_matrix: Optional[list] (= None)
        Affine transformation matrix (3x3 or 4x4).
    interpolate: bool (= False)
        If true, bi/trilinear interpolation will be applied, if hardware allows.
    resize: bool (= False)
        Automatically determines the size of the output depending on the rotation angles.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._affine_transform(device, input_image, output_image, transform_matrix, interpolate, resize)

@plugin_function(categories=["label", "in assistant"])
def eroded_otsu_labeling(
    input_image: Image,
    output_image: Optional[Image] =None,
    number_of_erosions: int =5,
    outline_sigma: float =2,
    device: Optional[Device] =None
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
        Input image to be transformed.
    output_image: Optional[Image] (= None)
        Output label image.
    number_of_erosions: int (= 5)
        Number of iteration of erosion.
    outline_sigma: float (= 2)
        Gaussian blur sigma applied before Otsu thresholding.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image

    References
    ----------
    [1] https://github.com/biovoxxel/bv3dbox (BV_LabelSplitter.java#L83)
    [2] https://zenodo.org/badge/latestdoi/434949702
    """
    return clic._eroded_otsu_labeling(device, input_image, output_image, int(number_of_erosions), float(outline_sigma))

@plugin_function(categories=["transform", "in assistant"])
def rigid_transform(
    input_image: Image,
    output_image: Optional[Image] =None,
    translate_x: float =0,
    translate_y: float =0,
    translate_z: float =0,
    angle_x: float =0,
    angle_y: float =0,
    angle_z: float =0,
    centered: bool =True,
    interpolate: bool =False,
    resize: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Translate the image by a given vector and rotate it by given angles. Angles are
    given in degrees. To convert radians to degrees, use this formula:
    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    input_image: Image 
        Input image to be transformed.
    output_image: Optional[Image] (= None)
        Output image.
    translate_x: float (= 0)
        Translation along x axis in pixels.
    translate_y: float (= 0)
        Translation along y axis in pixels.
    translate_z: float (= 0)
        Translation along z axis in pixels.
    angle_x: float (= 0)
        Rotation around x axis in radians.
    angle_y: float (= 0)
        Rotation around y axis in radians.
    angle_z: float (= 0)
        Rotation around z axis in radians.
    centered: bool (= True)
        If true, rotate image around center, else around the origin.
    interpolate: bool (= False)
        If true, bi/trilinear interpolation will be applied, if hardware allows.
    resize: bool (= False)
        Automatically determines the size of the output depending on the rotation angles.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._rigid_transform(device, input_image, output_image, float(translate_x), float(translate_y), float(translate_z), float(angle_x), float(angle_y), float(angle_z), centered, interpolate, resize)

@plugin_function(categories=["transform", "in assistant"])
def rotate(
    input_image: Image,
    output_image: Optional[Image] =None,
    angle_x: float =0,
    angle_y: float =0,
    angle_z: float =0,
    centered: bool =True,
    interpolate: bool =False,
    resize: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Rotate the image by given angles. Angles are given in degrees. To convert
    radians to degrees, use this formula: angle_in_degrees = angle_in_radians /
    numpy.pi * 180.0

    Parameters
    ----------
    input_image: Image 
        Input image to be rotated.
    output_image: Optional[Image] (= None)
        Output image.
    angle_x: float (= 0)
        Rotation around x axis in degrees.
    angle_y: float (= 0)
        Rotation around y axis in degrees.
    angle_z: float (= 0)
        Rotation around z axis in degrees.
    centered: bool (= True)
        If true, rotate image around center, else around the origin.
    interpolate: bool (= False)
        If true, bi/trilinear interpolation will be applied, if hardware allows.
    resize: bool (= False)
        Automatically determines the size of the output depending on the rotation angles.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._rotate(device, input_image, output_image, float(angle_x), float(angle_y), float(angle_z), centered, interpolate, resize)

@plugin_function(categories=["transform", "in assistant"])
def scale(
    input_image: Image,
    output_image: Optional[Image] =None,
    factor_x: float =1,
    factor_y: float =1,
    factor_z: float =1,
    centered: bool =True,
    interpolate: bool =False,
    resize: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Scale the image by given factors.

    Parameters
    ----------
    input_image: Image 
        Input image to be scaled.
    output_image: Optional[Image] (= None)
        Output image.
    factor_x: float (= 1)
        Scaling along x axis.
    factor_y: float (= 1)
        Scaling along y axis.
    factor_z: float (= 1)
        Scaling along z axis.
    centered: bool (= True)
        If true, the image will be scaled to the center of the image.
    interpolate: bool (= False)
        If true, bi/trilinear interplation will be applied.
    resize: bool (= False)
        Automatically determines output size image.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._scale(device, input_image, output_image, float(factor_x), float(factor_y), float(factor_z), centered, interpolate, resize)

@plugin_function(categories=["transform", "in assistant"])
def translate(
    input_image: Image,
    output_image: Optional[Image] =None,
    translate_x: float =0,
    translate_y: float =0,
    translate_z: float =0,
    interpolate: bool =False,
    device: Optional[Device] =None
) -> Image:
    """Translate the image by a given vector.

    Parameters
    ----------
    input_image: Image 
        Input image to be translated.
    output_image: Optional[Image] (= None)
        Output image.
    translate_x: float (= 0)
        Translation along x axis in pixels.
    translate_y: float (= 0)
        Translation along y axis in pixels.
    translate_z: float (= 0)
        Translation along z axis in pixels.
    interpolate: bool (= False)
        If true, bi/trilinear interplation will be applied.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._translate(device, input_image, output_image, float(translate_x), float(translate_y), float(translate_z), interpolate)

@plugin_function(categories=["label processing", "in assistant"])
def closing_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Apply a morphological closing operation to a label image. The operation consists
    of iterative dilation and erosion of the labels. With every iteration, box and
    diamond/sphere structuring elements are used and thus, the operation has an
    octagon as structuring element. Notes * This operation assumes input images are
    isotropic.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    radius: int (= 0)
        Radius size for the closing.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._closing_labels(device, input_image, output_image, int(radius))

@plugin_function(categories=["label processing", "in assistant"])
def erode_connected_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =1,
    device: Optional[Device] =None
) -> Image:
    """Erodes labels to a smaller size. Note: Depending on the label image and the
    radius,  labels may disappear and labels may split into multiple islands. Thus,
    overlapping labels of input and output may  not have the same identifier.

    Parameters
    ----------
    input_image: Image 
        Input image to process
    output_image: Optional[Image] (= None)
        Output label image
    radius: int (= 1)
        
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._erode_connected_labels(device, input_image, output_image, int(radius))

@plugin_function(categories=["label processing", "in assistant"])
def opening_labels(
    input_image: Image,
    output_image: Optional[Image] =None,
    radius: int =0,
    device: Optional[Device] =None
) -> Image:
    """Apply a morphological opening operation to a label image. The operation consists
    of iterative erosion and dilation of the labels. With every iteration, box and
    diamond/sphere structuring elements are used and thus, the operation has an
    octagon as structuring element. Notes * This operation assumes input images are
    isotropic.

    Parameters
    ----------
    input_image: Image 
        Input label image.
    output_image: Optional[Image] (= None)
        Output label image.
    radius: int (= 0)
        Radius size for the opening.
    device: Optional[Device] (= None)
        Device to perform the operation on.

    Returns
    -------
    Image
    """
    return clic._opening_labels(device, input_image, output_image, int(radius))

@plugin_function(categories=["label", "in assistant", "bia-bob-suggestion"])
def voronoi_otsu_labeling(
    input_image: Image,
    output_image: Optional[Image] =None,
    spot_sigma: float =2,
    outline_sigma: float =2,
    device: Optional[Device] =None
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
        Input intensity image.
    output_image: Optional[Image] (= None)
        Output label image.
    spot_sigma: float (= 2)
        Controls how close detected cells can be.
    outline_sigma: float (= 2)
        Controls how precise segmented objects are outlined.
    device: Optional[Device] (= None)
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
    return clic._voronoi_otsu_labeling(device, input_image, output_image, float(spot_sigma), float(outline_sigma))