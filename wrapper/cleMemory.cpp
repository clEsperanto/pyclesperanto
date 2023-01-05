#include "cleMemory.hpp"
#include "cleImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto Create(const std::shared_ptr<cle::Processor> &device, const pybind11::tuple &shape, const pybind11::object &dtype, const cle::MemoryType &mtype) -> cle::Image
{
    if (pybind11::len(shape) > 3 || pybind11::len(shape) < 1)
    {
        throw std::runtime_error("Wrong number of dimension provided. pyClesperanto does not support dimension > 3.");
    }
    std::array<size_t, 3> c_shape = {1, 1, 1};
    if (pybind11::len(shape) == 1)
    {
        c_shape[0] = shape[0].cast<size_t>();
    }
    else if (pybind11::len(shape) == 2)
    {
        c_shape[0] = shape[1].cast<size_t>();
        c_shape[1] = shape[0].cast<size_t>();
    }
    else if (pybind11::len(shape) == 3)
    {
        c_shape[0] = shape[2].cast<size_t>();
        c_shape[1] = shape[1].cast<size_t>();
        c_shape[2] = shape[0].cast<size_t>();
    }

    if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("float32")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::FLOAT32, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("int64")) || pybind11::dtype::from_args(dtype).is(pybind11::dtype("int")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::INT64, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("int32")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::INT32, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("int16")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::INT16, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("int8")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::INT8, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("uint64")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::UINT64, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("uint32")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::UINT32, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("uint16")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::UINT16, mtype);
    }
    else if (pybind11::dtype::from_args(dtype).is(pybind11::dtype("uint8")))
    {
        return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::UINT8, mtype);
    }
    else
    {
        throw std::runtime_error("Unsupported data type");
    }
}

template <typename Type>
auto Push(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<Type, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> c_shape = {1, 1, 1};
    if (arr.ndim == 1)
    {
        c_shape[0] = static_cast<size_t>(arr.shape[0]);
    }
    else if (arr.ndim == 2)
    {
        c_shape[0] = static_cast<size_t>(arr.shape[1]);
        c_shape[1] = static_cast<size_t>(arr.shape[0]);
    }
    else if (arr.ndim == 3)
    {
        c_shape[0] = static_cast<size_t>(arr.shape[2]);
        c_shape[1] = static_cast<size_t>(arr.shape[1]);
        c_shape[2] = static_cast<size_t>(arr.shape[0]);
    }

    cle::DataType dtype = cle::DataType::FLOAT32;
    if (std::is_same<Type, int64_t>::value)
    {
        dtype = cle::DataType::INT64;
    }
    else if (std::is_same<Type, int32_t>::value)
    {
        dtype = cle::DataType::INT32;
    }
    else if (std::is_same<Type, int16_t>::value)
    {
        dtype = cle::DataType::INT16;
    }
    else if (std::is_same<Type, int8_t>::value)
    {
        dtype = cle::DataType::INT8;
    }
    else if (std::is_same<Type, uint64_t>::value)
    {
        dtype = cle::DataType::UINT64;
    }
    else if (std::is_same<Type, uint32_t>::value)
    {
        dtype = cle::DataType::UINT32;
    }
    else if (std::is_same<Type, uint16_t>::value)
    {
        dtype = cle::DataType::UINT16;
    }
    else if (std::is_same<Type, uint8_t>::value)
    {
        dtype = cle::DataType::UINT8;
    }
    auto image = cle::Memory::AllocateMemory(device, c_shape, dtype, mtype);
    cle::Memory::WriteObject<Type>(image, (Type *)arr.ptr, arr.size);
    return image;
};

