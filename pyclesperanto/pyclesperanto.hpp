#ifndef __pyclesperanto_h
#define __pyclesperanto_h


#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>

void init_pygpu(pybind11::module_ &);
void init_pydata(pybind11::module_ &);
void init_pytier1(pybind11::module_ &);
void init_pytier2(pybind11::module_ &);
void init_pytier3(pybind11::module_ &);
void init_pytier4(pybind11::module_ &);

#endif // __pyclesperanto_h