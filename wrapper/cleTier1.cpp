#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"
#include <pybind11/stl.h>

#include <variant>

auto std_variant(pybind11::handle obj) -> std::variant<cle::Image, float, int>
{
	if (pybind11::isinstance<pybind11::int_>(obj))
	{
		return pybind11::cast<int>(obj);
	}
	else if (pybind11::isinstance<pybind11::float_>(obj))
	{
		return pybind11::cast<float>(obj);
	}
	else if (pybind11::isinstance<cle::Image>(obj))
	{
		return pybind11::cast<cle::Image>(obj);
	}
	else
	{
		throw std::runtime_error("Error: Unsupported type.");
	}
}

auto init_cletier1(pybind11::module_ &m) -> void
{
	m.def("_std_variant", &std_variant, "Convert pybind11::handle to std::variant<cle::Image, float, int>");

	m.def("_CustomKernel_Call", &cle::CustomKernel_Call, "Call CustomKernel_call from C++.",
		  pybind11::arg("device"), pybind11::arg("file_name"), pybind11::arg("kernel_name"), pybind11::arg("dx"), pybind11::arg("dy"), pybind11::arg("dz"), pybind11::arg("parameters"));

	m.def("_AbsoluteKernel_Call", &cle::AbsoluteKernel_Call, "Call AbsoluteKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_AddImageAndScalarKernel_Call", &cle::AddImageAndScalarKernel_Call, "Call AddImageAndScalarKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_AddImagesWeightedKernel_Call", &cle::AddImagesWeightedKernel_Call, "Call AddImagesWeightedKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"), pybind11::arg("w1"), pybind11::arg("w2"));

	m.def("_BinaryAndKernel_Call", &cle::BinaryAndKernel_Call, "Call BinaryAndKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_BinaryNotKernel_Call", &cle::BinaryNotKernel_Call, "Call BinaryNotKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_BinaryOrKernel_Call", &cle::BinaryOrKernel_Call, "Call BinaryOrKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_BinarySubtractKernel_Call", &cle::BinarySubtractKernel_Call, "Call BinarySubtractKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_BinaryXorKernel_Call", &cle::BinaryXorKernel_Call, "Call BinaryXorKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_BlockEnumerateKernel_Call", &cle::BlockEnumerateKernel_Call, "Call BlockEnumerateKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("sum"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_ConvolveKernel_Call", &cle::ConvolveKernel_Call, "Call ConvolveKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("convolve_kernel"), pybind11::arg("dst"));

	m.def("_CopyKernel_Call", &cle::CopyKernel_Call, "Call CopyKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_CropKernel_Call", &cle::CropKernel_Call, "Call CropKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("index0"), pybind11::arg("index1"), pybind11::arg("index2"));

	m.def("_DetectMaximaKernel_Call", &cle::DetectMaximaKernel_Call, "Call DetectMaximaKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_DilateSphereKernel_Call", &cle::DilateSphereKernel_Call, "Call DilateSphereKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_DivideImagesKernel_Call", &cle::DivideImagesKernel_Call, "Call DivideImagesKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_EqualConstantKernel_Call", &cle::EqualConstantKernel_Call, "Call EqualConstantKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_EqualKernel_Call", &cle::EqualKernel_Call, "Call EqualKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_ErodeSphereKernel_Call", &cle::ErodeSphereKernel_Call, "Call ErodeSphereKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_FlagExistingLabelsKernel_Call", &cle::FlagExistingLabelsKernel_Call, "Call FlagExistingLabelsKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_GaussianBlurKernel_Call", &cle::GaussianBlurKernel_Call, "Call GaussianBlurKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("sigma_x"), pybind11::arg("sigma_y"), pybind11::arg("sigma_z"));

	m.def("_GradientXKernel_Call", &cle::GradientXKernel_Call, "Call GradientXKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_GradientYKernel_Call", &cle::GradientYKernel_Call, "Call GradientYKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_GradientZKernel_Call", &cle::GradientZKernel_Call, "Call GradientZKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_GreaterConstantKernel_Call", &cle::GreaterConstantKernel_Call, "Call GreaterConstantKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_GreaterKernel_Call", &cle::GreaterKernel_Call, "Call GreaterKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_GreaterOrEqualConstantKernel_Call", &cle::GreaterOrEqualConstantKernel_Call, "Call GreaterOrEqualConstantKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_GreaterOrEqualKernel_Call", &cle::GreaterOrEqualKernel_Call, "Call GreaterOrEqualKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_MaskKernel_Call", &cle::MaskKernel_Call, "Call MaskKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("mask"), pybind11::arg("dst"));

	m.def("_MaximumBoxKernel_Call", &cle::MaximumBoxKernel_Call, "Call MaximumBoxKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

	m.def("_MaximumXProjectionKernel_Call", &cle::MaximumXProjectionKernel_Call, "Call MaximumXProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_MaximumYProjectionKernel_Call", &cle::MaximumYProjectionKernel_Call, "Call MaximumYProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_MaximumZProjectionKernel_Call", &cle::MaximumZProjectionKernel_Call, "Call MaximumZProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_MeanBoxKernel_Call", &cle::MeanBoxKernel_Call, "Call MeanBoxKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

	m.def("_MeanSphereKernel_Call", &cle::MeanSphereKernel_Call, "Call MeanSphereKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

	m.def("_MinimumBoxKernel_Call", &cle::MinimumBoxKernel_Call, "Call MinimumBoxKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

	m.def("_MinimumXProjectionKernel_Call", &cle::MinimumXProjectionKernel_Call, "Call MinimumXProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_MinimumYProjectionKernel_Call", &cle::MinimumYProjectionKernel_Call, "Call MinimumYProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_MinimumZProjectionKernel_Call", &cle::MinimumZProjectionKernel_Call, "Call MinimumZProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_MultiplyImageAndScalarKernel_Call", &cle::MultiplyImageAndScalarKernel_Call, "Call MultiplyImageAndScalarKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_MultiplyImagesKernel_Call", &cle::MultiplyImagesKernel_Call, "Call MultiplyImagesKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_NonzeroMinimumBoxKernel_Call", &cle::NonzeroMinimumBoxKernel_Call, "Call NonzeroMinimumBoxKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("flag"));

	m.def("_NotEqualConstantKernel_Call", &cle::NotEqualConstantKernel_Call, "Call NotEqualConstantKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_NotEqualKernel_Call", &cle::NotEqualKernel_Call, "Call NotEqualKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_OnlyzeroOverwriteMaximumBoxKernel_Call", &cle::OnlyzeroOverwriteMaximumBoxKernel_Call, "Call OnlyzeroOverwriteMaximumBoxKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst1"), pybind11::arg("dst2"));

	m.def("_OnlyzeroOverwriteMaximumDiamondKernel_Call", &cle::OnlyzeroOverwriteMaximumDiamondKernel_Call, "Call OnlyzeroOverwriteMaximumDiamondKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst1"), pybind11::arg("dst2"));

	m.def("_PowerImagesKernel_Call", &cle::PowerImagesKernel_Call, "Call PowerImagesKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_PowerKernel_Call", &cle::PowerKernel_Call, "Call PowerKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

	m.def("_ReplaceIntensitiesKernel_Call", &cle::ReplaceIntensitiesKernel_Call, "Call ReplaceIntensitiesKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("map"));

	m.def("_ReplaceIntensityKernel_Call", &cle::ReplaceIntensityKernel_Call, "Call ReplaceIntensityKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("in_value"), pybind11::arg("out_value"));

	m.def("_SetColumnKernel_Call", &cle::SetColumnKernel_Call, "Call SetColumnKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("index"), pybind11::arg("value"));

	m.def("_SetKernel_Call", &cle::SetKernel_Call, "Call SetKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("value"));

	m.def("_SetNonzeroPixelsToPixelindexKernel_Call", &cle::SetNonzeroPixelsToPixelindexKernel_Call, "Call SetNonzeroPixelsToPixelindexKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_SmallerConstantKernel_Call", &cle::SmallerConstantKernel_Call, "Call SmallerConstantKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_SmallerKernel_Call", &cle::SmallerKernel_Call, "Call SmallerKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_SmallerOrEqualConstantKernel_Call", &cle::SmallerOrEqualConstantKernel_Call, "Call SmallerOrEqualConstantKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_SmallerOrEqualKernel_Call", &cle::SmallerOrEqualKernel_Call, "Call SmallerOrEqualKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

	m.def("_SobelKernel_Call", &cle::SobelKernel_Call, "Call SobelKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_SubtractImageFromScalarKernel_Call", &cle::SubtractImageFromScalarKernel_Call, "Call SubtractImageFromScalarKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_SumReductionXKernel_Call", &cle::SumReductionXKernel_Call, "Call SumReductionXKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

	m.def("_SumXProjectionKernel_Call", &cle::SumXProjectionKernel_Call, "Call SumXProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_SumYProjectionKernel_Call", &cle::SumYProjectionKernel_Call, "Call SumYProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));

	m.def("_SumZProjectionKernel_Call", &cle::SumZProjectionKernel_Call, "Call SumZProjectionKernel_Call from C++.",
		  pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));
}