auto PullFloat(const cle::Image &image) -> pybind11::array_t<float, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<float, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<float>(image, (float *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullInt64(const cle::Image &image) -> pybind11::array_t<int64_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<int64_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<int64_t>(image, (int64_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullInt32(const cle::Image &image) -> pybind11::array_t<int32_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<int32_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<int32_t>(image, (int32_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullInt16(const cle::Image &image) -> pybind11::array_t<int16_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<int16_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<int16_t>(image, (int16_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullInt8(const cle::Image &image) -> pybind11::array_t<int8_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<int8_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<int8_t>(image, (int8_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullUint64(const cle::Image &image) -> pybind11::array_t<uint64_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<uint64_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<uint64_t>(image, (uint64_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullUint32(const cle::Image &image) -> pybind11::array_t<uint32_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<uint32_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<uint32_t>(image, (uint32_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullUint16(const cle::Image &image) -> pybind11::array_t<uint16_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<uint16_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<uint16_t>(image, (uint16_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

auto PullUint8(const cle::Image &image) -> pybind11::array_t<uint8_t, pybind11::array::c_style>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];

    pybind11::array_t<uint8_t, pybind11::array::c_style> result(size);
    cle::Memory::ReadObject<uint8_t>(image, (uint8_t *)result.request().ptr, size);
    if (image.Ndim() == 2)
    {
        result.resize({image.Shape()[1], image.Shape()[0]});
    }
    else if (image.Ndim() == 3)
    {
        result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    }
    return result;
}

// template <class Type>
// auto Pull(const cle::Image &image, const cle::DataType &dtype) -> pybind11::array_t<Type, pybind11::array::c_style | pybind11::array::forcecast>
// {
//     const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];
//
//     switch (dtype)
//     {
//     case cle::DataType::FLOAT:
//     {
//         std::cout << "FLOAT" << std::endl;
//         pybind11::array_t<float, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<float>(image, (float *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::INT8:
//     {
//         std::cout << "INT8" << std::endl;
//         pybind11::array_t<int8_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<int8_t>(image, (int8_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::INT16:
//     {
//         std::cout << "INT16" << std::endl;
//         pybind11::array_t<int16_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<int16_t>(image, (int16_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::INT32:
//     {
//         std::cout << "INT32" << std::endl;
//         pybind11::array_t<int32_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<int32_t>(image, (int32_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::INT64:
//     {
//         std::cout << "INT64" << std::endl;
//         pybind11::array_t<int64_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<int64_t>(image, (int64_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::UINT8:
//     {
//         std::cout << "UINT8" << std::endl;
//         pybind11::array_t<uint8_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<uint8_t>(image, (uint8_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::UINT16:
//     {
//         std::cout << "UINT16" << std::endl;
//         pybind11::array_t<uint16_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<uint16_t>(image, (uint16_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::UINT32:
//     {
//         std::cout << "UINT32" << std::endl;
//         pybind11::array_t<uint32_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<uint32_t>(image, (uint32_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     case cle::DataType::UINT64:
//     {
//         std::cout << "UINT64" << std::endl;
//         pybind11::array_t<uint64_t, pybind11::array::c_style> result(size);
//         cle::Memory::ReadObject<uint64_t>(image, (uint64_t *)result.request().ptr, size);
//         if (image.Ndim() == 2)
//         {
//             result.resize({image.Shape()[1], image.Shape()[0]});
//         }
//         else if (image.Ndim() == 3)
//         {
//             result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
//         }
//         return result;
//     }
//     default:
//         throw(std::runtime_error("Unsupported data type"));
//         break;
//     }
// }

auto init_clememory(pybind11::module_ &m) -> void
{
    m.def("_Create", &Create, "", pybind11::arg("device"), pybind11::arg("shape"), pybind11::arg("dtype"), pybind11::arg("mtype"));

    m.def("_Push", &Push<float>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<int64_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<int32_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<int16_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<int8_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<uint64_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<uint32_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<uint16_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Push", &Push<uint8_t>, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));

    m.def("_PullFloat", &PullFloat, "", pybind11::arg("image"));
    m.def("_PullInt64", &PullInt64, "", pybind11::arg("image"));
    m.def("_PullInt32", &PullInt32, "", pybind11::arg("image"));
    m.def("_PullInt16", &PullInt16, "", pybind11::arg("image"));
    m.def("_PullInt8", &PullInt8, "", pybind11::arg("image"));
    m.def("_PullUint64", &PullUint64, "", pybind11::arg("image"));
    m.def("_PullUint32", &PullUint32, "", pybind11::arg("image"));
    m.def("_PullUint16", &PullUint16, "", pybind11::arg("image"));
    m.def("_PullUint8", &PullUint8, "", pybind11::arg("image"));

    // m.def("_Pull", &Pull<float>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<int64_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<int32_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<int16_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<int8_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<uint64_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<uint32_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<uint16_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
    // m.def("_Pull", &Pull<uint8_t>, "", pybind11::arg("image"), pybind11::arg("dtype"));
}
