// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "tier4.hpp"

namespace py = pybind11;

auto tier4_(py::module &m) -> void {
m.def("_label_bounding_box", &cle::tier4::label_bounding_box_func, "Call cle::tier4::label_bounding_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("label_id"));

    m.def("_mean_squared_error", &cle::tier4::mean_squared_error_func, "Call cle::tier4::mean_squared_error_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"));

    m.def("_spots_to_pointlist", &cle::tier4::spots_to_pointlist_func, "Call cle::tier4::spots_to_pointlist_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_relabel_sequential", &cle::tier4::relabel_sequential_func, "Call cle::tier4::relabel_sequential_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("blocksize"));

    m.def("_threshold_otsu", &cle::tier4::threshold_otsu_func, "Call cle::tier4::threshold_otsu_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));
}
