# pyClEsperanto Import
from ._version import VERSION as __version__
from ._version import CLIC_VERSION as __clic_version__

from ._memory_operations import (
    create,
    create_like,
    pull,
    push,
)
from ._types import (
    MemoryType,
    DataType,
)
from ._image import (
    Image,
)
from ._device import (
    Device,
    get_device,
    select_device,
    new_device,
    list_available_devices,
    set_wait_for_kernel_to_finish,
    info,
)
from ._functionalities import (
    imshow,
    execute,
)
from ._tier1 import (
    add_image_and_scalar,
    add_images_weighted,
    gaussian_blur,
    mean_box,
    maximum_box,
    minimum_box,
    copy,
    divide_images,
    gradient_x,
    gradient_z,
    gradient_y,
    greater,
    greater_or_equal_constant,
    greater_constant,
    greater_or_equal,
    binary_not,
    binary_and,
    binary_or,
    binary_xor,
    binary_subtract,
    dilate_sphere,
    equal_constant,
    equal,
    erode_sphere,
    maximum_z_projection,
    maximum_y_projection,
    maximum_x_projection,
    subtract_image_from_scalar,
    sobel,
    minimum_z_projection,
    minimum_y_projection,
    minimum_x_projection,
    multiply_images,
    multiply_image_and_scalar,
    not_equal_constant,
    not_equal,
    power,
    power_images,
    smaller_constant,
    smaller,
    smaller_or_equal_constant,
    smaller_or_equal,
    sum_z_projection,
    sum_y_projection,
    sum_x_projection,
)
from ._tier2 import (
    difference_of_gaussian,
    detect_maxima_box,
    maximum_of_all_pixels,
    minimum_of_all_pixels,
    sum_of_all_pixels,
    extend_labeling_via_voronoi,
    top_hat_box,
)
from ._tier3 import (
    histogram,
)
from ._tier4 import (
    connected_components_labeling_box,
    threshold_otsu,
)
from ._tier5 import (
    masked_voronoi_labeling,
)
from ._tier6 import (
    voronoi_otsu_labeling,
)

# Generic Import
import os

# Supports for ocl-icd find shipped OpenCL ICDs, cf.
os.environ["PYCLESPERANTO_HOME"] = os.path.dirname(os.path.abspath(__file__))

# redefine memory type for easy usage
buffer = MemoryType.buffer
image = MemoryType.image

__common_alias__ = "cle"
