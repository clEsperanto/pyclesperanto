# Set minimum version of CMake.
cmake_minimum_required(VERSION 3.20)

# Set project name and version
project(pyClesperanto VERSION "0.6.0")

# Compilation tag for CLIc library linking
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")

# find required package
set(Python_FIND_VIRTUALENV "FIRST") # look for python in virtual env or conda first before checking the system.
find_package(Python3 COMPONENTS Interpreter Development.Module REQUIRED)

# message(NOTICE "Python include dirs: ${Python3_INCLUDE_DIRS}")
# include_directories(SYSTEM ${Python3_INCLUDE_DIRS})

# find opencl icd-loader in virtual environment
file(GLOB PYTHON_OpenCL_LIBRARY ${Python_LIBRARY_DIRS}/libOpenCL.so)

if(PYTHON_OpenCL_LIBRARY STREQUAL "")
    message(STATUS "WARNING: No ICD found in virtual environment.")
else()
    message(STATUS ${PYTHON_OpenCL_LIBRARY})
    set(OpenCL_LIBRARIES ${PYTHON_OpenCL_LIBRARY})
    set(OpenCL_LIBRARY ${PYTHON_OpenCL_LIBRARY})
    set(OpenCL_FOUND TRUE)
endif()

# Compile CLIc Back-end library
add_subdirectory(CLIc)

# # split c++ stand-alone build from python wrapper build with scikit-build
if(DEFINED SKBUILD)
    find_package(pybind11 CONFIG REQUIRED)
    set(ignoreMe "${SKBUILD}")
    set(PACKAGE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pyclesperanto)
    set(WRAPPER_DIR ${CMAKE_CURRENT_SOURCE_DIR}/wrapper)

    file(GLOB_RECURSE WRAPPER_SOURCES_FILES ${WRAPPER_DIR}/*.cpp)

    # call pybind11-config to obtain the root of the cmake package
    execute_process(COMMAND ${PYTHON_EXECUTABLE} -m pybind11 --cmakedir
        OUTPUT_VARIABLE pybind11_ROOT_RAW)
    string(STRIP ${pybind11_ROOT_RAW} pybind11_ROOT)

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
endif()
