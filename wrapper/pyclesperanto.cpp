
#include "pyclesperanto.hpp"

// define a module. module name = file name = cmake target name
PYBIND11_MODULE(_pyclesperanto, m)
{
  // Wrap clesperanto core functionality for operability
  init_cletypes(m);
  init_cleprocessor(m);
  init_cleimage(m);
  init_clememory(m);

  // Wrap clesperanto kernel function per tiers
  init_cletier1(m);
  init_cletier2(m);
  init_cletier3(m);
  init_cletier4(m);
  init_cletier5(m);
  init_cletier6(m);
}
