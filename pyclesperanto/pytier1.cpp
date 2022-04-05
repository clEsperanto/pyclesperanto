

#include "cleObject.hpp"
#include "cleGPU.hpp"

#include "cleAddImageAndScalarKernel.hpp"
#include "cleGaussianBlurKernel.hpp"
#include "cleMaximumOfAllPixelsKernel.hpp"
#include "cleConnectedComponentsLabelingBoxKernel.hpp"
#include "cleCopyKernel.hpp"

#include "pygpu.hpp"  // todo: find a cleaner way to call the class PyGPU
#include "pyclesperanto.hpp"

using namespace cle;




void AddImageAndScalar(PyGPU& device, Object& input, Object& output, float scalar)
{
    AddImageAndScalarKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetScalar(scalar);
    kernel.Execute();
}


void GaussianBlur(PyGPU& device, Object& input, Object& output, float simga_x, float sigma_y, float sigma_z)
{
    GaussianBlurKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetSigma(simga_x, sigma_y, sigma_z);
    kernel.Execute();
}


void MaximumOfAllPixels(PyGPU& device, Object& input, Object& output)
{
    MaximumOfAllPixelsKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void Copy(PyGPU& device, Object& input, Object& output)
{
    CopyKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void ConnectedComponentsLabelingBox(PyGPU& device, Object& input, Object& output)
{
    ConnectedComponentsLabelingBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

// PYBIND11_MODULE(_tier1, m) {
void init_pytier1(pybind11::module_ &m) {
    
    m.def("add_image_and_scalar", &AddImageAndScalar, "Add buffer and scalar",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("scalar") =0);

    m.def("gaussian_blur", &GaussianBlur, "Apply gaussian blur",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("simga_x") =0, pybind11::arg("simga_y") =0, pybind11::arg("simga_z") =0);

    m.def("maximum_all_pixels", &MaximumOfAllPixels, "return maximum pixel value",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("copy", &Copy, "copy data",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));    

    m.def("connected_component_labelling_box", &ConnectedComponentLabellingBox, "copy data",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output")); 

    m.doc() = R"pbdoc(
        tier1 wrapper
        -----------------------
        add_image_and_scalar()
        maximum_all_pixels()
        gaussian_blur()
        copy()
        connected_component_labelling_box()
    )pbdoc";

}
