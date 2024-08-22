// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "tier5.hpp"

namespace py = pybind11;

auto tier5_(py::module &m) -> void {
m.def("_array_equal", &cle::tier5::array_equal_func, "Call cle::tier5::array_equal_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"));

    m.def("_combine_labels", &cle::tier5::combine_labels_func, "Call cle::tier5::combine_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_connected_components_labeling", &cle::tier5::connected_components_labeling_func, "Call cle::tier5::connected_components_labeling_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("connectivity"));
}
