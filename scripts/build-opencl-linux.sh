#!/usr/bin/env bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

set -e -x

mkdir -p ~/deps
cd ~/deps

git clone --branch v2.3.1 https://github.com/OCL-dev/ocl-icd
cd ocl-icd

# set includes content in OpenCL folder instead of CL for consistancy
curl -L -O https://raw.githubusercontent.com/conda-forge/ocl-icd-feedstock/e2c03e3ddb1ff86630ccf80dc7b87a81640025ea/recipe/install-headers.patch
git apply install-headers.patch

# Use PYOPENCL_HOME if define in OCL-ICD lib
# see https://github.com/inducer/pyopencl/blob/2bb87e0f7d886dfb86523cf08b269cad0c0b79fc/pyopencl/__init__.py 
# curl -L -O https://github.com/isuruf/ocl-icd/commit/3862386b51930f95d9ad1089f7157a98165d5a6b.patch
curl -L -O https://github.com/StRigaud/ocl-icd/commit/83bbc51b8ac80354fe30bf9b081b83181f8b3f82.patch
git apply 83bbc51b8ac80354fe30bf9b081b83181f8b3f82.patch

autoreconf -i
chmod +x configure
./configure --prefix=/usr
make -j4
make install

# Bundle license files
echo "pyclesperanto wheel includes ocl-icd which is licensed as below" >> ${SCRIPT_DIR}/../LICENSE
cat ~/deps/ocl-icd/COPYING >> ${SCRIPT_DIR}/../LICENSE 