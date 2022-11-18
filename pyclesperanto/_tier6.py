from ._image import Image
from ._device import Device
from ._decorators import plugin_function


@plugin_function
def voronoi_otsu_labeling(
    input_image: Image,
    output_image: Image = None,
    spot_sigma: float = 2,
    outline_sigma: float = 2,
    device: Device = None,
) -> Image:
    """Labels objects directly from grey-value images.

    The two sigma parameters allow tuning the segmentation result. Under the hood,
    this filter applies two Gaussian blurs, spot detection, Otsu-thresholding [1] and Voronoi-labeling [2]. The
    thresholded binary image is flooded using the Voronoi tesselation approach starting from the found local maxima.

    Parameters
    ----------
    input_image : Image
        Input grey-value image
    output_image : Image, optional
        Output image
    spot_sigma : float, optional
        controls how close detected cells can be
    outline_sigma : float, optional
        controls how precise segmented objects are outlined.

    Returns
    -------
    output_image

    References
    ----------
    .. [1] https://ieeexplore.ieee.org/document/4310076
    .. [2] https://en.wikipedia.org/wiki/Voronoi_diagram
    """
    from ._pyclesperanto import _VoronoiOtsuLabelingKernel_Call as op

    op(
        device,
        src=input_image,
        dst=output_image,
        sigma_spot=float(spot_sigma),
        sigma_outline=float(outline_sigma),
    )
    return output_image
