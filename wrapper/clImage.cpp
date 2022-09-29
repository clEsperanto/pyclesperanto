
#include "clImage.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

clImage::clImage(const cle::Image &img) : cle::Image(img) {}

auto clImage::getShape() const -> clImage::ShapeTuple
{
  return std::make_tuple(this->Shape()[2], this->Shape()[1], this->Shape()[0]);
}

auto clImage::Print() const -> std::string
{
  std::stringstream out_string;
  out_string << this->GetMemoryType_Str();
  out_string << "<(" << std::get<0>(this->getShape()) << ", " << std::get<1>(this->getShape()) << ", " << std::get<2>(this->getShape()) << "), ";
  out_string << this->GetDataType_Str(false) << ">";
  return out_string.str();
}

auto init_climage(const pybind11::module_ &m) -> void
{

  pybind11::class_<clImage, std::shared_ptr<clImage>> object(m, "clImage");
  object.def(pybind11::init<>());

  object.def_property_readonly("ndim", &clImage::Ndim, "");
  object.def_property_readonly("shape", &clImage::getShape, "");
  object.def_property_readonly("dtype", &clImage::GetDataType, "");
  object.def_property_readonly("mtype", &clImage::GetMemoryType, "");

  object.def("fill", &clImage::Fill, "", pybind11::arg("value") = 0);
  object.def("copy_data_to", &clImage::CopyDataTo, "", pybind11::arg("image"));

  object.def("__repr__", &clImage::Print);

  object.doc() = R"pbdoc(
        clImage class wrapper
        -----------------------
    )pbdoc";
}