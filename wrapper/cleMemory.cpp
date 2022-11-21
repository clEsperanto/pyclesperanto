#include "cleMemory.hpp"
#include "cleImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto Create(const std::shared_ptr<cle::Processor> &device, const pybind11::tuple &shape, const cle::MemoryType &mtype) -> cle::Image
{
    if (pybind11::len(shape) > 3)
    {
        throw std::runtime_error("Wrong number of dimension provided. pyClesperanto does not support dimension > 3.");
    }
    std::array<size_t, 3> arr = {1, 1, 1};
    for (int i = pybind11::len(shape) - 1, j = 0; i >= 0 && j < arr.size(); --i, ++j)
    {
        //! We flip the dimensions from numpy to c++
        arr[j] = shape[i].cast<size_t>();
    }
    return cle::Memory::AllocateMemory(device, arr, cle::DataType::FLOAT, mtype);
};

auto Push(const std::shared_ptr<cle::Processor> &device, const pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast> &nd_array, const cle::MemoryType &mtype) -> cle::Image
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
    float *arr_ptr = static_cast<float *>(arr.ptr);
    std::vector<float> values(arr_ptr, arr_ptr + arr.size);

    auto image = cle::Memory::AllocateMemory(device, shape, cle::DataType::FLOAT, mtype);
    cle::Memory::WriteObject(image, values);
    return image;
};

auto Pull(const cle::Image &image) -> pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>
{
    auto output = cle::Memory::ReadObject<float>(image);
    auto result = pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>(output.size());
    float *ptr = static_cast<float *>(result.request().ptr);
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
    m.def("_Create", &Create, "", pybind11::arg("device"), pybind11::arg("shape"), pybind11::arg("mtype"));
    m.def("_Push", &Push, "", pybind11::arg("device"), pybind11::arg("array"), pybind11::arg("mtype"));
    m.def("_Pull", &Pull, "", pybind11::arg("image"));
}
