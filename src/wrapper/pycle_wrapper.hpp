#ifndef __WRAPPER_PYCLESPERANTO_HPP
#define __WRAPPER_PYCLESPERANTO_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto types_(pybind11::module_ &module) -> void;
auto core_(pybind11::module_ &module) -> void;
auto array_(pybind11::module_ &module) -> void;
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
