#ifndef __data_h
#define __data_h

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>

#include "cleGPU.hpp"
#include "cleObject.hpp"

using namespace cle;


// todo: trampoline class for interface C++ python
// Should we do that for all wrapped class? (aka overlayer of wrapper)

class PyData : public Object {
public:

    using Object::Object;

    PyData(const Object&);
    std::array<size_t,3> Shape_zyx() const;

};

#endif