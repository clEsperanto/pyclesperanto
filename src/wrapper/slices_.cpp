// cle::slice_.cpp — pybind11 bindings for cle::cle::Slice and cle::cle::slice()

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <optional>
#include <tuple>
#include <vector>

#include "slicing.hpp"

namespace py = pybind11;

// ─── Helpers to convert Python objects → cle::cle::Slice ─────────────────────────

/**
 * Convert a single Python object to a cle::cle::Slice.
 *
 * Accepted inputs:
 *   - int              → cle::Slice(index)         i.e. single-index, collapses axis
 *   - Python cle::slice     → cle::Slice(start, stop, step)  with None → std::nullopt
 *   - cle::cle::Slice       → pass-through
 *   - None             → cle::Slice()              i.e. full axis [:]
 */
static auto
py_to_slice(const py::object & obj) -> cle::Slice
{
  // Already a C++ cle::Slice (bound below)
  if (py::isinstance<cle::Slice>(obj))
  {
    return obj.cast<cle::Slice>();
  }

  // None → full axis [:]
  if (obj.is_none())
  {
    return cle::Slice();
  }

  // Plain integer → single index
  if (py::isinstance<py::int_>(obj))
  {
    return cle::Slice(obj.cast<int>());
  }

  // Python cle::slice object
  if (py::isinstance<py::slice>(obj))
  {
    // Extract the raw attributes; they can each be None or int
    py::object py_start = obj.attr("start");
    py::object py_stop  = obj.attr("stop");
    py::object py_step  = obj.attr("step");

    std::optional<int> start = py_start.is_none() ? std::nullopt : std::optional<int>(py_start.cast<int>());
    std::optional<int> stop  = py_stop.is_none()  ? std::nullopt : std::optional<int>(py_stop.cast<int>());
    int                step  = py_step.is_none()   ? 1            : py_step.cast<int>();

    return cle::Slice(start, stop, step);
  }

  throw py::type_error("Expected int, slice, None, or Slice, got " + std::string(py::str(py::type::of(obj))));
}

/**
 * Convert a Python tuple/list of cle::slice-like objects (or a single one)
 * into a std::vector<cle::Slice>.
 */
static auto
py_to_slice_vector(const py::object & key) -> std::vector<cle::Slice>
{
  std::vector<cle::Slice> result;

  if (py::isinstance<py::tuple>(key))
  {
    for (auto item : key.cast<py::tuple>())
    {
      result.push_back(py_to_slice(py::reinterpret_borrow<py::object>(item)));
    }
  }
  else if (py::isinstance<py::list>(key))
  {
    for (auto item : key.cast<py::list>())
    {
      result.push_back(py_to_slice(py::reinterpret_borrow<py::object>(item)));
    }
  }
  else
  {
    // Single item (int, cle::slice, None, cle::Slice)
    result.push_back(py_to_slice(key));
  }

  return result;
}

// ─── Module binding ─────────────────────────────────────────────────────────

auto slice_(py::module &m) -> void
{
  // ── Bind cle::cle::Slice ───────────────────────────────────────────────────

  py::class_<cle::Slice>(m, "_cle::Slice", R"doc(
      Single-axis cle::slice specification, analogous to Python's ``cle::slice(start, stop, step)``.

      Examples::

          cle::Slice()              # [:]      full axis
          cle::Slice(5)             # [5]      single index (collapses axis)
          cle::Slice(1, 10)         # [1:10]   range
          cle::Slice(1, 10, 2)      # [1:10:2] range with step
          cle::Slice(None, 5)       # [:5]     from start
          cle::Slice(3, None)       # [3:]     to end
          cle::Slice(-3, None)      # [-3:]    negative index
  )doc")
    // Default: full axis [:]
    .def(py::init<>(), "Full axis ``[:]``.")

    // Single index
    .def(py::init<int>(), py::arg("index"), "Single index — collapses this axis.")

    // Range [start:stop]
    .def(
      py::init([](std::optional<int> start, std::optional<int> stop) { return cle::Slice(start, stop); }),
      py::arg("start"),
      py::arg("stop"),
      "Range ``[start:stop]``.  Use ``None`` for open-ended.")

    // Range with step [start:stop:step]
    .def(
      py::init([](std::optional<int> start, std::optional<int> stop, int step) { return cle::Slice(start, stop, step); }),
      py::arg("start"),
      py::arg("stop"),
      py::arg("step"),
      "Range ``[start:stop:step]``.  Use ``None`` for open-ended.")

    // ── Properties ────────────────────────────────────────────────────
    .def_readwrite("start", &cle::Slice::start)
    .def_readwrite("stop", &cle::Slice::stop)
    .def_readwrite("step", &cle::Slice::step)
    .def_readwrite("is_index", &cle::Slice::is_index)

    // ── Methods ───────────────────────────────────────────────────────
    .def(
      "resolve",
      &cle::Slice::resolve,
      py::arg("axis_len"),
      R"doc(
          Resolve the cle::slice against a concrete axis length.

          Returns:
              tuple: ``(start, stop, step)`` with absolute, clamped values.
      )doc")

    .def(
      "output_length",
      &cle::Slice::output_length,
      py::arg("axis_len"),
      R"doc(
          Number of elements this cle::slice selects along an axis of the given length.
      )doc")

    // ── Repr ──────────────────────────────────────────────────────────
    .def("__repr__", [](const cle::Slice & s) -> std::string {
      if (s.is_index)
      {
        return "cle::Slice(" + std::to_string(s.start.value()) + ")";
      }

      auto opt_str = [](const std::optional<int> & v) -> std::string {
        return v.has_value() ? std::to_string(v.value()) : "None";
      };

      std::string r = "cle::Slice(" + opt_str(s.start) + ", " + opt_str(s.stop);
      if (s.step != 1)
      {
        r += ", " + std::to_string(s.step);
      }
      r += ")";
      return r;
    });

  // ── Bind free-function cle::cle::slice ─────────────────────────────────────

  m.def(
    "slice",
    [](const cle::Array::Pointer & src, const py::args & args) -> cle::Array::Pointer {
      std::vector<cle::Slice> slices;
      for (auto item : args)
      {
        slices.push_back(py_to_slice(py::reinterpret_borrow<py::object>(item)));
      }
      return cle::slice(src, slices);
    },
    py::arg("src"),
    R"doc(
        Extract a sub-array from ``src`` described by up to 3 cle::slice specs (x, y, z order).

        Each positional argument can be:
          - ``int``          — single index (collapses that axis)
          - ``cle::slice(...)``   — Python cle::slice object
          - ``cle::Slice(...)``   — explicit cle.cle::Slice
          - ``None``         — full axis ``[:]``

        Examples::

            # Single z-plane (returns 2-D)
            cle.cle::slice(img, cle::slice(None), cle::slice(None), 50)

            # Crop
            cle.cle::slice(img, cle::slice(0, 100), cle::slice(0, 100), cle::slice(0, 100))

            # Every other column
            cle.cle::slice(img, cle::slice(None, None, 2))

            # Last 10 z-planes
            cle.cle::slice(img, cle::slice(None), cle::slice(None), cle::slice(-10, None))
    )doc");
}


