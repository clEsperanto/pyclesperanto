
#include "pydata.hpp" 
#include "pygpu.hpp"  
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleExtendLabelingViaVoronoiKernel.hpp"
#include "cleMaximumOfAllPixelsKernel.hpp"
#include "cleMinimumOfAllPixelsKernel.hpp"
#include "cleSumOfAllPixelsKernel.hpp"
#include "cleTopHatBoxKernel.hpp"

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

void TopHatBox(PyGPU& device, PyData& input, PyData& output, float radius_x, float radius_y, float radius_z)
{
    TopHatBoxKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetRadius(radius_x, radius_y, radius_z);
    kernel.Execute();
}

void init_pytier2(pybind11::module_ &m) {
    
    m.def("extend_labeling_via_voronoi", &ExtendLabelingViaVoronoi, "Add buffer and scalar",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("maximum_of_all_pixels", &MaximumOfAllPixels, "return the maximum value of all pixels",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("minimum_of_all_pixels", &MinimumOfAllPixels, "return the minimum value of all pixels",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("sum_all_pixels", &SumOfAllPixels, "return sum values of all pixels",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"));

    m.def("top_hat_box", &TopHatBox, "perform a top hat box filter",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

    m.doc() = R"pbdoc(
        tier2 wrapper
        -----------------------
        extend_label_via_voronoi()
        maximum_all_pixels()
        minimum_all_pixels()
        sum_all_pixels()
        top_hat_box()
    )pbdoc";

}
