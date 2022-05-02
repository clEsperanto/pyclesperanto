
#include "pydata.hpp" 
#include "pygpu.hpp" 
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleVoronoiOtsuLabelingKernel.hpp"

using namespace cle;

void VoronoiOtsuLabeling(PyGPU& device, PyData& input, PyData& output, float spot_sigma, float outline_sigma)
{
    VoronoiOtsuLabelingKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetOutput(output);
    kernel.SetSpotSigma(spot_sigma);
    kernel.SetOutlineSigma(outline_sigma);
    kernel.Execute();
}

void init_pytier6(pybind11::module_ &m) {
    
    m.def("voronoi_otsu_labeling", &VoronoiOtsuLabeling, "voronoi otsu labeling",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("output"), pybind11::arg("spot_sigma"), pybind11::arg("outline_sigma"));

    m.doc() = R"pbdoc(
        tier6 wrapper
        -----------------------
        voronoi_otsu_labeling()
    )pbdoc";

}
