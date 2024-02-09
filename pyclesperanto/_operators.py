import numpy as np
from typing import Optional, Union

from ._array import Array

from ._utils import _compute_range, _process_ellipsis_into_slice, _trim_index_to_shape
from ._utils import _assert_supported_dtype

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

    from ._tier1 import copy
    from ._memory import create_like

    result = create_like(self, dtype=dtype)
    copy(input_image=self, output_image=result)
    return result


def _max(self, axis: Optional[int] = None, out=None):
    """Return the maximum value in the Array, or along an axis if specified."""
    from ._tier2 import maximum_of_all_pixels
    from ._tier1 import maximum_x_projection
    from ._tier1 import maximum_y_projection
    from ._tier1 import maximum_z_projection

    if axis == 0:
        result = maximum_z_projection(self)
    elif axis == 1:
        result = maximum_y_projection(self)
    elif axis == 2:
        result = maximum_x_projection(self)
    elif axis is None:
        result = maximum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + axis + " not supported")
    if out is not None:
        if isinstance(out, (Array, np.ndarray)):
            np.copyto(out, result.get().astype(out.dtype))
        else:
            out = result
    return result


def _min(self, axis: Optional[int] = None, out=None):
    """Return the minimum value in the Array, or along an axis if specified."""
    from ._tier2 import minimum_of_all_pixels
    from ._tier1 import minimum_x_projection
    from ._tier1 import minimum_y_projection
    from ._tier1 import minimum_z_projection

    if axis == 0:
        result = minimum_z_projection(self)
    elif axis == 1:
        result = minimum_y_projection(self)
    elif axis == 2:
        result = minimum_x_projection(self)
    elif axis is None:
        result = minimum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + axis + " not supported")
    if out is not None:
        if isinstance(out, (Array, np.ndarray)):
            np.copyto(out, result.get().astype(out.dtype))
    return result


def _sum(self, axis: Optional[int] = None, out=None):
    """Return the sum of the Array, or along an axis if specified."""
    from ._tier2 import sum_of_all_pixels
    from ._tier1 import sum_x_projection
    from ._tier1 import sum_y_projection
    from ._tier1 import sum_z_projection

    if axis == 0:
        result = sum_z_projection(self)
    elif axis == 1:
        result = sum_y_projection(self)
    elif axis == 2:
        result = sum_x_projection(self)
    elif axis is None:
        result = sum_of_all_pixels(self)
    else:
        raise ValueError("Axis " + axis + " not supported")
    if out is not None:
        if isinstance(out, (Array, np.ndarray)):
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
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        return add_image_and_scalar(x1, scalar=x2)
    else:
        from ._tier1 import add_images_weighted

        return add_images_weighted(x1, x2, factor0=1, factor1=1)


def __iadd__(x1, x2):
    """Addition of two arrays."""
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        add_image_and_scalar(temp, output_image=x1, scalar=x2)
    else:
        from ._tier1 import add_images_weighted

        add_images_weighted(temp, x2, output_image=x1, factor0=1, factor1=1)
    return x1


def __sub__(x1, x2):
    """Subtraction of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        return add_image_and_scalar(x1, scalar=-x2)
    else:
        from ._tier1 import add_images_weighted

        return add_images_weighted(x1, x2, factor0=1, factor1=-1)


def __div__(x1, x2):
    """Division of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(x1, scalar=1.0 / x2)
    else:
        from ._tier1 import divide_images

        return divide_images(x1, x2)


def __truediv__(x1, x2):
    """Division of two arrays."""
    return x1.__div__(x2)


def __idiv__(x1, x2):
    """Division of two arrays."""
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
    else:
        from ._tier1 import divide_images

        return divide_images(temp, x2, x1)


def __itruediv__(x1, x2):
    """Division of two arrays."""
    return x1.__idiv__(x2)


def __mul__(x1, x2):
    """Multiplication of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(x1, scalar=x2)
    else:
        from ._tier1 import multiply_images

        return multiply_images(x1, x2)


def __imul__(x1, x2):
    """Multiplication of two arrays."""
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(temp, x1, scalar=x2)
    else:
        from ._tier1 import multiply_images

        return multiply_images(temp, x2, x1)


def __gt__(x1, x2):
    """Greater than comparison of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import greater_constant

        return greater_constant(x1, scalar=x2)
    else:
        from ._tier1 import greater

        return greater(x1, x2)


def __ge__(x1, x2):
    """Greater than or equal comparison of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import greater_or_equal_constant

        return greater_or_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import greater_or_equal

        return greater_or_equal(x1, x2)


def __lt__(x1, x2):
    """Less than comparison of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import smaller_constant

        return smaller_constant(x1, scalar=x2)
    else:
        from ._tier1 import smaller

        return smaller(x1, x2)


def __le__(x1, x2):
    """Less than or equal comparison of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import smaller_or_equal_constant

        return smaller_or_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import smaller_or_equal

        return smaller_or_equal(x1, x2)


def __eq__(x1, x2):
    """Equal comparison of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import equal_constant

        return equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import equal

        return equal(x1, x2)


