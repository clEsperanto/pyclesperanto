import os
import platform


# fetch and set OCL_ICD_VENDORS to ensure OpenCL ICD discovery works in isolated environments (pixi, conda)
def _ensure_opencl_icd():
    """Ensure OpenCL ICD vendors are discoverable in isolated environments (pixi, conda)."""

    if platform.system() == "Windows":
        return  # Windows uses registry-based discovery, not affected

    conda_prefix = os.environ.get("CONDA_PREFIX", "")
    if not conda_prefix:
        return  # Not in conda/pixi, system loader will work fine

    # Collect all candidate vendor directories
    vendor_dirs = []

    # 1. Conda environment's own vendor dir (e.g., pocl, or other conda-provided ICDs)
    conda_vendors = os.path.join(conda_prefix, "etc", "OpenCL", "vendors")
    if os.path.isdir(conda_vendors) and os.listdir(conda_vendors):
        vendor_dirs.append(conda_vendors)

    # 2. System vendor directories
    if platform.system() == "Darwin":
        system_path = "/System/Library/Frameworks/OpenCL.framework/Versions/Current/lib"
        if os.path.exists(system_path):
            vendor_dirs.append(system_path)
    else:  # Linux
        # Standard system ICD directory
        if os.path.isdir("/etc/OpenCL/vendors"):
            vendor_dirs.append("/etc/OpenCL/vendors")
        # Some distros also use these
        for extra in [
            "/usr/local/etc/OpenCL/vendors",
            "/opt/intel/opencl/vendors",  # Intel GPU runtime
        ]:
            if os.path.isdir(extra) and os.listdir(extra):
                vendor_dirs.append(extra)

    # 3. Respect any existing user-set value
    existing = os.environ.get("OCL_ICD_VENDORS", "")
    if existing:
        # Prepend existing user paths (they take priority)
        existing_dirs = [d for d in existing.split(":") if d]
        vendor_dirs = existing_dirs + [d for d in vendor_dirs if d not in existing_dirs]

    if vendor_dirs:
        os.environ["OCL_ICD_VENDORS"] = ":".join(vendor_dirs)


_ensure_opencl_icd()

from ._pyclesperanto import *  # noqa: E402
from importlib.metadata import version

__version__ = version("pyclesperanto-opencl")
__backend__ = "opencl"

__all__ = [
    "__backend__",
    "__version__",
]
