cmake_minimum_required(VERSION 3.20)

# Convenience top-level CMakeLists for developers
# Use: pip install -e ./backends/opencl -v  (or ./backends/cuda)
add_subdirectory(backends/opencl)
# add_subdirectory(backends/cuda)