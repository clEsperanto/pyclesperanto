
#include "pycle_wrapper.hpp"

#include "array.hpp"
#include "utils.hpp"
#include "device.hpp"
#include "dlpack/dlpack.h"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;


// dlpack device type mapping function
static int get_dlpack_device_type(const cle::Array::Pointer & array)
{
    auto dev_type = array->device()->getType(); // returns DeviceType enum
    // adjust to your DeviceType enum values
    switch (dev_type)
    {
        case cle::Device::Type::CUDA:   return kDLCUDA;
        case cle::Device::Type::OPENCL: return kDLOpenCL;
        default: throw std::runtime_error("Unsupported device type for DLPack");
    }
}

// function that takes a py tuple or list, invert it, and store it in a std::array of size 3
// if the tuple or list is smaller than 3, the remaining values are set to 0
// if the tuple or list is bigger than 3, the remaining values are ignored
auto invert_tuple(py::tuple tuple, std::array<size_t, 3> *res_array) -> void
{
     // Check if pointer is null
     if (!res_array)
     {
          throw std::invalid_argument("Null Pointer passed to function");
     }

     size_t dim = std::min(static_cast<size_t>(3), static_cast<size_t>(py::len(tuple)));

     for (size_t i = 0; i < dim; ++i)
     {
          (*res_array)[dim - i - 1] = tuple[i].cast<size_t>();
     }
}

template <typename T>
py::array_t<T, py::array::c_style> read_region(const cle::Array &array, const py::object &origin_obj = py::none(), const py::object &region_obj = py::none())
{
     std::array<size_t, 3> origin_ = {0, 0, 0};
     std::array<size_t, 3> region_ = {static_cast<size_t>(array.width()), static_cast<size_t>(array.height()), static_cast<size_t>(array.depth())};

     if (!origin_obj.is_none())
     {
          invert_tuple(origin_obj.cast<py::tuple>(), &origin_);
     }
     if (!region_obj.is_none())
     {
          invert_tuple(region_obj.cast<py::tuple>(), &region_);
     }

     py::array_t<T, py::array::c_style> np_array;
     switch (array.dimension())
     {
     case 1:
          np_array = py::array_t<T, py::array::c_style>({static_cast<py::ssize_t>(region_[0])});
          break;
     case 2:
          np_array = py::array_t<T, py::array::c_style>({static_cast<py::ssize_t>(region_[1]), static_cast<py::ssize_t>(region_[0])});
          break;
     case 3:
          np_array = py::array_t<T, py::array::c_style>({static_cast<py::ssize_t>(region_[2]), static_cast<py::ssize_t>(region_[1]), static_cast<py::ssize_t>(region_[0])});
          break;
     }

     py::buffer_info info = np_array.request();
     void *data = info.ptr;
     size_t size = info.size * info.itemsize;
     array.readTo(data, region_, origin_);
     return np_array;
}

template <typename T>
void write_region(cle::Array &array, const py::array_t<T, py::array::c_style> &value, const py::object &origin_obj = py::none(), const py::object &region_obj = py::none())
{
     std::array<size_t, 3> origin_ = {0, 0, 0};
     std::array<size_t, 3> region_ = {static_cast<size_t>(array.width()), static_cast<size_t>(array.height()), static_cast<size_t>(array.depth())};

     if (!origin_obj.is_none())
     {
          invert_tuple(origin_obj.cast<py::tuple>(), &origin_);
     }
     if (!region_obj.is_none())
     {
          invert_tuple(region_obj.cast<py::tuple>(), &region_);
     }

     py::buffer_info info = value.request();
     const void *data = info.ptr;
     size_t size = info.size * info.itemsize;
     array.writeFrom(data, region_, origin_);
}

