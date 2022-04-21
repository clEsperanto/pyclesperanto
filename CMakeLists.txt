# Set minimum version of CMake.
cmake_minimum_required(VERSION 3.20)

# Set project name and version
project(pyClesperanto VERSION 0.2.0)

# Compilation tag for CLIc library linking
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -fvisibility=hidden")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC -fvisibility=hidden")

# find required package
set(Python_FIND_VIRTUALENV "FIRST") # look for python in virtual env or conda first before checking the system.
find_package(Python COMPONENTS Interpreter Development REQUIRED)

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

# split c++ stand-alone build from python wrapper build with scikit-build
if(DEFINED SKBUILD)

    set(ignoreMe "${SKBUILD}")
    set(PY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pyclesperanto)

    file(GLOB_RECURSE PY_SOURCES_FILES ${PY_DIR}/*.cpp) 

    # call pybind11-config to obtain the root of the cmake package
    execute_process(COMMAND ${PYTHON_EXECUTABLE} -m pybind11 --cmakedir
                    OUTPUT_VARIABLE pybind11_ROOT_RAW)
    string(STRIP ${pybind11_ROOT_RAW} pybind11_ROOT)
    find_package(pybind11)

    pybind11_add_module(_pyclesperanto MODULE ${PY_SOURCES_FILES})
    target_link_libraries(_pyclesperanto PRIVATE CLIc)
    add_dependencies(_pyclesperanto CLIc)
    target_include_directories(_pyclesperanto PUBLIC "$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/pyclesperanto/>")

    # Installing the extension module to the root of the package
    install(TARGETS _pyclesperanto DESTINATION .)

    configure_file("${PROJECT_SOURCE_DIR}/pyclesperanto/__main__.py.in"
                   "${PROJECT_BINARY_DIR}/pyclesperanto/__main__.py")

    install(FILES "${PROJECT_BINARY_DIR}/pyclesperanto/__main__.py" DESTINATION .)

    if(APPLE)
        set_target_properties(
            _pyclesperanto PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR}")
    else()
        set_target_properties(_pyclesperanto PROPERTIES INSTALL_RPATH
            "$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
    endif()

endif()