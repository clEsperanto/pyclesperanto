#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier6(pybind11::module_ &m) -> void
{
      m.def("_VoronoiOtsuLabelingKernel_Call", &cle::VoronoiOtsuLabelingKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("sigma_spot"), pybind11::arg("sigma_outline"));
}