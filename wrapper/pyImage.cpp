
// #include "pyImage.hpp"
#include "cleImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

using cle::Image;

auto init_pyimage(const pybind11::module_ &m) -> void {

  pybind11::class_<Image, std::shared_ptr<Image>> object(m, "Image");
  object.def(pybind11::init<>());

  object.def("Ndim", &Image::Ndim, "");
  object.def("Shape", &Image::ShapeZYX, "");
  object.def("Dtype", &Image::DataInfo, "");
  object.def("Otype", &Image::MemoryInfo, "");
  object.def("Fill", &Image::Fill, "", pybind11::arg("value") = 0);
  object.def("CopyDataTo", &Image::CopyDataTo, "", pybind11::arg("image"));
  object.def("ToString", &Image::ToString, "");

  object.doc() = R"pbdoc(
        data class wrapper
        -----------------------
    )pbdoc";
}