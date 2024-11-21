// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier4.hpp"

namespace py = pybind11;

auto tier4_(py::module &m) -> void {
m.def("_label_bounding_box", &cle::tier4::label_bounding_box_func, "Call cle::tier4::label_bounding_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("label_id"));

    m.def("_mean_squared_error", &cle::tier4::mean_squared_error_func, "Call cle::tier4::mean_squared_error_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"));

    m.def("_spots_to_pointlist", &cle::tier4::spots_to_pointlist_func, "Call cle::tier4::spots_to_pointlist_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_relabel_sequential", &cle::tier4::relabel_sequential_func, "Call cle::tier4::relabel_sequential_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("blocksize"));

    m.def("_threshold_otsu", &cle::tier4::threshold_otsu_func, "Call cle::tier4::threshold_otsu_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mean_intensity_map", &cle::tier4::mean_intensity_map_func, "Call cle::tier4::mean_intensity_map_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("labels"), py::arg("dst"));

    m.def("_pixel_count_map", &cle::tier4::pixel_count_map_func, "Call cle::tier4::pixel_count_map_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_label_pixel_count_map", &cle::tier4::label_pixel_count_map_func, "Call cle::tier4::label_pixel_count_map_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_centroids_of_labels", &cle::tier4::centroids_of_labels_func, "Call cle::tier4::centroids_of_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("label_image"), py::arg("centroids_coordinates"), py::arg("include_background"));

    m.def("_remove_labels_with_map_values_out_of_range", &cle::tier4::remove_labels_with_map_values_out_of_range_func, "Call cle::tier4::remove_labels_with_map_values_out_of_range_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("values"), py::arg("dst"), py::arg("min_value"), py::arg("max_value"));

    m.def("_remove_labels_with_map_values_within_range", &cle::tier4::remove_labels_with_map_values_within_range_func, "Call cle::tier4::remove_labels_with_map_values_within_range_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("values"), py::arg("dst"), py::arg("min_value"), py::arg("max_value"));

    m.def("_exclude_labels_with_map_values_out_of_range", &cle::tier4::exclude_labels_with_map_values_out_of_range_func, "Call cle::tier4::exclude_labels_with_map_values_out_of_range_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("values_map"), py::arg("label_map_input"), py::arg("dst"), py::arg("minimum_value_range"), py::arg("maximum_value_range"));

    m.def("_exclude_labels_with_map_values_within_range", &cle::tier4::exclude_labels_with_map_values_within_range_func, "Call cle::tier4::exclude_labels_with_map_values_within_range_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("values_map"), py::arg("label_map_input"), py::arg("dst"), py::arg("minimum_value_range"), py::arg("maximum_value_range"));

    m.def("_extension_ratio_map", &cle::tier4::extension_ratio_map_func, "Call cle::tier4::extension_ratio_map_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));
}