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

unzip -d "${WHEEL_DIR}" "${WHEEL}"

LIBS_DIR="${WHEEL_DIR}/pyclesperanto_cuda.libs"

if [ ! -d "${LIBS_DIR}" ]; then
  echo "ERROR: ${LIBS_DIR} not found"
  exit 1
fi

# -L must precede paths; follow symlinks to match real files
BUILTINS=$(find -L "${CUDA_LIB}" -maxdepth 1 -name "libnvrtc-builtins.so.*" ! -name "*_static*" -type f 2>/dev/null | head -n1)
if [ -z "${BUILTINS}" ]; then
  echo "ERROR: libnvrtc-builtins not found in ${CUDA_LIB}"
  ls -la "${CUDA_LIB}"/*nvrtc* 2>/dev/null || true
  exit 1
fi

# Read canonical soname that libnvrtc will dlopen (e.g. libnvrtc-builtins.so.12.6)
SONAME=$(objdump -p "${BUILTINS}" | awk '/SONAME/{print $2}')
: "${SONAME:=$(basename "${BUILTINS}")}"

echo "Copying ${BUILTINS} as ${SONAME} into wheel .libs/"
cp "${BUILTINS}" "${LIBS_DIR}/${SONAME}"

# Update RECORD with proper hash (PEP 376: sha256=<urlsafe_b64>)
RECORD=$(find "${WHEEL_DIR}" -name "RECORD" -path "*.dist-info/*")
HASH=$(python3 -c "
import hashlib, base64, sys
with open(sys.argv[1], 'rb') as f:
    print(base64.urlsafe_b64encode(hashlib.sha256(f.read()).digest()).decode().rstrip('='))
" "${LIBS_DIR}/${SONAME}")
SIZE=$(stat -c%s "${LIBS_DIR}/${SONAME}")
echo "pyclesperanto_cuda.libs/${SONAME},sha256=${HASH},${SIZE}" >> "${RECORD}"

# Repack wheel — use * (not .) to avoid ./ prefix in zip entries
rm -f "${WHEEL}"
(cd "${WHEEL_DIR}" && zip -r "${WHEEL}" *)