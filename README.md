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
import numpy as np
from pyclesperanto import cle

arr = np.ones((3,3,1))

# push and create buffer
gpu_output = cle.create(arr.shape)
gpu_input = cle.push(arr)

# apply kernel
cle.add_image_and_scalar(gpu_input, gpu_output, scalar=100)

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
[Segment + analyze blobs](user_docs/images/process_blobs.ipynb)
</td></tr>

<tr><td>
<img src="user_docs/images/image_filtering.png" width="300"/>
</td><td>
[3D Tribolium nuclei segmentation](user_docs/images/image_filtering.ipynb)
</td></tr>

<tr><td>
<img src="user_docs/images/tribolium3d_segmentation.png" width="300"/>
</td><td>
[3D Tribolium nuclei segmentation](user_docs/images/process_tribolium.ipynb)
</td></tr>



<!--
<tr><td>

<img src="user_docs/images/multi-gpu.png" width="300"/>

</td><td>

[Multi-GPU developer_docs](user_docs/images/multi_gpu_demo.ipynb)

</td></tr>
-->
</table>
More usage and example can be found as notebooks in the [demo](./demo) folder

## Installation

Download the repository and update the submodule
```
git clone https://github.com/clEsperanto/pyclesperanto.git
cd pyclesperanto && git submodule update --init --recursive
```

We assume that your system has an OpenCL valide device and that all its drivers are correctly installed.
Using anaconda (or miniconda), create a virtual environment and activate it as such:
```
conda create --name pycle python=3.9
conda activate pycle
```
Install the following package in order to compile our package
```
conda install -c conda-forge -y ocl-icd ocl-icd-system scikit-build numpy cmake pytest pytest-cov pytest-benchmark
```
You can then use the pip to compile and install pyclesperanto on your environment
```
pip install -e .
```

## Contributing

Contributions are very welcome. Before spending effort on coding and filing a pull-request, please get in touch, 
[file an issue], and let's discuss your potential contribution.

## License

Distributed under the terms of the [BSD-3] license,
"napari-workflow-inspector" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[BSD-3]: http://opensource.org/licenses/BSD-3-Clause

[file an issue]: https://github.com/haesleinhuepf/napari-workflow-inspector/issues
