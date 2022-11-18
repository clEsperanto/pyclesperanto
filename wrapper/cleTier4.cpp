#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier4(pybind11::module_ &m) -> void
{
      m.def("_ConnectedComponentLabelingBoxKernel_Call",
            &cle::ConnectedComponentLabelingBoxKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_ThresholdOtsuKernel_Call", &cle::ThresholdOtsuKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));
}