
#include "pycle_wrapper.hpp"

#include "array.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

template <typename T>
py::array_t<T> get(const cle::Array &array)
{
     py::array_t<T> np_array({array.depth(), array.height(), array.width()});
     py::buffer_info info = np_array.request();
     void *data = info.ptr;
     size_t size = info.size * info.itemsize;
     array.read(data);
     return np_array;
}

template <typename T>
void set(cle::Array &array, const py::array_t<T> &np_array)
{
     py::buffer_info info = np_array.request();
     const void *data = info.ptr;
     size_t size = info.size * info.itemsize;
     array.write(data);
}

auto array_(py::module_ &m) -> void
{
     py::class_<cle::Array, std::shared_ptr<cle::Array>>(m, "_Array")
         .def(py::init<cle::Array const &>())
         .def_static("create",
                     py::overload_cast<const size_t &, const size_t &, const size_t &, const cle::dType &, const cle::mType &, const cle::Device::Pointer &>(&cle::Array::create), py::return_value_policy::take_ownership, py::arg("width"), py::arg("height"), py::arg("depth"), py::arg("dtype"), py::arg("mtype"), py::arg("device"))

         .def("set", set<float>)
         .def("set", set<int8_t>)
         .def("set", set<int16_t>)
         .def("set", set<int32_t>)
         .def("set", set<int64_t>)
         .def("set", set<uint8_t>)
         .def("set", set<uint16_t>)
         .def("set", set<uint32_t>)
         .def("set", set<uint64_t>)

         .def("get_float32", get<float>, py::return_value_policy::take_ownership)
         .def("get_int8", get<int8_t>, py::return_value_policy::take_ownership)
         .def("get_int16", get<int16_t>, py::return_value_policy::take_ownership)
         .def("get_int32", get<int32_t>, py::return_value_policy::take_ownership)
         .def("get_int64", get<int64_t>, py::return_value_policy::take_ownership)
         .def("get_uint8", get<uint8_t>, py::return_value_policy::take_ownership)
         .def("get_uint16", get<uint16_t>, py::return_value_policy::take_ownership)
         .def("get_uint32", get<uint32_t>, py::return_value_policy::take_ownership)
         .def("get_uint64", get<uint64_t>, py::return_value_policy::take_ownership)

         .def("copy", &cle::Array::copy, py::arg("dst"))
         .def("fill", &cle::Array::fill, py::arg("value"))

         .def_property_readonly("dtype", &cle::Array::dtype)
         .def_property_readonly("mtype", &cle::Array::mtype)
         .def_property_readonly("width", &cle::Array::width)
         .def_property_readonly("height", &cle::Array::height)
         .def_property_readonly("depth", &cle::Array::depth)
         .def_property_readonly("size", &cle::Array::nbElements)
         .def_property_readonly("itemsize", &cle::Array::bytesPerElements)
         .def_property_readonly("device", &cle::Array::device)
         .def_property_readonly("ndim", &cle::Array::dim)
         .def_property_readonly("shape", [](const cle::Array::Pointer &array)
                                {
          switch (array->dim())
          {
          case 1:
               return py::make_tuple(array->width());
               break;
          case 2:
               return py::make_tuple(array->height(), array->width());
               break;
          case 3:
               return py::make_tuple(array->depth(), array->height(), array->width());
               break;
          } });
}