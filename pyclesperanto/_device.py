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
        """name returns the name of the device

        Returns
        -------
        str
            device name
        """
        return super().name

    @property
    def info(self) -> str:
        """info returns a description of the device
        
        Returns
        -------
        str
            device description
        """
        return super().info

    def select_device(self, name: str = "", device_type: str = "all") -> None:
        """select_device selects a device by name and type
        
        Parameters
        ----------
        name : str, default = ""
            Name or subname of the device to be selected (e.g. "NVIDIA", "RTX", "Intel Iris", etc.)
        device_type : str, default = "all"
            Type of device to be selected (e.g. "all", "cpu", "gpu")
        """
        super().select_device(name=name, type=device_type)

    def wait_for_kernel_to_finish(self, flag: bool = True) -> None:
        """wait_for_kernel_to_finish configures asyncronous execution of OpenCL kernels (False)

        Configure clEsperanto to wait for the kernel to finish before returning control to the host.

        Parameters
        ----------
        flag : bool, default = True
        """
        super().wait_for_kernel_to_finish(flag=flag)


class _current_device:
    _instance: Optional[Device] = None


def get_device() -> Device:
    """Return the current device instance

    Returns
    -------
    device : Device
    """
    return _current_device._instance or select_device()


def new_device(name: str ="", device_type: str = "all") -> Device:
    dev = Device()
    dev.select_device(name, device_type)
    return dev


def select_device(name: str = "", device_type: str = "all") -> Device:
    """Select a device by name and return it

    Select device using its name or subname (e.g. "NVIDIA", "RTX", "Intel Iris", etc.)
    To retrieve a list of available devices, use `list_available_devices()`

    Parameters
    ----------
    name : str, default = ""
        Name or subname of the device to be selected (e.g. "NVIDIA", "RTX", "Intel Iris", etc.)
    device_type : str, default = "all"
        Type of device to be selected (e.g. "all", "cpu", "gpu")

    Returns
    -------
    device : Device
    """
    if not _current_device._instance:
        _current_device._instance = Device()
    _current_device._instance.select_device(name, device_type)
    return _current_device._instance


def list_available_devices(device_type: str = "all") -> list:
    """Retrieve a list of names of available OpenCL-devices

    Will search system for available OpenCL compatible device and return a list of their names.
    Use 'select_device' to select a device by name.

    Returns
    -------
    name list : list[str]
    """
    from ._pyclesperanto import _ListAvailableDevices

    return list(_ListAvailableDevices(type=device_type))


def set_wait_for_kernel_to_finish(flag: bool = True) -> None:
    """Configure asyncronous execution of OpenCL kernels (False)

    Configure clEsperanto to wait for the kernel to finish before returning control to the host.

    Parameters
    ----------
    flag : bool, default = True
    """
    get_device().wait_for_kernel_to_finish(flag=flag)


def info() -> str:
    """Return description of the current device

    Returns
    -------
    info : str
    """
    return get_device().info
