# Set minimum version of CMake.
cmake_minimum_required(VERSION 3.20)

# Set project name and version
# - package version is managed in file `version.py`
project(pyClesperanto)

set(CMAKE_BUILD_TYPE Release)

string(TOLOWER ${PROJECT_NAME} PY_PACKAGE_NAME)
set(CY_PACKAGE_NAME _${PY_PACKAGE_NAME})

message(STATUS "Package: ${PY_PACKAGE_NAME}")
message(STATUS "C++ Module: ${CY_PACKAGE_NAME}")

# Compilation tag for CLIc library linking for UNIX
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
endif()
# set(CMAKE_CXX_STANDARD 17) # Use C++17
set(CMAKE_CXX_STANDARD_REQUIRED ON) # Require (at least) it

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

message(STATUS "OpenCL_FOUND: ${OpenCL_FOUND}")
message(STATUS "OpenCL_LIBRARY: ${OpenCL_LIBRARY}")
message(STATUS "OpenCL_LIBRARIES: ${OpenCL_LIBRARIES}")

# CMake Warning:
#   Manually-specified variables were not used by the project:
#     PYTHON_INCLUDE_DIR
#     PYTHON_LIBRARY
#     PYTHON_VERSION_STRING
#     Python_EXECUTABLE
#     Python_INCLUDE_DIR
#     Python_LIBRARY

# Define CLIc Backend library
option(BUILD_TESTING  OFF)
add_subdirectory(CLIc)

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

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(${CY_PACKAGE_NAME} MODULE ${WRAPPER_SOURCES_FILES})

target_link_libraries(${CY_PACKAGE_NAME} PRIVATE CLIc::CLIc)
add_dependencies(${CY_PACKAGE_NAME} CLIc)
target_include_directories(${CY_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
target_compile_features(${CY_PACKAGE_NAME} PRIVATE cxx_std_17)

# Installing the extension module to the root of the package
install(TARGETS ${CY_PACKAGE_NAME} DESTINATION .)

if(APPLE)
    set_target_properties(
        ${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH "@loader_path/${CMAKE_INSTALL_LIBDIR}")
else()
    set_target_properties(${CY_PACKAGE_NAME} PROPERTIES INSTALL_RPATH
        "$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
endif()
