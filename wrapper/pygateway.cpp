

#include "pygateway.hpp"
#include "pyImage.hpp"

auto pygateway::Create(ndarray_f &shape) -> Image {
  pybind11::buffer_info arr = shape.request();
  if (arr.ndim > 1) {
    throw std::runtime_error("Expecting 1d shape array");
  }
  if (arr.size > 3) {
    throw std::runtime_error("Number of dimensions must be three or less");
  }
  float *ptr = static_cast<float *>(arr.ptr);
  std::array<size_t, 3> shape_arr = {1, 1, 1};
  for (int i = arr.size - 1, j = 0; i >= 0 && j < shape_arr.size(); --i, ++j) {
    //! We flip the dimensions from numpy to c++
    shape_arr[j] = static_cast<size_t>(ptr[i]);
  }
  return this->Clesperanto::Create<float>(shape_arr, cle::BUFFER);
};

auto pygateway::Push(ndarray_f &source) -> Image {
  pybind11::buffer_info arr = source.request();
  if (arr.ndim > 3) {
    throw std::runtime_error("Number of dimensions must be three or less");
  }
  std::array<size_t, 3> shape = {1, 1, 1};
  for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j) {
    //! We flip the dimensions from numpy to c++
    shape[j] = static_cast<size_t>(arr.shape[i]);
  }
  float *arr_ptr = static_cast<float *>(arr.ptr);
  std::vector<float> values(arr_ptr, arr_ptr + arr.size);
  return this->Clesperanto::Push<float>(values, shape, cle::BUFFER);
};

auto pygateway::Pull(Image &source) -> pygateway::ndarray_f {
  auto output = this->Clesperanto::Pull<float>(source);
  auto result = ndarray_f(output.size());
  float *ptr = static_cast<float *>(result.request().ptr);
  for (int i = 0; i < output.size(); ++i) {
    ptr[i] = output[i];
  }
  //! We flip the dimensions from c++ to numpy
  result.resize({source.Shape()[2], source.Shape()[1], source.Shape()[0]});
  return result.squeeze();
}

