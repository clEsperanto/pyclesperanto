
#include "pyclesperanto.hpp"

PYBIND11_MODULE(_pyclesperanto, m)
{
  // define a module. module name = file name = cmake target name
  init_cltypes(m);
  init_climage(m);
  init_clgateway(m);
}
