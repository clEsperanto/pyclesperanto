# Set minimum version of CMake.
cmake_minimum_required(VERSION 3.20)

# Set project name and version
project(pyClesperanto)# VERSION "0.6.2")

# Compilation tag for CLIc library linking
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
endif()
set(CMAKE_CXX_STANDARD 17) # Use C++17
set(CMAKE_CXX_STANDARD_REQUIRED ON) # Require (at least) it

# find required package
set(Python_FIND_VIRTUALENV "FIRST") # look for python in virtual env or conda first before checking the system.
find_package(Python3 COMPONENTS Interpreter Development.Embed Development.Module)

if(Python3_Development.Module_FOUND)
    message(STATUS "Python Developement Module found")
endif()

if(Python3_Development.Embed_FOUND)
    message(STATUS "Python Developement Embed found")
endif()

message(STATUS "OpenCL_FOUND: ${OpenCL_FOUND}")
message(STATUS "OpenCL_LIBRARY: ${OpenCL_LIBRARY}")
message(STATUS "OpenCL_LIBRARIES: ${OpenCL_LIBRARIES}")

# include_directories(SYSTEM ${Python3_INCLUDE_DIRS})
# find opencl icd-loader in virtual environment
# file(GLOB PYTHON_OpenCL_LIBRARY ${Python3_LIBRARY_DIRS}/libOpenCL.so)
# if(PYTHON_OpenCL_LIBRARY STREQUAL "")
#     message(STATUS "WARNING: No ICD found in virtual environment, searching for system ICD.")
# else()
#     message(STATUS ${PYTHON_OpenCL_LIBRARY})
#     set(OpenCL_LIBRARIES ${PYTHON_OpenCL_LIBRARY})
#     set(OpenCL_LIBRARY ${PYTHON_OpenCL_LIBRARY})
#     set(OpenCL_FOUND TRUE)
# endif()

# Compile CLIc Back-end library
add_subdirectory(CLIc)

# extra steps for scikit-build to find pybind11
if(DEFINED SKBUILD)
    # call pybind11-config to obtain the root of the cmake package
    execute_process(COMMAND ${PYTHON_EXECUTABLE} -m pybind11 --cmakedir
        OUTPUT_VARIABLE pybind11_ROOT_RAW)
    string(STRIP ${pybind11_ROOT_RAW} pybind11_ROOT)
endif()

set(PACKAGE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pyclesperanto)
set(WRAPPER_DIR ${CMAKE_CURRENT_SOURCE_DIR}/wrapper)
file(GLOB_RECURSE WRAPPER_SOURCES_FILES ${WRAPPER_DIR}/*.cpp)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_pyclesperanto MODULE ${WRAPPER_SOURCES_FILES})

target_link_libraries(_pyclesperanto PRIVATE CLIc::CLIc)
add_dependencies(_pyclesperanto CLIc)
target_include_directories(_pyclesperanto PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
target_compile_definitions(_pyclesperanto PRIVATE VERSION_INFO=${PROJECT_VERSION})

# Installing the extension module to the root of the package
install(TARGETS _pyclesperanto DESTINATION .)

if(APPLE)
    set_target_properties(
        _pyclesperanto PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR}")
else()
    set_target_properties(_pyclesperanto PROPERTIES INSTALL_RPATH
        "$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
endif()
