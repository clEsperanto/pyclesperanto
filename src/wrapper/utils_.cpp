#include "utils.hpp"
#include "pycle_wrapper.hpp"

namespace py = pybind11;

auto utils_(py::module_ &m) -> void
{

    m.def("_fft_smooth_shape", &cle::fft_smooth_shape, "find the next smooth shape for FFT optimisation",
        py::return_value_policy::take_ownership,
        py::arg("shape")
    );

}
