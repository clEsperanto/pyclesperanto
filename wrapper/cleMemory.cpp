#include "cleMemory.hpp"
#include "cleImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto Create(const std::shared_ptr<cle::Processor> &device, const pybind11::tuple &shape, const cle::MemoryType &mtype) -> cle::Image
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

auto Push(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
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

auto Pull(const cle::Image &image) -> pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>
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

auto init_clememory(pybind11::module_ &m) -> void
{
    m.def("_Create", &Create, "", pybind11::arg("device"), pybind11::arg("shape"), pybind11::arg("mtype"));
    m.def("_Push", &Push, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Pull", &Pull, "", pybind11::arg("image"));
}
