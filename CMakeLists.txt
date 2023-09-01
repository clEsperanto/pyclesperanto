# Set minimum version of CMake.
cmake_minimum_required(VERSION 3.20)

# Set project name and version
# - package version is managed in file `version.py`
project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

# enforce release build type if possible
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_LIBCPP_DISABLE_AVAILABILITY")
# if(WIN32)
#   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /d2FH4-")
# endif(WIN32)

string(TOLOWER ${PROJECT_NAME} PY_PACKAGE_NAME)
set(CY_PACKAGE_NAME _${PY_PACKAGE_NAME})

# Compilation tag for CLIc library linking for UNIX
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
endif()

# find python dev library
# look for python in virtual env or conda first before checking the system.
set(Python_FIND_VIRTUALENV "FIRST")
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

## fetch CLIc using CMake FetchContent
include(FetchContent)
option(BUILD_TESTING  OFF)
option(BUILD_BENCHMARK  OFF)
option(BUILD_SHARED_LIBS OFF)
FetchContent_Declare(
  CLIc 
  GIT_REPOSITORY https://github.com/clEsperanto/CLIc_prototype.git
  GIT_TAG 0.7.1
)
FetchContent_MakeAvailable(CLIc)

set(PACKAGE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/${PY_PACKAGE_NAME})
set(WRAPPER_DIR ${CMAKE_CURRENT_SOURCE_DIR}/wrapper)
file(GLOB_RECURSE WRAPPER_SOURCES_FILES ${WRAPPER_DIR}/*.cpp)

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
  add_dependencies(${CY_PACKAGE_NAME} CLIc)
  target_include_directories(${CY_PACKAGE_NAME} PUBLIC "$<BUILD_INTERFACE:${WRAPPER_DIR}>")
  target_compile_definitions(${CY_PACKAGE_NAME} PRIVATE VERSION_INFO=${PROJECT_VERSION})

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
