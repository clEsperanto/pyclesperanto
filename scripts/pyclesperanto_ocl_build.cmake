message(STATUS "Building OCL version --------")

set(CY_PACKAGE_NAME _ocl_clesperanto)

set(BUILD_CUDA_BACKEND OFF)
set(BUILD_OCL_BACKEND ON)
if (DEFINED OpenCL_LIBRARIES AND DEFINED OpenCL_INCLUDE_DIRS)
    set(OpenCL_FOUND true)
else()
    find_package(OpenCL REQUIRED)
endif()

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(${CY_PACKAGE_NAME} MODULE ${WRAPPER_SOURCES_FILES})

# # add_definitions(-DCY_PACKAGE_NAME=${CY_PACKAGE_NAME})
# add_compile_definitions(
#     # $<$<BOOL:${BUILD_CUDA_BACKEND}>:BUILD_CUDA_BACKEND>
#     $<$<BOOL:${BUILD_OCL_BACKEND}>:BUILD_OCL_BACKEND>
# )

target_link_libraries(${CY_PACKAGE_NAME} PRIVATE CLIc::CLIc)
if(BUILD_OCL_BACKEND AND OpenCL_FOUND)
  target_link_libraries(${CY_PACKAGE_NAME} PRIVATE OpenCL::OpenCL)  
endif()
add_dependencies(${CY_PACKAGE_NAME} CLIc)
target_include_directories(${CY_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
target_compile_features(${CY_PACKAGE_NAME} PRIVATE cxx_std_17)
# set_target_properties(${CY_PACKAGE_NAME} PROPERTIES OUTPUT_NAME ${CY_PACKAGE_NAME})

# Installing the extension module to the root of the package
install(TARGETS ${CY_PACKAGE_NAME} DESTINATION .)

if(APPLE)
    set_target_properties(
        ${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR};${CMAKE_PREFIX_PATH}/lib" INSTALL_RPATH_USE_LINK_PATH TRUE)
else()
    set_target_properties(${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH
        "$ORIGIN/${CMAKE_INSTALL_LIBDIR}:$ORIGIN/../lib:${CMAKE_PREFIX_PATH}/lib"
        INSTALL_RPATH_USE_LINK_PATH TRUE)
endif()