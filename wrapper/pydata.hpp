#ifndef __pydata_h
#define __pydata_h

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include "cleGPU.hpp"
#include "cleObject.hpp"

using namespace cle;

class PyData : public Object {
public:

    using Object::Object;
       
    PyData() = default;   
    PyData(const Object&);
    std::array<size_t,3> Shape_zyx() const;
    std::array<size_t,3> Shape_xyz() const;

};

#endif