auto init_pygateway(const pybind11::module_ &m) -> void {

  pybind11::class_<pygateway, std::shared_ptr<pygateway>> object(m,
                                                                 "pygateway");

  object.def(pybind11::init<>(), "default constructor");

  object.def("Create", &pygateway::Create, "", pybind11::arg("shape"));

  object.def("Push", &pygateway::Push, "", pybind11::arg("array"));

  object.def("Pull", &pygateway::Pull, "", pybind11::arg("image"));

  object.def("WaitForKernelToFinish", &pygateway::WaitForKernelToFinish, "",
             pybind11::arg("flag") = true);

  object.def("SelectDevice", &pygateway::SelectDevice, "",
             pybind11::arg("name") = "");

  object.def("Info", &pygateway::Info, "");

  object.def("Absolute", &pygateway::Absolute, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("AddImageAndScalar", &pygateway::AddImageAndScalar, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("AddImages", &pygateway::AddImages, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("AddImagesWeighted", &pygateway::AddImagesWeighted, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"), pybind11::arg("weight1") = 1,
             pybind11::arg("weight2") = 1);
  object.def("BinaryAnd", &pygateway::BinaryAnd, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("BinaryNot", &pygateway::BinaryNot, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("BinaryOr", &pygateway::BinaryOr, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("BinarySubtract", &pygateway::BinarySubtract, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("BinaryXor", &pygateway::BinaryXor, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("BlockEnumerate", &pygateway::BlockEnumerate, "",
             pybind11::arg("source"), pybind11::arg("sum"),
             pybind11::arg("destination"), pybind11::arg("block_size") = 1);
  object.def("CloseIndexGapsInLabelMap", &pygateway::CloseIndexGapsInLabelMap,
             "", pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("block_size") = 4096);
  object.def("ConnectedComponentLabelingBox",
             &pygateway::ConnectedComponentLabelingBox, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("Copy", &pygateway::Copy, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("DetectMaximaBox", &pygateway::DetectMaximaBox, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("DifferenceOfGaussian", &pygateway::DifferenceOfGaussian, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("sigma1_x") = 0, pybind11::arg("sigma1_y") = 0,
             pybind11::arg("sigma1_z") = 0, pybind11::arg("sigma2_x") = 0,
             pybind11::arg("sigma2_y") = 0, pybind11::arg("sigma2_z") = 0);
  object.def("DilateLabels", &pygateway::DilateLabels, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("radius"));
  object.def("DilateSphere", &pygateway::DilateSphere, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("DivideImages", &pygateway::DivideImages, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("Equal", &pygateway::Equal, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("EqualConstant", &pygateway::EqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("ErodeSphere", &pygateway::ErodeSphere, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("ExtendLabelingViaVoronoi", &pygateway::ExtendLabelingViaVoronoi,
             "", pybind11::arg("source"), pybind11::arg("destination"));
  object.def("FlagExistingLabels", &pygateway::FlagExistingLabels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("GaussianBlur", &pygateway::GaussianBlur, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("sigma_x") = 0, pybind11::arg("sigma_y") = 0,
             pybind11::arg("sigma_z") = 0);
  object.def("Greater", &pygateway::Greater, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("GreaterConstant", &pygateway::GreaterConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("GreaterOrEqual", &pygateway::GreaterOrEqual, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("GreaterOrEqualConstant", &pygateway::GreaterOrEqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("Histogram", &pygateway::Histogram, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("  bins") = 255,
             pybind11::arg("min_intensity") = pybind11::none(),
             pybind11::arg("max_intensity") = pybind11::none());
  object.def("Mask", &pygateway::Mask, "", pybind11::arg("source"),
             pybind11::arg("t_mask"), pybind11::arg("destination"));
  object.def("MaskedVoronoiLabeling", &pygateway::MaskedVoronoiLabeling, "",
             pybind11::arg("source"), pybind11::arg("t_mask"),
             pybind11::arg("destination"));
  object.def("MaximumBox", &pygateway::MaximumBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x") = 0,
             pybind11::arg("radius_y") = 0, pybind11::arg("radius_z") = 0);
  object.def("MaximumOfAllPixels", &pygateway::MaximumOfAllPixels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MaximumXProjection", &pygateway::MaximumXProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MaximumYProjection", &pygateway::MaximumYProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MaximumZProjection", &pygateway::MaximumZProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MeanBox", &pygateway::MeanBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x") = 0,
             pybind11::arg("radius_y") = 0, pybind11::arg("radius_z") = 0);
  object.def("MeanSphere", &pygateway::MeanSphere, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x") = 0,
             pybind11::arg("radius_y") = 0, pybind11::arg("radius_z") = 0);
  object.def("MinimumBox", &pygateway::MinimumBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x") = 0,
             pybind11::arg("radius_y") = 0, pybind11::arg("radius_z") = 0);
  object.def("MinimumOfAllPixels", &pygateway::MinimumOfAllPixels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MinimumXProjection", &pygateway::MinimumXProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MinimumYProjection", &pygateway::MinimumYProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MinimumZProjection", &pygateway::MinimumZProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MultiplyImages", &pygateway::MultiplyImages, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("NonzeroMinimumBox", &pygateway::NonzeroMinimumBox, "",
             pybind11::arg("source"), pybind11::arg("t_flag"),
             pybind11::arg("destination"));
  object.def("NotEqual", &pygateway::NotEqual, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("NotEqualConstant", &pygateway::NotEqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("OnlyzeroOverwriteMaximumBox",
             &pygateway::OnlyzeroOverwriteMaximumBox, "",
             pybind11::arg("source"), pybind11::arg("flag"),
             pybind11::arg("destination"));
  object.def("OnlyzeroOverwriteMaximumDiamond",
             &pygateway::OnlyzeroOverwriteMaximumDiamond, "",
             pybind11::arg("source"), pybind11::arg("flag"),
             pybind11::arg("destination"));
  object.def("ReplaceIntensities", &pygateway::ReplaceIntensities, "",
             pybind11::arg("source"), pybind11::arg("intensity_map"),
             pybind11::arg("destination"));
  object.def("ReplaceIntensity", &pygateway::ReplaceIntensity, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("input_intensity"),
             pybind11::arg("output_intensity"));
  object.def("Set", &pygateway::Set, "", pybind11::arg("source"),
             pybind11::arg("scalar") = 0);
  object.def("SetColumn", &pygateway::SetColumn, "", pybind11::arg("source"),
             pybind11::arg("column_index"), pybind11::arg("scalar") = 0);
  object.def("SetNonzeroPixelsToPixelindex",
             &pygateway::SetNonzeroPixelsToPixelindex, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("Smaller", &pygateway::Smaller, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("SmallerConstant", &pygateway::SmallerConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("SmallerOrEqual", &pygateway::SmallerOrEqual, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("SmallerOrEqualConstant", &pygateway::SmallerOrEqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("Sobel", &pygateway::Sobel, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("SubtractImageFromScalar", &pygateway::SubtractImageFromScalar, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar") = 0);
  object.def("SubtractImages", &pygateway::SubtractImages, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("SumOfAllPixels", &pygateway::SumOfAllPixels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("SumReductionX", &pygateway::SumReductionX, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("block_size"));
  object.def("SumXProjection", &pygateway::SumXProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("SumYProjection", &pygateway::SumYProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("SumZProjection", &pygateway::SumZProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("ThresholdOtsu", &pygateway::ThresholdOtsu, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("TopHatBox", &pygateway::TopHatBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x") = 0,
             pybind11::arg("radius_y") = 0, pybind11::arg("radius_z") = 0);
  object.def("VoronoiOtsuLabeling", &pygateway::VoronoiOtsuLabeling, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("sigma_spot") = 0,
             pybind11::arg("sigma_outline") = 0);

  object.doc() = R"pbdoc(
            gpu class wrapper
            -----------------------
        )pbdoc";
}
