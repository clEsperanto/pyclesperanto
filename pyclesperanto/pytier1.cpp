

#include "pydata.hpp" 
#include "pygpu.hpp"  
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleAbsoluteKernel.hpp"
#include "cleAddImageAndScalarKernel.hpp"
#include "cleAddImagesWeightedKernel.hpp"
#include "cleBinaryAndKernel.hpp"
#include "cleBinaryNotKernel.hpp"
#include "cleBinaryOrKernel.hpp"
#include "cleBinarySubtractKernel.hpp"
#include "cleBinaryXorKernel.hpp"
#include "cleBlockEnumerateKernel.hpp"
#include "cleCopyKernel.hpp"
#include "cleCustomKernel.hpp"
#include "cleDetectMaximaKernel.hpp"
#include "cleDilateSphereKernel.hpp"
#include "cleEqualConstantKernel.hpp"
#include "cleEqualKernel.hpp"
#include "cleErodeSphereKernel.hpp"
#include "cleExecuteSeparableKernel.hpp"
#include "cleExtendLabelingViaVoronoiKernel.hpp"
#include "cleFlagExistingLabelsKernel.hpp"
#include "cleGaussianBlurKernel.hpp"
#include "cleGreaterConstantKernel.hpp"
#include "cleGreaterKernel.hpp"
#include "cleGreaterOrEqualConstantKernel.hpp"
#include "cleGreaterOrEqualKernel.hpp"
#include "cleMaskKernel.hpp"
#include "cleMaximumBoxKernel.hpp"
#include "cleMaximumXProjectionKernel.hpp"
#include "cleMaximumYProjectionKernel.hpp"
#include "cleMaximumZProjectionKernel.hpp"
#include "cleMeanBoxKernel.hpp"
#include "cleMeanSphereKernel.hpp"
#include "cleMinimumBoxKernel.hpp"
#include "cleMinimumXProjectionKernel.hpp"
#include "cleMinimumYProjectionKernel.hpp"
#include "cleMinimumZProjectionKernel.hpp"
#include "cleNonzeroMinimumBoxKernel.hpp"
#include "cleNotEqualConstantKernel.hpp"
#include "cleNotEqualKernel.hpp"
#include "cleOnlyzeroOverwriteMaximumBoxKernel.hpp"
#include "cleOnlyzeroOverwriteMaximumDiamondKernel.hpp"
#include "cleReplaceIntensitiesKernel.hpp"
#include "cleReplaceIntensityKernel.hpp"
#include "cleSeparableKernel.hpp"
#include "cleSetColumnKernel.hpp"
#include "cleSetKernel.hpp"
#include "cleSetNonzeroPixelsToPixelindexKernel.hpp"
#include "cleSmallerConstantKernel.hpp"
#include "cleSmallerKernel.hpp"
#include "cleSmallerOrEqualConstantKernel.hpp"
#include "cleSmallerOrEqualKernel.hpp"
#include "cleSobelKernel.hpp"
#include "cleSumReductionXKernel.hpp"
#include "cleSumXProjectionKernel.hpp"
#include "cleSumYProjectionKernel.hpp"
#include "cleSumZProjectionKernel.hpp"

using namespace cle;

void Absolute(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    AbsoluteKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute();  
}

void AddImageAndScalar(PyGPU& device, PyData& input, PyData& output, float scalar)
{
    AddImageAndScalarKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetScalar(scalar);
    kernel.Execute();
}

void AddImagesWeighted(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst, float t_factor1, float t_factor2)
{
    AddImagesWeightedKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.SetFactor1(t_factor1);
    kernel.SetFactor2(t_factor2);
    kernel.Execute();
}

void AddImages(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    AddImagesWeighted(device, t_src1, t_src2, t_dst, 1, 1);
}

void BlockEnumerate(PyGPU& device, PyData& t_src, PyData& sum, PyData& t_dst, int t_blocksize)
{
    BlockEnumerateKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetInputSums(sum);
    kernel.SetOutput(t_dst);
    kernel.SetBlocksize(t_blocksize);
    kernel.Execute();   
}

