#include "pycle_wrapper.hpp"

#include "transform.hpp"

#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <algorithm>
#include <cmath>
#include <tuple>

namespace py = pybind11;

// convert an Eigen 4x4 column-major matrix to a numpy row-major (C-order) array
py::array_t<float, py::array::c_style> matrix_to_numpy(const cle::transform::AffineTransform::matrix & mat)
{
    py::array_t<float, py::array::c_style> array({ 4, 4 });
    auto data = array.mutable_unchecked<2>();
    for (py::ssize_t i = 0; i < 4; ++i)
    {
        for (py::ssize_t j = 0; j < 4; ++j)
        {
            data(i, j) = mat(i, j);
        }
    }
    return array;
}

// convert a numpy row-major (C-order) array to an Eigen 4x4 column-major matrix
cle::transform::AffineTransform::matrix numpy_to_matrix(const py::array_t<float, py::array::c_style | py::array::forcecast> & array)
{
    if (array.ndim() != 2 || array.shape(0) != 4 || array.shape(1) != 4)
    {
        throw std::invalid_argument("Expected a 4x4 matrix.");
    }
    auto data = array.unchecked<2>();
    cle::transform::AffineTransform::matrix mat;
    for (py::ssize_t i = 0; i < 4; ++i)
    {
        for (py::ssize_t j = 0; j < 4; ++j)
        {
            mat(i, j) = data(i, j);
        }
    }
    return mat;
}

// embed a flat row-major 3x3 (2D affine, homogeneous rows [a,b,tx],[c,d,ty],[0,0,1]) matrix
// into a flat row-major 4x4 (3D affine) matrix, leaving the z axis untouched (identity)
std::array<float, 16> embed_2d_into_3d(const std::array<float, 9> & mat2d)
{
    return { mat2d[0], mat2d[1], 0.f, mat2d[2],
             mat2d[3], mat2d[4], 0.f, mat2d[5],
             0.f,      0.f,      1.f, 0.f,
             0.f,      0.f,      0.f, 1.f };
}

// Compute the output shape (width, height, depth) and updated transform for the given source array shape.
// NOTE: CLIc's public header declares cle::transform::prepare_output_shape_and_transform(Array::Pointer, AffineTransform),
// but only an internal (width, height, depth, transform) overload is actually implemented/linkable.
// We replicate that bounding-box algorithm here against the public AffineTransform API.
std::tuple<size_t, size_t, size_t, cle::transform::AffineTransform>
prepare_output_shape_and_transform(const cle::Array::Pointer & src, const cle::transform::AffineTransform & transform)
{
    using point = Eigen::Vector4f;
    using bounding_box = std::array<point, 8>;

    const auto width = static_cast<float>(src->width());
    const auto height = static_cast<float>(src->height());
    const auto depth = static_cast<float>(src->depth());

    bounding_box bbox = { point{ 0.0F, 0.0F, 0.0F, 1.0F },
                          point{ 0.0F, 0.0F, depth, 1.0F },
                          point{ 0.0F, height, 0.0F, 1.0F },
                          point{ width, 0.0F, 0.0F, 1.0F },
                          point{ width, height, 0.0F, 1.0F },
                          point{ 0.0F, height, depth, 1.0F },
                          point{ width, 0.0F, depth, 1.0F },
                          point{ width, height, depth, 1.0F } };

    bounding_box updated_bbox;
    std::transform(bbox.begin(), bbox.end(), updated_bbox.begin(),
                    [&](const point & p) { return transform.getMatrix() * p; });

    point min = updated_bbox[0];
    point max = updated_bbox[0];
    for (const auto & p : updated_bbox)
    {
        min = min.cwiseMin(p);
        max = max.cwiseMax(p);
    }

    cle::transform::AffineTransform update_transform(transform);
    const auto new_width = static_cast<size_t>(std::round(max[0] - min[0]));
    const auto new_height = static_cast<size_t>(std::round(max[1] - min[1]));
    const auto new_depth = static_cast<size_t>(std::round(max[2] - min[2]));
    update_transform.translate(-min[0], -min[1], -min[2]);

    return std::make_tuple(new_width, new_height, new_depth, update_transform);
}

