// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier8.hpp"

namespace py = pybind11;

auto tier8_(py::module &m) -> void {
m.def("_smooth_labels", &cle::tier8::smooth_labels_func, "Call cle::tier8::smooth_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

    m.def("_smooth_connected_labels", &cle::tier8::smooth_connected_labels_func, "Call cle::tier8::smooth_connected_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));
}