
#include "clGateway.hpp"
#include "clImage.hpp"

auto clGateway::Create(const pybind11::tuple &shape, const cle::MemoryType &mtype) -> clImage
{
  if (pybind11::len(shape) > 3)
  {
    throw std::runtime_error("Wrong number of dimension provided. pyClesperanto does not support dimension > 3.");
  }
  std::array<size_t, 3> arr = {1, 1, 1};
  for (int i = pybind11::len(shape) - 1, j = 0; i >= 0 && j < arr.size(); --i, ++j)
  {
    //! We flip the dimensions from numpy to c++
    arr[j] = shape[i].cast<size_t>();
  }
  return this->Clesperanto::Create<float>(arr, mtype);
};

auto clGateway::Push(clGateway::ndarray_f &nd_arr, const cle::MemoryType &mtype) -> clImage
{
  pybind11::buffer_info arr = nd_arr.request();
  if (arr.ndim > 3)
  {
    throw std::runtime_error("Number of dimensions must be three or less");
  }
  std::array<size_t, 3> shape = {1, 1, 1};
  for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
  {
    //! We flip the dimensions from numpy to c++
    shape[j] = static_cast<size_t>(arr.shape[i]);
  }
  float *arr_ptr = static_cast<float *>(arr.ptr);
  std::vector<float> values(arr_ptr, arr_ptr + arr.size);
  return this->Clesperanto::Push<float>(values, shape, cle::BUFFER);
};

auto clGateway::Pull(clImage &source) -> clGateway::ndarray_f
{
  auto output = this->Clesperanto::Pull<float>(source);
  auto result = ndarray_f(output.size());
  float *ptr = static_cast<float *>(result.request().ptr);
  for (int i = 0; i < output.size(); ++i)
  {
    ptr[i] = output[i];
  }
  //! We flip the dimensions from c++ to numpy
  result.resize({source.Shape()[2], source.Shape()[1], source.Shape()[0]});
  return result.squeeze();
}

