#include "cleMemory.hpp"
#include "cleImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto Create(const std::shared_ptr<cle::Processor> &device, const pybind11::tuple &shape, const cle::DataType &dtype, const cle::MemoryType &mtype) -> cle::Image
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
    return cle::Memory::AllocateMemory(device, c_shape, cle::DataType::FLOAT, mtype);
};

auto PushFloat(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
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

    float *arr_ptr = static_cast<float *>(arr.ptr);
    auto image = cle::Memory::AllocateMemory(device, c_shape, cle::DataType::FLOAT, mtype);
    cle::Memory::WriteObject(image, arr_ptr, arr.size * sizeof(float));
    return image;
};

auto PushInt32(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<int32_t, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> shape = {1, 1, 1};
    for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        shape[j] = static_cast<size_t>(arr.shape[i]);
    }
    int32_t *arr_ptr = static_cast<int32_t *>(arr.ptr);
    std::vector<int32_t> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::INT32, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto PushInt16(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<int16_t, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> shape = {1, 1, 1};
    for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        shape[j] = static_cast<size_t>(arr.shape[i]);
    }
    int16_t *arr_ptr = static_cast<int16_t *>(arr.ptr);
    std::vector<int16_t> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::INT16, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto PushInt8(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<int8_t, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> shape = {1, 1, 1};
    for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        shape[j] = static_cast<size_t>(arr.shape[i]);
    }
    int8_t *arr_ptr = static_cast<int8_t *>(arr.ptr);
    std::vector<int8_t> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::INT8, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto PushUint32(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<uint32_t, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> shape = {1, 1, 1};
    for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        shape[j] = static_cast<size_t>(arr.shape[i]);
    }
    uint32_t *arr_ptr = static_cast<uint32_t *>(arr.ptr);
    std::vector<uint32_t> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::UINT32, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto PushUint16(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<uint16_t, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> shape = {1, 1, 1};
    for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        shape[j] = static_cast<size_t>(arr.shape[i]);
    }
    uint16_t *arr_ptr = static_cast<uint16_t *>(arr.ptr);
    std::vector<uint16_t> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::UINT16, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto PushUint8(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<uint8_t, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
{
    pybind11::buffer_info arr = nd_array.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t, 3> shape = {1, 1, 1};
    for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        shape[j] = static_cast<size_t>(arr.shape[i]);
    }
    uint8_t *arr_ptr = static_cast<uint8_t *>(arr.ptr);
    std::vector<uint8_t> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::UINT8, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto PullFloat(const cle::Image &image) -> pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>
{
    const size_t size = image.Shape()[0] * image.Shape()[1] * image.Shape()[2];
    if (image.Ndim() == 1)
    {
        pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> result(image.Shape()[0]);
        float *ptr = static_cast<float *>(result.request().ptr);
        cle::Memory::ReadObject<float>(image, ptr, size * sizeof(float));
        return result;
    }
    if (image.Ndim() == 2)
    {
        pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> result({image.Shape()[1], image.Shape()[0]});
        float *ptr = static_cast<float *>(result.request().ptr);
        cle::Memory::ReadObject<float>(image, ptr, size * sizeof(float));
        return result;
    }
    pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> result({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    float *ptr = static_cast<float *>(result.request().ptr);
    cle::Memory::ReadObject<float>(image, ptr, size * sizeof(float));
    return result;
}

auto PullInt32(const cle::Image &image) -> pybind11::array_t<int32_t, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<int32_t>(image);
    auto result = pybind11::array_t<int32_t, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    int32_t *ptr = static_cast<int32_t *>(result.request().ptr);
    for (int i = 0; i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    //! We flip the dimensions from c++ to numpy
    result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    return result.squeeze();
}

auto PullInt16(const cle::Image &image) -> pybind11::array_t<int16_t, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<int16_t>(image);
    auto result = pybind11::array_t<int16_t, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    int16_t *ptr = static_cast<int16_t *>(result.request().ptr);
    for (int i = 0; i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    //! We flip the dimensions from c++ to numpy
    result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    return result.squeeze();
}

auto PullInt8(const cle::Image &image) -> pybind11::array_t<int8_t, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<int8_t>(image);
    auto result = pybind11::array_t<int8_t, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    int8_t *ptr = static_cast<int8_t *>(result.request().ptr);
    for (int i = 0; i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    //! We flip the dimensions from c++ to numpy
    result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    return result.squeeze();
}

auto PullUint32(const cle::Image &image) -> pybind11::array_t<uint32_t, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<uint32_t>(image);
    auto result = pybind11::array_t<uint32_t, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    uint32_t *ptr = static_cast<uint32_t *>(result.request().ptr);
    for (int i = 0; i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    //! We flip the dimensions from c++ to numpy
    result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    return result.squeeze();
}

auto PullUint16(const cle::Image &image) -> pybind11::array_t<uint16_t, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<uint16_t>(image);
    auto result = pybind11::array_t<uint16_t, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    uint16_t *ptr = static_cast<uint16_t *>(result.request().ptr);
    for (int i = 0; i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    //! We flip the dimensions from c++ to numpy
    result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    return result.squeeze();
}

auto PullUint8(const cle::Image &image) -> pybind11::array_t<uint8_t, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<uint8_t>(image);
    auto result = pybind11::array_t<uint8_t, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    uint8_t *ptr = static_cast<uint8_t *>(result.request().ptr);
    for (int i = 0; i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    //! We flip the dimensions from c++ to numpy
    result.resize({image.Shape()[2], image.Shape()[1], image.Shape()[0]});
    return result.squeeze();
}

auto init_clememory(pybind11::module_ &m) -> void
{
    m.def("_Create", &Create, "", pybind11::arg("device"), pybind11::arg("shape"), pybind11::arg("dtype"), pybind11::arg("mtype"));

    m.def("_PushFloat", &PushFloat, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullFloat", &PullFloat, "", pybind11::arg("image"));

    m.def("_PushInt32", &PushInt32, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullInt32", &PullInt32, "", pybind11::arg("image"));

    m.def("_PushInt16", &PushInt16, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullInt16", &PullInt16, "", pybind11::arg("image"));

    m.def("_PushInt8", &PushInt8, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullInt8", &PullInt8, "", pybind11::arg("image"));

    m.def("_PushUint32", &PushUint32, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullUint32", &PullUint32, "", pybind11::arg("image"));

    m.def("_PushUint16", &PushUint16, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullUint16", &PullUint16, "", pybind11::arg("image"));

    m.def("_PushUint8", &PushUint8, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_PullUint8", &PullUint8, "", pybind11::arg("image"));
}
