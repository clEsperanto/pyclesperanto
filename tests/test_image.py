import pytest
import numpy as np

import pyclesperanto as cle

cle.select_device("TX")

dtypes = {
    "int8",
    "int16",
    "int32",
    # 'int64',
    "uint8",
    "uint16",
    "uint32",
    # 'uint64',
    # 'float16',
    "float32",
    # 'float64',
    # 'complex64',
}


@pytest.fixture(params=dtypes)
def dtype(request):
    return np.dtype(request.param)


@pytest.mark.parametrize(
    "shape", [(256, 256), (3, 256, 256), (256, 256, 3), (10, 256, 256)]
)
def test_create_image(dtype, shape):
    array = np.random.randint(0, 255, shape).astype(dtype)
    cle.create(array, mtype="image")
