
#include "pydata.hpp"
#include "pyclesperanto.hpp"

#include "cleObject.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>

using namespace cle;

PyData::PyData(const Object& obj) : Object(obj)
{}

std::array<size_t,3> PyData::Shape_zyx() const
{
    return {this->m_Shape[2],this->m_Shape[1],this->m_Shape[0]};
}

// PYBIND11_MODULE(_data, m) {
void init_pydata(pybind11::module_ &m) {

    pybind11::class_<PyData, std::shared_ptr<PyData>> object(m, "data");
    object.def(pybind11::init<>());
    object.def("ndim", &PyData::nDim, "return object dimensionality");
    object.def("size", &PyData::Size, "return object size (elements wise)");
    object.def("shape_zyx", &PyData::Shape_zyx, "return object shape (z,y,x)");
    object.def("shape", &PyData::Shape, "return object shape (x,y,z)");
    object.def("dtype", &PyData::GetDataType, "return object data type (float, double, etc.)");
    object.def("reset", &PyData::Reset, "reset object, free device memory");
    object.doc() = R"pbdoc(
        data class wrapper
        -----------------------
        shape()
        ndim()
        size()
    )pbdoc";

}