# Test Organization

The test suite has been organized into 12 functional categories for easier management and navigation.

## Test Categories

| Category | Files | Purpose |
|----------|-------|---------|
| **arithmetic** | 26 | Basic arithmetic operations (add, subtract, multiply, divide, power, etc.) |
| **comparison** | 12 | Comparison operations (equal, greater, smaller, not_equal) |
| **morphology** | 11 | Morphological operations (erosion, dilation, smoothing, max/min box/sphere) |
| **labeling** | 12 | Labeling algorithms (Voronoi, Otsu, connected components, Gauss) |
| **filtering** | 10 | Filtering operations (Gaussian blur, Sobel, convolution, derivatives) |
| **statistics** | 16 | Statistical operations (mean, variance, reduction, histogram) |
| **shape** | 15 | Shape transformations (transpose, crop, flip, affine, ramp) |
| **detection** | 9 | Feature detection (maxima, minima, edges) |
| **array** | 27 | Array operations (indexing, slicing, concatenation, masking) |
| **label_operations** | 14 | Label-specific operations (bounding box, pixelcount, spots) |
| **api** | 11 | API and core functionality (import, device management, execution) |
| **other** | 10 | Miscellaneous tests |

**Total: 174 test files**

## Running Tests

```bash
# Run all tests (parametrized tests run on all available backends)
pixi run test

# Run tests from a specific category
pixi run test tests/arithmetic/

# Run a specific test file
pixi run test tests/arithmetic/test_add_images.py

# Run only on OpenCL backend
pixi run test -k opencl

# Run only on CUDA backend
pixi run test -k cuda

# Run with verbose output to see which backend each test uses
pixi run test -v
```

## Multi-Backend Testing

Tests marked with `@pytest.mark.backend` are automatically parametrized to run on all available GPU backends. See [BACKENDS.md](BACKENDS.md) for detailed information on how to use backend fixtures and markers.

## Structure

```
tests/
├── arithmetic/          # 26 files
├── comparison/          # 12 files
├── morphology/          # 11 files
├── labeling/            # 12 files
├── filtering/           # 10 files
├── statistics/          # 16 files
├── shape/               # 15 files
├── detection/           # 9 files
├── array/               # 27 files
├── label_operations/    # 14 files
├── api/                 # 11 files
├── other/               # 10 files
└── _test_*.cl           # OpenCL test kernels
```

## Notes

- Pytest automatically discovers test files in all subdirectories
- Test configuration remains in `pyproject.toml`
- All tests maintain backward compatibility
- The organization follows the functional grouping of operations in pyclesperanto
