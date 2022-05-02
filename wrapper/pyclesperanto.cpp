// #include <pybind11/stl.h>
// #include <pybind11/functional.h>

#include "pyclesperanto.hpp"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

PYBIND11_MODULE(_pyclic, m) {  // define a module. module name = file name = cmake target name 
    init_pygpu(m);
    init_pydata(m);
    init_pytier1(m);
    init_pytier2(m);
    init_pytier3(m);
    init_pytier4(m);
    init_pytier5(m);
    init_pytier6(m);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif   
}
