#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier3(pybind11::module_ &m) -> void
{
      m.def("_DifferenceOfGaussianKernel_Call", &cle::DifferenceOfGaussianKernel_Call, "", pybind11::arg("device"),
            pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("sigma1_x"), pybind11::arg("sigma1_y"), pybind11::arg("sigma1_z"), pybind11::arg("sigma2_x"), pybind11::arg("sigma2_y"), pybind11::arg("sigma2_z"));

      m.def("_CloseIndexGapsInLabelMapKernel_Call", &cle::CloseIndexGapsInLabelMapKernel_Call, pybind11::arg("device"),
            "", pybind11::arg("src"), pybind11::arg("dst"), pybind11::arg("value"));

      m.def("_HistogramKernel_Call", &cle::HistogramKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"),
            pybind11::arg("dst"), pybind11::arg("bins"), pybind11::arg("min_intensity"), pybind11::arg("max_intensity"));
}