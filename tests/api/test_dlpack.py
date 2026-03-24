# test_dlpack_cupy.py
import numpy as np
import pytest

cupy = pytest.importorskip("cupy", reason="cupy not installed")

import pyclesperanto as cle

pytestmark = pytest.mark.backend("cuda")


@pytest.fixture
def device(request):
    return cle.select_device(request.param)


@pytest.mark.parametrize(
    "dtype", [np.float32, np.int8, np.int16, np.int32, np.uint8, np.uint16, np.uint32]
)
def test_cle_to_cupy_dtypes(device, dtype):
    data = np.ones((4, 4), dtype=dtype)
    arr = cle.Array.from_array(data, device=device)
    cp_arr = cupy.from_dlpack(arr)
    assert cp_arr.dtype == dtype
    np.testing.assert_array_equal(cupy.asnumpy(cp_arr), data)


def test_cle_to_cupy(device):
    data = np.arange(24, dtype=np.float32).reshape(4, 6)
    arr = cle.Array.from_array(data, device=device)
    cp_arr = cupy.from_dlpack(arr)
    assert cp_arr.shape == data.shape
    assert cp_arr.dtype == np.float32
    np.testing.assert_array_equal(cupy.asnumpy(cp_arr), data)


def test_cupy_to_cle(device):
    data = np.arange(24, dtype=np.float32).reshape(4, 6)
    cp_arr = cupy.asarray(data)
    arr = cle.Array.from_dlpack(cp_arr)
    assert arr.shape == data.shape
    assert arr.dtype == np.float32
    np.testing.assert_array_equal(arr.get(), data)


def test_round_trip(device):
    data = np.random.rand(8, 8).astype(np.float32)
    arr = cle.Array.from_array(data, device=device)
    cp_arr = cupy.from_dlpack(arr)
    arr2 = cle.Array.from_dlpack(cp_arr)
    np.testing.assert_array_almost_equal(arr2.get(), data)


def test_3d_array(device):
    data = np.arange(60, dtype=np.float32).reshape(3, 4, 5)
    arr = cle.Array.from_array(data, device=device)
    cp_arr = cupy.from_dlpack(arr)
    assert cp_arr.shape == (3, 4, 5)
    np.testing.assert_array_equal(cupy.asnumpy(cp_arr), data)


def test_no_copy_same_memory(device):
    """Exported CuPy array shares GPU memory — in-place modification reflects in cle."""
    data = np.zeros((4, 4), dtype=np.float32)
    arr = cle.Array.from_array(data, device=device)
    cp_arr = cupy.from_dlpack(arr)
    cp_arr[:] = 42.0
    np.testing.assert_array_equal(arr.get(), np.full((4, 4), 42.0))


def test_image_mtype_raises(device):
    if not device.supportImage():
        pytest.skip("device does not support image memory")
    arr = cle.Array.empty((4, 4), dtype=np.float32, mtype="image", device=device)
    with pytest.raises(RuntimeError):
        arr.__dlpack__()


def test_dlpack_device_type(device):
    arr = cle.Array.empty((4, 4), dtype=np.float32, device=device)
    device_type, device_index = arr.__dlpack_device__()
    assert device_type == 2  # kDLCUDA
    assert isinstance(device_index, int)
