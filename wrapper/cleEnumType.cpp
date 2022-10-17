#include "cleTypes.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

auto init_cletypes(pybind11::module_ &m) -> void
{
    pybind11::enum_<cle::DataType> dtype(m, "_cleDataType");
    dtype.value("float", cle::DataType::FLOAT);
    dtype.value("int32", cle::DataType::INT32);
    dtype.value("int16", cle::DataType::INT16);
    dtype.value("int8", cle::DataType::INT8);
    dtype.value("uint32", cle::DataType::UINT32);
    dtype.value("uint16", cle::DataType::UINT16);
    dtype.value("uint8", cle::DataType::UINT8);
    dtype.export_values();

    pybind11::enum_<cle::MemoryType> otype(m, "_cleMemType");
    otype.value("buffer", cle::MemoryType::BUFFER);
    otype.value("image", cle::MemoryType::IMAGE);
    otype.value("image1d", cle::MemoryType::IMAGE1D);
    otype.value("image2d", cle::MemoryType::IMAGE2D);
    otype.value("image3d", cle::MemoryType::IMAGE3D);
    otype.export_values();
}
