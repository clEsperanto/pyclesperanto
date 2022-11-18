from ._pyclesperanto import _cleProcessor
from typing import Optional


class Device(_cleProcessor):
    """Device

    OpenCL compatible device class

    Parameters
    ----------
    _cleProcessor : C++ wrapper class
        C++ OpenCL device class running behind Device accessible using `super()`
    """

    def __init__(self) -> None:
        super().__init__()

    @property
    def name(self) -> str:
        return super().name

    @property
    def info(self) -> str:
        return super().info

    def select_device(self, name: str = "") -> None:
        super().select_device(name)

    def wait_for_kernel_to_finish(self, flag: bool = True) -> None:
        super().wait_for_kernel_to_finish(flag)


class _current_device:
    _instance: Optional[Device] = None


def get_device() -> Device:
    """Return the current device"""
    return _current_device._instance or select_device()


def select_device(name: str = "") -> Device:
    """Return the selected device"""
    if not _current_device._instance:
        _current_device._instance = Device()
    _current_device._instance.select_device(name)
    return _current_device._instance


def list_available_devices() -> list:
    """Retrieve a list of names of available OpenCL-devices"""
    from ._pyclesperanto import _ListAvailableDevices

    return list(_ListAvailableDevices())


def set_wait_for_kernel_to_finish(flag: bool = True) -> None:
    """Configure asyncronous execution of OpenCL kernels (False)"""
    get_device().wait_for_kernel_to_finish(flag)


def info() -> str:
    """Return full description of the current device"""
    return get_device().info
