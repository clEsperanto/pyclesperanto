def list_available_devices(self) -> list:
    """Retrieve a list of names of available OpenCL-devices"""
    from ._pyclesperanto import _ListAvailableDevices

    return list(_ListAvailableDevices())


def select_device(self, device_name: str) -> str:
    """Select an OpenCL device that contains `device_name` in its name."""
    return self._gpu.select_device(device_name)


def set_wait_for_kernel_to_finish(self, flag: bool = True):
    """Configure asyncronous execution of OpenCL kernels (False)"""
    return self._gpu.wait_for_kernel_to_finish(flag)


def operations(self):
    """Return all operations/filters pyclesperanto supports"""
    all_operation_names = dir(self)
    result = {}
    for operation_name in [o for o in all_operation_names if not o.startswith("_")]:
        potential_function = getattr(self, operation_name)
        if callable(potential_function):
            result[operation_name] = potential_function
    return result


def operation(self, operation_name: str):
    """Return a function pyclesperanto supports specified by name"""
    potential_function = getattr(self, operation_name)
    if callable(potential_function):
        return potential_function
