
#include "pyclesperanto.hpp"

// define a module. module name = file name = cmake target name
PYBIND11_MODULE(_pyclesperanto, m)
{
  // Wrap clesperanto core functionality for operability
  wrapper_types(m);
  wrapper_backend(m);
  wrapper_array(m);

  wrapper_tier1(m);
  wrapper_tier2(m);
}
