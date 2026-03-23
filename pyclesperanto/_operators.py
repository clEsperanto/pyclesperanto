from typing import Optional, Union

import numpy as np

from ._utils import (
    _assert_supported_dtype,
    _compute_range,
    _process_ellipsis_into_slice,
    _trim_index_to_shape,
)


def _get_array_class():
    """Late import to avoid circular dependency with _array.py."""
    from ._backend import _get_backend

    return _get_backend()._Array


cl_buffer_datatype_dict = {
    bool: "bool",
    np.uint8: "uchar",
    np.uint16: "ushort",
    np.uint32: "uint",
    np.uint64: "ulong",
    np.int8: "char",
    np.int16: "short",
    np.int32: "int",
    np.int64: "long",
    np.float32: "float",
    np.complex64: "cfloat_t",
    int: "int",
    float: "float",
    np.float64: "float",
}

_INTEGER_TYPES = (
    int,
    np.intp,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
)

_supported_numeric_types = tuple(cl_buffer_datatype_dict.keys())


def _astype(self, dtype: type):
    """Convert the Array to a different data type."""
    if dtype not in _supported_numeric_types:
        raise ValueError(
            "dtype "
            + str(dtype)
            + " not supported. Use one of "
            + str(_supported_numeric_types)
        )
    if dtype == self.dtype:
        return self

    from ._memory import create_like
    from ._tier1 import copy

    result = create_like(self, dtype=dtype)
    copy(input_image=self, output_image=result)
    return result


def _max(self, axis: Optional[int] = None, out=None):
    """Return the maximum value in the Array, or along an axis if specified."""
    from ._tier1 import maximum_x_projection, maximum_y_projection, maximum_z_projection
    from ._tier2 import maximum_of_all_pixels

    if axis == 0:
        result = maximum_z_projection(self)
    elif axis == 1:
        result = maximum_y_projection(self)
    elif axis == 2:
        result = maximum_x_projection(self)
    elif axis is None:
        result = maximum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + str(axis) + " not supported")
    if out is not None:
        if isinstance(out, (_get_array_class(), np.ndarray)):
            np.copyto(out, result.get().astype(out.dtype))
        else:
            out = result
    return result


def _min(self, axis: Optional[int] = None, out=None):
    """Return the minimum value in the Array, or along an axis if specified."""
    from ._tier1 import minimum_x_projection, minimum_y_projection, minimum_z_projection
    from ._tier2 import minimum_of_all_pixels

    if axis == 0:
        result = minimum_z_projection(self)
    elif axis == 1:
        result = minimum_y_projection(self)
    elif axis == 2:
        result = minimum_x_projection(self)
    elif axis is None:
        result = minimum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + str(axis) + " not supported")
    if out is not None:
        if isinstance(out, (_get_array_class(), np.ndarray)):
            np.copyto(out, result.get().astype(out.dtype))
    return result


def _sum(self, axis: Optional[int] = None, out=None):
    """Return the sum of the Array, or along an axis if specified."""
    from ._tier1 import sum_x_projection, sum_y_projection, sum_z_projection
    from ._tier2 import sum_of_all_pixels

    if axis == 0:
        result = sum_z_projection(self)
    elif axis == 1:
        result = sum_y_projection(self)
    elif axis == 2:
        result = sum_x_projection(self)
    elif axis is None:
        result = sum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + str(axis) + " not supported")
    if out is not None:
        if isinstance(out, (_get_array_class(), np.ndarray)):
            np.copyto(out, result.get().astype(out.dtype))
    return result


def _std(self, axis: Optional[int] = None, out=None):
    """Return the std of the Array, or along an axis if specified."""
    from ._tier1 import std_x_projection, std_y_projection, std_z_projection
    from ._tier4 import standard_deviation_of_all_pixels

    if axis == 0:
        result = std_z_projection(self)
    elif axis == 1:
        result = std_y_projection(self)
    elif axis == 2:
        result = std_x_projection(self)
    elif axis is None:
        result = standard_deviation_of_all_pixels(self)
    else:
        raise ValueError("Axis " + str(axis) + " not supported")
    if out is not None:
        if isinstance(out, (_get_array_class(), np.ndarray)):
            np.copyto(out, result.get().astype(out.dtype))
    return result


def __pos__(x1):
    """Unary plus, propagates the sign of the argument."""
    return x1.__mul__(1)


def __neg__(x1):
    """Unary minus, returns an array with the negative of the elements of the argument."""
    return x1.__mul__(-1)


def __add__(x1, x2):
    """Addition of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted

    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(x1, scalar=x2)
    return add_images_weighted(x1, x2, factor1=1, factor2=1)


def __iadd__(x1, x2):
    """Addition of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted, copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(temp, output_image=x1, scalar=x2)
    return add_images_weighted(temp, x2, output_image=x1, factor1=1, factor2=1)


