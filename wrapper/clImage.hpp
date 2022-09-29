#ifndef __WRAPPER_CLIMAGE_HPP
#define __WRAPPER_CLIMAGE_HPP

#include <pybind11/pybind11.h>
#include <tuple>

#include "cleImage.hpp"

class clImage : public cle::Image
{
public:
  using cle::Image::Image;
  using ShapeTuple = std::tuple<size_t, size_t, size_t>;

  clImage() = default;
  clImage(const cle::Image &img);
  auto getShape() const -> ShapeTuple;
  auto Print() const -> std::string;
};

#endif // __WRAPPER_CLIMAGE_HPP
