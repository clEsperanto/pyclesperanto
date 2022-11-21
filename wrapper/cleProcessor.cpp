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

    object.def_property_readonly("name", &cle::Processor::GetDeviceName, "");
    object.def_property_readonly("info", &cle::Processor::GetDeviceInfo, "");

    object.def("wait_for_kernel_to_finish", &cle::Processor::WaitForKernelToFinish, "", pybind11::arg("flag"));
    object.def("select_device", &cle::Processor::SelectDevice, "", pybind11::arg("name"));

    object.def(
        "__str__", [](const cle::Processor &proc)
        {
                 std::stringstream out_string;
                 out_string << "<cle::Processor (" << proc.GetDeviceName() <<")>";
                 return out_string.str(); },
        "");
    object.def(
        "__repr__", [](const cle::Processor &proc)
        {
                 std::stringstream out_string;
                 out_string << "<cle::Processor (" << proc.GetDeviceName() <<")>";
                 return out_string.str(); },
        "");

    m.def("_ListAvailableDevices", &cle::Processor::ListAvailableDevices, "");
}