def __sub__(x1, x2):
    """Subtraction of two arrays."""
    from ._tier1 import add_image_and_scalar, add_images_weighted

    if isinstance(x2, _supported_numeric_types):
        return add_image_and_scalar(x1, scalar=-x2)
    return add_images_weighted(x1, x2, factor1=1, factor2=-1)


def __div__(x1, x2):
    """Division of two arrays."""
    from ._tier1 import divide_images, multiply_image_and_scalar

    if isinstance(x2, _supported_numeric_types):
        return multiply_image_and_scalar(x1, scalar=1.0 / x2)
    return divide_images(x1, x2)


def __truediv__(x1, x2):
    """Division of two arrays."""
    return x1.__div__(x2)


def __idiv__(x1, x2):
    """Division of two arrays."""
    from ._tier1 import copy, divide_images, multiply_image_and_scalar

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
    return divide_images(temp, x2, x1)


def __itruediv__(x1, x2):
    """Division of two arrays."""
    return x1.__idiv__(x2)


def __mul__(x1, x2):
    """Multiplication of two arrays."""
    from ._tier1 import multiply_image_and_scalar, multiply_images

    if isinstance(x2, _supported_numeric_types):
        return multiply_image_and_scalar(x1, scalar=x2)
    return multiply_images(x1, x2)


def __imul__(x1, x2):
    """Multiplication of two arrays."""
    from ._tier1 import copy, multiply_image_and_scalar, multiply_images

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        return multiply_image_and_scalar(temp, x1, scalar=x2)
    return multiply_images(temp, x2, x1)


def __gt__(x1, x2):
    """Greater than comparison of two arrays."""
    from ._tier1 import greater, greater_constant

    if isinstance(x2, _supported_numeric_types):
        return greater_constant(x1, scalar=x2)
    return greater(x1, x2)


def __ge__(x1, x2):
    """Greater than or equal comparison of two arrays."""
    from ._tier1 import greater_or_equal, greater_or_equal_constant

    if isinstance(x2, _supported_numeric_types):
        return greater_or_equal_constant(x1, scalar=x2)
    return greater_or_equal(x1, x2)


def __lt__(x1, x2):
    """Less than comparison of two arrays."""
    from ._tier1 import smaller, smaller_constant

    if isinstance(x2, _supported_numeric_types):
        return smaller_constant(x1, scalar=x2)
    return smaller(x1, x2)


def __le__(x1, x2):
    """Less than or equal comparison of two arrays."""
    from ._tier1 import smaller_or_equal, smaller_or_equal_constant

    if isinstance(x2, _supported_numeric_types):
        return smaller_or_equal_constant(x1, scalar=x2)
    return smaller_or_equal(x1, x2)


def __eq__(x1, x2):
    """Equal comparison of two arrays."""
    from ._tier1 import equal, equal_constant

    if isinstance(x2, _supported_numeric_types):
        return equal_constant(x1, scalar=x2)
    return equal(x1, x2)


def __ne__(x1, x2):
    """Not equal comparison of two arrays."""
    from ._tier1 import not_equal, not_equal_constant

    if isinstance(x2, _supported_numeric_types):
        return not_equal_constant(x1, scalar=x2)
    return not_equal(x1, x2)


def __pow__(x1, x2):
    """Power function of two arrays."""
    from ._tier1 import power, power_images

    if isinstance(x2, _supported_numeric_types):
        return power(x1, scalar=x2)
    return power_images(x1, x2)


def __ipow__(x1, x2):
    """Power function of two arrays."""
    from ._tier1 import copy, power, power_images

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        return power(temp, x1, scalar=x2)
    return power_images(temp, x2, x1)


def __iter__(self):
    """Iterate over the first dimension of the array."""

    class MyIterator:
        def __init__(self, image):
            self.image = image
            self._iter_index = 0

        def __next__(self):
            if not hasattr(self, "_iter_index"):
                self._iter_index = 0
            if self._iter_index < self.image.shape[0]:
                result = self.image[self._iter_index]
                self._iter_index = self._iter_index + 1
                return result
            else:
                raise StopIteration

    return MyIterator(self)


# adapted from https://github.com/napari/napari/blob/d6bc683b019c4a3a3c6e936526e29bbd59cca2f4/napari/utils/notebook_display.py#L54-L73
def _figure_to_png(fig):
    """Standalone helper — convert a Figure to PNG bytes."""
    from io import BytesIO

    with BytesIO() as file_obj:
        fig.savefig(file_obj, format="png")
        file_obj.seek(0)
        return file_obj.read()


def _png_to_html(png):
    """Standalone helper — convert PNG bytes to an HTML img tag."""
    import base64

    url = "data:image/png;base64," + base64.b64encode(png).decode("utf-8")
    return f'<img src="{url}"></img>'


