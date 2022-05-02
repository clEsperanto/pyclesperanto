
#include "pydata.hpp" 
#include "pygpu.hpp" 
#include "pyclesperanto.hpp"

#include "cleGPU.hpp"

#include "cleMaskedVoronoiLabelingKernel.hpp"

using namespace cle;

void MaskedVoronoiLabeling(PyGPU& device, PyData& input, PyData& mask, PyData& output)
{
    MaskedVoronoiLabelingKernel kernel(std::make_shared<GPU>(device));
    kernel.SetInput(input);
    kernel.SetMask(mask);
    kernel.SetOutput(output);
    kernel.Execute();
}

void init_pytier5(pybind11::module_ &m) {
    
    m.def("masked_voronoi_labeling", &MaskedVoronoiLabeling, "masked voronoi labeling",
        pybind11::arg("device"), pybind11::arg("input"), pybind11::arg("mask"), pybind11::arg("output"));

    m.doc() = R"pbdoc(
        tier5 wrapper
        -----------------------
        masked_voronoi_labeling()
    )pbdoc";

}
