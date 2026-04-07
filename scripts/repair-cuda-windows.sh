#!/usr/bin/env bash
set -e -x

DEST_DIR="${1:?Usage: $0 <dest_dir> <wheel>}"
WHEEL="${2:?Usage: $0 <dest_dir> <wheel>}"

CUDA_BIN="${CUDA_PATH}/bin"
if [ ! -d "${CUDA_BIN}" ]; then
  echo "ERROR: CUDA bin directory not found at ${CUDA_BIN} (CUDA_PATH=${CUDA_PATH})"
  exit 1
fi

BUILTINS_DLL=$(find "${CUDA_BIN}" -maxdepth 1 -name "nvrtc-builtins64_*.dll" -type f 2>/dev/null | head -n1)
if [ -z "${BUILTINS_DLL}" ]; then
  echo "ERROR: nvrtc-builtins64_*.dll not found in ${CUDA_BIN}"
  exit 1
fi

DLL_NAME=$(basename "${BUILTINS_DLL}")
echo "Discovered NVRTC builtins DLL: ${DLL_NAME}"

delvewheel show "${WHEEL}"
delvewheel repair \
  --add-path "${CUDA_BIN}" \
  --add-dll "${DLL_NAME}" \
  --no-dll "nvcuda.dll;msvcp140.dll;vcruntime140_1.dll;vcruntime140.dll" \
  -w "${DEST_DIR}" \
  "${WHEEL}"
