// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "fft.hpp"

namespace py = pybind11;


auto fft_(py::module &m) -> void {

    m.def("_fft_smooth_shape", &cle::fft::fft_smooth_shape, "find the next smooth shape for FFT optimisation",
        py::return_value_policy::take_ownership,
        py::arg("shape")
    );

    m.def("_performFFT", &cle::fft::performFFT, "Apply forward Fourier Transform (vkFFT)",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("output")
    );

    m.def("_performIFFT", &cle::fft::performIFFT, "Apply backward Fourier Transform (vkFFT)",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("output")
    );

    m.def("_performConvolution", &cle::fft::performConvolution, "Apply convolution (vkFFT)",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("kernel"),
        py::arg("output"),
        py::arg("correlate")
    );

    m.def("_performDeconvolution", &cle::fft::performDeconvolution, "Apply deconvolution (vkFFT)",
        // py::return_value_policy::take_ownership,
        py::arg("input"),
        py::arg("kernel"),
        py::arg("normal"),
        py::arg("output"),
        py::arg("iterations"),
        py::arg("regularization")
    );
}
