
#include "pyclesperanto.hpp"

PYBIND11_MODULE(_pyclesperanto, m) {
  // define a module. module name = file name = cmake target name
  init_pygateway(m);
  init_pyimage(m);

}
