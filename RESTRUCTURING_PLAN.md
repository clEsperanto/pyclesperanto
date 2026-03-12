# Multi-Backend Restructuring Plan

## Overview

Split into **3 packages** in a monorepo:

| Package | Type | Install via |
|---|---|---|
| `pyclesperanto` | Pure Python (no C++) | `pip install pyclesperanto` |
| `pyclesperanto-opencl` | C++ extension (OpenCL) | `pip install pyclesperanto[opencl]` |
| `pyclesperanto-cuda` | C++ extension (CUDA) | `pip install pyclesperanto[cuda]` |

---

## Phase 1 — Repository Structure

**New directory layout:**

```
pyclesperanto/                          # Repo root
├── pyproject.toml                      # MODIFIED → pure Python package
├── CMakeLists.txt                      # KEPT for local dev convenience
├── pyclesperanto/                      # Python source
│   ├── __init__.py                     # MODIFIED
│   ├── _backend.py                     # ★ NEW
│   ├── _core.py                        # MODIFIED
│   ├── _array.py                       # MODIFIED
│   ├── _execute.py                     # MODIFIED
│   ├── _utils.py                       # MODIFIED
│   ├── _tier1.py … _tier8.py           # MODIFIED (auto-generated, template change)
│   └── … (rest unchanged)
├── backends/
│   ├── opencl/
│   │   ├── pyproject.toml              # ★ NEW — pyclesperanto-opencl
│   │   ├── CMakeLists.txt              # ★ NEW — refs ../../src/
│   │   └── pyclesperanto_opencl/
│   │       └── __init__.py             # ★ NEW
│   └── cuda/
│       ├── pyproject.toml              # ★ NEW — pyclesperanto-cuda
│       ├── CMakeLists.txt              # ★ NEW — refs ../../src/
│       └── pyclesperanto_cuda/
│           └── __init__.py             # ★ NEW
├── src/                                # UNCHANGED — shared C++ sources
│   ├── clic/CMakeLists.txt
│   └── wrapper/*.cpp, *.hpp
├── scripts/
│   ├── build-opencl-linux.sh           # UNCHANGED
│   ├── build-opencl-windows.sh         # UNCHANGED
│   └── build-cuda-linux.sh             # ★ NEW (if needed for cibuildwheel)
└── .github/workflows/
    ├── build.yml                       # MODIFIED
    └── deploy.yml                      # MODIFIED — builds 3 packages
```

---

## Phase 2 — Main Package (`pyproject.toml`)

Convert from a scikit-build-core C++ package to a **pure Python package**:

- **Build backend**: `setuptools` (or `hatchling`) — no more scikit-build-core
- **Remove**: cmake/pybind11/ninja from build requirements
- **Add optional dependencies**:
  ```toml
  [project.optional-dependencies]
  opencl = ["pyclesperanto-opencl"]
  cuda = ["pyclesperanto-cuda"]
  all = ["pyclesperanto-opencl", "pyclesperanto-cuda"]
  ```
- **Move cibuildwheel config** out of root pyproject (it belongs in backend configs now)
- **Version**: switch from regex-in-`_version.py` to a simpler mechanism (e.g. `version = "0.20.0"` directly, or keep dynamic with setuptools)

---

## Phase 3 — Backend Packages

Each backend gets its own `pyproject.toml` + `CMakeLists.txt`.

**`backends/opencl/pyproject.toml`:**
- Package name: `pyclesperanto-opencl`
- Build system: scikit-build-core + pybind11
- Installs into: `pyclesperanto_opencl/`
- CMake defines: `CLE_BACKEND=OPENCL` hardcoded
- Version: synced with main package (read from shared `_version.py`)
- cibuildwheel config: moved here from root

**`backends/cuda/pyproject.toml`:**
- Same structure, `CLE_BACKEND=CUDA`
- cibuildwheel config: CUDA-specific (needs CUDA toolkit, different platform matrix, skip macOS) @ToDo

**`backends/*/CMakeLists.txt`:**
- Based on current root CMakeLists.txt
- References shared sources: `../../src/clic/` and `../../src/wrapper/`
- Module name matches package: `_pyclesperanto` installed into `pyclesperanto_opencl/` or `pyclesperanto_cuda/`

