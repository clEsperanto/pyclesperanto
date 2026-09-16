// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier8.hpp"

namespace py = pybind11;

auto tier8_(py::module &m) -> void {
m.def("_smooth_labels", &cle::tier8::smooth_labels_func, "Call cle::tier8::smooth_labels_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

    m.def("_smooth_connected_labels", &cle::tier8::smooth_connected_labels_func, "Call cle::tier8::smooth_connected_labels_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

    m.def("_make_isotropic", &cle::tier8::make_isotropic_func, "Call cle::tier8::make_isotropic_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("current_spacing_x"), py::arg("current_spacing_y"), py::arg("current_spacing_z"), py::arg("target_spacing"), py::arg("interpolate"));

    m.def("_make_anisotropic", &cle::tier8::make_anisotropic_func, "Call cle::tier8::make_anisotropic_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("current_spacing"), py::arg("target_spacing_x"), py::arg("target_spacing_y"), py::arg("target_spacing_z"), py::arg("interpolate"));
}