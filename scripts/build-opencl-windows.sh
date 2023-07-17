#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

set -o xtrace

git clone --branch v2022.01.04 https://github.com/KhronosGroup/OpenCL-ICD-Loader
git clone --branch v2022.01.04 https://github.com/KhronosGroup/OpenCL-Headers


cmake -D CMAKE_INSTALL_PREFIX=./OpenCL-Headers/install -S ./OpenCL-Headers -B ./OpenCL-Headers/build 
cmake --build ./OpenCL-Headers/build --target install

cp ./OpenCL-Headers/CL/*.h ./OpenCL-ICD-Loader/inc/

# if someone would like to try to create win32 wheels bellow lines may be useful
cmake -D CMAKE_PREFIX_PATH=${PWD}/OpenCL-Headers/install -S ./OpenCL-ICD-Loader -B ./OpenCL-ICD-Loader/build 
cmake --build ./OpenCL-ICD-Loader/build --target install --config Release

echo "pyclesperanto wheel includes Khronos Group OpenCL-ICD-Loader which is licensed as below" >> ${SCRIPT_DIR}/../LICENSE
cat ./OpenCL-ICD-Loader/LICENSE >> ${SCRIPT_DIR}/../LICENSE
