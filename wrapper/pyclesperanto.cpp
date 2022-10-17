
#include "pyclesperanto.hpp"

PYBIND11_MODULE(_pyclesperanto, m)
{
  // define a module. module name = file name = cmake target name
  init_cletypes(m);
  init_cleprocessor(m);
  init_cleimage(m);

  // init_clegateway(m);

  init_clememory(m);
  init_cletier1(m);
}
