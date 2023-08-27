
#include "pycle_wrapper.hpp"

#include "array.hpp"
#include "utils.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

template <typename T>
py::array_t<T, py::array::c_style> read(const cle::Array &array)
{
     py::array_t<T, py::array::c_style> np_array;
     switch (array.dim())
     {
     case 1:
          np_array = py::array_t<T, py::array::c_style>({static_cast<py::ssize_t>(array.width())});
          break;
     case 2:
          np_array = py::array_t<T, py::array::c_style>({static_cast<py::ssize_t>(array.height()), static_cast<py::ssize_t>(array.width())});
          break;
     case 3:
          np_array = py::array_t<T, py::array::c_style>({static_cast<py::ssize_t>(array.depth()), static_cast<py::ssize_t>(array.height()), static_cast<py::ssize_t>(array.width())});
          break;
     }
     py::buffer_info info = np_array.request();
     void *data = info.ptr;
     size_t size = info.size * info.itemsize;
     array.read(data);
     return np_array;
}

template <typename T>
void write(cle::Array &array, const py::array_t<T, py::array::c_style> &np_array)
{
     py::buffer_info info = np_array.request();
     const void *data = info.ptr;
     size_t size = info.size * info.itemsize;
     array.write(data);
}

py::object get_np_dtype(const cle::Array::Pointer &array)
{
     switch (array->dtype())
     {
     case cle::dType::FLOAT:
          return py::dtype::of<float>();
     case cle::dType::INT64:
          return py::dtype::of<int64_t>();
     case cle::dType::INT32:
          return py::dtype::of<int>();
     case cle::dType::INT16:
          return py::dtype::of<int16_t>();
     case cle::dType::INT8:
          return py::dtype::of<int8_t>();
     case cle::dType::UINT64:
          return py::dtype::of<uint64_t>();
     case cle::dType::UINT32:
          return py::dtype::of<uint32_t>();
     case cle::dType::UINT16:
          return py::dtype::of<uint16_t>();
     case cle::dType::UINT8:
          return py::dtype::of<uint8_t>();
     default:
          throw std::invalid_argument("Invalid dType value");
     }
}

cle::dType get_cle_dtype(const py::object &type)
{
     py::dtype dt = py::dtype::from_args(type);

     if (dt.equal(py::dtype("float32")))
     {
          return cle::dType::FLOAT;
     }
     else if (dt.equal(py::dtype("int64")) || dt.equal(py::dtype("int")))
     {
          return cle::dType::INT64;
     }
     else if (dt.equal(py::dtype("int32")))
     {
          return cle::dType::INT32;
     }
     else if (dt.equal(py::dtype("int16")))
     {
          return cle::dType::INT16;
     }
     else if (dt.equal(py::dtype("int8")))
     {
          return cle::dType::INT8;
     }
     else if (dt.equal(py::dtype("uint64")))
     {
          return cle::dType::UINT64;
     }
     else if (dt.equal(py::dtype("uint32")))
     {
          return cle::dType::UINT32;
     }
     else if (dt.equal(py::dtype("uint16")))
     {
          return cle::dType::UINT16;
     }
     else if (dt.equal(py::dtype("uint8")))
     {
          return cle::dType::UINT8;
     }
     else
     {
          throw std::invalid_argument("Invalid dtype value : " + dt.attr("name").cast<std::string>());
     }
}

std::string get_str_mtype(const cle::Array::Pointer &array)
{
     switch (array->mtype())
     {
     case cle::mType::BUFFER:
          return "buffer";
     case cle::mType::IMAGE:
          return "image";
     default:
          throw std::invalid_argument("Invalid mtype value");
     }
}

cle::mType get_cle_mtype(const std::string &mtype)
{
     if (mtype == "buffer")
     {
          return cle::mType::BUFFER;
     }
     else if (mtype == "image")
     {
          return cle::mType::IMAGE;
     }
     else
     {
          throw std::invalid_argument("Invalid mtype value");
     }
}

