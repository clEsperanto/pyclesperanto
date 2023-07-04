from ._pyclesperanto import _Device
from ._pyclesperanto import _BackendManager

from typing import Optional

Device = _Device
BackendManager = _BackendManager


class _current_device:
    _instance: Optional[Device] = None


def get_device() -> Device:
    """Return the current device instance

    Returns
    -------
    device : Device
    """
    return _current_device._instance or select_device()


def select_device(device_name: str = "", device_type: str = "all") -> Device:
    """Select a device by name and type, and return it

    Select device using its name or subname (e.g. "NVIDIA", "RTX", "Iris", etc.) and
    type (e.g. "all", "cpu", "gpu").
    To retrieve a list of available devices, use `list_available_devices()`

    Parameters
    ----------
    device_name : str, default = ""
        Name or subname of the device to be selected (e.g. "NVIDIA", "RTX", "Intel Iris", etc.)
    device_type : str, default = "all"
        Type of device to be selected (e.g. "all", "cpu", "gpu")

    Returns
    -------
    device : Device
    """
    device = BackendManager.get_backend().getDevice(device_name, device_type)
    if _current_device._instance and device == _current_device._instance:
        return _current_device._instance
    _current_device._instance = device
    return device


def list_available_devices(device_type: str = "all") -> list[str]:
    """Retrieve a list of names of available devices

    Will search system for backend available compatible device and return a list of their names.
    Use 'select_device' or 'get_devices' to select devices.

    Parameters
    ----------
    device_type : str, default = "all"
        Type of device to be selected (e.g. "all", "cpu", "gpu")

    Returns
    -------
    name list : list[str]
    """
    return list(BackendManager.get_backend().getDevicesList(type=device_type))


def select_backend(backend_type: str = "opencl") -> str:
    """select backend

    Select the backend used by pyclesperanto, OpenCL or CUDA.
    Default is OpenCL.

    Parameters
    ----------
    type : str, default = "opencl"
        determine the backend to use between opencl and cuda
    """

    # enforce lowercase for backend_type
    backend_type = backend_type.lower()
    # is backend_type is different than "cuda" or "opencl", raise an error
    if backend_type not in ["cuda", "opencl"]:
        raise ValueError(
            f"Backend type '{backend_type}' not supported. Please use 'opencl' or 'cuda'."
        )
    BackendManager.set_backend(backend=backend_type)
    # reset current device to default one
    select_device()
    return f"{BackendManager.get_backend()} selected."
