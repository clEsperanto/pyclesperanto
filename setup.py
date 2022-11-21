# # read the contents of your README file
# from pathlib import Path

# this_directory = Path(__file__).parent
# long_description = (this_directory / "README.md").read_text()

with open("README.md") as fp:
    readme = fp.read()


import sys, os

sys.path.append(os.path.dirname(__file__))


ver_dic = {}
version_file = open("pyclesperanto/_version.py")
try:
    version_file_contents = version_file.read()
finally:
    version_file.close()

exec(compile(version_file_contents, "pyclesperanto/_version.py", "exec"), ver_dic)

from skbuild import setup

setup(
    name="pyclesperanto",
    version=ver_dic["VERSION"],
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
