// this code is auto-generated, do not edit manually

#include "pycle_wrapper.hpp"
#include "tier4.hpp"

namespace py = pybind11;

auto tier4_(py::module &m) -> void {
m.def("_label_bounding_box", &cle::tier4::label_bounding_box_func, "Call cle::tier4::label_bounding_box_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("label_id"));

    m.def("_mean_squared_error", &cle::tier4::mean_squared_error_func, "Call cle::tier4::mean_squared_error_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src0"), py::arg("src1"));

    m.def("_spots_to_pointlist", &cle::tier4::spots_to_pointlist_func, "Call cle::tier4::spots_to_pointlist_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_relabel_sequential", &cle::tier4::relabel_sequential_func, "Call cle::tier4::relabel_sequential_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("blocksize"));

    m.def("_threshold_otsu", &cle::tier4::threshold_otsu_func, "Call cle::tier4::threshold_otsu_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_threshold_yen", &cle::tier4::threshold_yen_func, "Call cle::tier4::threshold_yen_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_threshold_mean", &cle::tier4::threshold_mean_func, "Call cle::tier4::threshold_mean_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_parametric_map", &cle::tier4::parametric_map_func, "Call cle::tier4::parametric_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("labels"), py::arg("intensity"), py::arg("property"), py::arg("dst"));

    m.def("_mean_intensity_map", &cle::tier4::mean_intensity_map_func, "Call cle::tier4::mean_intensity_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("labels"), py::arg("dst"));

    m.def("_label_mean_intensity_map", &cle::tier4::label_mean_intensity_map_func, "Call cle::tier4::label_mean_intensity_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("labels"), py::arg("dst"));

    m.def("_pixel_count_map", &cle::tier4::pixel_count_map_func, "Call cle::tier4::pixel_count_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_label_pixel_count_map", &cle::tier4::label_pixel_count_map_func, "Call cle::tier4::label_pixel_count_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_centroids_of_labels", &cle::tier4::centroids_of_labels_func, "Call cle::tier4::centroids_of_labels_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("label_image"), py::arg("centroids_coordinates"), py::arg("include_background"));

    m.def("_remove_labels_with_map_values_out_of_range", &cle::tier4::remove_labels_with_map_values_out_of_range_func, "Call cle::tier4::remove_labels_with_map_values_out_of_range_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("values"), py::arg("dst"), py::arg("min_value"), py::arg("max_value"));

    m.def("_remove_labels_with_map_values_within_range", &cle::tier4::remove_labels_with_map_values_within_range_func, "Call cle::tier4::remove_labels_with_map_values_within_range_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("values"), py::arg("dst"), py::arg("min_value"), py::arg("max_value"));

    m.def("_exclude_labels_with_map_values_out_of_range", &cle::tier4::exclude_labels_with_map_values_out_of_range_func, "Call cle::tier4::exclude_labels_with_map_values_out_of_range_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("values_map"), py::arg("label_map_input"), py::arg("dst"), py::arg("minimum_value_range"), py::arg("maximum_value_range"));

    m.def("_exclude_labels_with_map_values_within_range", &cle::tier4::exclude_labels_with_map_values_within_range_func, "Call cle::tier4::exclude_labels_with_map_values_within_range_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("values_map"), py::arg("label_map_input"), py::arg("dst"), py::arg("minimum_value_range"), py::arg("maximum_value_range"));

    m.def("_extension_ratio_map", &cle::tier4::extension_ratio_map_func, "Call cle::tier4::extension_ratio_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mean_extension_map", &cle::tier4::mean_extension_map_func, "Call cle::tier4::mean_extension_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_maximum_extension_map", &cle::tier4::maximum_extension_map_func, "Call cle::tier4::maximum_extension_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_minimum_intensity_map", &cle::tier4::minimum_intensity_map_func, "Call cle::tier4::minimum_intensity_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("labels"), py::arg("dst"));

    m.def("_maximum_intensity_map", &cle::tier4::maximum_intensity_map_func, "Call cle::tier4::maximum_intensity_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("labels"), py::arg("dst"));

    m.def("_standard_deviation_intensity_map", &cle::tier4::standard_deviation_intensity_map_func, "Call cle::tier4::standard_deviation_intensity_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("labels"), py::arg("dst"));

    m.def("_touching_neighbor_count_map", &cle::tier4::touching_neighbor_count_map_func, "Call cle::tier4::touching_neighbor_count_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("labels"), py::arg("dst"));

    m.def("_percentile", &cle::tier4::percentile_func, "Call cle::tier4::percentile_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"), py::arg("percentile"));

    m.def("_mean_of_touching_neighbors_map", &cle::tier4::mean_of_touching_neighbors_map_func, "Call cle::tier4::mean_of_touching_neighbors_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("map"), py::arg("labels"), py::arg("dst"), py::arg("radius"), py::arg("ignore_background"));

    m.def("_median_of_touching_neighbors_map", &cle::tier4::median_of_touching_neighbors_map_func, "Call cle::tier4::median_of_touching_neighbors_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("map"), py::arg("labels"), py::arg("dst"), py::arg("radius"), py::arg("ignore_background"));

    m.def("_minimum_of_touching_neighbors_map", &cle::tier4::minimum_of_touching_neighbors_map_func, "Call cle::tier4::minimum_of_touching_neighbors_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("map"), py::arg("labels"), py::arg("dst"), py::arg("radius"), py::arg("ignore_background"));

    m.def("_maximum_of_touching_neighbors_map", &cle::tier4::maximum_of_touching_neighbors_map_func, "Call cle::tier4::maximum_of_touching_neighbors_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("map"), py::arg("labels"), py::arg("dst"), py::arg("radius"), py::arg("ignore_background"));

    m.def("_standard_deviation_of_touching_neighbors_map", &cle::tier4::standard_deviation_of_touching_neighbors_map_func, "Call cle::tier4::standard_deviation_of_touching_neighbors_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("map"), py::arg("labels"), py::arg("dst"), py::arg("radius"), py::arg("ignore_background"));

    m.def("_mode_of_touching_neighbors_map", &cle::tier4::mode_of_touching_neighbors_map_func, "Call cle::tier4::mode_of_touching_neighbors_map_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("map"), py::arg("labels"), py::arg("dst"), py::arg("radius"), py::arg("ignore_background"));

    m.def("_standard_deviation_of_all_pixels", &cle::tier4::standard_deviation_of_all_pixels_func, "Call cle::tier4::standard_deviation_of_all_pixels_func from C++ CLIc.",
    py::return_value_policy::automatic_reference,
    py::arg("device"), py::arg("src"));
}
