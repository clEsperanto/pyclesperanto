#ifndef __WRAPPER_PYIMAGE_HPP
#define __WRAPPER_PYIMAGE_HPP

#include <pybind11/pybind11.h>

#include "cleImage.hpp"

using cle::Image;

class pyImage : public Image {
public:
  using Image::Image;
  using ShapeArray = std::array<size_t, 3>;

  pyImage() = default;
  pyImage(const Image &);
  [[nodiscard]] auto ShapeZYX() const -> ShapeArray;
};

#endif // __WRAPPER_PYIMAGE_HPP
