
// this code is auto-generated by the script 'pyclesperanto_autogen_tier_script.ipynb'.
// Do not edit manually. Instead, edit the script and run it again.
    
#include "pycle_wrapper.hpp"
#include "tier4.hpp"

namespace py = pybind11;

auto tier4_(py::module &m) -> void {

    
m.def("_mean_squared_error", &cle::tier4::mean_squared_error_func, "Call mean_squared_error from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"));

    
m.def("_relabel_sequential", &cle::tier4::relabel_sequential_func, "Call relabel_sequential from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("blocksize"));

    
m.def("_threshold_otsu", &cle::tier4::threshold_otsu_func, "Call threshold_otsu from C++.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));


}