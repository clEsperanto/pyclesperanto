// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "fft.hpp"

namespace py = pybind11;

auto fft_(py::module &m) -> void {

    m.def("_fft_forward", &cle::fft::fft_forward, "Apply forward Fourier Transform",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("output")
    );

    m.def("_fft_backward", &cle::fft::fft_backward, "Apply backward Fourier Transform",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("output")
    );

    m.def("_convolution", &cle::fft::convolution, "Apply convolution",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("kernel"),
        py::arg("output"),
        py::arg("correlate")
    );

    m.def("_deconvolution", &cle::fft::deconvolution, "Apply deconvolution",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("kernel"),
        py::arg("normal"),
        py::arg("output"),
        py::arg("iterations"),
        py::arg("regularization")
    );
}
