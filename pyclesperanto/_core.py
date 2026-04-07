import warnings
from typing import Optional, Union

import numpy as np

from ._backend import _get_backend


def _get_backend_manager():
    return _get_backend()._BackendManager


def _get_device_class():
    return _get_backend()._Device


# Re-export Device type for type annotations
# This is a lazy property — actual class comes from whichever backend is active
class _DeviceProxy(type):
    """Metaclass so that `Device` can be used as a type hint before backend is loaded."""

    def __instancecheck__(cls, instance):
        try:
            return isinstance(instance, _get_device_class())
        except RuntimeError:
            return False


class Device(metaclass=_DeviceProxy):
    """Type alias for the backend Device class."""

    pass


class _current_device:
    _instance = None


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
    backend_mgr = _get_backend_manager()
    if isinstance(device_id, str):
        device = backend_mgr.get_backend().getDeviceFromName(device_id, device_type)
    elif isinstance(device_id, int):
        device = backend_mgr.get_backend().getDeviceFromIndex(device_id, device_type)
    else:
        raise ValueError(
            f"'{device_id}' is not a supported device_id. Please use either a string or an integer."
        )

    if device is None:
        warnings.warn(
            "No device found in the system. Please check your system installation.",
            RuntimeWarning,
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
    dev_list = list(
        _get_backend_manager().get_backend().getDevicesList(type=device_type)
    )
    if not dev_list:
        warnings.warn(
            "No device available. Please check your system installation.",
            RuntimeWarning,
        )
    return dev_list


def wait_for_kernel_to_finish(wait: bool = True, device: Device = None):
    """Wait for kernel to finish

    Enforce the system to wait for the kernel to finish before continuing. Introducing a
    slowdown in the workflow. This is useful for debugging purposes, benchmarking and
    profiling, as well as for complex workflows where the order of operations is important.

    Parameters
    ----------
    wait : bool, default = True
        if True, wait for kernel to finish
    device : Device, default = None
        the device to set the flag. If None, set it to the current device
    """
    if device is None:
        get_device().set_wait_to_finish(wait)
    else:
        device.set_wait_to_finish(wait)


def info():
    """Print information about the devices available on the system"""
    device_info = [
        f"{idx} - {select_device(device).info}"
        for idx, device in enumerate(list_available_devices())
    ]
    print("".join(device_info))


def _default_initialisation():
    """Select a default device on the active backend."""
    try:
        from ._backend import get_backend_name

        backend_name = get_backend_name()
        if backend_name is None:
            # _get_backend() triggers auto-selection; then re-read the name
            _get_backend()
            backend_name = get_backend_name()
        _get_backend_manager().set_backend(backend_name)
        select_device()
    except Exception as e:
        warnings.warn(
            f"Error during device initialisation: {e}\n"
            "No GPU device found. Please check your system installation.",
            RuntimeWarning,
        )
