#ifndef __WRAPPER_PYCLESPERANTO_HPP
#define __WRAPPER_PYCLESPERANTO_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto init_cletypes(pybind11::module_ &module) -> void;
auto init_cleimage(pybind11::module_ &module) -> void;
auto init_cleprocessor(pybind11::module_ &module) -> void;
auto init_clememory(pybind11::module_ &module) -> void;

auto init_cletier1(pybind11::module_ &module) -> void;
auto init_cletier2(pybind11::module_ &module) -> void;
auto init_cletier3(pybind11::module_ &module) -> void;
auto init_cletier4(pybind11::module_ &module) -> void;
auto init_cletier5(pybind11::module_ &module) -> void;
auto init_cletier6(pybind11::module_ &module) -> void;

#endif // __WRAPPER_PYCLESPERANTO_HPP
