#ifndef __gpu_h
#define __gpu_h

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
// #include <pybind11/stl.h>
// #include <pybind11/functional.h>

#include "cleGPU.hpp"
#include "cleObject.hpp"

// #include "pyclesperanto.hpp"

using namespace cle;


// todo: trampoline class for interface C++ python
// Should we do that for all wrapped class? (aka overlayer of wrapper)

class PyGPU : public GPU {
public:

    using GPU::GPU;

    using ndarray_f = pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>;
    // using ndarray_i = pybind11::array_t<int, pybind11::array::c_style | pybind11::array::forcecast>;
    // using ndarray_ui = pybind11::array_t<unsigned int, pybind11::array::c_style | pybind11::array::forcecast>;
    // using ndarray_c = pybind11::array_t<char, pybind11::array::c_style | pybind11::array::forcecast>;
    // using ndarray_uc = pybind11::array_t<unsigned char, pybind11::array::c_style | pybind11::array::forcecast>;

    Object Create(ndarray_f&, std::string&);
    Object Push(ndarray_f&, std::string&);
    ndarray_f Pull(Object&);
   
};

#endif