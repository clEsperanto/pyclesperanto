# Conda Recipes for pyclesperanto

## Option A: Separate recipes

### Recipe 1: `pyclesperanto-opencl`

```yaml
package:
  name: pyclesperanto-opencl
  version: "0.21.0"

source:
  git_url: https://github.com/clEsperanto/pyclesperanto.git
  git_rev: main

build:
  script: pip install ./backends/opencl -v

requirements:
  build:
    - cmake
    - ninja
    - {{ compiler('cxx') }}
  host:
    - python
    - pip
    - scikit-build-core
    - pybind11
    - opencl-headers
    - ocl-icd          # [linux]
  run:
    - python
    - ocl-icd          # [linux]
```

### Recipe 2: `pyclesperanto-cuda`

```yaml
package:
  name: pyclesperanto-cuda
  version: "0.21.0"

source:
  git_url: https://github.com/clEsperanto/pyclesperanto.git
  git_rev: main

build:
  script: pip install ./backends/cuda -v
  skip: true  # [osx]

requirements:
  build:
    - cmake
    - ninja
    - {{ compiler('cxx') }}
  host:
    - python
    - pip
    - scikit-build-core
    - pybind11
    - cuda-nvcc
    - cuda-cudart-dev
    - cuda-nvrtc-dev
    - libnvjitlink-dev
  run:
    - python
    - cuda-cudart
    - cuda-nvrtc
    - libnvjitlink
```

### Recipe 3: `pyclesperanto`

```yaml
package:
  name: pyclesperanto
  version: "0.21.0"

source:
  git_url: https://github.com/clEsperanto/pyclesperanto.git
  git_rev: main

build:
  script: pip install . -v
  noarch: python

requirements:
  host:
    - python
    - pip
    - hatchling
  run:
    - python
    - numpy
    - toolz
    - matplotlib
```

## Option B: Single recipe with multiple outputs (preferred for conda-forge)

```yaml
source:
  git_url: https://github.com/clEsperanto/pyclesperanto.git
  git_rev: main

outputs:
  - name: pyclesperanto-opencl
    build:
      script: pip install ./backends/opencl -v
    requirements:
      build:
        - cmake
        - ninja
        - {{ compiler('cxx') }}
      host:
        - python
        - pip
        - scikit-build-core
        - pybind11
        - opencl-headers
        - ocl-icd          # [linux]
      run:
        - python
        - ocl-icd          # [linux]

  - name: pyclesperanto-cuda
    build:
      script: pip install ./backends/cuda -v
      skip: true  # [osx]
    requirements:
      build:
        - cmake
        - ninja
        - {{ compiler('cxx') }}
      host:
        - python
        - pip
        - scikit-build-core
        - pybind11
        - cuda-nvcc
        - cuda-cudart-dev
        - cuda-nvrtc-dev
        - libnvjitlink-dev
      run:
        - python
        - cuda-cudart
        - cuda-nvrtc
        - libnvjitlink

  - name: pyclesperanto
    build:
      script: pip install . -v
      noarch: python
    requirements:
      host:
        - python
        - pip
        - hatchling
      run:
        - python
        - numpy
        - toolz
        - matplotlib
```

## Notes

- CUDA output uses `skip: true # [osx]` to skip macOS builds
- CUDA runtime packages (`cuda-cudart`, `cuda-nvrtc`, `libnvjitlink`) are in `run` deps so they're available at runtime
- The root `pyclesperanto` package is `noarch: python` and doesn't depend on either backend — users install the backend they need separately (e.g. `conda install pyclesperanto pyclesperanto-opencl`)
