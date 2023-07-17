message(STATUS "Building CUDA version -------")

set(CY_CUDA_PACKAGE_NAME _cuda_clesperanto)

set(BUILD_CUDA_BACKEND ON)
set(BUILD_OCL_BACKEND OFF)
find_package(CUDAToolkit REQUIRED)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(${CY_CUDA_PACKAGE_NAME} MODULE ${WRAPPER_SOURCES_FILES})

target_link_libraries(${CY_CUDA_PACKAGE_NAME} PRIVATE CLIc::CLIc)
add_dependencies(${CY_CUDA_PACKAGE_NAME} CLIc)
target_include_directories(${CY_CUDA_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
target_compile_features(${CY_CUDA_PACKAGE_NAME} PRIVATE cxx_std_17)

# Installing the extension module to the root of the package
install(TARGETS ${CY_CUDA_PACKAGE_NAME} DESTINATION .)