py::tuple get_np_shape(const cle::Array::Pointer &array)
{
     switch (array->dim())
     {
     case 1:
          return py::make_tuple(array->width());
     case 2:
          return py::make_tuple(array->height(), array->width());
     case 3:
          return py::make_tuple(array->depth(), array->height(), array->width());
     default:
          throw std::invalid_argument("Invalid dimension value");
     }
}

cle::Array::Pointer create_array(py::tuple shape, py::object dtype, std::string mtype, cle::Device::Pointer device)
{
     size_t width(1), height(1), depth(1);
     switch (py::len(shape))
     {
     case 1:
          width = shape[0].cast<size_t>();
          break;
     case 2:
          height = shape[0].cast<size_t>();
          width = shape[1].cast<size_t>();
          break;
     case 3:
          depth = shape[0].cast<size_t>();
          height = shape[1].cast<size_t>();
          width = shape[2].cast<size_t>();
          break;
     default:
          throw std::invalid_argument("Invalid dimension value");
     }
     auto array = cle::Array::create(width, height, depth, get_cle_dtype(dtype), get_cle_mtype(mtype), device);
     return array;
}

auto array_(py::module_ &m) -> void
{
     py::class_<cle::Array, std::shared_ptr<cle::Array>>(m, "_Array")
         //     .def(py::init<cle::Array const &>())
         //     .def_static("create",
         //                 py::overload_cast<const size_t &, const size_t &, const size_t &, const cle::dType &, const cle::mType &, const cle::Device::Pointer &>(&cle::Array::create), py::return_value_policy::take_ownership, py::arg("width"), py::arg("height"), py::arg("depth"), py::arg("dtype"), py::arg("mtype"), py::arg("device"))
         .def_static("create", &create_array, py::arg("shape"), py::arg("dtype"), py::arg("mtype"), py::arg("device"))

         .def("_write", &write<float>)
         .def("_write", &write<int8_t>)
         .def("_write", &write<int16_t>)
         .def("_write", &write<int32_t>)
         .def("_write", &write<int64_t>)
         .def("_write", &write<uint8_t>)
         .def("_write", &write<uint16_t>)
         .def("_write", &write<uint32_t>)
         .def("_write", &write<uint64_t>)

         .def("_read_float32", &read<float>)
         .def("_read_int8", &read<int8_t>)
         .def("_read_int16", &read<int16_t>)
         .def("_read_int32", &read<int32_t>)
         .def("_read_int64", &read<int64_t>)
         .def("_read_uint8", &read<uint8_t>)
         .def("_read_uint16", &read<uint16_t>)
         .def("_read_uint32", &read<uint32_t>)
         .def("_read_uint64", &read<uint64_t>)

         .def("copy", &cle::Array::copy, py::arg("dst"))
         .def("fill", &cle::Array::fill, py::arg("value"))

         .def_property_readonly("width", &cle::Array::width)
         .def_property_readonly("height", &cle::Array::height)
         .def_property_readonly("depth", &cle::Array::depth)
         .def_property_readonly("size", &cle::Array::nbElements)
         .def_property_readonly("itemsize", &cle::Array::bytesPerElements)
         .def_property_readonly("device", &cle::Array::device)
         .def_property_readonly("ndim", &cle::Array::dim)
         .def_property_readonly("mtype", [](const cle::Array::Pointer &array)
                                { return get_str_mtype(array); })
         .def_property_readonly("dtype", [](const cle::Array::Pointer &array)
                                { return get_np_dtype(array); })
         .def_property_readonly("shape", [](const cle::Array::Pointer &array)
                                { return get_np_shape(array); })
         .def("__len__", [](const cle::Array::Pointer &array)
              {
          switch (array->dim())
          {
          case 1:
               return array->width();
          case 2:
               return array->height();
          case 3:
               return array->depth();
               ;
          } });
}