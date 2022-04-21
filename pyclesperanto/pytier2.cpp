
#include "pydata.hpp" 
#include "pygpu.hpp"  
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleExtendLabelingViaVoronoiKernel.hpp"
#include "cleMaximumOfAllPixelsKernel.hpp"
#include "cleMinimumOfAllPixelsKernel.hpp"
#include "cleSumOfAllPixelsKernel.hpp"

using namespace cle;

void ExtendLabelingViaVoronoi(PyGPU& device, PyData& input, PyData& output)
{
    ExtendLabelingViaVoronoiKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void MaximumOfAllPixels(PyGPU& device, PyData& input, PyData& output)
{
    MaximumOfAllPixelsKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void MinimumOfAllPixels(PyGPU& device, PyData& input, PyData& output)
{
    MinimumOfAllPixelsKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void SumOfAllPixels(PyGPU& device, PyData& input, PyData& output)
{
    SumOfAllPixelsKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.Execute();
}

void init_pytier2(pybind11::module_ &m) {
    
    m.def("extend_label_via_voronoi", &ExtendLabelingViaVoronoi, "Add buffer and scalar",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("maximum_all_pixels", &MaximumOfAllPixels, "return the maximum value of all pixels",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("minimum_all_pixels", &MinimumOfAllPixels, "return the minimum value of all pixels",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("sum_all_pixels", &SumOfAllPixels, "return sum values of all pixels",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.doc() = R"pbdoc(
        tier2 wrapper
        -----------------------
        extend_label_via_voronoi()
        maximum_all_pixels()
        minimum_all_pixels()
        sum_all_pixels()
    )pbdoc";

}