def __ne__(x1, x2):
    """Not equal comparison of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import not_equal_constant

        return not_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import not_equal

        return not_equal(x1, x2)


def __pow__(x1, x2):
    """Power function of two arrays."""
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import power

        return power(x1, scalar=x2)
    else:
        from ._tier1 import power_images

        return power_images(x1, x2)


def __ipow__(x1, x2):
    """Power function of two arrays."""
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import power

        return power(temp, x1, scalar=x2)
    else:
        from ._tier1 import power_images

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


def __getitem__(self, index):
    """Get a pixel value or a region of interest from the Array."""
    if (
        isinstance(index, (tuple, list, np.ndarray))
        and index[0] is not None
        and isinstance(index[0], (tuple, list, np.ndarray))
    ):
        if len(index) == len(self.shape):
            if len(index[0]) > 0:
                # switch xy in 2D / xz in 3D, because clesperanto expects an X-Y-Z array;
                # see also https://github.com/clEsperanto/pyclesperanto_prototype/issues/49
                index = list(index)
                index[0], index[-1] = index[-1], index[0]

                # send positions to GPU
                from ._memory import push

                positions = push(np.asarray(index))

                # read values from positions
                from ._tier1 import read_values_from_positions

                return read_values_from_positions(self, positions)
            else:
                return []

    if not isinstance(index, tuple):
        index = (index,)

    if len(index) > self.ndim:
        raise IndexError(
            f"too many indices for array: array is {self.ndim}-dimensional, but {len(index)} were indexed"
        )

    dst_dim = sum(1 for i in index if not isinstance(i, (int, float)))

    index = _process_ellipsis_into_slice(index, self.shape)
    index = _trim_index_to_shape(index, self.shape)
    slice_list = [[0, x, 1] for x in self.shape]
    for x in range(len(index)):
        if isinstance(index[x], slice):
            slice_list[x] = [index[x].start, index[x].stop, index[x].step]
        elif np.issubdtype(type(index[x]), np.integer):
            slice_list[x] = [
                index[x],
                index[x] + 1 if index[x] >= 0 else index[x] - 1,
                None,
            ]

    # manage range for (x,y,z), with nothing that we deal with a z,y,x order
    _, range_x, range_y, range_z = _compute_range(slice_list, self.shape)
    origin = [range_z[0], range_y[0], range_x[0]]
    region = [
        range_z[1] - range_z[0],
        range_y[1] - range_y[0],
        range_x[1] - range_x[0],
    ]
    region = [abs(x) if x != 0 else 1 for x in region]
    steps = [range_z[2], range_y[2], range_x[2]]

    trimmed_region = [int(abs(x / s)) for x, s in zip(region, steps) if x > 1]
    dst_shape = [1] * dst_dim
    dst_shape[-len(trimmed_region) :] = trimmed_region

    # we are dealing with a single pixel operation
    if np.prod(region) == 1:
        # TODO: return a float or return a buffer of one?
        return self.get(origin, region)

    # a specific step was provided, we are dealing with a range operation
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

    # if result is an Array, and one of the dimension is equal to 1
    if result.shape != tuple(dst_shape):
        from ._tier1 import transpose_xy, transpose_yz
        from ._memory import create

        tmp = create(
            dst_shape,
            dtype=self.dtype,
            mtype=self.mtype,
            device=self.device,
        )

        transpose = [x == 1 for x in region]
        if transpose[2]:  # x is empty
            result = transpose_xy(result)
            transpose_yz(result, tmp)
        elif transpose[1]:  # y is empty
            transpose_yz(result, tmp)
        else:
            result.copy(tmp)

        result = tmp

    return result


def __setitem__(self, index, value):
    """Set a pixel value or a region of interest in the Array."""
    if (
        isinstance(index, (tuple, np.ndarray))
        and index[0] is not None
        and isinstance(index[0], (tuple, list, np.ndarray))
    ):
        if len(index) == len(self.shape):
            if len(index[0]) > 0:
                # switch xy in 2D / xz in 3D, because clesperanto expects an X-Y-Z array;
                # see also https://github.com/clEsperanto/pyclesperanto_prototype/issues/49
                index = list(index)
                index[0], index[-1] = index[-1], index[0]

                # send positions to GPU
                from ._memory import push

                positions = push(np.asarray(index))

                num_positions = positions.shape[-1]
                if isinstance(value, (int, float)):
                    # make an array containing new values for every pixel
                    number = value

                    from ._memory import create

                    value_shape = [1] * len(self.shape)
                    value_shape[-1] = num_positions
                    value = create(value_shape)
                    value.fill(number)

                # overwrite pixels
                from ._tier1 import write_values_to_positions
                from ._tier2 import concatenate_along_y

                values_and_positions = concatenate_along_y(positions, value)
                write_values_to_positions(values_and_positions, self)
            return

    if not isinstance(value, (Array, np.ndarray)):
        value = np.array(value)

    if not isinstance(index, tuple):
        index = (index,)

    dst_dim = sum(1 for i in index if not isinstance(i, (int, float)))

    index = _process_ellipsis_into_slice(index, self.shape)
    index = _trim_index_to_shape(index, self.shape)
    slice_list = [[0, x, 1] for x in self.shape]
    for x in range(len(index)):
        if isinstance(index[x], slice):
            slice_list[x] = [index[x].start, index[x].stop, index[x].step]
        elif np.issubdtype(type(index[x]), np.integer):
            slice_list[x] = [
                index[x],
                index[x] + 1 if index[x] >= 0 else index[x] - 1,
                None,
            ]

    # manage range for (x,y,z), with nothing that we deal with a z,y,x order
    _, range_x, range_y, range_z = _compute_range(slice_list, self.shape)
    origin = [range_z[0], range_y[0], range_x[0]]
    region = [
        range_z[1] - range_z[0],
        range_y[1] - range_y[0],
        range_x[1] - range_x[0],
    ]
    region = [abs(x) if x != 0 else 1 for x in region]
    steps = [range_z[2], range_y[2], range_x[2]]

    trimmed_region = [int(abs(x / s)) for x, s in zip(region, steps) if x > 1]
    dst_shape = [1] * dst_dim
    dst_shape[-len(trimmed_region) :] = trimmed_region

    if value.size == 1:
        if np.prod(region) > 1:
            value = np.repeat(value, np.prod(region))
            value = value.reshape(region)

        self.set(value, origin, region)
        return

    if any([x != 1 for x in steps]):
        # TODO: not sure it work properly
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

    if isinstance(value, Array):
        if self.dtype == value.dtype:
            self.copy(value, origin, (0, 0, 0), region)
        else:
            # otherwise we copy with cast using paste
            from ._tier1 import paste

            paste(
                value,
                self,
                index_x=origin[-1] if len(origin) > 0 else 0,
                index_y=origin[-2] if len(origin) > 1 else 0,
                index_z=origin[-3] if len(origin) > 2 else 0,
            )
    else:
        self.set(value, origin, region)


# adapted from https://github.com/napari/napari/blob/d6bc683b019c4a3a3c6e936526e29bbd59cca2f4/napari/utils/notebook_display.py#L54-L73
def __plt_to_png__(self):
    """PNG representation of the image object for IPython.
    Returns
    -------
    In memory binary stream containing a PNG matplotlib image.
    """
    import matplotlib.pyplot as plt
    from io import BytesIO

    with BytesIO() as file_obj:
        plt.savefig(file_obj, format="png")
        plt.close()  # supress plot output
        file_obj.seek(0)
        png = file_obj.read()
    return png


def __png_to_html__(self, png):
    import base64

    url = "data:image/png;base64," + base64.b64encode(png).decode("utf-8")
    return f'<img src="{url}"></img>'


def __repr_html__(self):
    """HTML representation of the image object for IPython.
    Returns
    -------
    HTML text with the image and some properties.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from ._functionalities import imshow

    size_in_pixels = np.prod(self.size)
    size_in_bytes = size_in_pixels * self.dtype.itemsize

    labels = self.dtype == np.uint32

    # In case the image is 2D, 3D and larger than 100 pixels, turn on fancy view
    if len(self.shape) in (2, 3) and size_in_pixels >= 100:
        imshow(self, labels=labels, continue_drawing=True, colorbar=not labels)
        image = self._png_to_html(self._plt_to_png())
    else:
        return "<pre>" + repr(self) + "</pre>"

    units = ["B", "kB", "MB", "GB", "TB", "PB"]
    unit_index = 0
    while size_in_bytes > 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024
        unit_index += 1
    size = "{:.1f}".format(size_in_bytes) + " " + units[unit_index]

    histogram = ""
    if size_in_bytes < 100 * 1024 * 1024:
        if not labels:
            from ._tier3 import histogram

            num_bins = 32
            h = np.asarray(
                histogram(self, nbins=num_bins, min=self.min(), max=self.max())
            )
            plt.figure(figsize=(1.8, 1.2))
            plt.bar(range(0, len(h)), h)
            # hide axis text
            # https://stackoverflow.com/questions/2176424/hiding-axis-text-in-matplotlib-plots
            # https://pythonguides.com/matplotlib-remove-tick-labels
            frame1 = plt.gca()
            frame1.axes.xaxis.set_ticklabels([])
            frame1.axes.yaxis.set_ticklabels([])
            plt.tick_params(left=False, bottom=False)
            histogram = self._png_to_html(self._plt_to_png())
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
        '<b><a href="https://github.com/clEsperanto/pyclesperanto_prototype" target="_blank">cle._</a> image</b><br/>',
        "<table>",
        "<tr><td>shape</td><td>"
        + str(self.shape).replace(" ", "&nbsp;")
        + "</td></tr>",
        "<tr><td>dtype</td><td>" + str(self.dtype) + "</td></tr>",
        "<tr><td>size</td><td>" + size + "</td></tr>",
        min_max,
        "</table>",
        histogram,
        "</td>",
        "</tr>",
        "</table>",
    ]
    return "\n".join(all)
