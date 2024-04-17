from typing import Optional, Union
import numpy as np
import warnings

from ._pyclesperanto import _Device as Device
from ._pyclesperanto import _BackendManager as BackendManager


class _current_device:
    _instance: Optional[Device] = None


def get_device() -> Device:
    """Return the current device instance

    Returns
    -------
    device : Device
    """
    return _current_device._instance or select_device()


def select_device(device_id: Union[str, int] = "", device_type: str = "all") -> Device:
    """Select a device by 'name' or 'index' and by 'type', and store it as the current device

    If selecting the device by string, the function compares the device name and substring.
    (e.g. "NVIDIA", "RTX", "Iris", etc. will match the device name "NVIDIA RTX 2080" or "Intel Iris Pro")
    If selecting the device by index, the function will select the device at the given index in the list
    of available devices. (e.g. 0, 1, 2, etc. will select the first, second, third, etc. device in the list)
    If device_id is an empty string, the function will select the first available device.
    The device_type enables selecting the type of device to be selected (e.g. "all", "cpu", "gpu")
    To retrieve a list of available devices, use `list_available_devices()`

    Parameters
    ----------
    device_id : Union[str, int], default = ""
        Substring of device name or device index.
    device_type : str, default = "all"
        Type of device to be selected (e.g. "all", "cpu", "gpu")

    Returns
    -------
    device : Device
    """
    if isinstance(device_id, str):
        device = BackendManager.get_backend().getDeviceFromName(device_id, device_type)
    elif isinstance(device_id, int):
        device = BackendManager.get_backend().getDeviceFromIndex(device_id, device_type)
    else:
        raise ValueError(
            f"'{device_id}' is not a supported device_id. Please use either a string or an integer."
        )
    if _current_device._instance and device == _current_device._instance:
        return _current_device._instance
    _current_device._instance = device
    return device


def list_available_devices(device_type: str = "all") -> list:
    """Retrieve a list of names of available devices

    Will search the system for backend compatible device available and return a list of their names.
    This will NOT set the device!
    Use 'select_device' to select devices.
    Use 'get_device' to retrieve the current device.

    Parameters
    ----------
    device_type : str, default = "all"
        Type of device to be selected (e.g. "all", "cpu", "gpu")

    Returns
    -------
    name list : list[str]
    """
    dev_list = list(BackendManager.get_backend().getDevicesList(type=device_type))
    if not dev_list:
        warnings.warn(
            "No device available. Please install either OpenCL or CUDA on your system.",
            RuntimeWarning,
        )
    return dev_list


def list_available_backends() -> list:
    """Retrieve a list of names of available backends

    Will test system for available backends installed and return a list of their names.

    Returns
    -------
    name list : list[str]
    """
    back_list = list(BackendManager.get_backends_list())
    if not back_list:
        warnings.warn(
            "No backend available. Please install either OpenCL or CUDA on your system.",
            RuntimeWarning,
        )
    return back_list


def select_backend(backend: str = "opencl") -> str:
    """select backend

    Select the backend used by pyclesperanto, OpenCL or CUDA.
    Default is OpenCL.

    Parameters
    ----------
    type : str, default = "opencl"
        determine the backend to use between opencl and cuda
    """

    # enforce lowercase for backend_type
    backend = backend.lower()
    # is backend_type is different than "cuda" or "opencl", raise an error
    if backend not in ["cuda", "opencl"]:
        raise ValueError(
            f"'{backend}' is not a supported Backend. Please use either 'opencl' or 'cuda'."
        )
    BackendManager.set_backend(backend=backend)
    # reset current device to default one
    select_device()
    return f"{BackendManager.get_backend()} selected."


def wait_for_kernel_to_finish(flag: bool = True, device: Device = None):
    """Wait for kernel to finish

    Enforce the system to wait for the kernel to finish before continuing. Introducing a
    slowdown in the workflow. This is useful for debugging purposes, benchmarking and
    profiling, as well as for complex workflows where the order of operations is important.

    Parameters
    ----------
    flag : bool, default = True
        if True, wait for kernel to finish
    device : Device, default = None
        the device to set the flag. If None, set it to the current device
    """
    if device is None:
        get_device().set_wait_to_finish(flag)
    else:
        device.set_wait_to_finish(flag)


def default_initialisation():
    """Set default backend and device"""
    backends = list_available_backends()
    if backends:
        _ = select_backend(backends[-1])
    else:
        warnings.warn(
            "No backend available. Please install either OpenCL or CUDA on your system.",
            RuntimeWarning,
        )


def gpu_info():
    device_list = list_available_devices()
    info = []
    for device_name in device_list:
        info.append(select_device(device_name).info)
    return info
