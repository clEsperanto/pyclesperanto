

#include "pyclesperanto.hpp"
#include "pydata.hpp"

#include "cleObject.hpp"

using namespace cle;

PyData::PyData(const Object& obj) : Object(obj) {}

std::array<size_t,3> PyData::Shape_zyx() const
{
    return {this->m_Shape[2],this->m_Shape[1],this->m_Shape[0]};
}

std::array<size_t,3> PyData::Shape_xyz() const
{
    return this->m_Shape;
}


// PYBIND11_MODULE(_data, m) {
void init_pydata(pybind11::module_ &m) {

    pybind11::class_<PyData, std::shared_ptr<PyData>> object(m, "data");
    object.def(pybind11::init<>());
    object.def("ndim", &PyData::nDim, "return object dimensionality");
    object.def("size", &PyData::Size, "return object size (elements wise)");
    object.def("shape", &PyData::Shape, "return object shape (x,y,z)");
    object.def("shape_xyz", &PyData::Shape_xyz, "return object shape (x,y,z)");
    object.def("shape_zyx", &PyData::Shape_zyx, "return object shape (z,y,x)");
    object.def("dtype", &PyData::GetDataType, "return object data type (float, double, etc.)");
    object.doc() = R"pbdoc(
        data class wrapper
        -----------------------
        ndim()
        size()
        shape()
        shape_xyz()
        shape_zyx()
        dtype()
    )pbdoc";

}