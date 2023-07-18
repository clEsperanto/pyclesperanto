#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
VERSION="v2022.01.04"
OPENCL_HEADERS_DIR="${SCRIPT_DIR}/OpenCL-Headers"
OPENCL_ICD_LOADER_DIR="${SCRIPT_DIR}/OpenCL-ICD-Loader"

set -e

# Clone and install OpenCL-Headers
git clone --branch ${VERSION} https://github.com/KhronosGroup/OpenCL-Headers "${OPENCL_HEADERS_DIR}"
cmake -D CMAKE_INSTALL_PREFIX="${OPENCL_HEADERS_DIR}/install" -S "${OPENCL_HEADERS_DIR}" -B "${OPENCL_HEADERS_DIR}/build"
cmake --build "${OPENCL_HEADERS_DIR}/build" --target install

# Clone and install OpenCL-ICD-Loader
git clone --branch ${VERSION} https://github.com/KhronosGroup/OpenCL-ICD-Loader "${OPENCL_ICD_LOADER_DIR}"
cmake -D CMAKE_INSTALL_PREFIX="${OPENCL_ICD_LOADER_DIR}/install" -D OPENCL_ICD_LOADER_HEADERS_DIR="${OPENCL_HEADERS_DIR}/install/include" -S "${OPENCL_ICD_LOADER_DIR}" -B "${OPENCL_ICD_LOADER_DIR}/build"
cmake --build "${OPENCL_ICD_LOADER_DIR}/build" --target install --config Release


echo "pyclesperanto wheel includes Khronos Group OpenCL-ICD-Loader which is licensed as below" >> ${SCRIPT_DIR}/../LICENSE
cat ./OpenCL-ICD-Loader/LICENSE >> ${SCRIPT_DIR}/../LICENSE
