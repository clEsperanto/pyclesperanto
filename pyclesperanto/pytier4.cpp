
#include "pydata.hpp" 
#include "pygpu.hpp" 
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleThresholdOtsuKernel.hpp"
#include "cleConnectedComponentsLabelingBoxKernel.hpp"

using namespace cle;

void ThresholdOtsu(PyGPU& device, PyData& input, PyData& output)
{
    ThresholdOtsuKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void ConnectedComponentsLabelingBox(PyGPU& device, PyData& input, PyData& output)
{
    ConnectedComponentsLabelingBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void init_pytier4(pybind11::module_ &m) {
    
    m.def("threshold_otsu", &ThresholdOtsu, "copy data",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));    

    m.def("connected_components_labeling_box", &ConnectedComponentsLabelingBox, "connected components labeling box",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output")); 

    m.doc() = R"pbdoc(
        tier4 wrapper
        -----------------------
        threshold_otsu()
        connected_component_labelling_box()
    )pbdoc";

}
