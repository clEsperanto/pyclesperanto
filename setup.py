import sys, os

sys.path.append(os.path.dirname(__file__))

# Get the version from the version file and the package description from the README file
with open("README.md") as fp:
    readme = fp.read()

ver_dic = {}
version_file = open("pyclesperanto/_version.py")
try:
    version_file_contents = version_file.read()
finally:
    version_file.close()

exec(compile(version_file_contents, "pyclesperanto/_version.py", "exec"), ver_dic)

conda_prefix = os.environ.get('CONDA_PREFIX')
cmake_args_list = [
    "-DCLIC_VERSION:String=" + ver_dic["CLIC_VERSION"]
]
if conda_prefix:
    cmake_args_list.append("-DCMAKE_PREFIX_PATH:FILEPATH=" + conda_prefix)

from skbuild import setup

setup(
    name="pyclesperanto",
    version=ver_dic["VERSION"],
    cmake_args=cmake_args_list,
    author="Stephane Rigaud",
    author_email="stephane.rigaud@pasteur.fr",
    license="BSD-3-Clause",
    description="GPU-accelerated image processing in python using OpenCL",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=["pyclesperanto"],
    cmake_install_dir="pyclesperanto",
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "toolz",
        "matplotlib",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    project_urls={
        "Documentation": "https://github.com/clEsperanto/pyclesperanto#README.md",
        "Source": "https://github.com/clEsperanto/pyclesperanto/",
        "Issues": "https://github.com/clEsperanto/pyclesperanto/issues",
    },
)

# When building extension modules `cmake_install_dir` should always be set to the
# location of the package you are building extension modules for.
# Specifying the installation directory in the CMakeLists subtley breaks the relative
# paths in the helloTargets.cmake file to all of the library components.