**`backends/*/pyclesperanto_*/\__init__.py`:**
- Thin re-export: `from ._pyclesperanto import *`
- Exposes a `BACKEND_NAME = "opencl"` or `"cuda"` constant

---

## Phase 4 — New `_backend.py` Module

Central backend detection and loading. This is the **hardest/most critical** piece:

```python
# pyclesperanto/_backend.py

_opencl_module = None
_cuda_module = None
_active_backend = None

def _detect_backends():
    """Try importing each backend package."""
    global _opencl_module, _cuda_module
    try:
        import pyclesperanto_opencl
        _opencl_module = pyclesperanto_opencl._pyclesperanto
    except ImportError:
        pass
    try:
        import pyclesperanto_cuda
        _cuda_module = pyclesperanto_cuda._pyclesperanto
    except ImportError:
        pass

def get_backend():
    """Return the active compiled backend module."""
    if _active_backend is None:
        raise RuntimeError(
            "No pyclesperanto backend installed.\n"
            "Install one with:\n"
            "  pip install pyclesperanto[opencl]   # for OpenCL\n"
            "  pip install pyclesperanto[cuda]     # for CUDA\n"
            "  pip install pyclesperanto[all]      # for both"
        )
    return _active_backend

def select_backend(name):
    """Switch between 'opencl' and 'cuda' backends."""
    ...

def list_available_backends():
    """Return list of installed backend names."""
    ...
```

All modules that currently do `from ._pyclesperanto import X` will instead do:
```python
from ._backend import get_backend
clic = get_backend()
# then use clic._Array, clic._execute, etc.
```

---

## Phase 5 — Python Module Updates

**Files that import `._pyclesperanto` (all need modification):**

| File | Current import | New import |
|---|---|---|
| `_core.py` | `from ._pyclesperanto import _BackendManager, _Device` | `from ._backend import get_backend` |
| `_array.py` | `from ._pyclesperanto import _Array as Array` | `from ._backend import get_backend` |
| `_execute.py` | `from ._pyclesperanto import _execute, ...` | `from ._backend import get_backend` |
| `_utils.py` | `importlib.import_module("._pyclesperanto", ...)` | `from ._backend import get_backend` |
| `_tier1.py` – `_tier8.py` | `importlib.import_module("._pyclesperanto", ...)` | `from ._backend import get_backend` |

**Key design decisions:**
- The `_Array` class comes from whichever backend is active — both backends expose the same C++ `_Array` class with identical API
- `select_backend()` in `_core.py` now also switches which compiled module is active via `_backend.py`
- The tier functions delegate to the active backend's tier bindings (they're all identically named)

**`__init__.py` changes:**
- Wrap `default_initialisation()` in a try/except that shows a friendly "no backend" message
- The import of tier modules should be lazy or guarded
- Import `select_backend` from `_backend.py` (not `_core.py`) — or have `_core.py` delegate

---

## Phase 6 — Auto-Generation Template Update

The `cle-roboto` tool auto-generates tier files (`_tier1.py`–`_tier8.py`). The template needs updating:

**Current** (in each tier file):
```python
clic = importlib.import_module("._pyclesperanto", package="pyclesperanto")
```

**New**:
```python
from ._backend import get_backend as _get_backend
```

And each function call changes from `clic._funcname(...)` to `_get_backend()._funcname(...)`.

> **Note**: This means coordinating with the `cle-roboto` tool's templates so future auto-updates generate the new import pattern. Until `cle-roboto` is updated, any auto-update will overwrite the tier files with the old pattern.

---

## Phase 7 — CI: Build Workflow (`build.yml`)

**Current**: Single matrix that builds the monolith package with OpenCL or CUDA.

**New structure**:
```yaml
jobs:
  build-opencl:
    # Build pyclesperanto-opencl from backends/opencl/
    # Install pyclesperanto from root
    # Run tests

  build-cuda:
    # Build pyclesperanto-cuda from backends/cuda/
    # Install pyclesperanto from root
    # Run tests (import only — no GPU in CI)

  build-no-backend:
    # Install pyclesperanto alone
    # Verify it imports and shows the "no backend" message
```

