

#include "pyclesperanto.hpp"
#include "pygpu.hpp"

using namespace cle;


Object PyGPU::Create(ndarray_f& dimensions, std::string& t_type) 
{ 
    pybind11::buffer_info arr = dimensions.request();
    if (arr.ndim > 1)
    {
        throw std::runtime_error("Expecting 1d shape array");
    }
    if (arr.size > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    float* ptr = static_cast<float*>(arr.ptr);
    std::array<size_t,3> shape = {1, 1, 1};
    for (auto i = 0;  i < arr.size; ++i)
    {
        if(ptr[i] > 0)
        {
            shape[i] = static_cast<size_t>(ptr[i]);
        }
    }
    return GPU::Create<float>(shape, t_type); 
};

Object PyGPU::Push(ndarray_f& ndarray, std::string& t_type) 
{ 
    pybind11::buffer_info arr = ndarray.request();
    if (arr.ndim > 3)
    {
        throw std::runtime_error("Number of dimensions must be three or less");
    }
    std::array<size_t,3> shape = {1, 1, 1};
    for (auto i = 0;  i < arr.ndim; ++i)
    {
        if(arr.shape[i] > 0)
        {
            shape[i] = static_cast<size_t>(arr.shape[i]);
        }
    }
    float* arr_ptr = static_cast<float*>(arr.ptr);
    std::vector<float> values(arr_ptr, arr_ptr + arr.size);
    return GPU::Push<float>(values, shape, t_type); 
};

PyGPU::ndarray_f PyGPU::Pull(Object& buffer) 
{ 
    auto output = GPU::Pull<float>(buffer);
    auto result = ndarray_f(output.size());
    float* ptr = static_cast<float*>(result.request().ptr);
    for (auto i = 0;  i < output.size(); ++i)
    {
        ptr[i] = output[i];
    }
    result.resize({buffer.Shape()[0], buffer.Shape()[1], buffer.Shape()[2]});
    return result.squeeze();
}    

// PYBIND11_MODULE(_gpu, m) {  // define a module. module name = file name = cmake target name 

void init_pygpu(pybind11::module_ &m) {

    pybind11::class_<PyGPU, std::shared_ptr<PyGPU>> object(m, "gpu");
        // constructor
        object.def(pybind11::init<>(), "GPU default constructor", pybind11::return_value_policy::move);
        object.def(pybind11::init<const char*, const char*>(), "GPU constructor", pybind11::return_value_policy::move, 
            pybind11::arg("t_device_name"), pybind11::arg("t_device_type") = "all");
        // generic methods
        object.def("select_device", &PyGPU::SelectDevice, "select GPU device", 
            pybind11::arg("t_device_name"), pybind11::arg("t_device_type") = "all");
        object.def("info", &PyGPU::Info, "return gpu informations");
        object.def("name", &PyGPU::Name, "return gpu name");
        object.def("score", &PyGPU::Score, "return gpu score");
        object.def("set_wait_for_kernel_to_finish", &GPU::SetWaitForKernelToFinish, "Force GPU to wait until kernel finished",
            pybind11::arg("t_flag") =true );
        // buffer methods
        object.def("create", &PyGPU::Create, pybind11::return_value_policy::move, "create a buffer object",
            pybind11::arg("dimensions"), pybind11::arg("t_type") = "buffer");
        object.def("push", &PyGPU::Push, pybind11::return_value_policy::move, "create and write a buffer object",
            pybind11::arg("ndarray"), pybind11::arg("t_type") = "buffer");
        object.def("pull", &PyGPU::Pull, pybind11::return_value_policy::move, "read a buffer object",
            pybind11::arg("buffer"));
        // help(gpu) cmd
        object.doc() = R"pbdoc(
            gpu class wrapper
            -----------------------
            info()
            name()
            set_wait_fo_kernel_to_finish()

            create()
            push()
            pull()

        )pbdoc";
}

// }