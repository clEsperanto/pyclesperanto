// this code is auto-generated, do not edit manually
    
#include "pycle_wrapper.hpp"
#include "tier1.hpp"

namespace py = pybind11;

auto tier1_(py::module &m) -> void {
m.def("_absolute", &cle::tier1::absolute_func, "Call cle::tier1::absolute_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_add_images_weighted", &cle::tier1::add_images_weighted_func, "Call cle::tier1::add_images_weighted_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("factor1"), py::arg("factor2"));

    m.def("_add_image_and_scalar", &cle::tier1::add_image_and_scalar_func, "Call cle::tier1::add_image_and_scalar_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_binary_and", &cle::tier1::binary_and_func, "Call cle::tier1::binary_and_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_binary_edge_detection", &cle::tier1::binary_edge_detection_func, "Call cle::tier1::binary_edge_detection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_binary_not", &cle::tier1::binary_not_func, "Call cle::tier1::binary_not_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_binary_or", &cle::tier1::binary_or_func, "Call cle::tier1::binary_or_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_binary_subtract", &cle::tier1::binary_subtract_func, "Call cle::tier1::binary_subtract_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_binary_xor", &cle::tier1::binary_xor_func, "Call cle::tier1::binary_xor_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_binary_supinf", &cle::tier1::binary_supinf_func, "Call cle::tier1::binary_supinf_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_binary_infsup", &cle::tier1::binary_infsup_func, "Call cle::tier1::binary_infsup_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_block_enumerate", &cle::tier1::block_enumerate_func, "Call cle::tier1::block_enumerate_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("blocksize"));

    m.def("_convolve", &cle::tier1::convolve_func, "Call cle::tier1::convolve_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_copy", &cle::tier1::copy_func, "Call cle::tier1::copy_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_copy_slice", &cle::tier1::copy_slice_func, "Call cle::tier1::copy_slice_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("slice_index"));

    m.def("_copy_horizontal_slice", &cle::tier1::copy_horizontal_slice_func, "Call cle::tier1::copy_horizontal_slice_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("slice_index"));

    m.def("_copy_vertical_slice", &cle::tier1::copy_vertical_slice_func, "Call cle::tier1::copy_vertical_slice_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("slice_index"));

    m.def("_crop", &cle::tier1::crop_func, "Call cle::tier1::crop_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("start_x"), py::arg("start_y"), py::arg("start_z"), py::arg("width"), py::arg("height"), py::arg("depth"));

    m.def("_cubic_root", &cle::tier1::cubic_root_func, "Call cle::tier1::cubic_root_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_detect_label_edges", &cle::tier1::detect_label_edges_func, "Call cle::tier1::detect_label_edges_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_dilation", &cle::tier1::dilation_func, "Call cle::tier1::dilation_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("footprint"), py::arg("dst"));

    m.def("_dilate_box", &cle::tier1::dilate_box_func, "Call cle::tier1::dilate_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_dilate_sphere", &cle::tier1::dilate_sphere_func, "Call cle::tier1::dilate_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_binary_dilate", &cle::tier1::binary_dilate_func, "Call cle::tier1::binary_dilate_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_divide_images", &cle::tier1::divide_images_func, "Call cle::tier1::divide_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("dividend"), py::arg("divisor"), py::arg("dst"));

    m.def("_divide_scalar_by_image", &cle::tier1::divide_scalar_by_image_func, "Call cle::tier1::divide_scalar_by_image_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_equal", &cle::tier1::equal_func, "Call cle::tier1::equal_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_equal_constant", &cle::tier1::equal_constant_func, "Call cle::tier1::equal_constant_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_erosion", &cle::tier1::erosion_func, "Call cle::tier1::erosion_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("footprint"), py::arg("dst"));

    m.def("_erode_box", &cle::tier1::erode_box_func, "Call cle::tier1::erode_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_erode_sphere", &cle::tier1::erode_sphere_func, "Call cle::tier1::erode_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_binary_erode", &cle::tier1::binary_erode_func, "Call cle::tier1::binary_erode_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_exponential", &cle::tier1::exponential_func, "Call cle::tier1::exponential_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_flip", &cle::tier1::flip_func, "Call cle::tier1::flip_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("flip_x"), py::arg("flip_y"), py::arg("flip_z"));

    m.def("_gaussian_blur", &cle::tier1::gaussian_blur_func, "Call cle::tier1::gaussian_blur_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("sigma_x"), py::arg("sigma_y"), py::arg("sigma_z"));

    m.def("_generate_distance_matrix", &cle::tier1::generate_distance_matrix_func, "Call cle::tier1::generate_distance_matrix_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("coordinate_list1"), py::arg("coordinate_list2"), py::arg("distance_matrix_destination"));

    m.def("_gradient_x", &cle::tier1::gradient_x_func, "Call cle::tier1::gradient_x_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_gradient_y", &cle::tier1::gradient_y_func, "Call cle::tier1::gradient_y_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_gradient_z", &cle::tier1::gradient_z_func, "Call cle::tier1::gradient_z_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_greater", &cle::tier1::greater_func, "Call cle::tier1::greater_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_greater_constant", &cle::tier1::greater_constant_func, "Call cle::tier1::greater_constant_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_greater_or_equal", &cle::tier1::greater_or_equal_func, "Call cle::tier1::greater_or_equal_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_greater_or_equal_constant", &cle::tier1::greater_or_equal_constant_func, "Call cle::tier1::greater_or_equal_constant_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_hessian_eigenvalues", &cle::tier1::hessian_eigenvalues_func, "Call cle::tier1::hessian_eigenvalues_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("small_eigenvalue"), py::arg("middle_eigenvalue"), py::arg("large_eigenvalue"));

    m.def("_laplace_box", &cle::tier1::laplace_box_func, "Call cle::tier1::laplace_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_laplace_diamond", &cle::tier1::laplace_diamond_func, "Call cle::tier1::laplace_diamond_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_laplace", &cle::tier1::laplace_func, "Call cle::tier1::laplace_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("connectivity"));

    m.def("_local_cross_correlation", &cle::tier1::local_cross_correlation_func, "Call cle::tier1::local_cross_correlation_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("kernel"), py::arg("dst"));

    m.def("_logarithm", &cle::tier1::logarithm_func, "Call cle::tier1::logarithm_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mask", &cle::tier1::mask_func, "Call cle::tier1::mask_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("mask"), py::arg("dst"));

    m.def("_mask_label", &cle::tier1::mask_label_func, "Call cle::tier1::mask_label_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"), py::arg("label"));

    m.def("_maximum_image_and_scalar", &cle::tier1::maximum_image_and_scalar_func, "Call cle::tier1::maximum_image_and_scalar_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_maximum_images", &cle::tier1::maximum_images_func, "Call cle::tier1::maximum_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_maximum_box", &cle::tier1::maximum_box_func, "Call cle::tier1::maximum_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_maximum_filter", &cle::tier1::maximum_filter_func, "Call cle::tier1::maximum_filter_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_grayscale_dilate", &cle::tier1::grayscale_dilate_func, "Call cle::tier1::grayscale_dilate_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_maximum_x_projection", &cle::tier1::maximum_x_projection_func, "Call cle::tier1::maximum_x_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_maximum_y_projection", &cle::tier1::maximum_y_projection_func, "Call cle::tier1::maximum_y_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_maximum_z_projection", &cle::tier1::maximum_z_projection_func, "Call cle::tier1::maximum_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mean_box", &cle::tier1::mean_box_func, "Call cle::tier1::mean_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_mean_sphere", &cle::tier1::mean_sphere_func, "Call cle::tier1::mean_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_mean_filter", &cle::tier1::mean_filter_func, "Call cle::tier1::mean_filter_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_mean_x_projection", &cle::tier1::mean_x_projection_func, "Call cle::tier1::mean_x_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mean_y_projection", &cle::tier1::mean_y_projection_func, "Call cle::tier1::mean_y_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mean_z_projection", &cle::tier1::mean_z_projection_func, "Call cle::tier1::mean_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_median_box", &cle::tier1::median_box_func, "Call cle::tier1::median_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_median_sphere", &cle::tier1::median_sphere_func, "Call cle::tier1::median_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_median", &cle::tier1::median_func, "Call cle::tier1::median_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_minimum_box", &cle::tier1::minimum_box_func, "Call cle::tier1::minimum_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_minimum_filter", &cle::tier1::minimum_filter_func, "Call cle::tier1::minimum_filter_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_grayscale_erode", &cle::tier1::grayscale_erode_func, "Call cle::tier1::grayscale_erode_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_minimum_image_and_scalar", &cle::tier1::minimum_image_and_scalar_func, "Call cle::tier1::minimum_image_and_scalar_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_minimum_images", &cle::tier1::minimum_images_func, "Call cle::tier1::minimum_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_minimum_x_projection", &cle::tier1::minimum_x_projection_func, "Call cle::tier1::minimum_x_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_minimum_y_projection", &cle::tier1::minimum_y_projection_func, "Call cle::tier1::minimum_y_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_minimum_z_projection", &cle::tier1::minimum_z_projection_func, "Call cle::tier1::minimum_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_mode_box", &cle::tier1::mode_box_func, "Call cle::tier1::mode_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_mode_sphere", &cle::tier1::mode_sphere_func, "Call cle::tier1::mode_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_mode", &cle::tier1::mode_func, "Call cle::tier1::mode_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_modulo_images", &cle::tier1::modulo_images_func, "Call cle::tier1::modulo_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_multiply_image_and_position", &cle::tier1::multiply_image_and_position_func, "Call cle::tier1::multiply_image_and_position_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("dimension"));

    m.def("_multiply_image_and_scalar", &cle::tier1::multiply_image_and_scalar_func, "Call cle::tier1::multiply_image_and_scalar_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_multiply_images", &cle::tier1::multiply_images_func, "Call cle::tier1::multiply_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_nan_to_num", &cle::tier1::nan_to_num_func, "Call cle::tier1::nan_to_num_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("nan"), py::arg("posinf"), py::arg("neginf"));

    m.def("_nonzero_maximum_box", &cle::tier1::nonzero_maximum_box_func, "Call cle::tier1::nonzero_maximum_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    m.def("_nonzero_maximum_diamond", &cle::tier1::nonzero_maximum_diamond_func, "Call cle::tier1::nonzero_maximum_diamond_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    m.def("_nonzero_maximum", &cle::tier1::nonzero_maximum_func, "Call cle::tier1::nonzero_maximum_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"), py::arg("connectivity"));

    m.def("_nonzero_minimum_box", &cle::tier1::nonzero_minimum_box_func, "Call cle::tier1::nonzero_minimum_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    m.def("_nonzero_minimum_diamond", &cle::tier1::nonzero_minimum_diamond_func, "Call cle::tier1::nonzero_minimum_diamond_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"));

    m.def("_nonzero_minimum", &cle::tier1::nonzero_minimum_func, "Call cle::tier1::nonzero_minimum_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst0"), py::arg("dst1"), py::arg("connectivity"));

    m.def("_not_equal", &cle::tier1::not_equal_func, "Call cle::tier1::not_equal_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_not_equal_constant", &cle::tier1::not_equal_constant_func, "Call cle::tier1::not_equal_constant_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_paste", &cle::tier1::paste_func, "Call cle::tier1::paste_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("destination_x"), py::arg("destination_y"), py::arg("destination_z"));

    m.def("_onlyzero_overwrite_maximum_box", &cle::tier1::onlyzero_overwrite_maximum_box_func, "Call cle::tier1::onlyzero_overwrite_maximum_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("flag"), py::arg("dst"));

    m.def("_onlyzero_overwrite_maximum_diamond", &cle::tier1::onlyzero_overwrite_maximum_diamond_func, "Call cle::tier1::onlyzero_overwrite_maximum_diamond_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("flag"), py::arg("dst"));

    m.def("_onlyzero_overwrite_maximum", &cle::tier1::onlyzero_overwrite_maximum_func, "Call cle::tier1::onlyzero_overwrite_maximum_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("flag"), py::arg("dst"), py::arg("connectivity"));

    m.def("_power", &cle::tier1::power_func, "Call cle::tier1::power_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_power_images", &cle::tier1::power_images_func, "Call cle::tier1::power_images_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_range", &cle::tier1::range_func, "Call cle::tier1::range_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("start_x"), py::arg("stop_x"), py::arg("step_x"), py::arg("start_y"), py::arg("stop_y"), py::arg("step_y"), py::arg("start_z"), py::arg("stop_z"), py::arg("step_z"));

    m.def("_read_values_from_positions", &cle::tier1::read_values_from_positions_func, "Call cle::tier1::read_values_from_positions_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("list"), py::arg("dst"));

    m.def("_replace_values", &cle::tier1::replace_values_func, "Call cle::tier1::replace_values_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_replace_value", &cle::tier1::replace_value_func, "Call cle::tier1::replace_value_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("value_to_replace"), py::arg("value_replacement"));

    m.def("_replace_intensity", &cle::tier1::replace_intensity_func, "Call cle::tier1::replace_intensity_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("value_to_replace"), py::arg("value_replacement"));

    m.def("_replace_intensities", &cle::tier1::replace_intensities_func, "Call cle::tier1::replace_intensities_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_maximum_sphere", &cle::tier1::maximum_sphere_func, "Call cle::tier1::maximum_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_minimum_sphere", &cle::tier1::minimum_sphere_func, "Call cle::tier1::minimum_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_multiply_matrix", &cle::tier1::multiply_matrix_func, "Call cle::tier1::multiply_matrix_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("matrix1"), py::arg("matrix2"), py::arg("matrix_destination"));

    m.def("_reciprocal", &cle::tier1::reciprocal_func, "Call cle::tier1::reciprocal_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_set", &cle::tier1::set_func, "Call cle::tier1::set_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("scalar"));

    m.def("_set_column", &cle::tier1::set_column_func, "Call cle::tier1::set_column_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("column_index"), py::arg("value"));

    m.def("_set_image_borders", &cle::tier1::set_image_borders_func, "Call cle::tier1::set_image_borders_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    m.def("_set_plane", &cle::tier1::set_plane_func, "Call cle::tier1::set_plane_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("plane_index"), py::arg("value"));

    m.def("_set_ramp_x", &cle::tier1::set_ramp_x_func, "Call cle::tier1::set_ramp_x_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_set_ramp_y", &cle::tier1::set_ramp_y_func, "Call cle::tier1::set_ramp_y_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_set_ramp_z", &cle::tier1::set_ramp_z_func, "Call cle::tier1::set_ramp_z_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"));

    m.def("_set_row", &cle::tier1::set_row_func, "Call cle::tier1::set_row_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("row_index"), py::arg("value"));

    m.def("_set_nonzero_pixels_to_pixelindex", &cle::tier1::set_nonzero_pixels_to_pixelindex_func, "Call cle::tier1::set_nonzero_pixels_to_pixelindex_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("offset"));

    m.def("_set_where_x_equals_y", &cle::tier1::set_where_x_equals_y_func, "Call cle::tier1::set_where_x_equals_y_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    m.def("_set_where_x_greater_than_y", &cle::tier1::set_where_x_greater_than_y_func, "Call cle::tier1::set_where_x_greater_than_y_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    m.def("_set_where_x_smaller_than_y", &cle::tier1::set_where_x_smaller_than_y_func, "Call cle::tier1::set_where_x_smaller_than_y_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("value"));

    m.def("_sign", &cle::tier1::sign_func, "Call cle::tier1::sign_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_smaller", &cle::tier1::smaller_func, "Call cle::tier1::smaller_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_smaller_constant", &cle::tier1::smaller_constant_func, "Call cle::tier1::smaller_constant_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_smaller_or_equal", &cle::tier1::smaller_or_equal_func, "Call cle::tier1::smaller_or_equal_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src0"), py::arg("src1"), py::arg("dst"));

    m.def("_smaller_or_equal_constant", &cle::tier1::smaller_or_equal_constant_func, "Call cle::tier1::smaller_or_equal_constant_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_sobel", &cle::tier1::sobel_func, "Call cle::tier1::sobel_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_square_root", &cle::tier1::square_root_func, "Call cle::tier1::square_root_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_std_z_projection", &cle::tier1::std_z_projection_func, "Call cle::tier1::std_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_subtract_image_from_scalar", &cle::tier1::subtract_image_from_scalar_func, "Call cle::tier1::subtract_image_from_scalar_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("scalar"));

    m.def("_sum_reduction_x", &cle::tier1::sum_reduction_x_func, "Call cle::tier1::sum_reduction_x_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("blocksize"));

    m.def("_sum_x_projection", &cle::tier1::sum_x_projection_func, "Call cle::tier1::sum_x_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_sum_y_projection", &cle::tier1::sum_y_projection_func, "Call cle::tier1::sum_y_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_sum_z_projection", &cle::tier1::sum_z_projection_func, "Call cle::tier1::sum_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_transpose_xy", &cle::tier1::transpose_xy_func, "Call cle::tier1::transpose_xy_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_transpose_xz", &cle::tier1::transpose_xz_func, "Call cle::tier1::transpose_xz_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_transpose_yz", &cle::tier1::transpose_yz_func, "Call cle::tier1::transpose_yz_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_undefined_to_zero", &cle::tier1::undefined_to_zero_func, "Call cle::tier1::undefined_to_zero_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_variance_box", &cle::tier1::variance_box_func, "Call cle::tier1::variance_box_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_variance_sphere", &cle::tier1::variance_sphere_func, "Call cle::tier1::variance_sphere_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"));

    m.def("_variance_filter", &cle::tier1::variance_filter_func, "Call cle::tier1::variance_filter_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"), py::arg("radius_x"), py::arg("radius_y"), py::arg("radius_z"), py::arg("connectivity"));

    m.def("_write_values_to_positions", &cle::tier1::write_values_to_positions_func, "Call cle::tier1::write_values_to_positions_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_x_position_of_maximum_x_projection", &cle::tier1::x_position_of_maximum_x_projection_func, "Call cle::tier1::x_position_of_maximum_x_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_x_position_of_minimum_x_projection", &cle::tier1::x_position_of_minimum_x_projection_func, "Call cle::tier1::x_position_of_minimum_x_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_y_position_of_maximum_y_projection", &cle::tier1::y_position_of_maximum_y_projection_func, "Call cle::tier1::y_position_of_maximum_y_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_y_position_of_minimum_y_projection", &cle::tier1::y_position_of_minimum_y_projection_func, "Call cle::tier1::y_position_of_minimum_y_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_z_position_of_maximum_z_projection", &cle::tier1::z_position_of_maximum_z_projection_func, "Call cle::tier1::z_position_of_maximum_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));

    m.def("_z_position_of_minimum_z_projection", &cle::tier1::z_position_of_minimum_z_projection_func, "Call cle::tier1::z_position_of_minimum_z_projection_func from C++ CLIc.",
    py::return_value_policy::take_ownership,
    py::arg("device"), py::arg("src"), py::arg("dst"));
}