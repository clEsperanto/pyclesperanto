#include "utils.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

auto types_(py::module_ &m) -> void
{
    py::enum_<cle::dType> dtype(m, "_DataType");
    dtype.value("float32", cle::dType::FLOAT);
    dtype.value("int64", cle::dType::INT64);
    dtype.value("int32", cle::dType::INT32);
    dtype.value("int16", cle::dType::INT16);
    dtype.value("int8", cle::dType::INT8);
    dtype.value("uint64", cle::dType::UINT64);
    dtype.value("uint32", cle::dType::UINT32);
    dtype.value("uint16", cle::dType::UINT16);
    dtype.value("uint8", cle::dType::UINT8);
    dtype.export_values();

    py::enum_<cle::mType> mtype(m, "_MemoryType");
    mtype.value("buffer", cle::mType::BUFFER);
    mtype.value("image", cle::mType::IMAGE);
    mtype.export_values();
}
