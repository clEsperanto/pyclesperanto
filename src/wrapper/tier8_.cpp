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

    m.def("_fft", &cle::tier8::fft_func, "Call cle::tier8::fft_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_ifft", &cle::tier8::ifft_func, "Call cle::tier8::fft_func from C++ CLIc.",
        py::return_value_policy::take_ownership,
        py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_fft_convolution", &cle::tier8::fft_convolution_func, "Call cle::tier8::fft_convolution_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
        py::arg("device"), py::arg("src"), py::arg("kernel"), py::arg("dst"), py::arg("correlate"));

    m.def("_fft_deconvolution", &cle::tier8::fft_deconvolution_func, "Call cle::tier8::fft_deconvolution_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
        py::arg("device"), py::arg("src"), py::arg("kernel"), py::arg("normal"), py::arg("dst"), py::arg("iterations"), py::arg("regularization"));
}
