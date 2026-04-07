cmake_minimum_required(VERSION 3.20)

project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

# The compiled module is always _pyclesperanto, installed into pyclesperanto_metal/
set(PY_PACKAGE_NAME "pyclesperanto_metal")
set(CY_PACKAGE_NAME "_pyclesperanto")

## flags and options
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_LIBCPP_DISABLE_AVAILABILITY")
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU") # library linking for UNIX
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
endif()
set(CMAKE_SKIP_INSTALL_ALL_DEPENDENCY TRUE)
option(BUILD_TESTING  OFF)
option(BUILD_BENCHMARK  OFF)
option(BUILD_SHARED_LIBS OFF)

# Hide all internal C++ symbols so that CLIc symbols statically linked into this
# .so do not collide with those in the other backend .so (e.g. cuda).
# pybind11 already marks PyInit_* with __attribute__((visibility("default"))).
set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN YES)


## CLIc dependency
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/../../pyclesperanto/_version.py" VERSION_FILE_CONTENT)
string(REGEX MATCH "CLIC_VERSION = \"([^\"]+)\"" _ ${VERSION_FILE_CONTENT})
set(CLIC_REPO_TAG ${CMAKE_MATCH_1})
set(CLIC_REPO_URL "https://github.com/clEsperanto/CLIc.git")
# if not set, set the default build type to Release
set(CLE_BACKEND "METAL" CACHE STRING "Backend to use (CUDA or OCL)")
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../../src/clic ${CMAKE_CURRENT_BINARY_DIR}/clic EXCLUDE_FROM_ALL)


## look for python
set(Python_FIND_VIRTUALENV "FIRST")
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

## list of files to compile and folder to include
set(PACKAGE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/${PY_PACKAGE_NAME})
set(WRAPPER_DIR ${CMAKE_CURRENT_SOURCE_DIR}/../../src/wrapper)
file(GLOB_RECURSE WRAPPER_SOURCES_FILES ${WRAPPER_DIR}/*.cpp)


## build the python package
if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
  find_package(pybind11 CONFIG REQUIRED)
  python_add_library(${CY_PACKAGE_NAME} MODULE ${WRAPPER_SOURCES_FILES} WITH_SOABI)

  target_link_libraries(${CY_PACKAGE_NAME} PRIVATE CLIc::CLIc pybind11::headers)
  target_include_directories(${CY_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
  target_compile_definitions(${CY_PACKAGE_NAME} PRIVATE VERSION_INFO=${PROJECT_VERSION})

  # On Linux, hide all symbols from static archives and force internal symbol resolution
  # to prevent cross-module symbol interposition when both backend .so files are loaded.
  if(UNIX AND NOT APPLE)
      target_link_options(${CY_PACKAGE_NAME} PRIVATE "LINKER:--exclude-libs,ALL" "LINKER:-Bsymbolic")
  endif()

  # Install the target to the appropriate location
  install(TARGETS ${CY_PACKAGE_NAME} DESTINATION ${PY_PACKAGE_NAME})

  # Configure the RPATH based on the platform
  if(APPLE)
      set(CY_PACKAGE_RPATH "@loader_path;@loader_path/${CMAKE_INSTALL_LIBDIR};@loader_path/${CMAKE_INSTALL_BINDIR}")
  elseif(WIN32)
      set(CY_PACKAGE_RPATH ".;@ORIGIN/${CMAKE_INSTALL_LIBDIR};@ORIGIN/${CMAKE_INSTALL_BINDIR}")
  else()
      set(CY_PACKAGE_RPATH "$ORIGIN;$ORIGIN/${CMAKE_INSTALL_LIBDIR};$ORIGIN/${CMAKE_INSTALL_BINDIR}")
  endif()
  set_target_properties(${CY_PACKAGE_NAME} PROPERTIES
      INSTALL_RPATH "${CY_PACKAGE_RPATH}"
      BUILD_WITH_INSTALL_RPATH TRUE
      INSTALL_RPATH_USE_LINK_PATH TRUE
  )
endif()