auto init_clgateway(const pybind11::module_ &m) -> void
{

  pybind11::class_<clGateway, std::shared_ptr<clGateway>> object(m,
                                                                 "clGateway");

  object.def(pybind11::init<>(), "default constructor");

  object.def("Create", &clGateway::Create, "", pybind11::arg("shape"), pybind11::arg("mtype") = cle::BUFFER);
  object.def("Push", &clGateway::Push, "", pybind11::arg("nd_arr"), pybind11::arg("mtype") = cle::BUFFER);
  object.def("Pull", &clGateway::Pull, "", pybind11::arg("image"));

  object.def("WaitForKernelToFinish", &clGateway::WaitForKernelToFinish, "",
             pybind11::arg("flag") = true);

  object.def("SelectDevice", &clGateway::SelectDevice, "",
             pybind11::arg("name") = "");

  object.def("Info", &clGateway::Info, "");

  object.def("Absolute", &clGateway::Absolute, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("AddImageAndScalar", &clGateway::AddImageAndScalar, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("AddImages", &clGateway::AddImages, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("AddImagesWeighted", &clGateway::AddImagesWeighted, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"), pybind11::arg("weight1") = 1,
             pybind11::arg("weight2") = 1);
  object.def("BinaryAnd", &clGateway::BinaryAnd, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("BinaryNot", &clGateway::BinaryNot, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("BinaryOr", &clGateway::BinaryOr, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("BinarySubtract", &clGateway::BinarySubtract, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("BinaryXor", &clGateway::BinaryXor, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("BlockEnumerate", &clGateway::BlockEnumerate, "",
             pybind11::arg("source"), pybind11::arg("sum"),
             pybind11::arg("destination"), pybind11::arg("block_size"));
  object.def("CloseIndexGapsInLabelMap", &clGateway::CloseIndexGapsInLabelMap,
             "", pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("block_size") = 4096);
  object.def("ConnectedComponentLabelingBox",
             &clGateway::ConnectedComponentLabelingBox, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("Copy", &clGateway::Copy, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("DetectMaximaBox", &clGateway::DetectMaximaBox, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("DifferenceOfGaussian", &clGateway::DifferenceOfGaussian, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("sigma1_x"), pybind11::arg("sigma1_y"),
             pybind11::arg("sigma1_z"), pybind11::arg("sigma2_x"),
             pybind11::arg("sigma2_y"), pybind11::arg("sigma2_z"));
  object.def("DilateLabels", &clGateway::DilateLabels, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("radius"));
  object.def("DilateSphere", &clGateway::DilateSphere, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("DivideImages", &clGateway::DivideImages, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("Equal", &clGateway::Equal, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("EqualConstant", &clGateway::EqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("ErodeSphere", &clGateway::ErodeSphere, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("ExtendLabelingViaVoronoi", &clGateway::ExtendLabelingViaVoronoi,
             "", pybind11::arg("source"), pybind11::arg("destination"));
  object.def("FlagExistingLabels", &clGateway::FlagExistingLabels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("GaussianBlur", &clGateway::GaussianBlur, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("sigma_x"), pybind11::arg("sigma_y"),
             pybind11::arg("sigma_z"));
  object.def("Greater", &clGateway::Greater, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("GreaterConstant", &clGateway::GreaterConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("GreaterOrEqual", &clGateway::GreaterOrEqual, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("GreaterOrEqualConstant", &clGateway::GreaterOrEqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("Histogram", &clGateway::Histogram, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("bins"),
             pybind11::arg("min_intensity") = pybind11::none(),
             pybind11::arg("max_intensity") = pybind11::none());
  object.def("Mask", &clGateway::Mask, "", pybind11::arg("source"),
             pybind11::arg("t_mask"), pybind11::arg("destination"));
  object.def("MaskedVoronoiLabeling", &clGateway::MaskedVoronoiLabeling, "",
             pybind11::arg("source"), pybind11::arg("t_mask"),
             pybind11::arg("destination"));
  object.def("MaximumBox", &clGateway::MaximumBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x"),
             pybind11::arg("radius_y"), pybind11::arg("radius_z"));
  object.def("MaximumOfAllPixels", &clGateway::MaximumOfAllPixels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MaximumXProjection", &clGateway::MaximumXProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MaximumYProjection", &clGateway::MaximumYProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MaximumZProjection", &clGateway::MaximumZProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MeanBox", &clGateway::MeanBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x"),
             pybind11::arg("radius_y"), pybind11::arg("radius_z"));
  object.def("MeanSphere", &clGateway::MeanSphere, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x"),
             pybind11::arg("radius_y"), pybind11::arg("radius_z"));
  object.def("MinimumBox", &clGateway::MinimumBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x"),
             pybind11::arg("radius_y"), pybind11::arg("radius_z"));
  object.def("MinimumOfAllPixels", &clGateway::MinimumOfAllPixels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MinimumXProjection", &clGateway::MinimumXProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MinimumYProjection", &clGateway::MinimumYProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MinimumZProjection", &clGateway::MinimumZProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("MultiplyImages", &clGateway::MultiplyImages, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("NonzeroMinimumBox", &clGateway::NonzeroMinimumBox, "",
             pybind11::arg("source"), pybind11::arg("t_flag"),
             pybind11::arg("destination"));
  object.def("NotEqual", &clGateway::NotEqual, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("NotEqualConstant", &clGateway::NotEqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("OnlyzeroOverwriteMaximumBox",
             &clGateway::OnlyzeroOverwriteMaximumBox, "",
             pybind11::arg("source"), pybind11::arg("flag"),
             pybind11::arg("destination"));
  object.def("OnlyzeroOverwriteMaximumDiamond",
             &clGateway::OnlyzeroOverwriteMaximumDiamond, "",
             pybind11::arg("source"), pybind11::arg("flag"),
             pybind11::arg("destination"));
  object.def("ReplaceIntensities", &clGateway::ReplaceIntensities, "",
             pybind11::arg("source"), pybind11::arg("intensity_map"),
             pybind11::arg("destination"));
  object.def("ReplaceIntensity", &clGateway::ReplaceIntensity, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("input_intensity"),
             pybind11::arg("output_intensity"));
  object.def("Set", &clGateway::Set, "", pybind11::arg("source"),
             pybind11::arg("scalar"));
  object.def("SetColumn", &clGateway::SetColumn, "", pybind11::arg("source"),
             pybind11::arg("column_index"), pybind11::arg("scalar"));
  object.def("SetNonzeroPixelsToPixelindex",
             &clGateway::SetNonzeroPixelsToPixelindex, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("Smaller", &clGateway::Smaller, "", pybind11::arg("source1"),
             pybind11::arg("source2"), pybind11::arg("destination"));
  object.def("SmallerConstant", &clGateway::SmallerConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("SmallerOrEqual", &clGateway::SmallerOrEqual, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("SmallerOrEqualConstant", &clGateway::SmallerOrEqualConstant, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("Sobel", &clGateway::Sobel, "", pybind11::arg("source"),
             pybind11::arg("destination"));
  object.def("SubtractImageFromScalar", &clGateway::SubtractImageFromScalar, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("scalar"));
  object.def("SubtractImages", &clGateway::SubtractImages, "",
             pybind11::arg("source1"), pybind11::arg("source2"),
             pybind11::arg("destination"));
  object.def("SumOfAllPixels", &clGateway::SumOfAllPixels, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("SumReductionX", &clGateway::SumReductionX, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("block_size"));
  object.def("SumXProjection", &clGateway::SumXProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("SumYProjection", &clGateway::SumYProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("SumZProjection", &clGateway::SumZProjection, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("ThresholdOtsu", &clGateway::ThresholdOtsu, "",
             pybind11::arg("source"), pybind11::arg("destination"));
  object.def("TopHatBox", &clGateway::TopHatBox, "", pybind11::arg("source"),
             pybind11::arg("destination"), pybind11::arg("radius_x"),
             pybind11::arg("radius_y"), pybind11::arg("radius_z"));
  object.def("VoronoiOtsuLabeling", &clGateway::VoronoiOtsuLabeling, "",
             pybind11::arg("source"), pybind11::arg("destination"),
             pybind11::arg("sigma_spot"),
             pybind11::arg("sigma_outline"));

  object.doc() = R"pbdoc(
            gpu class wrapper
            -----------------------
        )pbdoc";
}