def __repr_html__(self):
    """HTML representation of the image object for IPython."""
    import matplotlib.pyplot as plt
    import numpy as np

    from ._functionalities import imshow

    size_in_pixels = np.prod(self.size)
    size_in_bytes = size_in_pixels * self.dtype.itemsize
    labels = self.dtype == np.uint32

    if len(self.shape) in (2, 3) and size_in_pixels >= 100:
        with plt.ioff():
            imshow(self, labels=labels, continue_drawing=True, colorbar=not labels)
            fig = plt.gcf()
            image = _png_to_html(_figure_to_png(fig))
            plt.close(fig)
    else:
        return "<pre>" + repr(self) + "</pre>"

    raw_size_in_bytes = size_in_bytes
    units = ["B", "kB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    while size_in_bytes > 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024
        unit_index += 1
    size = "{:.1f}".format(size_in_bytes) + " " + units[unit_index]

    histogram_html = ""
    if raw_size_in_bytes < 100 * 1024 * 1024:
        if not labels:

            from ._tier3 import histogram

            num_bins = 32
            h = np.asarray(
                histogram(
                    input_image=self,
                    num_bins=num_bins,
                    minimum_intensity=self.min(),
                    maximum_intensity=self.max(),
                )
            )
            with plt.ioff():
                plt.figure(figsize=(1.8, 1.2))
                plt.bar(range(0, len(h)), h)
                frame1 = plt.gca()
                frame1.axes.xaxis.set_ticklabels([])
                frame1.axes.yaxis.set_ticklabels([])
                plt.tick_params(left=False, bottom=False)
                hist_fig = plt.gcf()
                histogram_html = _png_to_html(_figure_to_png(hist_fig))
                plt.close(hist_fig)

        min_max = (
            "<tr><td>min</td><td>"
            + str(self.min())
            + "</td></tr>"
            + "<tr><td>max</td><td>"
            + str(self.max())
            + "</td></tr>"
        )
    else:
        min_max = ""

    all = [
        "<table>",
        "<tr>",
        "<td>",
        image,
        "</td>",
        '<td style="text-align: center; vertical-align: top;">',
        '<b><a href="https://github.com/clEsperanto/pyclesperanto" target="_blank">cle._</a> image</b><br/>',
        "<table>",
        "<tr><td>shape</td><td>"
        + str(self.shape).replace(" ", "&nbsp;")
        + "</td></tr>",
        "<tr><td>dtype</td><td>" + str(self.dtype) + "</td></tr>",
        "<tr><td>size</td><td>" + size + "</td></tr>",
        min_max,
        "</table>",
        histogram_html,
        "</td>",
        "</tr>",
        "</table>",
    ]
    return "\n".join(all)


def _is_fancy_index(index, ndim):
    """Return True if *index* is a sequence of coordinate arrays (fancy indexing)."""
    if not isinstance(index, (tuple, list, np.ndarray)):
        return False
    if len(index) != ndim:
        return False
    first = index[0]
    return first is not None and isinstance(first, (tuple, list, np.ndarray))


def _parse_index(index, shape):
    ndim = len(shape)

    if not isinstance(index, tuple):
        index = (index,)

    if len(index) > ndim:
        raise IndexError(
            f"too many indices for array: array is {ndim}-dimensional, "
            f"but {len(index)} were indexed"
        )

    # Expand ellipsis BEFORE determining which axes are scalar-indexed
    index = _process_ellipsis_into_slice(index, shape)
    index = _trim_index_to_shape(index, shape)

    squeeze_axes = [
        i for i, idx in enumerate(index) if isinstance(idx, (int, float, np.integer))
    ]

    slice_list = [[0, s, 1] for s in shape]
    for i in range(len(index)):
        idx = index[i]
        if isinstance(idx, slice):
            slice_list[i] = [idx.start, idx.stop, idx.step]
        elif isinstance(idx, _INTEGER_TYPES):
            slice_list[i] = [
                idx,
                idx + 1 if idx >= 0 else idx - 1,
                None,
            ]

    _, range_x, range_y, range_z = _compute_range(slice_list, shape)

    origin = [range_z[0], range_y[0], range_x[0]]
    region = [
        abs(range_z[1] - range_z[0]) or 1,
        abs(range_y[1] - range_y[0]) or 1,
        abs(range_x[1] - range_x[0]) or 1,
    ]
    steps = [range_z[2], range_y[2], range_x[2]]

    return origin, region, steps, squeeze_axes, range_x, range_y, range_z


def _compute_dst_shape(region, steps, squeeze_axes, ndim):
    """Compute the output shape after slicing, honouring squeezed (scalar-indexed) axes."""
    # Full 3-D stepped shape
    full = [int(abs(r / s)) for r, s in zip(region, steps)]
    # Map back to the original ndim (region is always 3-D internally)
    offset = 3 - ndim
    out = full[offset:]
    # Drop axes that were scalar-indexed
    return [s for i, s in enumerate(out) if i not in squeeze_axes]


def _reshape_result(result, dst_shape, region):
    if result.shape == tuple(dst_shape):
        return result

    ndim = len(dst_shape)

    # Pad to 3D for the C++ reshape call
    while len(dst_shape) < 3:
        dst_shape.insert(0, 1)

    return result.reshape(
        width=int(dst_shape[-1]),
        height=int(dst_shape[-2]),
        depth=int(dst_shape[-3]),
        dimension=ndim,
    )


# ---------------------------------------------------------------------------
# Fancy-index helpers
# ---------------------------------------------------------------------------


def _swap_first_last(index):
    """Swap first and last coordinate arrays (X↔Z / X↔Y) for clesperanto's X-Y-Z order."""
    index = list(index)
    index[0], index[-1] = index[-1], index[0]
    return index


def _fancy_getitem(self, index):
    if len(index[0]) == 0:
        return []

    from ._memory import push
    from ._tier1 import read_values_from_positions

    positions = push(np.asarray(_swap_first_last(index)))
    return read_values_from_positions(self, positions)


def _fancy_setitem(self, index, value):
    if len(index[0]) == 0:
        return

    from ._memory import create, push
    from ._tier1 import write_values_to_positions
    from ._tier2 import concatenate_along_y

    positions = push(np.asarray(_swap_first_last(index)))
    num_positions = positions.shape[-1]

    if isinstance(value, (int, float)):
        scalar = value  # save before reassigning
        value_shape = [1] * len(self.shape)
        value_shape[-1] = num_positions
        value = create(value_shape)
        value.fill(scalar)

    values_and_positions = concatenate_along_y(positions, value)
    write_values_to_positions(values_and_positions, self)


# ---------------------------------------------------------------------------
# Public operators
# ---------------------------------------------------------------------------


def __getitem__(self, index):
    """Get a pixel value or a region of interest from the Array."""
    if _is_fancy_index(index, len(self.shape)):
        return _fancy_getitem(self, index)

    # Fast path: all-integer index → single pixel, skip all parsing
    if not isinstance(index, tuple):
        index = (index,)
    if len(index) == self.ndim and all(isinstance(i, (int, np.integer)) for i in index):
        # Reverse to x,y,z order for the C++ side
        origin = [0, 0, 0]
        offset = 3 - self.ndim
        for i, idx in enumerate(index):
            origin[offset + i] = int(idx) if idx >= 0 else self.shape[i] + int(idx)
        return self.get(origin, [1, 1, 1])

    origin, region, steps, squeeze_axes, range_x, range_y, range_z = _parse_index(
        index, self.shape
    )

    total = region[0] * region[1] * region[2]
    if total == 1:
        return self.get(origin, region)

    from ._tier1 import range as gpu_range

    result = gpu_range(
        self,
        start_x=range_x[0],
        stop_x=range_x[1],
        step_x=range_x[2],
        start_y=range_y[0],
        stop_y=range_y[1],
        step_y=range_y[2],
        start_z=range_z[0],
        stop_z=range_z[1],
        step_z=range_z[2],
    )

    dst_shape = _compute_dst_shape(region, steps, squeeze_axes, self.ndim)
    return _reshape_result(result, dst_shape, region)


def __setitem__(self, index, value):
    """Set a pixel value or a region of interest in the Array."""
    if _is_fancy_index(index, len(self.shape)):
        _fancy_setitem(self, index, value)
        return

    if not isinstance(value, (_get_array_class(), np.ndarray)):
        value = np.asarray(value)

    origin, region, steps, squeeze_axes, range_x, range_y, range_z = _parse_index(
        index, self.shape
    )
    total = region[0] * region[1] * region[2]

    if value.size == 1:
        if total > 1:
            value = np.broadcast_to(np.asarray(value).ravel(), total)
            value = value.reshape(region)
        self.set(value, origin, region)
        return

    if any(s != 1 for s in steps):
        from ._tier1 import range as gpu_range

        gpu_range(
            value,
            self,
            start_x=range_x[0],
            stop_x=range_x[1],
            step_x=range_x[2],
            start_y=range_y[0],
            stop_y=range_y[1],
            step_y=range_y[2],
            start_z=range_z[0],
            stop_z=range_z[1],
            step_z=range_z[2],
        )
        return

    if isinstance(value, _get_array_class()):
        if self.dtype == value.dtype:
            self.copy(value, origin, (0, 0, 0), region)
        else:
            from ._tier1 import paste

            paste(
                value,
                self,
                index_x=origin[2],
                index_y=origin[1],
                index_z=origin[0],
            )
    else:
        self.set(value, origin, region)
