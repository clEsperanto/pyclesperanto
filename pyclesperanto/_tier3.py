#
# This code is auto-generated from 'tier3.hpp' file, using 'gencle' script.
# Do not edit manually.
#

from ._core import Device
from ._array import Image
from ._decorators import plugin_function
import numpy as np


@plugin_function
def bounding_box(
    input_image: Image,
    device: Device = None
) -> list:
    """Determines the bounding box of all nonzero pixels in a binary image. The
    positions are returned in  an array of 6 values as follows: minX, minY, minZ,
    maxX, maxY, maxZ.

    Parameters
    ----------
    input_image: Image
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    list
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_boundingBox
    """

    from ._pyclesperanto import _bounding_box as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def center_of_mass(
    input_image: Image,
    device: Device = None
) -> list:
    """Determines the center of mass of an image or image stack. It writes the result
    in the results table in the columns MassX, MassY and MassZ.

    Parameters
    ----------
    input_image: Image
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    list
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_centerOfMass
    """

    from ._pyclesperanto import _center_of_mass as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def exclude_labels(
    input_image: Image,
    list: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """This operation removes labels from a labelmap and renumbers the remaining
    labels. Hand over a binary flag list vector starting with a flag for the
    background, continuing with label1, label2,... For example if you pass
    0,1,0,0,1: Labels 1 and 4 will be removed (those with a 1 in the vector will be
    excluded). Labels 2 and 3 will be kept and renumbered to 1 and 2.

    Parameters
    ----------
    input_image: Image
    list: Image
    output_image: Image = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabels
    """

    from ._pyclesperanto import _exclude_labels as op

    return op(
        device=device,
        src=input_image,
        list=list,
        dst=output_image
    )



@plugin_function(category=['label processing', 'in assistant', 'bia-bob-suggestion'])
def exclude_labels_on_edges(
    input_image: Image,
    output_image: Image = None,
    exclude_x: bool = True,
    exclude_y: bool = True,
    exclude_z: bool = True,
    device: Device = None
) -> Image:
    """Removes all labels from a label map which touch the edges of the image.
    Remaining label elements are renumbered afterwards.

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    exclude_x: bool = True
        Exclude labels along min and max x
    exclude_y: bool = True
        Exclude labels along min and max y
    exclude_z: bool = True
        Exclude labels along min and max z
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_excludeLabelsOnEdges
    """

    from ._pyclesperanto import _exclude_labels_on_edges as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        exclude_x=bool(exclude_x),
        exclude_y=bool(exclude_y),
        exclude_z=bool(exclude_z)
    )



@plugin_function
def flag_existing_labels(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Given a label map this function will generate a binary vector where all pixels
    are set to 1 if label with given xcoordinate in the vector exists. For example a
    label image such as ``` 0 1 3 5 ``` will produce a flag_vector like this: ``` 1
    1 0 1 0 1 ```

    Parameters
    ----------
    input_image: Image
        a label image
    output_image: Image = None
        binary vector, if given should have size 1*n with n = maximum label + 1
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    """

    from ._pyclesperanto import _flag_existing_labels as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function(category=['filter', 'in assistant'])
def gamma_correction(
    input_image: Image,
    output_image: Image = None,
    gamma: float = 1,
    device: Device = None
) -> Image:
    """Applies a gamma correction to an image. Therefore, all pixels x of the Image X
    are normalized and the power to gamma g is computed, before normlization is
    reversed (^ is the power operator):f(x) = (x / max(X)) ^ gamma * max(X)

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    gamma: float = 1
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_gammaCorrection
    """

    from ._pyclesperanto import _gamma_correction as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        gamma=float(gamma)
    )



@plugin_function
def generate_binary_overlap_matrix(
    input_image0: Image,
    input_image1: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes two labelmaps with n and m labels and generates a (n+1)*(m+1) matrix where
    all pixels are set to 0 exept those where labels overlap between the label maps.
    For example, if labels 3 in labelmap1 and 4 in labelmap2 are touching then the
    pixel (3,4) in the matrix will be set to 1.

    Parameters
    ----------
    input_image0: Image
    input_image1: Image
    output_image: Image = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_generateBinaryOverlapMatrix
    """

    from ._pyclesperanto import _generate_binary_overlap_matrix as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1,
        dst=output_image
    )



