

#include "cleObject.hpp"
#include "pyclesperanto.hpp"

using namespace cle;

// PYBIND11_MODULE(_data, m) {
void init_pydata(pybind11::module_ &m) {

    pybind11::class_<Object> object(m, "data");
    object.def(pybind11::init<>());
    object.def("ndim", &Object::nDim, "return object dimensionality");
    object.def("size", &Object::Size, "return object size (elements wise)");
    object.def("shape", &Object::Shape, "return object shape (x,y,z)");
    object.def("dtype", &Object::GetDataType, "return object data type (float, double, etc.)");
    object.def("reset", &Object::Reset, "reset object, free device memory");
    object.doc() = R"pbdoc(
        data class wrapper
        -----------------------
        shape()
        ndim()
        size()
    )pbdoc";

}