#ifndef __WRAPPER_CLEGATEWAY_HPP
#define __WRAPPER_CLEGATEWAY_HPP

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "cleImage.hpp"
#include "clesperanto.hpp"

class cleGateway : public cle::Clesperanto
{
public:
  using cle::Clesperanto::Clesperanto;
  using ndarray_f = pybind11::array_t<float, pybind11::array::c_style | pybind11::array::forcecast>;

  auto Create(const pybind11::tuple &shape, const cle::MemoryType &mtype) -> cle::Image;
  auto Push(const ndarray_f &nd_arr, const cle::MemoryType &mtype) -> cle::Image;
  auto Pull(const cle::Image &image) -> ndarray_f;
};

#endif // __WRAPPER_CLEGATEWAY_HPP
