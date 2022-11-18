#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier5(pybind11::module_ &m) -> void
{
      m.def("_MaskedVoronoiLabelingKernel_Call", &cle::MaskedVoronoiLabelingKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("t_mask"), pybind11::arg("dst"));
}