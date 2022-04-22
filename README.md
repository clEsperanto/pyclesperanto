# py-clesperanto
[![Build](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build_and_deploy.yml/badge.svg)](https://github.com/clEsperanto/pyclesperanto/actions/workflows/build_and_deploy.yml)
[![License](https://img.shields.io/badge/license-BSD-informational)](https://github.com/clEsperanto/pyclesperanto/blob/main/LICENSE)
[![Website](https://img.shields.io/website?url=http%3A%2F%2Fclesperanto.net)](http://clesperanto.net)
[![GitHub stars](https://img.shields.io/github/stars/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)
[![GitHub forks](https://img.shields.io/github/forks/clEsperanto/pyclesperanto?style=social)](https://github.com/clEsperanto/pyclesperanto)


pyclEsperanto is a python package for [clEsperanto](http://clesperanto.net/) - a multi-language framework for GPU-accelerated image processing.

clEsperanto uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/). 

This package rely on the [CLIc](https://github.com/clEsperanto/CLIc_prototype) back-end for processing.

## Download

Download the repository and update the submodule
```
git clone https://github.com/clEsperanto/pyclesperanto.git
cd pyclesperanto && git submodule update --init --recursive
```
## Compilation and usage

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
## Usage

_**Warning**_, though global usage should remain the same more, the API is currently beeing designed and implemented. Hence, possible change is to be expected on how to import and use pyclesperanto package.

```python
Import numpy as np
import pyclesperanto as cle

arr = np.ones((3,3,1), dtype=np.float32)

device = cle.gpu() # init gpu device
        
# push and create buffer
gpu_output = device.create(arr.shape)
gpu_input = device.push(arr)

# apply kernel
cle.add_image_and_scalar(device=device, input=gpu_input, output=gpu_output, scalar=100)

# pull from device result and assert
result = device.pull(gpu_output)
```

More usage and example can be found as notebooks in the [demo](./demo) folder

