#!/usr/bin/env bash
# repair-nvrtc-linux.sh
# libnvrtc-builtins is loaded via dlopen() by libnvrtc, so auditwheel
# cannot detect it. This script copies it into the wheel's .libs/ directory.

set -e -x

DEST_DIR="${1:?Usage: $0 <dest_dir>}"

# Debug: show what nvrtc files actually exist
echo "=== Searching for all libnvrtc-builtins files ==="
find /usr/local/cuda* -name "libnvrtc-builtins*" 2>/dev/null || true
echo "=== Contents of /usr/local/cuda/lib64/ (nvrtc related) ==="
ls -la /usr/local/cuda/lib64/*nvrtc* 2>/dev/null || true

WHEEL=$(ls "${DEST_DIR}"/*.whl | head -n1)
WHEEL_DIR=$(mktemp -d)
trap "rm -rf ${WHEEL_DIR}" EXIT

unzip -d "${WHEEL_DIR}" "${WHEEL}"

LIBS_DIR="${WHEEL_DIR}/pyclesperanto_cuda.libs"

if [ ! -d "${LIBS_DIR}" ]; then
  echo "ERROR: ${LIBS_DIR} not found"
  exit 1
fi

# Broad search: follow symlinks, search all cuda dirs, match any suffix
BUILTINS=$(find /usr/local/cuda* -L -name "libnvrtc-builtins*.so*" -type f 2>/dev/null | head -n1)
if [ -z "${BUILTINS}" ]; then
  echo "ERROR: libnvrtc-builtins not found anywhere under /usr/local/cuda*"
  exit 1
fi

# Read canonical soname that libnvrtc will dlopen
SONAME=$(objdump -p "${BUILTINS}" | awk '/SONAME/{print $2}')
: "${SONAME:=$(basename "${BUILTINS}")}"

echo "Copying ${BUILTINS} as ${SONAME} into wheel"
cp "${BUILTINS}" "${LIBS_DIR}/${SONAME}"

# Update RECORD
RECORD=$(find "${WHEEL_DIR}" -name "RECORD" -path "*.dist-info/*")
HASH=$(sha256sum "${LIBS_DIR}/${SONAME}" | awk '{print $1}' | xxd -r -p | base64 | tr '+/' '-_' | tr -d '=')
SIZE=$(stat -c%s "${LIBS_DIR}/${SONAME}")
echo "pyclesperanto_cuda.libs/${SONAME},sha256=${HASH},${SIZE}" >> "${RECORD}"

rm -f "${WHEEL}"
(cd "${WHEEL_DIR}" && zip -r "${WHEEL}" .)
