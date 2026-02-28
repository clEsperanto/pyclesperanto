from inspect import getmembers, isfunction
from os import path
from pathlib import Path
from typing import Callable, Optional, Union

import numpy as np
from matplotlib.colors import ListedColormap

from ._memory import pull

def imshow(
    image,
    title: Optional[str] = None,
    labels: Optional[bool] = False,
    min_display_intensity: Optional[float] = None,
    max_display_intensity: Optional[float] = None,
    color_map: Optional[str] = None,
    plot=None,
    colorbar: Optional[bool] = False,
    colormap: Union[str, ListedColormap, None] = None,
    alpha: Optional[float] = None,
    continue_drawing: Optional[bool] = False,
):
    """Visualize an image, e.g. in Jupyter notebooks using matplotlib.

    Parameters
    ----------
    image: np.ndarray
        numpy or OpenCL-backed image to visualize
    title: str, optional
        Obsolete (kept for ImageJ-compatibility)
    labels: bool, optional
        True: integer labels will be visualized with colors
        False: Specified or default colormap will be used to display intensities.
    min_display_intensity: float, optional
        lower limit for display range
    max_display_intensity: float, optional
        upper limit for display range
    color_map: str, optional
        deprecated, use colormap instead
    plot: matplotlib axis, optional
        Plot object where the image should be shown. Useful for putting multiple images in subfigures.
    colorbar: bool, optional
        True puts a colorbar next to the image. Will not work with label images and when visualizing multiple
        images (continue_drawing=True).
    colormap: str or matplotlib colormap, optional
    alpha: float, optional
        alpha blending value
    continue_drawing: float
        True: the next shown image can be visualized on top of the current one, e.g. with alpha = 0.5
    """
    if len(image.shape) == 3:
        from ._tier1 import maximum_z_projection

        image = pull(maximum_z_projection(image))

    image = pull(image)

    if color_map is not None:
        import warnings

        warnings.warn(
            "The imshow parameter color_map is deprecated. Use colormap instead."
        )
        if colormap is None:
            colormap = color_map

    if labels:
        if not hasattr(imshow, "colormap"):
            from numpy.random import MT19937, RandomState, SeedSequence

            rs = RandomState(MT19937(SeedSequence(3)))
            lut = rs.rand(65537, 3)
            lut[0, :] = 0
            # these are the first four colours from matplotlib's default
            lut[1] = [0.12156862745098039, 0.4666666666666667, 0.7058823529411765]
            lut[2] = [1.0, 0.4980392156862745, 0.054901960784313725]
            lut[3] = [0.17254901960784313, 0.6274509803921569, 0.17254901960784313]
            lut[4] = [0.8392156862745098, 0.15294117647058825, 0.1568627450980392]
            colormap = ListedColormap(lut)

        if min_display_intensity is None:
            min_display_intensity = 0
        if max_display_intensity is None:
            max_display_intensity = 65536

    if colormap is None:
        colormap = "Greys_r"

    cmap = colormap
    if plot is None:
        import matplotlib.pyplot as plt

        plt.imshow(
            image,
            cmap=cmap,
            vmin=min_display_intensity,
            vmax=max_display_intensity,
            interpolation="nearest",
            alpha=alpha,
        )
        if colorbar:
            plt.colorbar()
        if not continue_drawing:
            plt.show()
    else:
        plot.imshow(
            image,
            cmap=cmap,
            vmin=min_display_intensity,
            vmax=max_display_intensity,
            interpolation="nearest",
            alpha=alpha,
        )
        if colorbar:
            plot.colorbar()
    if title is not None:
        plt.title(title)


def operations(
    must_have_categories: list = None, must_not_have_categories: list = None
) -> dict:
    """Retrieve a dictionary of operations, which can be filtered by annotated categories.

    Parameters
    ----------
    must_have_categories : list of str, optional
        if provided, the result will be filtered so that operations must contain all given categories.
    must_not_have_categories : list of str, optional
        if provided, the result will be filtered so that operations must not contain all given categories.

    Returns
    -------
    dict of str : Callable function
    """

    import pyclesperanto as cle

    if isinstance(must_have_categories, str):
        must_have_categories = [must_have_categories]
    if isinstance(must_not_have_categories, str):
        must_have_categories = [must_not_have_categories]

    result = {}

    # retrieve all operations and cache the result for later reuse
    if not hasattr(operations, "_all") or operations._all is None:
        operations._all = getmembers(cle, isfunction)

    # filter operations according to given constraints
    for operation_name, operation in operations._all:
        keep_it = True
        if hasattr(operation, "categories") and operation.categories is not None:
            if must_have_categories is not None:
                if not all(
                    item in operation.categories for item in must_have_categories
                ):
                    keep_it = False

            if must_not_have_categories is not None:
                if any(
                    item in operation.categories for item in must_not_have_categories
                ):
                    keep_it = False
        else:
            if must_have_categories is not None:
                keep_it = False
        if keep_it:
            result[operation_name] = operation

    return result


def operation(name: str) -> Callable:
    """Returns a function from the pyclesperanto package

    Parameters
    ----------
    name : str
        name of the operation

    Returns
    -------
        Callable function
    """
    dict = operations()
    return dict[name]


def search_operation_names(name: str) -> list:
    """
    Returns a list of operation names containing the given string

    Parameters
    ----------
    name : str
        string to search for in operation names

    Returns
    -------
    list
        list of operation names containing the given string
    """
    return [a for a in list(operations().keys()) if name in a]
