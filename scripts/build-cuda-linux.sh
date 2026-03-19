#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
CUDA_VERSION="12-6"

set -e -x

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

# Debug: confirm builtins is installed
echo "=== Installed nvrtc files ==="
rpm -ql cuda-nvrtc-${CUDA_VERSION} | grep builtins || true
find /usr/local/cuda* -name "libnvrtc-builtins*" || true

ln -sf /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1

echo "pyclesperanto-cuda wheel includes NVIDIA CUDA toolkit components subject to the NVIDIA CUDA EULA" >>"${SCRIPT_DIR}/../LICENSE"