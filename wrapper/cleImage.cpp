#include "pyclesperanto.hpp"

#include "cleImage.hpp"
#include "cleTypes.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto init_cleimage(pybind11::module_ &m) -> void
{

  pybind11::class_<cle::Image, std::shared_ptr<cle::Image>> object(m, "_cleImage");
  object.def(pybind11::init<>());
  object.def(pybind11::init<cle::Image const &>());

  object.def("GetDevice", &cle::Image::GetDevice, "");
  object.def("Ndim", &cle::Image::Ndim, "");
  object.def("GetDataType", &cle::Image::GetDataType, "");
  object.def("GetMemoryType", &cle::Image::GetMemoryType, "");
  object.def(
      "Shape",
      [](const cle::Image &image)
      {
        return std::make_tuple(image.Shape()[2], image.Shape()[1], image.Shape()[0]);
      },
      "");
  object.def("BytesSize", &cle::Image::GetMemorySize, "");
  object.def("Size", &cle::Image::GetNumberOfElements, "");
  object.def("Fill", &cle::Image::Fill, "", pybind11::arg("value"));
  object.def("CopyDataTo", &cle::Image::CopyDataTo, "", pybind11::arg("image"));
  object.def(
      "__repr__", [](const cle::Image &image)
      {
                 std::stringstream out_string;
                 out_string << "<pyclesperanto object cle::Image " << cle::MemoryTypeToString(image.GetMemoryType());
                 out_string << "("<<cle::DataTypeToString(image.GetDataType()) <<"),";
                 out_string << "shape=(" << image.Shape()[2] << ", " << image.Shape()[1] << ", " << image.Shape()[0] <<")>";
                 return out_string.str(); },
      "");
  object.def(
      "__len__", [](const cle::Image &image)
      {
    switch(image.Ndim())
    {
    case 1:
      return image.Shape()[0];
    case 2:
      return image.Shape()[1];
    case 3:
      return image.Shape()[2];
    } },
      "");

  object.doc() = R"pbdoc(
        clImage class wrapper
        -----------------------
    )pbdoc";
}