@plugin_function(category=['bia-bob-suggestion'])
def generate_touch_matrix(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Takes a labelmap with n labels and generates a (n+1)*(n+1) matrix where all
    pixels are set to 0 exept those where labels are touching. Only half of the
    matrix is filled (with x < y). For example, if labels 3 and 4 are touching then
    the pixel (3,4) in the matrix will be set to 1. The touch matrix is a
    representation of a region adjacency graph

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_generateTouchMatrix
    """

    from ._pyclesperanto import _generate_touch_matrix as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def histogram(
    input_image: Image,
    output_image: Image = None,
    nbins: int = 256,
    min: float = None,
    max: float = None,
    device: Device = None
) -> Image:
    """Determines the histogram of a given image. The histogram image is of dimensions
    number_of_bins/1/1; a 3D image with height=1 and depth=1. Histogram bins contain
    the number of pixels with intensity in this corresponding bin. The histogram
    bins are uniformly distributed between given minimum and maximum grey value
    intensity. If the flag determine_min_max is set, minimum and maximum intensity
    will be determined. When calling this operation many times, it is recommended to
    determine minimum and maximum intensity once at the beginning and handing over
    these values. Author(s): Robert Haase adapted work from Aaftab Munshi, Benedict
    Gaster, Timothy Mattson, James Fung, Dan Ginsburg License: adapted code from
    https://github.com/bgaster/openclbooksamples/blob/master/src/Chapter_14/histogram/histogram_image.cl
    It was published unter BSD license according to
    https://code.google.com/archive/p/openclbooksamples/ Book: OpenCL(R) Programming
    Guide Authors: Aaftab Munshi, Benedict Gaster, Timothy Mattson, James Fung, Dan
    Ginsburg ISBN10: 0321749642 ISBN13: 9780321749642 Publisher: AddisonWesley
    Professional URLs: http://safari.informit.com/9780132488006/
    http://www.openclprogrammingguide.com

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    nbins: int = 256
    min: float = None
    max: float = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_histogram
    """

    from ._pyclesperanto import _histogram as op

    return op(
        device=device,
        src=input_image,
        dst=output_image,
        nbins=int(nbins),
        min=float(min),
        max=float(max)
    )



@plugin_function
def jaccard_index(
    input_image0: Image,
    input_image1: Image,
    device: Device = None
) -> float:
    """Determines the overlap of two binary images using the Jaccard index. A value of
    0 suggests no overlap, 1 means perfect overlap. The resulting Jaccard index is
    saved to the results table in the 'Jaccard_Index' column. Note that the
    SorensenDice coefficient can be calculated from the Jaccard index j using this
    formula: <pre>s = f(j) = 2 j / (j + 1)</pre>

    Parameters
    ----------
    input_image0: Image
    input_image1: Image
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_jaccardIndex
    """

    from ._pyclesperanto import _jaccard_index as op

    return op(
        device=device,
        src0=input_image0,
        src1=input_image1
    )



@plugin_function(category=['bia-bob-suggestion'])
def labelled_spots_to_pointlist(
    input_image: Image,
    output_image: Image = None,
    device: Device = None
) -> Image:
    """Generates a coordinate list of points in a labelled spot image. Transforms a
    labelmap of spots (single pixels with values 1, 2,..., n for n spots) as
    resulting from connected components analysis in an image where every column
    contains d pixels (with d = dimensionality of the original image) with the
    coordinates of the maxima/minima.

    Parameters
    ----------
    input_image: Image
    output_image: Image = None
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    Image
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_labelledSpotsToPointList
    """

    from ._pyclesperanto import _labelled_spots_to_pointlist as op

    return op(
        device=device,
        src=input_image,
        dst=output_image
    )



@plugin_function
def maximum_position(
    input_image: Image,
    device: Device = None
) -> list:
    """Determines the position of the maximum of all pixels in a given image.

    Parameters
    ----------
    input_image: Image
        The image of which the position of the maximum of all pixels will be determined.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    list
    
    """

    from ._pyclesperanto import _maximum_position as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def mean_of_all_pixels(
    input_image: Image,
    device: Device = None
) -> float:
    """Determines the mean average of all pixels in a given image.

    Parameters
    ----------
    input_image: Image
        The image of which the mean average of all pixels will be determined.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    float
    
    References
    ----------
    [1] https://clij.github.io/clij2-docs/reference_meanOfAllPixels
    """

    from ._pyclesperanto import _mean_of_all_pixels as op

    return op(
        device=device,
        src=input_image
    )



@plugin_function
def minimum_position(
    input_image: Image,
    device: Device = None
) -> list:
    """Determines the position of the minimum of all pixels in a given image.

    Parameters
    ----------
    input_image: Image
        The image of which the position of the minimum of all pixels will be determined.
    device: Device = None
        Device to perform the operation on.

    Returns
    -------
    list
    
    """

    from ._pyclesperanto import _minimum_position as op

    return op(
        device=device,
        src=input_image
    )

