#ifndef __WRAPPER_PYCLESPERANTO_HPP
#define __WRAPPER_PYCLESPERANTO_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto init_pygateway(const pybind11::module_ &module) -> void;
auto init_pyimage(const pybind11::module_ &module) -> void;

#endif // __WRAPPER_PYCLESPERANTO_HPP