void copy_region(const cle::Array &array, const cle::Array::Pointer &dst,
                 const py::object &src_origin_obj = py::none(),
                 const py::object &dst_origin_obj = py::none(),
                 const py::object &region_obj = py::none())
{
     std::array<size_t, 3> src_origin_ = {0, 0, 0};
     std::array<size_t, 3> dst_origin_ = {0, 0, 0};
     std::array<size_t, 3> region_ = {static_cast<size_t>(dst->width()), static_cast<size_t>(dst->height()), static_cast<size_t>(dst->depth())};

     if (!src_origin_obj.is_none())
     {
          invert_tuple(src_origin_obj.cast<py::tuple>(), &src_origin_);
     }
     if (!dst_origin_obj.is_none())
     {
          invert_tuple(dst_origin_obj.cast<py::tuple>(), &dst_origin_);
     }
     if (!region_obj.is_none())
     {
          invert_tuple(region_obj.cast<py::tuple>(), &region_);
     }
     array.copyTo(dst, region_, src_origin_, dst_origin_);
}

py::object get_np_dtype(const cle::Array::Pointer &array)
{
     switch (array->dtype())
     {
     case cle::dType::FLOAT:
          return py::dtype::of<float>();
     case cle::dType::COMPLEX:
          return py::dtype::of<float>();
     // case cle::dType::INT64:
     //      return py::dtype::of<int64_t>();
     case cle::dType::INT32:
          return py::dtype::of<int>();
     case cle::dType::INT16:
          return py::dtype::of<int16_t>();
     case cle::dType::INT8:
          return py::dtype::of<int8_t>();
     // case cle::dType::UINT64:
     //      return py::dtype::of<uint64_t>();
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
     py::dtype np_type = py::dtype::from_args(type);

     if (np_type.equal(py::dtype("float32")) || np_type.equal(py::dtype("float")) || np_type.equal(py::dtype("float64")))
     {
          return cle::dType::FLOAT;
     }
     else if (np_type.equal(py::dtype("int32")) || np_type.equal(py::dtype("int")) || np_type.equal(py::dtype("int64")))
     {
          return cle::dType::INT32;
     }
     else if (np_type.equal(py::dtype("int16")))
     {
          return cle::dType::INT16;
     }
     else if (np_type.equal(py::dtype("int8")))
     {
          return cle::dType::INT8;
     }
     else if (np_type.equal(py::dtype("uint32")) || np_type.equal(py::dtype("uint64")))
     {
          return cle::dType::UINT32;
     }
     else if (np_type.equal(py::dtype("uint16")))
     {
          return cle::dType::UINT16;
     }
     else if (np_type.equal(py::dtype("uint8")))
     {
          return cle::dType::UINT8;
     }
     else
     {
          throw std::invalid_argument("Invalid dtype value : " + np_type.attr("name").cast<std::string>());
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
     switch (array->dimension())
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
     std::array<size_t, 3> c_shape = {1, 1, 1};
     invert_tuple(shape, &c_shape);

     auto dimension = py::len(shape);

     auto array = cle::Array::create(c_shape[0], c_shape[1], c_shape[2], dimension, get_cle_dtype(dtype), get_cle_mtype(mtype), device);
     return array;
}

auto array_(py::module_ &m) -> void
{
     py::class_<cle::Array, std::shared_ptr<cle::Array>>(m, "_Array", py::module_local())
         .def_static("create", &create_array, py::return_value_policy::automatic_reference, py::arg("shape"), py::arg("dtype"), py::arg("mtype"), py::arg("device"))

         .def("_write", &write_region<float>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_write", &write_region<int8_t>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_write", &write_region<int16_t>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_write", &write_region<int32_t>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_write", &write_region<uint8_t>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_write", &write_region<uint16_t>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_write", &write_region<uint32_t>, py::arg("value"), py::arg("origin") = py::none(), py::arg("region") = py::none())

         .def("_read_float32", &read_region<float>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_read_int8", &read_region<int8_t>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_read_int16", &read_region<int16_t>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_read_int32", &read_region<int32_t>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_read_uint8", &read_region<uint8_t>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_read_uint16", &read_region<uint16_t>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())
         .def("_read_uint32", &read_region<uint32_t>, py::return_value_policy::move, py::arg("origin") = py::none(), py::arg("region") = py::none())


         .def("copy", &copy_region, py::arg("dst"), py::arg("src_origin") = py::none(), py::arg("dst_origin") = py::none(), py::arg("region") = py::none())
         .def("reshape", &cle::Array::reshape, py::arg("width") =1, py::arg("height") =1, py::arg("depth") =1, py::arg("dimension") = 0)
         .def("fill", &cle::Array::fill, py::arg("value"))

         .def_property_readonly("width", &cle::Array::width)
         .def_property_readonly("height", &cle::Array::height)
         .def_property_readonly("depth", &cle::Array::depth)
         .def_property_readonly("size", &cle::Array::size)
         .def_property_readonly("itemsize", &cle::Array::itemSize)
         .def_property_readonly("device", &cle::Array::device)
         .def_property_readonly("ndim", &cle::Array::dimension)
         .def_property_readonly("mtype", [](const cle::Array::Pointer &array) { return get_str_mtype(array); })
         .def_property_readonly("dtype", [](const cle::Array::Pointer &array) { return get_np_dtype(array); })
         .def_property_readonly("shape", [](const cle::Array::Pointer &array) { return get_np_shape(array); })
         .def("__len__", [](const cle::Array::Pointer &array)
              {
          switch (array->dimension())
          {
          case 1:
               return array->width();
          case 2:
               return array->height();
          case 3:
               return array->depth();
          default:
               throw std::invalid_argument("Invalid dimension value");
          } })


          .def("_dlpack", [](const cle::Array::Pointer &arr, py::object stream, py::tuple version) {

               if (arr->mtype() == cle::mType::IMAGE)
                         throw std::runtime_error("DLPack export not supported for IMAGE memory type");

               // stream sync handling:
               int64_t stream_val = stream.is_none() ? 0 : stream.cast<int64_t>();
               arr->syncToStream(stream_val);
               // arr->device()->finish();

               // version handling: for now we only support 1.0
               // toDLPack return a DLManagedTensorVersioned
               auto * managed = arr->toDLPack();

               // we return a capsule with name "dltensor_versioned", and a custom destructor
               return py::capsule(managed, "dltensor_versioned", [](PyObject *obj)
               {
                    // Only clean up if the capsule was never consumed.
                    // A consumer (torch, cupy) renames it to "used_dltensor_versioned"
                    // and takes ownership of calling managed->deleter itself.
                    const char *name = PyCapsule_GetName(obj);
                    if (name && std::strcmp(name, "dltensor_versioned") == 0)
                    {
                         auto * m = static_cast<DLManagedTensorVersioned*>(
                              PyCapsule_GetPointer(obj, "dltensor_versioned"));
                         if (m && m->deleter) m->deleter(m);
                    }
               });
               }, py::arg("stream") = py::none(), py::arg("version") = py::make_tuple(1, 0))


          .def("_dlpack_device",
               [](const cle::Array::Pointer & arr) -> py::tuple
               {
                    return py::make_tuple( // avoid creating a DLManagedTensor just to get device info
                         get_dlpack_device_type(arr),
                         arr->device()->getDeviceIndex()  // device index / ordinal
                    );
               })

          .def_static("_from_dlpack", [](py::object capsule_or_tensor, cle::Device::Pointer device) {
               py::object capsule;
               if (py::hasattr(capsule_or_tensor, "__dlpack__")) {
                    capsule = capsule_or_tensor.attr("__dlpack__")(py::arg("max_version") = py::make_tuple(1, 0));
               } else {
                    capsule = capsule_or_tensor;
               }

               void * ptr = PyCapsule_GetPointer(capsule.ptr(), "dltensor_versioned");
               if (!ptr) {
                    PyErr_Clear();
                    throw std::runtime_error("Invalid DLPack capsule: expected 'dltensor_versioned'");
               }

               auto * managed = static_cast<DLManagedTensorVersioned *>(ptr);
               auto array = cle::Array::fromDLPack(managed, device);
               PyCapsule_SetName(capsule.ptr(), "used_dltensor_versioned");
               return array;
               }, py::arg("capsule_or_tensor"), py::arg("device"));

}

                         
