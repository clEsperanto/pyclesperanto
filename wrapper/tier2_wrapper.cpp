#include "pyclesperanto.hpp"
#include "tier2.hpp"

namespace py = pybind11;

auto wrapper_tier2(py::module_ &m) -> void
{

	m.def("_difference_of_gaussian", &cle::tier2::difference_of_gaussian_func, "Call difference_of_gaussian from C++.",
		py::return_value_policy::take_ownership,
		py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma1_x"), py::arg("sigma1_y"), py::arg("sigma1_z"), py::arg("sigma2_x"), py::arg("sigma2_y"), py::arg("sigma2_z"));

}