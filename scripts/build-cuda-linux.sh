#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
CUDA_RELEASE="${CUDA_RELEASE:-12.6.0}"
CUDA_ROOT="/usr/local/cuda-${CUDA_RELEASE%.*}"
REDIST_URL="https://developer.download.nvidia.com/compute/cuda/redist"
# Components required by CLIc (CUDA::cudart, CUDA::cuda_driver, CUDA::nvrtc) + nvcc for FindCUDAToolkit
COMPONENTS="cuda_nvcc cuda_cudart cuda_nvrtc libnvjitlink"

set -e -x

# Install from NVIDIA's redist archives rather than the rhel8 yum repo, whose
# metadata is regularly out of sync on the CDN (404 on repodata files).
PYTHON=$(ls /opt/python/cp3*/bin/python | head -n1)
curl -fsSL --retry 5 "${REDIST_URL}/redistrib_${CUDA_RELEASE}.json" -o /tmp/redistrib.json

mkdir -p "${CUDA_ROOT}"
for component in ${COMPONENTS}; do
    archive=$("${PYTHON}" -c "import json, sys; print(json.load(open('/tmp/redistrib.json'))[sys.argv[1]]['linux-x86_64']['relative_path'])" "${component}")
    curl -fsSL --retry 5 "${REDIST_URL}/${archive}" | tar -xJ -C "${CUDA_ROOT}" --strip-components=1
done

# Match the layout of the rpm install: lib64/ and a /usr/local/cuda symlink
ln -sfn lib "${CUDA_ROOT}/lib64"
ln -sfn "${CUDA_ROOT}" /usr/local/cuda

# Debug: confirm builtins is installed
echo "=== Installed nvrtc files ==="
find /usr/local/cuda/lib64/ -name "libnvrtc-builtins*" || true

ln -sf /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1

echo "pyclesperanto-cuda wheel includes NVIDIA CUDA toolkit components subject to the NVIDIA CUDA EULA" >>"${SCRIPT_DIR}/../LICENSE"
