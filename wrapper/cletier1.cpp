#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier1(pybind11::module_ &m) -> void
{
      m.def("_AbsoluteKernel_Call", &cle::AbsoluteKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"));

      m.def("_AddImageAndScalarKernel_Call", &cle::AddImageAndScalarKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_AddImagesWeightedKernel_Call", &cle::AddImagesWeightedKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"), pybind11::arg("weight1"), pybind11::arg("weight2"));

      m.def("_BinaryAndKernel_Call", &cle::BinaryAndKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_BinaryNotKernel_Call", &cle::BinaryNotKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"));

      m.def("_BinaryOrKernel_Call", &cle::BinaryOrKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_BinarySubtractKernel_Call", &cle::BinarySubtractKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_BinaryXorKernel_Call", &cle::BinaryXorKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_BlockEnumerateKernel_Call", &cle::BlockEnumerateKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("sum"), pybind11::arg("dst"), pybind11::arg("block_size"));

      m.def("_CopyKernel_Call", &cle::CopyKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"));

      m.def("_DilateSphereKernel_Call", &cle::DilateSphereKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_DivideImagesKernel_Call", &cle::DivideImagesKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_EqualKernel_Call", &cle::EqualKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_EqualConstantKernel_Call", &cle::EqualConstantKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_ErodeSphereKernel_Call", &cle::ErodeSphereKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      // m.def("_FlagExistingLabelsKernel_Call", &cle::FlagExistingLabelsKernel_Call, "", pybind11::arg("device"),
      //       pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_GaussianBlurKernel_Call", &cle::GaussianBlurKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("sigma_x"), pybind11::arg("sigma_y"), pybind11::arg("sigma_z"));

      m.def("_GreaterKernel_Call", &cle::GreaterKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_GreaterConstantKernel_Call", &cle::GreaterConstantKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_GreaterOrEqualKernel_Call", &cle::GreaterOrEqualKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_GreaterOrEqualConstantKernel_Call", &cle::GreaterOrEqualConstantKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_MaskKernel_Call", &cle::MaskKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("t_mask"), pybind11::arg("dst"));

      m.def("_MaximumBoxKernel_Call", &cle::MaximumBoxKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

      m.def("_MaximumXProjectionKernel_Call", &cle::MaximumXProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MaximumYProjectionKernel_Call", &cle::MaximumYProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MaximumZProjectionKernel_Call", &cle::MaximumZProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MeanBoxKernel_Call", &cle::MeanBoxKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

      m.def("_MeanSphereKernel_Call", &cle::MeanSphereKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

      m.def("_MinimumBoxKernel_Call", &cle::MinimumBoxKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

      m.def("_MinimumXProjectionKernel_Call", &cle::MinimumXProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MinimumYProjectionKernel_Call", &cle::MinimumYProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MinimumZProjectionKernel_Call", &cle::MinimumZProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MultiplyImagesKernel_Call", &cle::MultiplyImagesKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_NonzeroMinimumBoxKernel_Call", &cle::NonzeroMinimumBoxKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("t_flag"), pybind11::arg("dst"));

      m.def("_NotEqualKernel_Call", &cle::NotEqualKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_NotEqualConstantKernel_Call", &cle::NotEqualConstantKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_OnlyzeroOverwriteMaximumBoxKernel_Call",
            &cle::OnlyzeroOverwriteMaximumBoxKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("flag"), pybind11::arg("dst"));

      m.def("_OnlyzeroOverwriteMaximumDiamondKernel_Call",
            &cle::OnlyzeroOverwriteMaximumDiamondKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("flag"), pybind11::arg("dst"));

      m.def("_ReplaceIntensitiesKernel_Call", &cle::ReplaceIntensitiesKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("intensity_map"), pybind11::arg("dst"));

      m.def("_ReplaceIntensityKernel_Call", &cle::ReplaceIntensityKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("input_intensity"), pybind11::arg("output_intensity"));

      m.def("_SetKernel_Call", &cle::SetKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("scalar"));

      m.def("_SetColumnKernel_Call", &cle::SetColumnKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("column_index"), pybind11::arg("scalar"));

      m.def("_SetNonzeroPixelsToPixelindexKernel_Call", &cle::SetNonzeroPixelsToPixelindexKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

      m.def("_SmallerKernel_Call", &cle::SmallerKernel_Call, "", pybind11::arg("device"), pybind11::arg("src1"),
            pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_SmallerConstantKernel_Call", &cle::SmallerConstantKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_SmallerOrEqualKernel_Call", &cle::SmallerOrEqualKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src1"), pybind11::arg("src2"), pybind11::arg("dst"));

      m.def("_SmallerOrEqualConstantKernel_Call", &cle::SmallerOrEqualConstantKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_SobelKernel_Call", &cle::SobelKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"));

      m.def("_SubtractImageFromScalarKernel_Call", &cle::SubtractImageFromScalarKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("scalar"));

      m.def("_SumReductionXKernel_Call", &cle::SumReductionXKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("block_size"));

      m.def("_SumXProjectionKernel_Call", &cle::SumXProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_SumYProjectionKernel_Call", &cle::SumYProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_SumZProjectionKernel_Call", &cle::SumZProjectionKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));
}