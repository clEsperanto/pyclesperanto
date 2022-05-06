# pyclesperanto
[![Build](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build_and_deploy.yml/badge.svg)](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build_and_deploy.yml)
[![License](https://img.shields.io/badge/license-BSD-informational)](https://github.com/clEsperanto/pyclesperanto/blob/main/LICENSE)
[![Website](https://img.shields.io/website?url=http%3A%2F%2Fclesperanto.net)](http://clesperanto.net)
[![GitHub stars](https://img.shields.io/github/stars/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)
[![GitHub forks](https://img.shields.io/github/forks/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)

pyclesperanto is a python package for [clEsperanto](http://clesperanto.net/) - a multi-language framework for GPU-accelerated image processing.
clEsperanto uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/).
This package relies on the [CLIc](https://github.com/clEsperanto/CLIc_prototype) back-end for processing.

## Usage

**Note**: This project is under heavy development. Functions and parameters are subject to change.

```python
from skimage.io import imread
from pyclesperanto import cle

image = imread("https://imagej.nih.gov/ij/images/blobs.gif")

# push and create buffer
gpu_output = cle.create(image.shape)
gpu_input = cle.push(image)

# apply kernel
cle.add_image_and_scalar(input_image=gpu_input, output_image=gpu_output, scalar=100)

# visualize result
cle.imshow(gpu_output)

# get result as numpy array
result = cle.pull(gpu_output)
```

## Example gallery 

<table border="0">

<tr><td>
<img src="user_docs/images/labeled_blobs.png" width="300"/>
</td><td>

[Segment + analyze blobs](user_docs/process_blobs.ipynb)

</td></tr>

<tr><td>
<img src="user_docs/images/cell_segmentation.png" width="300"/>
</td><td>

[Cell segmentation + Voronoi labeling](user_docs/cell_segmentation.ipynb)

</td></tr>

<tr><td>
<img src="user_docs/images/image_filtering.png" width="300"/>
</td><td>

[3D image filtering](user_docs/image_filtering.ipynb)

</td></tr>


<tr><td>
<img src="user_docs/images/find_local_maxima.png" width="300"/>
</td><td>

[Find local maxima](user_docs/find_local_maxima.ipynb)

</td></tr>

<tr><td>
<img src="user_docs/images/tribolium3d_segmentation.png" width="300"/>
</td><td>

[3D Tribolium nuclei segmentation](user_docs/process_tribolium.ipynb)

</td></tr>

<tr><td>
<img src="user_docs/images/explore_API.png" width="300"/>
</td><td>

[Explore application programming interface (API)](user_docs/explore_API.ipynb)

</td></tr>



<!--
<tr><td>

<img src="user_docs/images/multi-gpu.png" width="300"/>

</td><td>

[Multi-GPU developer_docs](user_docs/multi_gpu_demo.ipynb)

</td></tr>
-->
</table>


More usage and example can be found as notebooks in the [user documentation](./user_docs) folder

## Installation

Download the repository and update the associated submodules:
```
git clone https://github.com/clEsperanto/pyclesperanto.git
cd pyclesperanto && git submodule update --init --recursive
```

Here, we assume that your system has an OpenCL valid device and that all its drivers are correctly installed.
Using anaconda (or miniconda), create a virtual environment and activate it:
```
conda create --name pycle python=3.9
conda activate pycle
```
Finally, install pyclesperanto and all its dependencies by running the command:
```
pip install -e .
```

***For MacOS users***, Please install the following package:
```
conda install -c conda-forge -y ocl_icd_wrapper_apple
```

***For Linux users***, Please install the following package:
```
conda install -c conda-forge -y ocl-icd-system
```

## Contributing

Contributions are very welcome. Before spending effort on coding and filing a pull-request, please get in touch, 
[file an issue], and let's discuss your potential contribution.

## License

Distributed under the terms of the [BSD-3] license,
"py-clesperanto" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[file an issue]: https://github.com/clEsperanto/pyclesperanto/issues