void BinaryAnd(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    BinaryAndKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void BinaryOr(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    BinaryOrKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void BinaryNot(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    BinaryNotKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void BinarySubtract(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    BinarySubtractKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void BinaryXor(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    BinaryXorKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void Copy(PyGPU& device, PyData& input, PyData& output)
{
    CopyKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void DetectMaximaBox(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    DetectMaximaKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute();  
}

void DilateSphere(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    DilateSphereKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void ErodeSphere(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    ErodeSphereKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void Equal(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    EqualKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void EqualConstant(PyGPU& device, PyData& t_src, PyData& t_dst, float t_scalar)
{
    EqualConstantKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetScalar(t_scalar);
    kernel.Execute();
}

void FlagExistingLabels(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    FlagExistingLabelsKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void GaussianBlur(PyGPU& device, PyData& input, PyData& output, float sigma_x, float sigma_y, float sigma_z)
{
    GaussianBlurKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetSigma(sigma_x, sigma_y, sigma_z);
    kernel.Execute();
}

void Greater(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    GreaterKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void GreaterOrEqual(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    GreaterOrEqualKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void GreaterConstant(PyGPU& device, PyData& t_src, PyData& t_dst, float t_scalar)
{
    GreaterConstantKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetScalar(t_scalar);
    kernel.Execute();
}

void GreaterOrEqualConstant(PyGPU& device, PyData& t_src, PyData& t_dst, float t_scalar)
{
    GreaterOrEqualConstantKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetScalar(t_scalar);
    kernel.Execute();
}

void MaximumBox(PyGPU& device, PyData& t_src, PyData& t_dst, int t_radius_x, int t_radius_y, int t_radius_z)
{
    MaximumBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetRadius(t_radius_x, t_radius_y, t_radius_z);
    kernel.Execute();
}

void MinimumBox(PyGPU& device, PyData& t_src, PyData& t_dst, int t_radius_x, int t_radius_y, int t_radius_z)
{
    MinimumBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetRadius(t_radius_x, t_radius_y, t_radius_z);
    kernel.Execute();
}

void MeanBox(PyGPU& device, PyData& t_src, PyData& t_dst, int t_radius_x, int t_radius_y, int t_radius_z)
{
    MeanBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetRadius(t_radius_x, t_radius_y, t_radius_z);
    kernel.Execute();
}

void Mask(PyGPU& device, PyData& t_src, PyData& t_mask, PyData& t_dst)
{
    MaskKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetMask(t_mask);
    kernel.SetOutput(t_dst);
    kernel.Execute();  
}

void MaximumZProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    MaximumZProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void MaximumYProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    MaximumYProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void MaximumXProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    MaximumXProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void MinimumZProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    MinimumZProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void MinimumYProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    MinimumYProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void MinimumXProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    MinimumXProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void MeanSphere(PyGPU& device, PyData& t_src, PyData& t_dst, int t_radius_x, int t_radius_y, int t_radius_z)
{
    MeanSphereKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetRadius(t_radius_x, t_radius_y, t_radius_z);
    kernel.Execute();
}

void NonzeroMinimumBox(PyGPU& device, PyData& t_src, PyData& t_flag, PyData& t_dst)
{
    NonzeroMinimumBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetOutputFlag(t_flag);
    kernel.Execute();  
}

void NotEqual(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    NotEqualKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void NotEqualConstant(PyGPU& device, PyData& t_src, PyData& t_dst, float t_scalar)
{
    NotEqualConstantKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetScalar(t_scalar);
    kernel.Execute();
}

void OnlyzeroOverwriteMaximumBox(PyGPU& device, PyData& t_src, PyData& t_dst1, PyData& t_dst2)
{
    OnlyzeroOverwriteMaximumBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput1(t_dst1);
    kernel.SetOutput2(t_dst2);
    kernel.Execute();
}   

void OnlyzeroOverwriteMaximumDiamond(PyGPU& device, PyData& t_src, PyData& t_dst1, PyData& t_dst2)
{
    OnlyzeroOverwriteMaximumDiamondKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput1(t_dst1);
    kernel.SetOutput2(t_dst2);
    kernel.Execute();
}

void ReplaceIntensity(PyGPU& device, PyData& t_src, PyData& t_dst, float t_int_in, float t_int_out)
{
    ReplaceIntensityKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetInValue(t_int_in);
    kernel.SetOutValue(t_int_out);
    kernel.Execute(); 
}

void ReplaceIntensities(PyGPU& device, PyData& t_src, PyData& ref, PyData& t_dst)
{
    ReplaceIntensitiesKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetMap(ref);
    kernel.Execute(); 
}

void SetColumn(PyGPU& device, PyData& t_src, int t_column_idx, float t_scalar)
{
    SetColumnKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetColumn(t_column_idx);
    kernel.SetValue(t_scalar);
    kernel.Execute();   
}

void SumReductionX(PyGPU& device, PyData& t_src, PyData& t_dst, int t_blocksize)
{
    SumReductionXKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetBlocksize(t_blocksize);
    kernel.Execute();   
}

void Smaller(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    SmallerKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void SmallerOrEqual(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    SmallerOrEqualKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput1(t_src1);
    kernel.SetInput2(t_src2);
    kernel.SetOutput(t_dst);
    kernel.Execute();
}

void SmallerConstant(PyGPU& device, PyData& t_src, PyData& t_dst, float t_scalar)
{
    SmallerConstantKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetConstant(t_scalar);
    kernel.Execute();  
}

void SmallerOrEqualConstant(PyGPU& device, PyData& t_src, PyData& t_dst, float t_scalar)
{
    SmallerOrEqualConstantKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetConstant(t_scalar);
    kernel.Execute();
}

void Sobel(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    SobelKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute();  
}

void Set(PyGPU& device, PyData& t_src, float t_scalar)
{
    SetKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetValue(t_scalar);
    kernel.Execute();  
}

void SetNonzeroPixelsToPixelindex(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    SetNonzeroPixelsToPixelindexKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.SetOffset(1);
    kernel.Execute();  
}

void SumZProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    SumZProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void SumYProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    SumYProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void SumXProjection(PyGPU& device, PyData& t_src, PyData& t_dst)
{
    SumXProjectionKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(t_src);
    kernel.SetOutput(t_dst);
    kernel.Execute(); 
}

void SubtractImages(PyGPU& device, PyData& t_src1, PyData& t_src2, PyData& t_dst)
{
    AddImagesWeighted(device, t_src1, t_src2, t_dst, 1, -1);
}




void init_pytier1(pybind11::module_ &m) {
        
    m.def("absolute", &Absolute, "compute absolute values",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("add_image_and_scalar", &AddImageAndScalar, "add scalar value to image",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("add_images_weighted", &AddImagesWeighted, "add images with weight",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"), pybind11::arg("scalar0"), pybind11::arg("scalar1"));
    
    m.def("add_images", &AddImages, "add images",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("block_enumerate", &BlockEnumerate, "",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("sums"), pybind11::arg("output"), pybind11::arg("blocksize"));
    
    m.def("binary_and", &BinaryAnd, "binary and operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("binary_or", &BinaryOr, "binary or operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("binary_not", &BinaryNot, "binary not operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("binary_subtract", &BinarySubtract, "binary subtract operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("binary_xor", &BinaryXor, "binary xor operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("copy", &Copy, "copy",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("detect_maxima_box", &DetectMaximaBox, "detect maxima",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("dilate_sphere", &DilateSphere, "dilate sphere",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("erode_sphere", &ErodeSphere, "erode sphere",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("equal", &Equal, "equal binary operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("equal_constant", &EqualConstant, "equal constant binary operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("flag_existing_labels", &FlagExistingLabels, "list existing label values",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("gaussian_blur", &GaussianBlur, "gaussian blur filter",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("sigma_x"), pybind11::arg("sigma_y"), pybind11::arg("sigma_z"));
    
    m.def("greater", &Greater, "greater binary operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("greater_or_equal", &GreaterOrEqual, "greater or equal binary operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("greater_constant", &GreaterConstant, "greater than constant binary operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("greater_or_equal_constant", &GreaterOrEqualConstant, "greater or equal constant binary operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("maximum_box", &MaximumBox, "maximum box filter",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("radiux_x"), pybind11::arg("radiux_y"), pybind11::arg("radiux_z"));
    
    m.def("minimum_box", &MinimumBox, "minimum box filter",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("radiux_x"), pybind11::arg("radiux_y"), pybind11::arg("radiux_z"));
    
    m.def("mean_box", &MeanBox, "mean box filter",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("radiux_x"), pybind11::arg("radiux_y"), pybind11::arg("radiux_z"));
    
    m.def("mask", &Mask, "mask",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("mask"), pybind11::arg("output"));
    
    m.def("maximum_z_projection", &MaximumZProjection, "maximum z projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("maximum_y_projection", &MaximumYProjection, "maximum y projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("maximum_x_projection", &MaximumXProjection, "maximum x projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("minimum_z_projection", &MinimumZProjection, "minimum z projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("minimum_y_projection", &MinimumYProjection, "minimum y projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("minimum_x_projection", &MinimumXProjection, "minimum x projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("mean_sphere", &MeanSphere, "mean sphere",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("radiux_x"), pybind11::arg("radiux_y"), pybind11::arg("radiux_z"));
    
    m.def("nonzero_minimum_box", &NonzeroMinimumBox, "non-zero minimum value box",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("flag"), pybind11::arg("output"));
    
    m.def("not_equal", &NotEqual, "not equal binary operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("not_equal_constant", &NotEqualConstant, "not equal constant binary operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("onlyzero_overwrite_maximum_box", &OnlyzeroOverwriteMaximumBox, "overwrite zero value pixel with maximum local pixel box",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("flag"), pybind11::arg("output"));
    
    m.def("onlyzero_overwrite_maximum_diamond", &OnlyzeroOverwriteMaximumDiamond, "overwrite zero value pixel with maximum local pixel diamond",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("flag"), pybind11::arg("output"));
    
    m.def("replace_intensity", &ReplaceIntensity, "replace intensity",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar0"), pybind11::arg("scalar1"));
    
    m.def("replace_intensities", &ReplaceIntensities, "replace intensities using intensity map",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("map"), pybind11::arg("output"));
    
    m.def("set_column", &SetColumn, "set column with value",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("column"), pybind11::arg("scalar"));
    
    m.def("sum_reduction_x", &SumReductionX, "sum reduction along x",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("blocksize"));
    
    m.def("smaller", &Smaller, "smaller binary operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("smaller_or_equal", &SmallerOrEqual, "smaller or equal binary operation",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));
    
    m.def("smaller_constant", &SmallerConstant, "smaller constant binary operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("smaller_or_equal_constant", &SmallerOrEqualConstant, "smaller or equal const binary operation",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar"));
    
    m.def("sobel", &Sobel, "sobel edge filter",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("set", &Set, "set value",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("scalar"));
    
    m.def("set_nonzero_pixels_to_pixelindex", &SetNonzeroPixelsToPixelindex, "",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("sum_z_projection", &SumZProjection, "sum z projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("sum_y_projection", &SumYProjection, "sum y projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("sum_x_projection", &SumXProjection, "sum x projection",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));
    
    m.def("subtract_images", &SubtractImages, "subtract images",
        pybind11::arg("device"), pybind11::arg("input1"), pybind11::arg("input2"), pybind11::arg("output"));

    m.doc() = R"pbdoc(
        tier1 wrapper
        -----------------------
        absolute()
        add_image_and_scalar()
        add_images_weighted()
        add_images()
        block_enumerate()
        binary_and()
        binary_or()
        binary_not()
        binary_subtract()
        binary_xor()
        copy()
        detect_maxima_box()
        dilate_sphere()
        erode_sphere()
        equal()
        equal_constant()
        flag_existing_labels()
        gaussian_blur()
        greater()
        greater_or_equal()
        greater_constant()
        greater_or_equal_constant()
        maximum_box()
        minimum_box()
        mean_box()
        mask()
        maximum_z_projection()
        maximum_y_projection()
        maximum_x_projection()
        minimum_z_projection()
        minimum_y_projection()
        minimum_x_projection()
        mean_sphere()
        nonzero_minimum_box()
        not_equal()
        not_equal_constant()
        onlyzero_overwrite_maximum_box()
        onlyzero_overwrite_maximum_diamond()
        replace_intensity()
        replace_intensities()
        set_column()
        sum_reduction_x()
        smaller()
        smaller_or_equal()
        smaller_constant()
        smaller_or_equal_constant()
        sobel()
        set()
        set_nonzero_pixels_to_pixelindex()
        sum_z_projection()
        sum_y_projection()
        sum_x_projection()
        subtract_images()
    )pbdoc";

}
