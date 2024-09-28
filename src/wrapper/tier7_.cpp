// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier7.hpp"

namespace py = pybind11;

auto tier7_(py::module &m) -> void {
m.def("_affine_transform", &cle::tier7::affine_transform_func, "Call cle::tier7::affine_transform_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("transform_matrix"), py::arg("interpolate"), py::arg("resize"));

    m.def("_eroded_otsu_labeling", &cle::tier7::eroded_otsu_labeling_func, "Call cle::tier7::eroded_otsu_labeling_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("number_of_erosions"), py::arg("outline_sigma"));

    m.def("_rigid_transform", &cle::tier7::rigid_transform_func, "Call cle::tier7::rigid_transform_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("translate_x"), py::arg("translate_y"), py::arg("translate_z"), py::arg("angle_x"), py::arg("angle_y"), py::arg("angle_z"), py::arg("centered"), py::arg("interpolate"), py::arg("resize"));

    m.def("_rotate", &cle::tier7::rotate_func, "Call cle::tier7::rotate_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("angle_x"), py::arg("angle_y"), py::arg("angle_z"), py::arg("centered"), py::arg("interpolate"), py::arg("resize"));

    m.def("_scale", &cle::tier7::scale_func, "Call cle::tier7::scale_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("factor_x"), py::arg("factor_y"), py::arg("factor_z"), py::arg("centered"), py::arg("interpolate"), py::arg("resize"));

    m.def("_translate", &cle::tier7::translate_func, "Call cle::tier7::translate_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("translate_x"), py::arg("translate_y"), py::arg("translate_z"), py::arg("interpolate"));

    m.def("_closing_labels", &cle::tier7::closing_labels_func, "Call cle::tier7::closing_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

    m.def("_erode_connected_labels", &cle::tier7::erode_connected_labels_func, "Call cle::tier7::erode_connected_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

    m.def("_opening_labels", &cle::tier7::opening_labels_func, "Call cle::tier7::opening_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius"));

    m.def("_voronoi_otsu_labeling", &cle::tier7::voronoi_otsu_labeling_func, "Call cle::tier7::voronoi_otsu_labeling_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("spot_sigma"), py::arg("outline_sigma"));
}