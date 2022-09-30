#ifndef __WRAPPER_CLGATEWAY_HPP
#define __WRAPPER_CLGATEWAY_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "clImage.hpp"
#include "clesperanto.hpp"

// using cle::Clesperanto;
// using cle::Image;
// using cle::MemoryType;

class clGateway : public cle::Clesperanto
{
public:
  using cle::Clesperanto::Clesperanto;
  using ndarray_f = pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>;

  auto Create(const pybind11::tuple &shape, const cle::MemoryType &mtype) -> clImage;
  auto Push(ndarray_f &nd_arr, const cle::MemoryType &mtype) -> clImage;
  auto Pull(clImage &image) -> ndarray_f;
};

#endif // __WRAPPER_CLGATEWAY_HPP
