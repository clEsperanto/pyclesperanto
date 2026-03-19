#!/usr/bin/env bash
# repair-nvrtc-linux.sh
# libnvrtc-builtins is loaded via dlopen() by libnvrtc, so auditwheel
# cannot detect it. This script injects it into the wheel's .libs/ directory.
# The bundled libnvrtc already has RUNPATH=$ORIGIN (set by auditwheel),
# so dlopen("libnvrtc-builtins.so.12.6") searches .libs/ and finds it.

set -e -x

DEST_DIR="${1:?Usage: $0 <dest_dir>}"
CUDA_LIB="/usr/local/cuda/lib64"

# Find the real builtins shared library
BUILTINS=$(find -L "${CUDA_LIB}" -maxdepth 1 -name "libnvrtc-builtins.so.*" ! -name "*_static*" -type f 2>/dev/null | head -n1)
if [ -z "${BUILTINS}" ]; then
  echo "ERROR: libnvrtc-builtins not found in ${CUDA_LIB}"
  ls -la "${CUDA_LIB}"/*nvrtc* 2>/dev/null || true
  exit 1
fi

# Read canonical soname that libnvrtc will dlopen (e.g. libnvrtc-builtins.so.12.6)
SONAME=$(objdump -p "${BUILTINS}" | awk '/SONAME/{print $2}')
: "${SONAME:=$(basename "${BUILTINS}")}"

echo "Injecting ${BUILTINS} as ${SONAME} into wheel"

# Use python3 + zipfile to inject directly — no unzip/zip/temp dir needed
python3 - "${DEST_DIR}" "${BUILTINS}" "${SONAME}" <<'PYEOF'
import sys, os, glob, hashlib, base64, zipfile, tempfile

dest_dir, builtins_path, soname = sys.argv[1], sys.argv[2], sys.argv[3]
whl = glob.glob(os.path.join(dest_dir, "*.whl"))[0]

with open(builtins_path, "rb") as f:
    lib_data = f.read()

digest = base64.urlsafe_b64encode(hashlib.sha256(lib_data).digest()).decode().rstrip("=")
record_line = f"pyclesperanto_cuda.libs/{soname},sha256={digest},{len(lib_data)}\n"

tmp = tempfile.mktemp(suffix=".whl", dir=dest_dir)
with zipfile.ZipFile(whl, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename.endswith(".dist-info/RECORD"):
            data += record_line.encode()
        zout.writestr(item, data)
    zout.writestr(f"pyclesperanto_cuda.libs/{soname}", lib_data)

os.replace(tmp, whl)
print(f"Injected {soname} into {os.path.basename(whl)}")
PYEOF