#include "pyclesperanto.hpp"

#include "cleImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto init_cleimage(pybind11::module_ &m) -> void
{

  pybind11::class_<cle::Image, std::shared_ptr<cle::Image>> object(m, "cleImage");
  object.def(pybind11::init<>());

  object.def_property_readonly("ndim", &cle::Image::Ndim, "");
  object.def_property_readonly("dtype", &cle::Image::GetDataType, "");
  object.def_property_readonly("mtype", &cle::Image::GetMemoryType, "");
  object.def_property_readonly(
      "shape",
      [](const cle::Image &image)
      {
        return std::make_tuple(image.Shape()[2], image.Shape()[1], image.Shape()[0]);
      },
      "");
  object.def_property_readonly(
      "nbytes", [](const cle::Image &image)
      { return image.GetSize(); },
      "");
  object.def_property_readonly(
      "size", [](const cle::Image &image)
      { return image.Shape()[2] * image.Shape()[1] * image.Shape()[0]; },
      "");

  object.def("fill", &cle::Image::Fill, "", pybind11::arg("value"));
  object.def("copy_to", &cle::Image::CopyDataTo, "", pybind11::arg("image"));

  object.def(
      "__str__", [](const cle::Image &image)
      {
                 std::stringstream out_string;
                 out_string << "<cle::Image::" << image.GetMemoryType_Str();
                 out_string << "("<<image.GetDataType_Str(false) <<"),";
                 out_string << "shape=(" << image.Shape()[2] << ", " << image.Shape()[1] << ", " << image.Shape()[0] <<")>";
                 return out_string.str(); },
      "");
  object.def(
      "__repr__", [](const cle::Image &image)
      {
                 std::stringstream out_string;
                 out_string << "<pyclesperanto object cle::Image::" << image.GetMemoryType_Str();
                 out_string << "("<<image.GetDataType_Str(false) <<"),";
                 out_string << "shape=(" << image.Shape()[2] << ", " << image.Shape()[1] << ", " << image.Shape()[0] <<")>";
                 return out_string.str(); },
      "");

  object.def(
      "__len__", [](const cle::Image &image)
      {
                 if (image.Shape()[2] > 1)
                 {
                   return image.Shape()[2];
                 }
                 if(image.Shape()[1] > 1 )
                 {
                   return image.Shape()[1];
                 }
                 return image.Shape()[0]; },
      "");

  // object.__lt__(self, other)
  // object.__le__(self, other)
  // object.__eq__(self, other)
  // object.__ne__(self, other)
  // object.__gt__(self, other)
  // object.__ge__(self, other)

  object.doc() = R"pbdoc(
        clImage class wrapper
        -----------------------
    )pbdoc";
}