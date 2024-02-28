#include "pycle_wrapper.hpp"

#include "backend.hpp"
#include "device.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

auto core_(pybind11::module_ &m) -> void
{
    py::enum_<cle::Backend::Type>(m, "_BackendType")
        .value("OpenCL", cle::Backend::Type::OPENCL)
        .value("CUDA", cle::Backend::Type::CUDA);

    py::enum_<cle::Device::Type>(m, "_DeviceType")
        .value("OpenCL", cle::Device::Type::OPENCL)
        .value("CUDA", cle::Device::Type::CUDA);

    py::class_<cle::Device, std::shared_ptr<cle::Device>>(m, "_Device")
        // .def_property_readonly("name", &cle::Device::getName, py::arg("lowercase"))
        .def_property_readonly("name", [](const cle::Device &device)
                               { return device.getName(false); })
        .def_property_readonly("info", &cle::Device::getInfo)
        .def_property_readonly("type", &cle::Device::getType)
        .def("set_wait_to_finish", &cle::Device::setWaitToFinish)
        .def("__str__", [](const cle::Device &device)
             {
            std::ostringstream oss;
            oss << &device;
            return oss.str(); })
        .def("__repr__", [](const cle::Device &device)
             {
        std::ostringstream oss;
        oss << device.getInfo();
        return oss.str(); });

    py::class_<cle::Backend, std::shared_ptr<cle::Backend>>(m, "_Backend")
        .def_property_readonly("type", &cle::Backend::getType)
        .def("getDevicesList", &cle::Backend::getDevicesList, py::arg("type"))
        .def("getDevices", &cle::Backend::getDevices, py::return_value_policy::take_ownership)
        .def("getDeviceFromName", &cle::Backend::getDevice, py::return_value_policy::take_ownership, py::arg("name"), py::arg("type"))
        .def("getDeviceFromIndex", &cle::Backend::getDeviceFromIndex, py::return_value_policy::take_ownership, py::arg("index"), py::arg("type"))
        .def("__str__", [](const cle::Backend &Backend)
             {
        std::ostringstream oss;
        oss << Backend;
        return oss.str(); })
        .def("__repr__", [](const cle::Backend &Backend)
             {
        std::ostringstream oss;
        oss << Backend;
        return oss.str(); });

    py::class_<cle::BackendManager, std::shared_ptr<cle::BackendManager>>(m, "_BackendManager")
        .def_static("get_backends_list", &cle::BackendManager::getBackendsList)
        .def_static(
            "set_backend", [](const std::string &backend)
            { cle::BackendManager::getInstance().setBackend(backend); },
            py::arg("backend"))
        .def_static(
            "get_backend", []
            {
        const cle::Backend &backend = cle::BackendManager::getInstance().getBackend();
        return &backend; },
            py::return_value_policy::reference)
        .def("__str__", [](const cle::BackendManager &backendManager)
             {
        std::ostringstream oss;
        oss << backendManager;
        return oss.str(); })
        .def("__repr__", [](const cle::BackendManager &backendManager)
             {
        std::ostringstream oss;
        oss << backendManager;
        return oss.str(); });
}
