#ifndef __WRAPPER_PYCLESPERANTO_HPP
#define __WRAPPER_PYCLESPERANTO_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

// Release the GIL during CLIc calls, build with -DPYCLE_NO_GIL_RELEASE to keep it held.
// PYCLE_RELEASE_GIL is a pybind11 extra for bindings whose arguments are all C++ types.
// PYCLE_RELEASE_GIL_SCOPE releases until the end of the enclosing scope, for bindings that
// must first convert Python arguments: no Python API may be used after it in that scope.
#ifndef PYCLE_NO_GIL_RELEASE
#  define PYCLE_RELEASE_GIL       pybind11::call_guard<pybind11::gil_scoped_release>()
#  define PYCLE_RELEASE_GIL_SCOPE pybind11::gil_scoped_release pycle_gil_release_
#else
#  define PYCLE_RELEASE_GIL       pybind11::call_guard<>()
#  define PYCLE_RELEASE_GIL_SCOPE (void)0
#endif

auto types_(pybind11::module_ &module) -> void;
auto core_(pybind11::module_ &module) -> void;
auto array_(pybind11::module_ &module) -> void;
auto transform_(pybind11::module_ &module) -> void;
auto fft_(pybind11::module_ &module) -> void;
auto execute_(pybind11::module_ &module) -> void;

auto tier1_(pybind11::module_ &module) -> void;
auto tier2_(pybind11::module_ &module) -> void;
auto tier3_(pybind11::module_ &module) -> void;
auto tier4_(pybind11::module_ &module) -> void;
auto tier5_(pybind11::module_ &module) -> void;
auto tier6_(pybind11::module_ &module) -> void;
auto tier7_(pybind11::module_ &module) -> void;
auto tier8_(pybind11::module_ &module) -> void;

#endif // __WRAPPER_PYCLESPERANTO_HPP
