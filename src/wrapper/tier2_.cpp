// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier2.hpp"

namespace py = pybind11;

auto tier2_(py::module &m) -> void {
m.def("_absolute_difference", &cle::tier2::absolute_difference_func, "Call cle::tier2::absolute_difference_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_add_images", &cle::tier2::add_images_func, "Call cle::tier2::add_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_bottom_hat_box", &cle::tier2::bottom_hat_box_func, "Call cle::tier2::bottom_hat_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_bottom_hat_sphere", &cle::tier2::bottom_hat_sphere_func, "Call cle::tier2::bottom_hat_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_bottom_hat", &cle::tier2::bottom_hat_func, "Call cle::tier2::bottom_hat_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_clip", &cle::tier2::clip_func, "Call cle::tier2::clip_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("min_intensity"), py::arg("max_intensity"));

    m.def("_closing_box", &cle::tier2::closing_box_func, "Call cle::tier2::closing_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_closing_sphere", &cle::tier2::closing_sphere_func, "Call cle::tier2::closing_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_grayscale_closing", &cle::tier2::grayscale_closing_func, "Call cle::tier2::grayscale_closing_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_closing", &cle::tier2::closing_func, "Call cle::tier2::closing_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("footprint"), py::arg("dst"));

    m.def("_binary_closing", &cle::tier2::binary_closing_func, "Call cle::tier2::binary_closing_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_concatenate_along_x", &cle::tier2::concatenate_along_x_func, "Call cle::tier2::concatenate_along_x_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_concatenate_along_y", &cle::tier2::concatenate_along_y_func, "Call cle::tier2::concatenate_along_y_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_concatenate_along_z", &cle::tier2::concatenate_along_z_func, "Call cle::tier2::concatenate_along_z_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_count_touching_neighbors", &cle::tier2::count_touching_neighbors_func, "Call cle::tier2::count_touching_neighbors_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("touch_matrix"), py::arg("touching_neighbors_count_destination"), py::arg("ignore_background"));

    m.def("_crop_border", &cle::tier2::crop_border_func, "Call cle::tier2::crop_border_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("border_size"));

    m.def("_divide_by_gaussian_background", &cle::tier2::divide_by_gaussian_background_func, "Call cle::tier2::divide_by_gaussian_background_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));

    m.def("_degrees_to_radians", &cle::tier2::degrees_to_radians_func, "Call cle::tier2::degrees_to_radians_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_detect_maxima_box", &cle::tier2::detect_maxima_box_func, "Call cle::tier2::detect_maxima_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_detect_maxima", &cle::tier2::detect_maxima_func, "Call cle::tier2::detect_maxima_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_detect_minima_box", &cle::tier2::detect_minima_box_func, "Call cle::tier2::detect_minima_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_detect_minima", &cle::tier2::detect_minima_func, "Call cle::tier2::detect_minima_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_difference_of_gaussian", &cle::tier2::difference_of_gaussian_func, "Call cle::tier2::difference_of_gaussian_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma1_x"), py::arg("sigma1_y"), py::arg("sigma1_z"), py::arg("sigma2_x"), py::arg("sigma2_y"), py::arg("sigma2_z"));

    m.def("_extend_labeling_via_voronoi", &cle::tier2::extend_labeling_via_voronoi_func, "Call cle::tier2::extend_labeling_via_voronoi_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_invert", &cle::tier2::invert_func, "Call cle::tier2::invert_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_label_spots", &cle::tier2::label_spots_func, "Call cle::tier2::label_spots_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_large_hessian_eigenvalue", &cle::tier2::large_hessian_eigenvalue_func, "Call cle::tier2::large_hessian_eigenvalue_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_maximum_of_all_pixels", &cle::tier2::maximum_of_all_pixels_func, "Call cle::tier2::maximum_of_all_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_minimum_of_all_pixels", &cle::tier2::minimum_of_all_pixels_func, "Call cle::tier2::minimum_of_all_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_minimum_of_masked_pixels", &cle::tier2::minimum_of_masked_pixels_func, "Call cle::tier2::minimum_of_masked_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("mask"));

    m.def("_opening_box", &cle::tier2::opening_box_func, "Call cle::tier2::opening_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_opening_sphere", &cle::tier2::opening_sphere_func, "Call cle::tier2::opening_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_grayscale_opening", &cle::tier2::grayscale_opening_func, "Call cle::tier2::grayscale_opening_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_opening", &cle::tier2::opening_func, "Call cle::tier2::opening_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("footprint"), py::arg("dst"));

    m.def("_binary_opening", &cle::tier2::binary_opening_func, "Call cle::tier2::binary_opening_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_radians_to_degrees", &cle::tier2::radians_to_degrees_func, "Call cle::tier2::radians_to_degrees_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_reduce_labels_to_label_edges", &cle::tier2::reduce_labels_to_label_edges_func, "Call cle::tier2::reduce_labels_to_label_edges_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_small_hessian_eigenvalue", &cle::tier2::small_hessian_eigenvalue_func, "Call cle::tier2::small_hessian_eigenvalue_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_square", &cle::tier2::square_func, "Call cle::tier2::square_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_squared_difference", &cle::tier2::squared_difference_func, "Call cle::tier2::squared_difference_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_standard_deviation_box", &cle::tier2::standard_deviation_box_func, "Call cle::tier2::standard_deviation_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_standard_deviation_sphere", &cle::tier2::standard_deviation_sphere_func, "Call cle::tier2::standard_deviation_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_standard_deviation", &cle::tier2::standard_deviation_func, "Call cle::tier2::standard_deviation_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_subtract_gaussian_background", &cle::tier2::subtract_gaussian_background_func, "Call cle::tier2::subtract_gaussian_background_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));

    m.def("_subtract_images", &cle::tier2::subtract_images_func, "Call cle::tier2::subtract_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_sub_stack", &cle::tier2::sub_stack_func, "Call cle::tier2::sub_stack_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("start_z"), py::arg("end_z"));

    m.def("_reduce_stack", &cle::tier2::reduce_stack_func, "Call cle::tier2::reduce_stack_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("reduction_factor"), py::arg("offset"));

    m.def("_sum_of_all_pixels", &cle::tier2::sum_of_all_pixels_func, "Call cle::tier2::sum_of_all_pixels_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_top_hat_box", &cle::tier2::top_hat_box_func, "Call cle::tier2::top_hat_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_top_hat_sphere", &cle::tier2::top_hat_sphere_func, "Call cle::tier2::top_hat_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_top_hat", &cle::tier2::top_hat_func, "Call cle::tier2::top_hat_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));
}