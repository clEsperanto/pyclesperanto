#ifndef __WRAPPER_PYGATEWAY_HPP
#define __WRAPPER_PYGATEWAY_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "clImage.hpp"
#include "clesperanto.hpp"

using pybind11::array;
using pybind11::array_t;

using cle::Clesperanto;
// using cle::Image;
// using cle::MemoryType;

class clGateway : public Clesperanto
{
public:
  using Clesperanto::Clesperanto;

  //* numpy array datatype
  using ndarray_f = array_t<float, array::c_style | array::forcecast>;

  //* overload create push pull operation from gpu
  auto Create(ndarray_f &shape) -> clImage;
  auto Push(ndarray_f &source) -> clImage;
  auto Pull(clImage &source) -> ndarray_f;
};

#endif // __WRAPPER_PYGATEWAY_HPP
