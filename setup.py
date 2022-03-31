from skbuild import setup

setup(
    name="pyclesperanto",
    version="0.5.2",
    description="GPU accelerated image processing library",
    author="Stephane Rigaud",
    license="BDS",
    packages=['pyclesperanto'],
    # package_dir={'': 'pyclesperanto'},
    cmake_install_dir='pyclesperanto',
    python_requires='>=3.7',
    )

# When building extension modules `cmake_install_dir` should always be set to the
# location of the package you are building extension modules for.
# Specifying the installation directory in the CMakeLists subtley breaks the relative
# paths in the helloTargets.cmake file to all of the library components.