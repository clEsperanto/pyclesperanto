#include "pycle_wrapper.hpp"
#include "tier1.hpp"

namespace py = pybind11;

auto tier1_(py::module_ &m) -> void
{

	m.def("_gaussian_blur", &cle::tier1::gaussian_blur_func, "Call gaussian_blur from C++.",
		  py::return_value_policy::take_ownership,
		  py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));

	m.def("_absolute", &cle::tier1::absolute_func, "Call absolute from C++.",
		  py::return_value_policy::take_ownership,
		  py::arg("device"), py::arg("src"), py::arg("dst"));

	m.def("_add_images_weighted", &cle::tier1::add_images_weighted_func, "Call add_images_weighted from C++.",
		  py::return_value_policy::take_ownership,
		  py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("factor0"), py::arg("factor1"));
}