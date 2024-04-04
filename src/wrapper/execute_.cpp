
#include "pycle_wrapper.hpp"

#include "device.hpp"
#include "array.hpp"
#include "utils.hpp"
#include "execution.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

auto py_execute(const cle::Device::Pointer &device, const std::string &kernel_name, const std::string &kernel_source, const py::dict &parameters, const py::tuple &range, const py::dict &constants) -> void
{
     cle::RangeArray global_range = {1, 1, 1};
     switch (range.size())
     {
     case 1:
          global_range[0] = range[0].cast<size_t>();
          break;
     case 2:
          global_range[0] = range[1].cast<size_t>();
          global_range[1] = range[0].cast<size_t>();
          break;
     case 3:
          global_range[0] = range[2].cast<size_t>();
          global_range[1] = range[1].cast<size_t>();
          global_range[2] = range[0].cast<size_t>();
          break;
     default:
          throw std::invalid_argument("Error: range tuple must have 3 elements or less. Received " + std::to_string(range.size()) + " elements.");
          break;
     }

     // manage kernel name and code
     const cle::KernelInfo kernel_info = {kernel_name, kernel_source};

     // convert py::dict paramter to vector<pair<string, array>>
     cle::ParameterList clic_parameters;
     for (auto item : parameters)
     {
          // check if item.second is cle::Array::Pointer
          if (py::isinstance<cle::Array>(item.second))
          {
               clic_parameters.push_back({item.first.cast<std::string>(), item.second.cast<cle::Array::Pointer>()});
          }
          else if (py::isinstance<py::int_>(item.second))
          {
               // convert py::int to int
               clic_parameters.push_back({item.first.cast<std::string>(), item.second.cast<int>()});
          }
          else if (py::isinstance<py::float_>(item.second))
          {
               // convert py::float to float
               clic_parameters.push_back({item.first.cast<std::string>(), item.second.cast<float>()});
          }
          else
          {
               throw std::invalid_argument("Error: parameter type not supported. Received " + std::string(py::str(item.second.get_type()).cast<std::string>()));
          }
     }

     // convert py::dict constant to vector<pair<string, int>>
     cle::ConstantList clic_constants;
     if (!constants.empty())
     {
          for (auto item : constants)
          {
               clic_constants.push_back({item.first.cast<std::string>(), item.second.cast<int>()});
          }
     }

     // execute
     cle::execute(device, kernel_info, clic_parameters, global_range, clic_constants);
}

auto execute_(py::module_ &m) -> void
{
     m.def("_execute", &py_execute, "Call execute function from C++.",
           py::arg("device"), py::arg("kernel_name"), py::arg("kernel_source"), py::arg("parameters"), py::arg("range"), py::arg("constants"));
}
