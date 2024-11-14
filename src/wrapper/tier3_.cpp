// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier3.hpp"

namespace py = pybind11;

auto tier3_(py::module &m) -> void {
m.def("_bounding_box", &cle::tier3::bounding_box_func, "Call cle::tier3::bounding_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_center_of_mass", &cle::tier3::center_of_mass_func, "Call cle::tier3::center_of_mass_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_remove_labels", &cle::tier3::remove_labels_func, "Call cle::tier3::remove_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("list"), py::arg("dst"));

    m.def("_exclude_labels", &cle::tier3::exclude_labels_func, "Call cle::tier3::exclude_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("list"), py::arg("dst"));

    m.def("_remove_labels_on_edges", &cle::tier3::remove_labels_on_edges_func, "Call cle::tier3::remove_labels_on_edges_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("exclude_x"), py::arg("exclude_y"), py::arg("exclude_z"));

    m.def("_exclude_labels_on_edges", &cle::tier3::exclude_labels_on_edges_func, "Call cle::tier3::exclude_labels_on_edges_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("exclude_x"), py::arg("exclude_y"), py::arg("exclude_z"));

    m.def("_flag_existing_labels", &cle::tier3::flag_existing_labels_func, "Call cle::tier3::flag_existing_labels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_gamma_correction", &cle::tier3::gamma_correction_func, "Call cle::tier3::gamma_correction_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("gamma"));

    m.def("_generate_binary_overlap_matrix", &cle::tier3::generate_binary_overlap_matrix_func, "Call cle::tier3::generate_binary_overlap_matrix_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_generate_touch_matrix", &cle::tier3::generate_touch_matrix_func, "Call cle::tier3::generate_touch_matrix_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_histogram", &cle::tier3::histogram_func, "Call cle::tier3::histogram_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("num_bins"), py::arg("minimum_intensity"), py::arg("maximum_intensity"));

    m.def("_jaccard_index", &cle::tier3::jaccard_index_func, "Call cle::tier3::jaccard_index_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"));

    m.def("_labelled_spots_to_pointlist", &cle::tier3::labelled_spots_to_pointlist_func, "Call cle::tier3::labelled_spots_to_pointlist_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("label"), py::arg("pointlist"));

    m.def("_maximum_position", &cle::tier3::maximum_position_func, "Call cle::tier3::maximum_position_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_mean_of_all_pixels", &cle::tier3::mean_of_all_pixels_func, "Call cle::tier3::mean_of_all_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_minimum_position", &cle::tier3::minimum_position_func, "Call cle::tier3::minimum_position_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_morphological_chan_vese", &cle::tier3::morphological_chan_vese_func, "Call cle::tier3::morphological_chan_vese_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("num_iter"), py::arg("smoothing"), py::arg("lambda1"), py::arg("lambda2"));

    m.def("_statistics_of_labelled_pixels", &cle::tier3::statistics_of_labelled_pixels_func, "Call cle::tier3::statistics_of_labelled_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("intensity"), py::arg("label"));

    m.def("_statistics_of_background_and_labelled_pixels", &cle::tier3::statistics_of_background_and_labelled_pixels_func, "Call cle::tier3::statistics_of_background_and_labelled_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("intensity"), py::arg("label"));
}