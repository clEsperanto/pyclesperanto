#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
CUDA_VERSION="12-6"

set -e -x

# Install CUDA toolkit in manylinux container (AlmaLinux 8 / CentOS 8)
yum install -y yum-utils
yum-config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo

yum install -y \
    cuda-nvcc-${CUDA_VERSION} \
    cuda-cudart-devel-${CUDA_VERSION} \
    cuda-cudart-${CUDA_VERSION} \
    cuda-nvrtc-devel-${CUDA_VERSION} \
    cuda-nvrtc-${CUDA_VERSION} \
    libnvjitlink-${CUDA_VERSION} \
    libnvjitlink-devel-${CUDA_VERSION} \
    cuda-driver-devel-${CUDA_VERSION}

# Create stub symlink for linking
ln -sf /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1

# Append license information
echo "pyclesperanto-cuda wheel includes NVIDIA CUDA toolkit components subject to the NVIDIA CUDA EULA" >>"${SCRIPT_DIR}/../LICENSE"
