message(STATUS "Building OCL version --------")

set(CY_OCL_PACKAGE_NAME _ocl_clesperanto)

set(BUILD_CUDA_BACKEND OFF)
set(BUILD_OCL_BACKEND ON)
if (DEFINED OpenCL_LIBRARIES AND DEFINED OpenCL_INCLUDE_DIRS)
    set(OpenCL_FOUND true)
else()
    find_package(OpenCL REQUIRED)
endif()

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(${CY_OCL_PACKAGE_NAME} MODULE ${WRAPPER_SOURCES_FILES})

target_link_libraries(${CY_OCL_PACKAGE_NAME} PRIVATE CLIc::CLIc)
add_dependencies(${CY_OCL_PACKAGE_NAME} CLIc)
target_include_directories(${CY_OCL_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
target_compile_features(${CY_OCL_PACKAGE_NAME} PRIVATE cxx_std_17)

# Installing the extension module to the root of the package
install(TARGETS ${CY_OCL_PACKAGE_NAME} DESTINATION .)