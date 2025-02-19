// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "fft.hpp"

namespace py = pybind11;

auto fft_(py::module &m) -> void {
    m.def("_fft_execute", &cle::fft::fft_execute, "Call cle::fft::execute from C++ CLIc.",
        py::return_value_policy::take_ownership,
        py::arg("data"));
}
