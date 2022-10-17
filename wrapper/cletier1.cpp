#include "cleKernelList.hpp"
#include "pyclesperanto.hpp"

auto init_cletier1(pybind11::module_ &m) -> void
{
    m.def("_AbsoluteKernel_Call", &cle::AbsoluteKernel_Call, "", pybind11::arg("device"), pybind11::arg("src"), pybind11::arg("dst"));
}