auto transform_(py::module_ &m) -> void
{
    py::class_<cle::transform::AffineTransform, std::shared_ptr<cle::transform::AffineTransform>>(m, "_AffineTransform", py::module_local(),
        "Affine transformation class. Build an affine transformation matrix by applying "
        "scaling, rotation, translation, shearing, and deskewing transformations.")
        .def(py::init<>(), "Create a new AffineTransform object with the identity matrix.")
        .def(py::init<const cle::transform::AffineTransform &>(), py::arg("transform"),
             "Create a new AffineTransform object as a copy of another AffineTransform.")
        .def(py::init([](const std::vector<float> &matrix)
             {
                 if (matrix.size() == 16)
                 {
                     std::array<float, 16> flat;
                     std::copy(matrix.begin(), matrix.end(), flat.begin());
                     return cle::transform::AffineTransform(flat);
                 }
                 if (matrix.size() == 9)
                 {
                     std::array<float, 9> flat2d;
                     std::copy(matrix.begin(), matrix.end(), flat2d.begin());
                     return cle::transform::AffineTransform(embed_2d_into_3d(flat2d));
                 }
                 throw std::invalid_argument(
                     "Expected a flat list of 16 floats (row-major 4x4 matrix) or 9 floats (row-major 3x3 matrix).");
             }),
             py::arg("matrix"),
             "Create a new AffineTransform object from a flat list of 16 floats (row-major 4x4) "
             "or 9 floats (row-major 3x3, embedded into a 3D 4x4 matrix).")
        .def(py::init([](const py::array_t<float, py::array::c_style | py::array::forcecast> &matrix)
             {
                 if (matrix.ndim() == 1 && matrix.shape(0) == 16)
                 {
                     std::array<float, 16> flat;
                     auto data = matrix.unchecked<1>();
                     std::copy(data.data(0), data.data(0) + 16, flat.begin());
                     return cle::transform::AffineTransform(flat);
                 }
                 if (matrix.ndim() == 1 && matrix.shape(0) == 9)
                 {
                     std::array<float, 9> flat2d;
                     auto data = matrix.unchecked<1>();
                     std::copy(data.data(0), data.data(0) + 9, flat2d.begin());
                     return cle::transform::AffineTransform(embed_2d_into_3d(flat2d));
                 }
                 if (matrix.ndim() == 2 && matrix.shape(0) == 4 && matrix.shape(1) == 4)
                 {
                     std::array<float, 16> flat;
                     auto data = matrix.unchecked<2>();
                     for (py::ssize_t i = 0; i < 4; ++i)
                         for (py::ssize_t j = 0; j < 4; ++j)
                             flat[i * 4 + j] = data(i, j);
                     return cle::transform::AffineTransform(flat);
                 }
                 if (matrix.ndim() == 2 && matrix.shape(0) == 3 && matrix.shape(1) == 3)
                 {
                     std::array<float, 9> flat2d;
                     auto data = matrix.unchecked<2>();
                     for (py::ssize_t i = 0; i < 3; ++i)
                         for (py::ssize_t j = 0; j < 3; ++j)
                             flat2d[i * 3 + j] = data(i, j);
                     return cle::transform::AffineTransform(embed_2d_into_3d(flat2d));
                 }
                 throw std::invalid_argument(
                     "Expected a 4x4 or 3x3 matrix, or a flat array of 16 or 9 floats.");
             }),
             py::arg("matrix"),
             "Create a new AffineTransform object from a 4x4/3x3 matrix or a flat array of 16/9 "
             "floats (row-major). A 3x3/9-element (2D) matrix is embedded into a 3D 4x4 matrix, "
             "leaving the z axis untouched.")

        .def("scale", &cle::transform::AffineTransform::scale, "Scaling transformation.",
             py::arg("scale_x"), py::arg("scale_y"), py::arg("scale_z"))
        .def("rotate", &cle::transform::AffineTransform::rotate, "Rotation transformation.",
             py::arg("axis"), py::arg("angle_deg"))
        .def("rotate_around_x_axis", &cle::transform::AffineTransform::rotate_around_x_axis,
             "Rotation transformation around the x axis.", py::arg("angle_deg"))
        .def("rotate_around_y_axis", &cle::transform::AffineTransform::rotate_around_y_axis,
             "Rotation transformation around the y axis.", py::arg("angle_deg"))
        .def("rotate_around_z_axis", &cle::transform::AffineTransform::rotate_around_z_axis,
             "Rotation transformation around the z axis.", py::arg("angle_deg"))
        .def("translate", &cle::transform::AffineTransform::translate, "Translation transformation.",
             py::arg("translate_x"), py::arg("translate_y"), py::arg("translate_z"))
        .def("center", &cle::transform::AffineTransform::center, "Centering transformation.",
             py::arg("shape"), py::arg("undo"))
        .def("shear_in_z_plane", &cle::transform::AffineTransform::shear_in_z_plane,
             "Shearing transformation in the z plane.", py::arg("shear_x_deg"), py::arg("shear_y_deg"))
        .def("shear_in_y_plane", &cle::transform::AffineTransform::shear_in_y_plane,
             "Shearing transformation in the y plane.", py::arg("shear_x_deg"), py::arg("shear_z_deg"))
        .def("shear_in_x_plane", &cle::transform::AffineTransform::shear_in_x_plane,
             "Shearing transformation in the x plane.", py::arg("shear_y_deg"), py::arg("shear_z_deg"))
        .def("deskew_x", &cle::transform::AffineTransform::deskew_x, "Deskewing transformation in the x plane.",
             py::arg("angle_deg"), py::arg("voxel_size_x"), py::arg("voxel_size_y"),
             py::arg("voxel_size_z"), py::arg("scale_factor"))
        .def("deskew_y", &cle::transform::AffineTransform::deskew_y, "Deskewing transformation in the y plane.",
             py::arg("angle_deg"), py::arg("voxel_size_x"), py::arg("voxel_size_y"),
             py::arg("voxel_size_z"), py::arg("scale_factor"))

        .def("get_matrix", [](const cle::transform::AffineTransform &self)
             { return matrix_to_numpy(self.getMatrix()); },
             "Return the transformation matrix as a 4x4 numpy array.")
        .def("get_inverse", [](const cle::transform::AffineTransform &self)
             { return matrix_to_numpy(self.getInverse()); },
             "Return the inverse transformation matrix as a 4x4 numpy array.")
        .def("get_transpose", [](const cle::transform::AffineTransform &self)
             { return matrix_to_numpy(self.getTranspose()); },
             "Return the transposed transformation matrix as a 4x4 numpy array.")
        .def("get_inverse_transpose", [](const cle::transform::AffineTransform &self)
             { return matrix_to_numpy(self.getInverseTranspose()); },
             "Return the inverse transposed transformation matrix as a 4x4 numpy array.")
        .def_static("to_array", [](const py::array_t<float, py::array::c_style | py::array::forcecast> & matrix)
             { return cle::transform::AffineTransform::toArray(numpy_to_matrix(matrix)); },
             "Convert a 4x4 matrix to a flat array of 16 floats.", py::arg("matrix"))

        .def("__array__", [](const cle::transform::AffineTransform &self, py::args, py::kwargs)
             { return matrix_to_numpy(self.getMatrix()); },
             "Return the transformation matrix as a 4x4 numpy array. Enables np.asarray(transform) / np.array(transform).")

        .def("__str__", [](const cle::transform::AffineTransform &self)
             {
                 std::ostringstream oss;
                 oss << "AffineTransform(";
                 for (py::ssize_t i = 0; i < 4; ++i)
                 {
                     oss << (i == 0 ? "[[" : " [");
                     for (py::ssize_t j = 0; j < 4; ++j)
                     {
                         oss << self.getMatrix()(i, j) << (j == 3 ? "]" : ", ");
                     }
                     oss << (i == 3 ? "])" : ",\n");
                 }
                 return oss.str(); })
        .def("__repr__", [](const cle::transform::AffineTransform &self)
             {
                 std::ostringstream oss;
                 oss << self.getMatrix();
                 return oss.str(); });

    m.def("_prepare_output_shape_and_transform", &cle::transform::prepare_output_shape_and_transform,
          "Prepare the output shape (width, height, depth) and updated transform for the given "
          "transformation matrix and array shape.",
          py::return_value_policy::automatic_reference,
          py::arg("width"), py::arg("height"), py::arg("depth"), py::arg("transform"));

    m.def("_affine_transform", &cle::transform::affine_transform,
          "Apply the affine transform matrix to an array.",
          py::return_value_policy::automatic_reference,
          py::arg("src"), py::arg("dst"), py::arg("transform"), py::arg("interpolate"), py::arg("auto_resize"));

     m.def("_affine_transform_deskew", &cle::transform::affine_transform_deskew_3d,
          "Apply the affine transform matrix to a 3D array with deskewing.",
          py::return_value_policy::automatic_reference,
          py::arg("src"), py::arg("dst"), py::arg("transform"), py::arg("deskew_angle"), py::arg("voxel_size_x"), py::arg("voxel_size_y"), py::arg("voxel_size_z"),
          py::arg("deskew_direction"), py::arg("auto_resize"));
}
