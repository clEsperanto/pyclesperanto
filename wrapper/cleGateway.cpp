
// #include "pyclesperanto.hpp"

// #include "cleGateway.hpp"
// #include "cleImage.hpp"

// auto cleGateway::Create(const pybind11::tuple &shape, const cle::MemoryType &mtype) -> cle::Image
// {
//   if (pybind11::len(shape) > 3)
//   {
//     throw std::runtime_error("Wrong number of dimension provided. pyClesperanto does not support dimension > 3.");
//   }
//   std::array<size_t, 3> arr = {1, 1, 1};
//   for (int i = pybind11::len(shape) - 1, j = 0; i >= 0 && j < arr.size(); --i, ++j)
//   {
//     //! We flip the dimensions from numpy to c++
//     arr[j] = shape[i].cast<size_t>();
//   }
//   return this->Clesperanto::Create<float>(arr, mtype);
// };

// auto cleGateway::Push(const cleGateway::ndarray_f &nd_arr, const cle::MemoryType &mtype) -> cle::Image
// {
//   pybind11::buffer_info arr = nd_arr.request();
//   if (arr.ndim > 3)
//   {
//     throw std::runtime_error("Number of dimensions must be three or less");
//   }
//   std::array<size_t, 3> shape = {1, 1, 1};
//   for (int i = arr.ndim - 1, j = 0; i >= 0 && j < shape.size(); --i, ++j)
//   {
//     //! We flip the dimensions from numpy to c++
//     shape[j] = static_cast<size_t>(arr.shape[i]);
//   }
//   float *arr_ptr = static_cast<float *>(arr.ptr);
//   std::vector<float> values(arr_ptr, arr_ptr + arr.size);
//   return this->Clesperanto::Push<float>(values, shape, mtype);
// };

// auto cleGateway::Pull(const cle::Image &source) -> cleGateway::ndarray_f
// {
//   auto output = this->Clesperanto::Pull<float>(source);
//   auto result = ndarray_f(output.size());
//   float *ptr = static_cast<float *>(result.request().ptr);
//   for (int i = 0; i < output.size(); ++i)
//   {
//     ptr[i] = output[i];
//   }
//   //! We flip the dimensions from c++ to numpy
//   result.resize({source.Shape()[2], source.Shape()[1], source.Shape()[0]});
//   return result.squeeze();
// }

// auto init_clegateway(pybind11::module_ &m) -> void
// {

//   pybind11::class_<cleGateway, std::shared_ptr<cleGateway>> object(m,
//                                                                    "cleGateway");

//   object.def(pybind11::init<>(), "default constructor");

//   object.def("Create", &cleGateway::Create, "", pybind11::arg("shape"), pybind11::arg("mtype"));
//   object.def("Push", &cleGateway::Push, "", pybind11::arg("nd_arr"), pybind11::arg("mtype"));
//   object.def("Pull", &cleGateway::Pull, "", pybind11::arg("image"));

//   object.def("WaitForKernelToFinish", &cleGateway::WaitForKernelToFinish, "",
//              pybind11::arg("flag") = true);

//   object.def("SelectDevice", &cleGateway::SelectDevice, "",
//              pybind11::arg("name"));

//   object.def("GetDevice", &cleGateway::GetDevice, "");

//   object.def("Info", &cleGateway::Info, "");