Build commands change to:
```bash
# Install main package
pip install .
# Install backend (from subdirectory)
pip install ./backends/opencl -v
```

---

## Phase 8 — CI: Deploy Workflow (`deploy.yml`)

This is the **most complex CI change**. Need to build and publish 3 packages:

```yaml
jobs:
  # 1. Build wheels for pyclesperanto-opencl
  build-opencl-wheels:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - uses: pypa/cibuildwheel@v3.4.0
        with:
          package-dir: backends/opencl
        # Uses scripts/build-opencl-linux.sh etc.

  # 2. Build wheels for pyclesperanto-cuda
  build-cuda-wheels:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]  # No macOS for CUDA
    steps:
      - uses: pypa/cibuildwheel@v3.4.0
        with:
          package-dir: backends/cuda
        # Needs CUDA toolkit installed before build

  # 3. Build sdist for pyclesperanto (pure Python)
  build-main-sdist:
    steps:
      - run: pipx run build --sdist  # From repo root

  # 4. Publish all to PyPI
  publish:
    needs: [build-opencl-wheels, build-cuda-wheels, build-main-sdist]
    # Upload 3 sets of artifacts to PyPI
```

**CUDA wheel challenges:**
- CUDA toolkit must be available during wheel build
- CUDA runtime libraries must be bundled in the wheel (or declared as dependency)
- macOS doesn't support CUDA → skip
- May need `nvidia-cuda-runtime-cu12` as a dependency instead of bundling
- `auditwheel`/`delocate` may need special handling for CUDA libs

---

## Phase 9 — Development Workflow Updates

**`pixi.toml` changes:**
```toml
[tasks]
build-ocl = "pip install -e . && pip install -e ./backends/opencl -v --config-settings=cmake.define.CLE_BACKEND=OPENCL"
build-cuda = "pip install -e . && pip install -e ./backends/cuda -v --config-settings=cmake.define.CLE_BACKEND=CUDA"
```

**Root `CMakeLists.txt`**: Keep as a convenience for developers who want a single `pip install -e . -v` build during development. Or remove and require backend-specific builds.

---

## Phase 10 — `cle-roboto` Auto-Update Workflow

`auto-update.yml` currently regenerates tier files. Needs updating to:
1. Generate tier files with the new import pattern (`_backend.get_backend()` instead of `._pyclesperanto`)
2. Or: update the `cle-roboto` tool's template first

---

## Execution Order (recommended)

| Step | Description | Difficulty | Risk |
|---|---|---|---|
| 1 | Create `_backend.py` | Medium | Low — additive |
| 2 | Update Python imports (`_core`, `_array`, `_execute`, `_utils`, tiers) | Medium | Medium — touches all modules |
| 3 | Create backend package structures (`backends/opencl/`, `backends/cuda/`) | Medium | Low |
| 4 | Convert root `pyproject.toml` to pure Python | Low | Medium — changes build system |
| 5 | Update `pixi.toml` dev tasks | Low | Low |
| 6 | Update `build.yml` CI | Medium | Low |
| 7 | Update `deploy.yml` CI | High | High — CUDA wheel builds are complex |
| 8 | Update `auto-update.yml` / `cle-roboto` template | Medium | Medium |
| 9 | Test all combinations (no backend, opencl, cuda, both) | — | — |
| 10 | Version coordination strategy across 3 packages | Low | Medium |

---

## Open Questions to Decide

1. **Version coupling**: Should all 3 packages share the same version number? (Recommended: yes, from shared `_version.py`). <-- share the same version!
2. **CUDA runtime dependency**: Bundle CUDA libs in wheel vs. require `nvidia-*` pip packages as dependencies? <-- we are not responsible for the CUDA lib, it should be already install on the user system
3. **sdist for backend packages**: Support building from sdist, or wheels-only? (Wheels-only is simpler for C++ packages) <-- use what is the best and simple, wheels-only
4. **Root CMakeLists.txt**: Keep for dev convenience or remove to avoid confusion? <-- remove to avoid confusion
5. **`cle-roboto` updates**: Update the tool's template before or after this migration? (Before is cleaner but adds a dependency) <-- I will deal with that 
6. **Minimum CUDA version**: Which CUDA versions to support? (12.x only, or also 11.x?) <-- 12.x only
