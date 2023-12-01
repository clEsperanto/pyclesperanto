import numpy as np
from typing import Optional, Union

from ._array import Array

from ._utils import _compute_range, _clean_index
from ._utils import assert_supported_dtype

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


def astype(self, dtype: type):
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


def max(self, axis: Optional[int] = None, out=None):
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
        if isinstance(out, Union[Array, np.ndarray]):
            np.copyto(out, result.get().astype(out.dtype))
        else:
            out = result
    return result


def min(self, axis: Optional[int] = None, out=None):
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
        if isinstance(out, Union[Array, np.ndarray]):
            np.copyto(out, result.get().astype(out.dtype))
    return result


def sum(self, axis: Optional[int] = None, out=None):
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
        if isinstance(out, Union[Array, np.ndarray]):
            np.copyto(out, result.get().astype(out.dtype))
    return result


def __iadd__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        return add_image_and_scalar(temp, x1, scalar=x2)
    else:
        from ._tier1 import add_images_weighted

        return add_images_weighted(temp, x2, x1, factor0=1, factor1=1)


def __sub__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import add_image_and_scalar

        return add_image_and_scalar(x1, scalar=-x2)
    else:
        from ._tier1 import add_images_weighted

        return add_images_weighted(x1, x2, factor0=1, factor1=-1)


def __div__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(x1, scalar=1.0 / x2)
    else:
        from ._tier1 import divide_images

        return divide_images(x1, x2)


def __truediv__(x1, x2):
    return x1.__div__(x2)


def __idiv__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(temp, x1, scalar=1.0 / x2)
    else:
        from ._tier1 import divide_images

        return divide_images(temp, x2, x1)


def __itruediv__(x1, x2):
    return x1.__idiv__(x2)


def __mul__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(x1, scalar=x2)
    else:
        from ._tier1 import multiply_images

        return multiply_images(x1, x2)


def __imul__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import multiply_image_and_scalar

        return multiply_image_and_scalar(temp, x1, scalar=x2)
    else:
        from ._tier1 import multiply_images

        return multiply_images(temp, x2, x1)


def __gt__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import greater_constant

        return greater_constant(x1, scalar=x2)
    else:
        from ._tier1 import greater

        return greater(x1, x2)


def __ge__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import greater_or_equal_constant

        return greater_or_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import greater_or_equal

        return greater_or_equal(x1, x2)


def __lt__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import smaller_constant

        return smaller_constant(x1, scalar=x2)
    else:
        from ._tier1 import smaller

        return smaller(x1, x2)


def __le__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import smaller_or_equal_constant

        return smaller_or_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import smaller_or_equal

        return smaller_or_equal(x1, x2)


def __eq__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import equal_constant

        return equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import equal

        return equal(x1, x2)


def __ne__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import not_equal_constant

        return not_equal_constant(x1, scalar=x2)
    else:
        from ._tier1 import not_equal

        return not_equal(x1, x2)


def __pow__(x1, x2):
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import power

        return power(x1, exponent=x2)
    else:
        from ._tier1 import power_images

        return power_images(x1, x2)


def __ipow__(x1, x2):
    from ._tier1 import copy

    temp = copy(x1)
    if isinstance(x2, _supported_numeric_types):
        from ._tier1 import power

        return power(temp, x1, exponent=x2)
    else:
        from ._tier1 import power_images

        return power_images(temp, x2, x1)


def __iter__(self):
    class MyIterator:
        def __init__(self, image):
            self.image = image
            self._iter_index = 0

        def __next__(self):
            import numpy as np
            from ._memory import create
            from ._tier1 import copy_slice

            if not hasattr(self, "_iter_index"):
                self._iter_index = 0
            if self._iter_index < self.image.shape[0]:
                result = self.image.shape[self._iter_index]
                self._iter_index = self._iter_index + 1
                return result
            else:
                raise StopIteration

    return MyIterator(self)


def __getitem__(self, key):
    result = None
    key = _clean_index(key)
    index = [[0, x, 1] for x in self.shape]
    for x in range(len(key)):
        if isinstance(key[x], slice):
            index[x] = [key[x].start, key[x].stop, key[x].step]
        elif np.issubdtype(type(key[x]), np.integer):
            index[x] = [key[x], key[x] + 1 if key[x] > 0 else key[x] - 1, None]
    key = index
    # manage range for (x,y,z), with nothing that we deal with a z,y,x order
    use_range, range_x, range_y, range_z = _compute_range(key, self.shape)
    origin = [range_z[0], range_y[0], range_x[0]]
    region = [
        range_z[1] - range_z[0],
        range_y[1] - range_y[0],
        range_x[1] - range_x[0],
    ]
    region = [abs(x) for x in region]
    # we are dealing with a single pixel operation
    if np.prod(region) == 1:
        result = self.get(origin, region)
    # a specific step was provided, we are dealing with a range operation
    if use_range and result is None:
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
    else:  # we are dealing with a sub-region operation
        from ._memory import create

        try:
            # we copy sub-region inside a new buffer to return
            result = create(
                region, dtype=self.dtype, mtype=self.mtype, device=self.device
            )
            self.copy(result, origin, [0] * len(region), region)
        except Exception:
            # if we fail to copy, we rely on numpy to do the job
            result = self.set(self.get().__getitem__(key))
    # if result is an Array, and one of the dimension is equal to 1
    if isinstance(result, Array) and any([x == 1 for x in result.shape]):
        from ._tier1 import transpose_xy, transpose_yz

        transpose = [x == 1 for x in region]
        if transpose[2]:  # x is empty
            result = transpose_xy(result)
            result = transpose_yz(result)
        if transpose[1]:  # y is empty
            result = transpose_yz(result)

    return result


def __setitem__(self, key, value):
    if not isinstance(value, (Array, np.ndarray)):
        value = np.array(value)
    key = _clean_index(key)
    # check if the dtype of the value is a numeric type such as float, int etc
    assert_supported_dtype(value.dtype)
    # define default index as slices(0, shape, 1), and iterate over keys and replace when relevant
    index = [[0, x, 1] for x in self.shape]
    for x in range(len(key)):
        if isinstance(key[x], slice):
            index[x] = [key[x].start, key[x].stop, key[x].step]
        elif np.issubdtype(type(key[x]), np.integer):
            index[x] = [key[x], key[x] + 1 if key[x] > 0 else key[x] - 1, None]
    key = index

    # manage range for (x,y,z), with nothing that we deal with a z,y,x order
    use_range, range_x, range_y, range_z = _compute_range(key, self.shape)
    origin = [range_z[0], range_y[0], range_x[0]]
    region = [
        range_z[1] - range_z[0],
        range_y[1] - range_y[0],
        range_x[1] - range_x[0],
    ]
    region = [abs(x) for x in region]

    stride_region = [
        abs(region[0] / range_z[2]),
        abs(region[1] / range_y[2]),
        abs(region[2] / range_x[2]),
    ]

    if value.size == 1:
        value = np.repeat(value, np.prod(region))
        value = value.reshape(region)
        self.set(value, origin, region)
        return
    if value.size != np.prod(stride_region):
        raise IndexError(
            f"Input value mismatch the indexed region: {value.size} != {np.prod(stride_region)} ({value.shape} != {region})"
        )
    if use_range:
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
    else:
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
def _plt_to_png(self):
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


def _png_to_html(self, png):
    import base64

    url = "data:image/png;base64," + base64.b64encode(png).decode("utf-8")
    return f'<img src="{url}"></img>'


def _repr_html_(self):
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
