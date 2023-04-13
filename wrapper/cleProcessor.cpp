#include "pyclesperanto.hpp"

#include "cleProcessor.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto init_cleprocessor(pybind11::module_ &m) -> void
{
    pybind11::class_<cle::Processor, std::shared_ptr<cle::Processor>> object(m, "_cleProcessor");
    object.def(pybind11::init<>());

    object.def_property_readonly("name", &cle::Processor::GetDeviceName, "C++ call to get device name");
    object.def_property_readonly("info", &cle::Processor::GetDeviceInfo, "C++ call to get device info");

    object.def("wait_for_kernel_to_finish", &cle::Processor::WaitForKernelToFinish, "Device behavior C++ option", pybind11::arg("flag"));

    object.def("select_device", pybind11::overload_cast<const std::string &, const std::string &>(&cle::Processor::SelectDevice),
               "Select device on the C++ side by name and type (string, string)", pybind11::arg("name"), pybind11::arg("type"));

    object.def(
        "__str__", [](const cle::Processor &proc)
        {
                 std::stringstream out_string;
                 out_string << "<Processing Unit: " << proc.GetDeviceName() <<">";
                 return out_string.str(); },
        "");

    object.def(
        "__repr__", [](const cle::Processor &proc)
        {
                 std::stringstream out_string;
                 out_string << "<cle::Processor (" << proc.GetDeviceName() <<")>";
                 return out_string.str(); },
        "");

    m.def("_ListAvailableDevices", &cle::Processor::ListAvailableDevices, "List available devices by names", pybind11::arg("type"));
}