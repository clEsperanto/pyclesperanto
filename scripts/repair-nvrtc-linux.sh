#!/usr/bin/env bash
# repair-nvrtc-linux.sh
# libnvrtc-builtins is loaded via dlopen() by libnvrtc, so auditwheel
# cannot detect it. This script copies it into the wheel's .libs/ directory.
# The bundled libnvrtc already has RUNPATH=$ORIGIN (set by auditwheel),
# so dlopen("libnvrtc-builtins.so.12.6") searches .libs/ and finds it.

set -e -x

DEST_DIR="${1:?Usage: $0 <dest_dir>}"
CUDA_LIB="/usr/local/cuda/lib64"

WHEEL=$(ls "${DEST_DIR}"/*.whl | head -n1)
WHEEL_DIR=$(mktemp -d)
trap "rm -rf ${WHEEL_DIR}" EXIT

# Wheels are zip files — unzip is always available in manylinux
unzip -d "${WHEEL_DIR}" "${WHEEL}"

# auditwheel places vendored libs at <package_name>.libs/ (top-level)
LIBS_DIR="${WHEEL_DIR}/pyclesperanto_cuda.libs"

if [ ! -d "${LIBS_DIR}" ]; then
  echo "ERROR: ${LIBS_DIR} not found"
  exit 1
fi

# Find the real file (not symlinks) in the CUDA installation
BUILTINS=$(find "${CUDA_LIB}" -maxdepth 1 -name "libnvrtc-builtins.so.12*" ! -type l | head -n1)
if [ -z "${BUILTINS}" ]; then
  echo "ERROR: libnvrtc-builtins not found in ${CUDA_LIB}"
  exit 1
fi

# Read canonical soname that libnvrtc will dlopen
SONAME=$(objdump -p "${BUILTINS}" | awk '/SONAME/{print $2}')
: "${SONAME:=libnvrtc-builtins.so.12.6}"

echo "Copying ${BUILTINS} as ${SONAME} into wheel"
cp "${BUILTINS}" "${LIBS_DIR}/${SONAME}"

# Update RECORD with the new file's hash and size
RECORD="${WHEEL_DIR}/pyclesperanto_cuda-"*".dist-info/RECORD"
HASH=$(sha256sum "${LIBS_DIR}/${SONAME}" | awk '{print $1}' | xxd -r -p | base64 | tr '+/' '-_' | tr -d '=')
SIZE=$(stat -c%s "${LIBS_DIR}/${SONAME}")
echo "pyclesperanto_cuda.libs/${SONAME},sha256=${HASH},${SIZE}" >> ${RECORD}

# Repack the wheel (zip from inside the directory to get correct paths)
rm -f "${WHEEL}"
(cd "${WHEEL_DIR}" && zip -r "${WHEEL}" .)