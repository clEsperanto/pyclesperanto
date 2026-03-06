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

// Helper function to safely cast tuple element with better error handling
size_t tuple_to_size_t(const py::tuple &t, size_t index)
{
    try
    {
        return t[index].cast<size_t>();
    }
    catch (const py::cast_error &e)
    {
        throw std::invalid_argument(
            "Error: Failed to convert range element at index " +
            std::to_string(index) + " to size_t. " + std::string(e.what()));
    }
}

// Helper function to parse range tuples (eliminates code duplication)
cle::RangeArray parse_range(const py::tuple &range_tuple, const std::string &range_name)
{
    if (range_tuple.size() > 3)
    {
        throw std::invalid_argument(
            "Error: " + range_name + " tuple must have 3 elements or less. "
            "Received " + std::to_string(range_tuple.size()) + " elements.");
    }

    cle::RangeArray range = {1, 1, 1};

    // Reverse indexing: Python uses [x, y, z], OpenCL uses [z, y, x]
    for (size_t i = 0; i < range_tuple.size(); ++i)
    {
        range[range_tuple.size() - 1 - i] = tuple_to_size_t(range_tuple, i);
    }

    return range;
}

// Helper function to convert Python dict parameters to ParameterList
cle::ParameterList convert_parameters(const py::dict &parameters)
{
    cle::ParameterList clic_parameters;
    clic_parameters.reserve(parameters.size());

    for (auto [key, value] : parameters)
    {
        std::string param_name = key.cast<std::string>();

        try
        {
            if (py::isinstance<cle::Array>(value))
            {
                clic_parameters.push_back(
                    {param_name, value.cast<cle::Array::Pointer>()});
            }
            else if (py::isinstance<py::int_>(value))
            {
                clic_parameters.push_back(
                    {param_name, value.cast<int>()});
            }
            else if (py::isinstance<py::float_>(value))
            {
                clic_parameters.push_back(
                    {param_name, value.cast<float>()});
            }
            else
            {
                throw std::invalid_argument(
                    "Parameter '" + param_name +
                    "' has unsupported type: " +
                    std::string(py::str(py::type::of(value)).cast<std::string>()));
            }
        }
        catch (const py::cast_error &e)
        {
            throw std::invalid_argument(
                "Error converting parameter '" + param_name + "': " +
                std::string(e.what()));
        }
    }

    return clic_parameters;
}

// Helper function to convert constants
cle::ConstantList convert_constants(const py::dict &constants)
{
    cle::ConstantList clic_constants;

    if (constants.empty())
    {
        return clic_constants;
    }

    clic_constants.reserve(constants.size());

    for (auto [key, value] : constants)
    {
        try
        {
            clic_constants.push_back(
                {key.cast<std::string>(), value.cast<int>()});
        }
        catch (const py::cast_error &e)
        {
            throw std::invalid_argument(
                "Error converting constant '" +
                key.cast<std::string>() + "': " +
                std::string(e.what()));
        }
    }

    return clic_constants;
}

auto py_execute(
    const cle::Device::Pointer &device,
    const std::string &kernel_name,
    const std::string &kernel_source,
    const py::dict &parameters,
    const py::tuple &global,
    const py::tuple &local,
    const py::dict &constants) -> void
{
    try
    {
        cle::RangeArray global_range = parse_range(global, "global");
        cle::RangeArray local_range = parse_range(local, "local");

        cle::KernelInfo kernel_info = {kernel_name, kernel_source};

        cle::ParameterList clic_parameters = convert_parameters(parameters);
        cle::ConstantList clic_constants = convert_constants(constants);

        cle::execute(device, kernel_info, clic_parameters,
                    global_range, local_range, clic_constants);
    }
    catch (const std::exception &e)
    {
        throw std::runtime_error("py_execute failed: " + std::string(e.what()));
    }
}

auto py_native_execute(
    const cle::Device::Pointer &device,
    const std::string &kernel_name,
    const std::string &kernel_source,
    const py::dict &parameters,
    const py::tuple &global,
    const py::tuple &local) -> void
{
    try
    {
        cle::RangeArray global_range = parse_range(global, "global");
        cle::RangeArray local_range = parse_range(local, "local");

        cle::KernelInfo kernel_info = {kernel_name, kernel_source};

        cle::ParameterList clic_parameters = convert_parameters(parameters);

        cle::native_execute(device, kernel_info, clic_parameters,
                           global_range, local_range);
    }
    catch (const std::exception &e)
    {
        throw std::runtime_error("py_native_execute failed: " + std::string(e.what()));
    }
}

// Helper function to convert Python dict to vector of ParameterType
std::vector<cle::ParameterType> convert_evaluate_parameters(const py::dict &parameters)
{
    std::vector<cle::ParameterType> param_vector;
    param_vector.reserve(parameters.size());

    for (auto [key, value] : parameters)
    {
        std::string param_name = key.cast<std::string>();

        try
        {
            if (py::isinstance<cle::Array>(value))
            {
                param_vector.push_back(value.cast<cle::Array::Pointer>());
            }
            else if (py::isinstance<py::int_>(value))
            {
                param_vector.push_back(value.cast<int>());
            }
            else if (py::isinstance<py::float_>(value))
            {
                param_vector.push_back(value.cast<float>());
            }
            else
            {
                throw std::invalid_argument(
                    "Parameter '" + param_name +
                    "' has unsupported type: " +
                    std::string(py::str(py::type::of(value)).cast<std::string>()));
            }
        }
        catch (const py::cast_error &e)
        {
            throw std::invalid_argument(
                "Error converting parameter '" + param_name + "': " +
                std::string(e.what()));
        }
    }

    return param_vector;
}

// Add this wrapper function:
auto py_evaluate(
    const cle::Device::Pointer &device,
    const std::string &expression,
    const py::dict &parameters,
    const cle::Array::Pointer &output) -> void
{
    try
    {
        std::vector<cle::ParameterType> param_vector =
            convert_evaluate_parameters(parameters);

        cle::evaluate(device, expression, param_vector, output);
    }
    catch (const std::exception &e)
    {
        throw std::runtime_error("py_evaluate failed: " + std::string(e.what()));
    }
}

auto execute_(py::module_ &m) -> void
{
    m.def("_execute",
          &py_execute,
          "Execute a kernel with parameters, global/local ranges, and constants.",
          py::arg("device"),
          py::arg("kernel_name"),
          py::arg("kernel_source"),
          py::arg("parameters"),
          py::arg("global"),
          py::arg("local"),
          py::arg("constants") = py::dict());

    m.def("_native_execute",
          &py_native_execute,
          "Execute a native kernel with parameters and global/local ranges.",
          py::arg("device"),
          py::arg("kernel_name"),
          py::arg("kernel_source"),
          py::arg("parameters"),
          py::arg("global"),
          py::arg("local"));

     m.def("_evaluate",
          &py_evaluate,
          "Evaluate an expression with the given parameters and output to an array.",
          py::arg("device"),
          py::arg("expression"),
          py::arg("parameters"),
          py::arg("output"));
}
