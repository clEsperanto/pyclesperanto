# pyClEsperanto Import
from ._version import VERSION as __version__
from ._memory_operations import (
    create,
    create_like,
    pull,
    push,
)
from ._image import (
    Image,
    mType,
    dType,
)
from ._device import (
    get_device,
    select_device,
    list_available_devices,
    set_wait_for_kernel_to_finish,
    info,
)
from ._functionalities import (
    imshow,
)
from ._tier1 import (
    add_image_and_scalar,
    add_images_weighted,
    gaussian_blur,
    mean_box,
    maximum_box,
    minimum_box,
    copy,
    greater_or_equal_constant,
    greater_or_equal,
    binary_not,
    binary_and,
    binary_or,
    binary_xor,
    binary_subtract,
    dilate_sphere,
    erode_sphere,
    maximum_z_projection,
    maximum_y_projection,
    maximum_x_projection,
    subtract_image_from_scalar,
    sobel,
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

# Init pyclesperanto (to remove in future)
print("pyclesperanto version:", __version__)

# redefine memory type for easy usage
buffer = mType.buffer
image = mType.image

# redefine data type for easy usage
float = dType.float
int32 = dType.int32
uint32 = dType.uint32
int8 = dType.int8
uint8 = dType.uint8
int16 = dType.int16
uint16 = dType.uint16


__common_alias__ = "cle"
