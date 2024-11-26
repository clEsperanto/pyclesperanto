# py-clesperanto
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pyclesperanto.svg)](https://anaconda.org/conda-forge/pyclesperanto)
[![PyPI](https://img.shields.io/pypi/v/pyclesperanto.svg?color=green)](https://pypi.org/project/pyclesperanto)
[![License](https://img.shields.io/pypi/l/pyclesperanto.svg?color=green)](https://github.com/clEsperanto/pyclesperanto/blob/main/LICENSE)
[![Development Status](https://img.shields.io/pypi/status/pyclesperanto.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![Build](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build.yml/badge.svg)](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/clesperanto/pyclesperanto/branch/main/graph/badge.svg)](https://codecov.io/gh/clesperanto/pyclesperanto)
[![Python Version](https://img.shields.io/pypi/pyversions/pyclesperanto.svg?color=green)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub stars](https://img.shields.io/github/stars/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)
[![GitHub forks](https://img.shields.io/github/forks/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13853800.svg)](https://doi.org/10.5281/zenodo.13853800)


pyclesperanto is the python package of [clEsperanto] - a multi-language framework for GPU-accelerated image processing.
It relies on a familly of [OpenCL kernels] originated from [CLIJ].
This package is developped in python and C++ wrapped using [PyBind11], and uses the C++ [CLIc] library as a processing backend.

### Reference and examples

An in-depth API reference and package documentation can be found [here](https://clesperanto.github.io/pyclesperanto/), and several demonstration notebook on how to use the library and major functionnality are available in the [demos folder](https://github.com/clEsperanto/pyclesperanto/tree/main/demos)

## __Installation__

* Get a conda/python environment, e.g. via [__mamba-forge__](https://github.com/conda-forge/miniforge#mambaforge).
    * If you never used python/conda environments before, please follow [these instructions](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html) first.
* Create a new environment and activate it:

```
mamba create --name cle
mamba activate cle
```

* Install pyclesperanto using [__mamba / conda__](https://focalplane.biologists.com/2022/12/08/managing-scientific-python-environments-using-conda-mamba-and-friends/):

```
mamba install -c conda-forge pyclesperanto
```

> [!WARNING]
__MacOS__ users may need to install the following package: `mamba install -c conda-forge ocl_icd_wrapper_apple`
__Linux__ users may need to install the following package: `mamba install -c conda-forge ocl-icd-system`

> [!NOTE]
pyclesperanto package is also available on `PyPI` and can be install with the command `pip install pyclesperanto`

## Troubleshooting: Graphics cards drivers

In case you encounter one of the following error messages:
* `"ImportError: DLL load failed while importing cl: The specified procedure could not be found"` [see also](https://github.com/clEsperanto/pyclesperanto_prototype/issues/55)
* `"clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR"`
* `"No backend available. Please install either OpenCL or CUDA on your system."`
* `"No device available. Please install either OpenCL or CUDA on your system."`

please install recent drivers for your graphics card and/or OpenCL device. Select the right driver source depending on your hardware from this list:

* [AMD drivers](https://www.amd.com/en/support)
* [NVidia drivers](https://www.nvidia.com/download/index.aspx)
* [Intel GPU drivers](https://www.intel.com/content/www/us/en/download/726609/intel-arc-graphics-windows-dch-driver.html)
* [Microsoft Windows OpenCL support](https://www.microsoft.com/en-us/p/opencl-and-opengl-compatibility-pack/9nqpsl29bfff)

Linux user may have to install packages such as `intel-opencl-icd` or `rocm-opencl-runtime` depending on their GPU.

## __Code Example__

```python
import pyclesperanto as cle
from skimage.io import imread, imsave

# initialize GPU
device = cle.select_device()
print("Used GPU: ", device)

image = imread("https://samples.fiji.sc/blobs.png?raw=true")

# push image to device memory
input_image = cle.push(image)

# process the image
inverted = cle.subtract_image_from_scalar(input_image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# read image from device memory
output_image = cle.pull(labeled)
imsave("result.tif", output_image)
```

## __Examples & Demos__

<table border="0">
<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/blob/main/demos/images/select_device.png?raw=true" width="300"/>
</td><td>

* [Select and Manage devices](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/api/select_devices.ipynb)
* [Host-Device memory management](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/api/push_pull_create.ipynb)
* [Process an image](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/api/process_image.ipynb)

</td></tr>

<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/blob/main/demos/images/crop_and_paste_images.png?raw=true" width="300"/>
</td><td>

* [Crop, Flip, Paste arrays](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/basics/crop_flip_paste.ipynb)
* [Math operations](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/basics/arithmetic_operators.ipynb)
* [Matrix operations](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/basics/matrices_operations.ipynb)
* [Vector and Matrix operations](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/basics/vector_and_matrices_operations.ipynb)
* [Inspecting 3D image](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/basics/inspecting_3d_images.ipynb)

</td></tr>


<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/blob/main/demos/images/segmentation_3d.png?raw=true" width="300"/>
</td><td>

* [Segment and analyse blosb](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/analyse_blobs.ipynb)
* [Segment cell based on membrane](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/membrane_segmentation_2d.ipynb)
* [Cell segmentation in 3D](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/Segmentation_3D.ipynb)
* [Voronoi_Otsu_labeling](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/voronoi_otsu_labeling.ipynb)

</td></tr>


<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/blob/main/demos/images/affine_transforms.png?raw=true" width="300"/>
</td><td>

* [Edge detection](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/edge_detection_and_enhancement.ipynb)
* [Parametric maps](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/parametric_maps.ipynb)
* [Rotation, scaling, translation, and affine transform](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/affine_transforms.ipynb)
<!-- * [Morphomathic operations](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/morphomath_operation.ipynb)   -->

</td></tr>


<tr><td>
<img src="https://github.com/clEsperanto/pyclesperanto/blob/main/demos/images/multi-device-tiling.png?raw=true" width="300"/>
</td><td>

* [Multi-device tile processing](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/example/multi-gpu_tile_processing_with_dask.ipynb)
* [Bia-Bob](https://github.com/clEsperanto/pyclesperanto/tree/main/demos/interoperability/multi-biabob-example.ipynb)

</td></tr>

</table>

More usage and example can be found as notebooks in the [demos](https://github.com/clEsperanto/pyclesperanto/tree/main/demos) folder. As well as in the [documentation](https://clesperanto.github.io/pyclesperanto/).

# __Contributing and Feedback__

clEsperanto is developed in the open because we believe in the [open source community].
Feel free to drop feedback as [github issue] or via [image.sc forum].
Contribution are also very welcome. Please read our [community guidelines] before you start and get in touch with us so that we can help you get started.
If you liked our work, star the repository, share it with your friends, and use it to make cool stuff!

## Acknowledgements

We acknowledge support by the Deutsche Forschungsgemeinschaft under Germany’s Excellence Strategy (EXC2068) Cluster of Excellence Physics of Life of TU Dresden.
This project has been made possible in part by grant number 2021-237734 ([GPU-accelerating Fiji and friends using distributed CLIJ, NEUBIAS-style, EOSS4](https://chanzuckerberg.com/eoss/proposals/gpu-accelerating-fiji-and-friends-using-distributed-clij-neubias-style/)) from the Chan Zuckerberg Initiative DAF, an advised fund of the Silicon Valley Community Foundation.


[clEsperanto]: http://clesperanto.net/
[OpenCL kernels]: https://github.com/clEsperanto/clij-opencl-kernels/tree/clesperanto_kernels
[CLIJ]: http://clij.github.io/
[CLIc]: https://github.com/clEsperanto/CLIc
[community guidelines]: https://clij.github.io/clij2-docs/community_guidelines
[github issue]: https://github.com/clEsperanto/pyclesperanto/issues
[image.sc forum]: https://forum.image.sc/
[PyBind11]: https://github.com/pybind
