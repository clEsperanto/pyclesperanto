from hatchling.metadata.plugin.interface import MetadataHookInterface


# This file is used by the hatchling build system to determine the dependencies of the
# main pyclesperanto package, which are the backend packages. It ensures that the
# backend packages are installed with the same version as the main package, to avoid
# compatibility issues.
# The version is read from the _version.py file, which is the source of truth for the package version.
#
class CustomMetadataHook(MetadataHookInterface):

    def update(self, metadata):
        v = metadata["version"]
        # For pre-releases (alpha, beta, rc, dev, post), use >= to allow testing together
        # For final releases, use == to pin exact versions
        op = ">=" if any(x in v for x in ["rc", "a", "b", "dev", "post"]) else "=="

        metadata["dependencies"] = [
            "numpy>=1.20,<3",
            "toolz>=0.11,<2",
            "matplotlib>=3.5,<4",
            f"pyclesperanto-opencl{op}{v}",
        ]
        metadata["optional-dependencies"] = {
            "cuda": [
                f"pyclesperanto-cuda{op}{v}; sys_platform != 'darwin'",
            ],
            "metal": [
                f"pyclesperanto-metal{op}{v}; sys_platform == 'darwin'",
            ],
            "all": [
                f"pyclesperanto-opencl{op}{v}",
                f"pyclesperanto-cuda{op}{v}; sys_platform != 'darwin'",
                f"pyclesperanto-metal{op}{v}; sys_platform == 'darwin'",
            ],
        }