//   object.def("Absolute", &cleGateway::Absolute, "", pybind11::arg("source"),
//              pybind11::arg("destination"));
//   object.def("AddImageAndScalar", &cleGateway::AddImageAndScalar, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("AddImages", &cleGateway::AddImages, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("AddImagesWeighted", &cleGateway::AddImagesWeighted, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"), pybind11::arg("weight1") = 1,
//              pybind11::arg("weight2") = 1);
//   object.def("BinaryAnd", &cleGateway::BinaryAnd, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("BinaryNot", &cleGateway::BinaryNot, "", pybind11::arg("source"),
//              pybind11::arg("destination"));
//   object.def("BinaryOr", &cleGateway::BinaryOr, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("BinarySubtract", &cleGateway::BinarySubtract, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"));
//   object.def("BinaryXor", &cleGateway::BinaryXor, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("BlockEnumerate", &cleGateway::BlockEnumerate, "",
//              pybind11::arg("source"), pybind11::arg("sum"),
//              pybind11::arg("destination"), pybind11::arg("block_size"));
//   object.def("CloseIndexGapsInLabelMap", &cleGateway::CloseIndexGapsInLabelMap,
//              "", pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("block_size") = 4096);
//   object.def("ConnectedComponentLabelingBox",
//              &cleGateway::ConnectedComponentLabelingBox, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("Copy", &cleGateway::Copy, "", pybind11::arg("source"),
//              pybind11::arg("destination"));
//   object.def("DetectMaximaBox", &cleGateway::DetectMaximaBox, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("DifferenceOfGaussian", &cleGateway::DifferenceOfGaussian, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("sigma1_x"), pybind11::arg("sigma1_y"),
//              pybind11::arg("sigma1_z"), pybind11::arg("sigma2_x"),
//              pybind11::arg("sigma2_y"), pybind11::arg("sigma2_z"));
//   object.def("DilateLabels", &cleGateway::DilateLabels, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("radius"));
//   object.def("DilateSphere", &cleGateway::DilateSphere, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("DivideImages", &cleGateway::DivideImages, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"));
//   object.def("Equal", &cleGateway::Equal, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("EqualConstant", &cleGateway::EqualConstant, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("ErodeSphere", &cleGateway::ErodeSphere, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("ExtendLabelingViaVoronoi", &cleGateway::ExtendLabelingViaVoronoi,
//              "", pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("FlagExistingLabels", &cleGateway::FlagExistingLabels, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("GaussianBlur", &cleGateway::GaussianBlur, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("sigma_x"), pybind11::arg("sigma_y"),
//              pybind11::arg("sigma_z"));
//   object.def("Greater", &cleGateway::Greater, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("GreaterConstant", &cleGateway::GreaterConstant, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("GreaterOrEqual", &cleGateway::GreaterOrEqual, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"));
//   object.def("GreaterOrEqualConstant", &cleGateway::GreaterOrEqualConstant, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("Histogram", &cleGateway::Histogram, "", pybind11::arg("source"),
//              pybind11::arg("destination"), pybind11::arg("bins"),
//              pybind11::arg("min_intensity") = pybind11::none(),
//              pybind11::arg("max_intensity") = pybind11::none());
//   object.def("Mask", &cleGateway::Mask, "", pybind11::arg("source"),
//              pybind11::arg("t_mask"), pybind11::arg("destination"));
//   object.def("MaskedVoronoiLabeling", &cleGateway::MaskedVoronoiLabeling, "",
//              pybind11::arg("source"), pybind11::arg("t_mask"),
//              pybind11::arg("destination"));
//   object.def("MaximumBox", &cleGateway::MaximumBox, "", pybind11::arg("source"),
//              pybind11::arg("destination"), pybind11::arg("radius_x"),
//              pybind11::arg("radius_y"), pybind11::arg("radius_z"));
//   object.def("MaximumOfAllPixels", &cleGateway::MaximumOfAllPixels, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MaximumXProjection", &cleGateway::MaximumXProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MaximumYProjection", &cleGateway::MaximumYProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MaximumZProjection", &cleGateway::MaximumZProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MeanBox", &cleGateway::MeanBox, "", pybind11::arg("source"),
//              pybind11::arg("destination"), pybind11::arg("radius_x"),
//              pybind11::arg("radius_y"), pybind11::arg("radius_z"));
//   object.def("MeanSphere", &cleGateway::MeanSphere, "", pybind11::arg("source"),
//              pybind11::arg("destination"), pybind11::arg("radius_x"),
//              pybind11::arg("radius_y"), pybind11::arg("radius_z"));
//   object.def("MinimumBox", &cleGateway::MinimumBox, "", pybind11::arg("source"),
//              pybind11::arg("destination"), pybind11::arg("radius_x"),
//              pybind11::arg("radius_y"), pybind11::arg("radius_z"));
//   object.def("MinimumOfAllPixels", &cleGateway::MinimumOfAllPixels, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MinimumXProjection", &cleGateway::MinimumXProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MinimumYProjection", &cleGateway::MinimumYProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MinimumZProjection", &cleGateway::MinimumZProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("MultiplyImages", &cleGateway::MultiplyImages, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"));
//   object.def("NonzeroMinimumBox", &cleGateway::NonzeroMinimumBox, "",
//              pybind11::arg("source"), pybind11::arg("t_flag"),
//              pybind11::arg("destination"));
//   object.def("NotEqual", &cleGateway::NotEqual, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("NotEqualConstant", &cleGateway::NotEqualConstant, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("OnlyzeroOverwriteMaximumBox",
//              &cleGateway::OnlyzeroOverwriteMaximumBox, "",
//              pybind11::arg("source"), pybind11::arg("flag"),
//              pybind11::arg("destination"));
//   object.def("OnlyzeroOverwriteMaximumDiamond",
//              &cleGateway::OnlyzeroOverwriteMaximumDiamond, "",
//              pybind11::arg("source"), pybind11::arg("flag"),
//              pybind11::arg("destination"));
//   object.def("ReplaceIntensities", &cleGateway::ReplaceIntensities, "",
//              pybind11::arg("source"), pybind11::arg("intensity_map"),
//              pybind11::arg("destination"));
//   object.def("ReplaceIntensity", &cleGateway::ReplaceIntensity, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("input_intensity"),
//              pybind11::arg("output_intensity"));
//   object.def("Set", &cleGateway::Set, "", pybind11::arg("source"),
//              pybind11::arg("scalar"));
//   object.def("SetColumn", &cleGateway::SetColumn, "", pybind11::arg("source"),
//              pybind11::arg("column_index"), pybind11::arg("scalar"));
//   object.def("SetNonzeroPixelsToPixelindex",
//              &cleGateway::SetNonzeroPixelsToPixelindex, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("Smaller", &cleGateway::Smaller, "", pybind11::arg("source1"),
//              pybind11::arg("source2"), pybind11::arg("destination"));
//   object.def("SmallerConstant", &cleGateway::SmallerConstant, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("SmallerOrEqual", &cleGateway::SmallerOrEqual, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"));
//   object.def("SmallerOrEqualConstant", &cleGateway::SmallerOrEqualConstant, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("Sobel", &cleGateway::Sobel, "", pybind11::arg("source"),
//              pybind11::arg("destination"));
//   object.def("SubtractImageFromScalar", &cleGateway::SubtractImageFromScalar, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("scalar"));
//   object.def("SubtractImages", &cleGateway::SubtractImages, "",
//              pybind11::arg("source1"), pybind11::arg("source2"),
//              pybind11::arg("destination"));
//   object.def("SumOfAllPixels", &cleGateway::SumOfAllPixels, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("SumReductionX", &cleGateway::SumReductionX, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("block_size"));
//   object.def("SumXProjection", &cleGateway::SumXProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("SumYProjection", &cleGateway::SumYProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("SumZProjection", &cleGateway::SumZProjection, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("ThresholdOtsu", &cleGateway::ThresholdOtsu, "",
//              pybind11::arg("source"), pybind11::arg("destination"));
//   object.def("TopHatBox", &cleGateway::TopHatBox, "", pybind11::arg("source"),
//              pybind11::arg("destination"), pybind11::arg("radius_x"),
//              pybind11::arg("radius_y"), pybind11::arg("radius_z"));
//   object.def("VoronoiOtsuLabeling", &cleGateway::VoronoiOtsuLabeling, "",
//              pybind11::arg("source"), pybind11::arg("destination"),
//              pybind11::arg("sigma_spot"),
//              pybind11::arg("sigma_outline"));

//   object.doc() = R"pbdoc(
//             gpu class wrapper
//             -----------------------
//         )pbdoc";
// }
