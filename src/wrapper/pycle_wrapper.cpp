
#include "pycle_wrapper.hpp"

// define a module. module name = file name = cmake target name
PYBIND11_MODULE(_pyclesperanto, m)
{
  // Wrap clesperanto core functionality for operability
  types_(m);
  core_(m);
  array_(m);
  execute_(m);

  tier1_(m);
  tier2_(m);
  tier3_(m);
  tier4_(m);
  tier5_(m);
  tier6_(m);
  tier7_(m);
  tier8_(m);
}
