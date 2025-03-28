// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "fft.hpp"

namespace py = pybind11;


auto fft_(py::module &m) -> void {

    // m.def("_fft_forward", &cle::fft::fft_forward, "Apply forward Fourier Transform (clFFT)",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("output")
    // );

    // m.def("_fft_backward", &cle::fft::fft_backward, "Apply backward Fourier Transform (clFFT)",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("output")
    // );

    // m.def("_convolution", &cle::fft::convolution, "Apply convolution (clFFT)",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("kernel"),
    //     py::arg("output"),
    //     py::arg("correlate")
    // );

    // m.def("_deconvolution", &cle::fft::deconvolution, "Apply deconvolution (clFFT)",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("kernel"),
    //     py::arg("normal"),
    //     py::arg("output"),
    //     py::arg("iterations"),
    //     py::arg("regularization")
    // );



    // m.def("_fft_complex_multiply", &complex_multiply, "Complex multiply",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("psf"),
    //     py::arg("output")
    // );

    // m.def("_fft_complex_conju_multiply", &complex_conju_multiply, "Complex conjugate multiply",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("psf"),
    //     py::arg("output")
    // );

    // m.def("_fft_real_divide", &real_divide, "Real divide",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("psf"),
    //     py::arg("output")
    // );

    // m.def("_fft_real_multiply", &real_multiply, "Real multiply",
    //     py::return_value_policy::take_ownership,
    //     py::arg("input"),
    //     py::arg("psf"),
    //     py::arg("output")
    // );











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
