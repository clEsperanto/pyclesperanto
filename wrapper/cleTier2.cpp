#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier2(pybind11::module_ &m) -> void
{
      m.def("_DetectMaximaKernel_Call", &cle::DetectMaximaKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_DilateLabelsKernel_Call", &cle::DilateLabelsKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("radius"));

      m.def("_MaximumOfAllPixelsKernel_Call", &cle::MaximumOfAllPixelsKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_MinimumOfAllPixelsKernel_Call", &cle::MinimumOfAllPixelsKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_SumOfAllPixelsKernel_Call", &cle::SumOfAllPixelsKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));

      m.def("_TopHatBoxKernel_Call", &cle::TopHatBoxKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"), pybind11::arg("radius_x"), pybind11::arg("radius_y"), pybind11::arg("radius_z"));

      m.def("_ExtendLabelingViaVoronoiKernel_Call", &cle::ExtendLabelingViaVoronoiKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"));
}