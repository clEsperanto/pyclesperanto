# Set minimum version of CMake.
cmake_minimum_required(VERSION 3.20)

# Set project name and version
# - package version is managed in file `version.py`
project(pyClesperanto)

# enforce release build type if possible
set(CMAKE_BUILD_TYPE Release)

if(NOT DEFINED BUILD_OCL_BACKEND)
  set(BUILD_OCL_BACKEND ON)
endif()
if(NOT DEFINED BUILD_CUDA_BACKEND)
  set(BUILD_CUDA_BACKEND ON)
endif()

string(TOLOWER ${PROJECT_NAME} PY_PACKAGE_NAME)
# set(CY_PACKAGE_NAME _${PY_PACKAGE_NAME})

# Compilation tag for CLIc library linking for UNIX
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
endif()

# find python dev library
# look for python in virtual env or conda first before checking the system.
set(Python_FIND_VIRTUALENV "FIRST")
find_package(Python3 COMPONENTS Interpreter Development.Embed Development.Module)
if(Python3_Development.Module_FOUND)
    message(STATUS "Python Developement Module found")
endif()
if(Python3_Development.Embed_FOUND)
    message(STATUS "Python Developement Embed found")
endif()

# if (BUILD_OCL_BACKEND)
#   if (DEFINED OpenCL_LIBRARIES AND DEFINED OpenCL_INCLUDE_DIRS)
#       set(OpenCL_FOUND true)
#   else()
#       find_package(OpenCL REQUIRED)
#   endif()
# endif()
# if (BUILD_CUDA_BACKEND)
#   find_package(CUDAToolkit REQUIRED)
# endif()

## fetch CLIc using CMake FetchContent
include(FetchContent)
option(BUILD_TESTING  OFF)
option(BUILD_BENCHMARK  OFF)
FetchContent_Declare(
  CLIc_lib 
  GIT_REPOSITORY https://github.com/clEsperanto/CLIc_prototype.git
  GIT_TAG add-cuda-backend
)
FetchContent_MakeAvailable(CLIc_lib)

if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()

set(PACKAGE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/${PY_PACKAGE_NAME})
set(WRAPPER_DIR ${CMAKE_CURRENT_SOURCE_DIR}/wrapper)
file(GLOB_RECURSE WRAPPER_SOURCES_FILES ${WRAPPER_DIR}/*.cpp)

# build pure ocl version
include(${PROJECT_SOURCE_DIR}/scripts/ocl_build.cmake)
# build pure cuda version
include(${PROJECT_SOURCE_DIR}/scripts/cuda_build.cmake)
# build cuda-ocl version
include(${PROJECT_SOURCE_DIR}/scripts/all_build.cmake)

# find_package(pybind11 CONFIG REQUIRED)
# pybind11_add_module(${CY_PACKAGE_NAME} MODULE ${WRAPPER_SOURCES_FILES})
# target_link_libraries(${CY_PACKAGE_NAME} PRIVATE CLIc::CLIc)
# # if(BUILD_OCL_BACKEND AND OpenCL_FOUND)
# #   target_link_libraries(${CY_PACKAGE_NAME} PRIVATE OpenCL::OpenCL)  
# # endif(OpenCL_FOUND)
# # if(BUILD_CUDA_BACKEND AND CUDAToolkit_FOUND)
# #   target_link_libraries(${CY_PACKAGE_NAME} PRIVATE CUDA::cudart CUDA::cuda_driver CUDA::nvrtc CUDA::OpenCL) 
# # endif()
# add_dependencies(${CY_PACKAGE_NAME} CLIc)
# target_include_directories(${CY_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
# target_compile_features(${CY_PACKAGE_NAME} PRIVATE cxx_std_17)
# # Installing the extension module to the root of the package
# install(TARGETS ${CY_PACKAGE_NAME} DESTINATION .)
# if(APPLE)
#     set_target_properties(
#         ${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR}")
# else()
#     set_target_properties(${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH
#         "$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
# endif()

if(APPLE)
    set_target_properties(
        ${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR};${CMAKE_PREFIX_PATH}/lib" INSTALL_RPATH_USE_LINK_PATH TRUE)
else()
    set_target_properties(${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH
        "$ORIGIN/${CMAKE_INSTALL_LIBDIR}:$ORIGIN/../lib:${CMAKE_PREFIX_PATH}/lib"
        INSTALL_RPATH_USE_LINK_PATH TRUE)
endif()
