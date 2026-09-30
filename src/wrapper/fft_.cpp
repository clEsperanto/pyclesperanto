#include "pycle_wrapper.hpp"
#include "fft.hpp"

namespace py = pybind11;

auto fft_(py::module_ &m) -> void
{
    m.def("_smooth_shape", &cle::fft::smooth_shape, "Call cle::fft::smooth_shape from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("shape"));

    m.def("_fft", &cle::fft::fft_func, "Call cle::fft::fft_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_ifft", &cle::fft::ifft_func, "Call cle::fft::ifft_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_convolve", &cle::fft::convolve_func, "Call cle::fft::convolve_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("kernel"), py::arg("dst"), py::arg("correlate"));

    m.def("_deconvolve", &cle::fft::deconvolve_func, "Call cle::fft::deconvolve_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("psf"), py::arg("normalization"), py::arg("dst"), py::arg("iteration"), py::arg("regularization"));
}
