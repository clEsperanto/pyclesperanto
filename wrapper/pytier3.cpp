
#include "pydata.hpp" 
#include "pygpu.hpp" 
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleCloseIndexGapsInLabelMapKernel.hpp"
#include "cleDifferenceOfGaussianKernel.hpp"
#include "cleHistogramKernel.hpp"

using namespace cle;

void CloseIndexGapsInLabelMap(PyGPU& device, PyData& input, PyData& output, int scalar)
{
    CloseIndexGapsInLabelMapKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetBlockSize(scalar);
    kernel.Execute();
}

void DifferenceOfGaussian(PyGPU& device, PyData& input, PyData& output, float sigma1_x, float sigma1_y, float sigma1_z, float sigma2_x, float sigma2_y, float sigma2_z)
{
    DifferenceOfGaussianKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetSigma1(sigma1_x, sigma1_y, sigma1_z);
    kernel.SetSigma2(sigma2_x, sigma2_y, sigma2_z);
    kernel.Execute();
}

void Histogram(PyGPU& device, PyData& input, PyData& output, int bins)
{
    HistogramKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetSteps(1, 1, 1);
    kernel.SetNumBins(bins);
    // kernel.SetMinimumIntensity(min);
    // kernel.SetMaximumIntensity(max);
    kernel.Execute();
}

void init_pytier3(pybind11::module_ &m) {
    
    m.def("close_index_gaps_in_labelmap", &CloseIndexGapsInLabelMap, "re-map label into continuous values",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), 
        pybind11::arg("scalar"));

    m.def("difference_of_gaussian", &DifferenceOfGaussian, "Apply a difference of gaussian",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"),
        pybind11::arg("sigma1_x"), pybind11::arg("sigma1_y"), pybind11::arg("sigma1_z"),
        pybind11::arg("sigma2_x"), pybind11::arg("sigma2_y"), pybind11::arg("sigma2_z"));

    m.def("histogram", &Histogram, "return the histogram",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("bins"));

    m.doc() = R"pbdoc(
        tier1 wrapper
        -----------------------
        close_index_gaps_in_labelmap()
        differnce_of_gaussian()
        histogram()
    )pbdoc";

}
