
#include "pyclesperanto.hpp"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

PYBIND11_MODULE(_pyclesperanto, m) {
  // define a module. module name = file name = cmake target name
  init_pygateway(m);
  init_pyimage(m);

#ifdef VERSION_INFO
  m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
  m.attr("__version__") = "dev";
#endif
}
