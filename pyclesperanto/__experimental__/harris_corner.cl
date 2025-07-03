#define K ldexp(1.0f, -22)
#define DOUBLE_TYPE float

__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE |
                               CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

inline void compute_gaussian_structure_tensor(
    IMAGE_src_TYPE src,       // Input 3D image
    IMAGE_g_x_TYPE g_x,       // Gaussian second derivative
    IMAGE_g_xy_TYPE g_xy,     // Gaussian second derivative mixed
    int x, int y, int z,      // Coordinates in the image
    DOUBLE_TYPE tensor[]) {

  // Temporary variables for derivatives
  float I_x = 0.0f;
  float I_y = 0.0f;
  float I_z = 0.0f;
  float I_xy = 0.0f;
  float I_xz = 0.0f;
  float I_yz = 0.0f;

  const int width = GET_IMAGE_WIDTH(src);
  const int height = GET_IMAGE_HEIGHT(src);
  const int depth = GET_IMAGE_DEPTH(src);

  const int kernel_width = GET_IMAGE_WIDTH(g_x);
  const int kernel_height = GET_IMAGE_HEIGHT(g_x);
  const int kernel_depth = GET_IMAGE_DEPTH(g_x);

  const int center_w = (kernel_width > 1) ? kernel_width / 2 : 0;
  const int center_h = (kernel_height > 1) ? kernel_height / 2 : 0;
  const int center_d = (kernel_depth > 1) ? kernel_depth / 2 : 0;

  // Compute second derivatives along x, y, z (Ixx, Iyy, Izz)
  for (int i = -center_w; i <= center_w; i++) {
    for (int j = -center_h; j <= center_h; j++) {
      for (int k = -center_d; k <= center_d; k++) {
        // Read values from the source image
        float value =
            (float)READ_IMAGE(src, sampler,
                              POS_src_INSTANCE(x + i, y + j, z + k, 0))
                .x;

        float value_kernel_x =
            (float)READ_IMAGE(g_x, sampler,
                              POS_g_x_INSTANCE(i + center_w, j + center_h,
                                                  k + center_d, 0))
                .x;
        I_x += value * value_kernel_x;

        float value_kernel_y =
            (float)READ_IMAGE(g_x, sampler,
                              POS_g_x_INSTANCE(j + center_h, i + center_w,
                                                  k + center_d, 0))
                .x;
        I_y += value * value_kernel_y;

        if (depth > 1) {
          float value_kernel_z =
              (float)READ_IMAGE(g_x, sampler,
                                POS_g_x_INSTANCE(k + center_d, i + center_w,
                                                    j + center_h, 0))
                  .x;
          I_z += value * value_kernel_z;
        }

        float value_xy_kernel =
            (float)READ_IMAGE(g_xy, sampler,
                              POS_g_xy_INSTANCE(i + center_w, j + center_h,
                                                  k + center_d, 0))
                .x;
        I_xy += value * value_xy_kernel;

        if (depth > 1) {
          float value_xz_kernel =
              (float)READ_IMAGE(g_xy, sampler,
                                POS_g_xy_INSTANCE(i + center_w, k + center_d,
                                                    j + center_h, 0))
                  .x;
          I_xz += value * value_xz_kernel;

          float value_yz_kernel =
              (float)READ_IMAGE(g_xy, sampler,
                                POS_g_xy_INSTANCE(j + center_h, k + center_d,
                                                    i + center_w, 0))
                  .x;
          I_yz += value * value_yz_kernel;
        }
      }
    }
  }

  // Store results in the tensor matrix
  tensor[0] = I_x * I_x; // x^2
  tensor[1] = I_xy; // xy
  tensor[2] = I_xz; // xz
  tensor[3] = I_y * I_y; // y^2
  tensor[4] = I_yz; // yz
  tensor[5] = I_z * I_z; // z^2
}

/*
  This kernel computes the eigenvalues of the tensor matrix of a 3d image
  using the Gaussian derivative.

  Tensor matrix:
    [Ix2, Ixy, Ixz]
    [Ixy, Iy2, Iyz]
    [Ixz, Iyz, Iz2]
  Where Ix2 denotes the first derivative in x^2.
*/
__kernel void harris_corner(
    IMAGE_src_TYPE src,       // Input 2D image
    IMAGE_g_x_TYPE g_x, // Gaussian second derivative 1d array
    IMAGE_g_xy_TYPE g_xy, // Gaussian second derivative mixed 2d array
    IMAGE_dst_TYPE dst,
    float precision) {

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const bool is_3d = GET_IMAGE_DEPTH(src) > 1;
  DOUBLE_TYPE tensor[6] = {0, 0, 0, 0, 0, 0};

  compute_gaussian_structure_tensor(src, g_x, g_xy, x, y, z, tensor); // Compute the tensor matrix

  DOUBLE_TYPE trace, det, response;
  trace = (tensor[0] + tensor[3] + tensor[5]); // trace
  if (is_3d) {
    // Ix2 = A = tensor[0]
    // Ixy = B = tensor[1]
    // Ixz = C = tensor[2]
    // Iy2 = D = tensor[3]
    // Iyz = E = tensor[4]
    // Iz2 = F = tensor[5]
    det = (
        tensor[0] * (tensor[1] * tensor[2] - tensor[5] * tensor[5]) -
        tensor[3] * (tensor[3] * tensor[2] - tensor[4] * tensor[5]) +
        tensor[4] * (tensor[3] * tensor[5] - tensor[1] * tensor[4])
    );
    response = det - precision * pow(trace, 3); // response
  } else {
    det = tensor[0] * tensor[3] - tensor[1] * tensor[1]; // determinant 2d
    response = det - precision * pow(trace, 2); // response
  }
  WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(response));
}
