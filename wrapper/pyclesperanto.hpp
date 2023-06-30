#ifndef __WRAPPER_PYCLESPERANTO_HPP
#define __WRAPPER_PYCLESPERANTO_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto wrapper_types(pybind11::module_ &module) -> void;
auto wrapper_backend(pybind11::module_ &module) -> void;
auto wrapper_array(pybind11::module_ &module) -> void;

auto wrapper_tier1(pybind11::module_ &module) -> void;
auto wrapper_tier2(pybind11::module_ &module) -> void;

#endif // __WRAPPER_PYCLESPERANTO_HPP
