#define PRECISION ldexp(1.0f, -22)
#define DOUBLE_TYPE float

// Returns 1 / sqrt(value)
inline DOUBLE_TYPE precise_rsqrt(DOUBLE_TYPE value) {
  // The opencl function rsqrt, might not give precise results.
  // This function uses the Newton method to improve the results precision.
  DOUBLE_TYPE x2 = value * 0.5;
  DOUBLE_TYPE y = rsqrt(value);
  y = y * (1.5 - (x2 * y * y)); // Newton
  y = y * (1.5 - (x2 * y * y)); // Newton
  y = y * (1.5 - (x2 * y * y)); // Newton
  y = y * (1.5 - (x2 * y * y)); // Newton
  y = y * (1.5 - (x2 * y * y)); // Newton
  return y;
}

// Return the square root of value.
// This method has higher precision than opencl's sqrt() method.
inline DOUBLE_TYPE precise_sqrt(DOUBLE_TYPE value) {
  return value * precise_rsqrt(value);
}

inline void swap(DOUBLE_TYPE x[], int a, int b) { // replace [] by * ? @strigaud
  DOUBLE_TYPE tmp = x[a];
  x[a] = x[b];
  x[b] = tmp;
}

// Calculates the two solutions of the equation: x^2 + c1 * x + c0 == 0
// The results are written to x[], smaller value first.
inline void solve_quadratic_equation(DOUBLE_TYPE c0, DOUBLE_TYPE c1,
                                     DOUBLE_TYPE x[]) {
  DOUBLE_TYPE p = 0.5 * c1;
  DOUBLE_TYPE dis = p * p - c0;
  dis = (dis > 0) ? precise_sqrt(dis) : 0;
  x[0] = (-p - dis);
  x[1] = (-p + dis);
}

// One iteration of Halleys method applied to the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
inline DOUBLE_TYPE halleys_method(DOUBLE_TYPE b0, DOUBLE_TYPE b1,
                                  DOUBLE_TYPE x) {
  DOUBLE_TYPE dy = 3 * x * x + b1;
  DOUBLE_TYPE y = (x * x + b1) * x + b0; /* ...looks odd, but saves CPU time */
  DOUBLE_TYPE dx = y * dy / (dy * dy - 3 * y * x);
  return dx;
}

// Returns one solution to the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
inline DOUBLE_TYPE find_root(DOUBLE_TYPE b0, DOUBLE_TYPE b1) {
  if (b0 == 0)
    return 0;
  DOUBLE_TYPE w = max(fabs(b0), fabs(b1)) + 1.0; /* radius of root circle */
  DOUBLE_TYPE h = (b0 > 0.0) ? -w : w;
  DOUBLE_TYPE dx;
  do { /* find 1st root by Halley's method */
    dx = halleys_method(b0, b1, h);
    h -= dx;
  } while (fabs(dx) > fabs(PRECISION * w));
  return h;
}

// Returns all three real solutions of the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
// The solutions are written to x[]. Smallest solution first.
inline void solve_cubic_scaled_equation(DOUBLE_TYPE b0, DOUBLE_TYPE b1,
                                        DOUBLE_TYPE x[]) {
  DOUBLE_TYPE h = find_root(b0, b1);
  x[2] = h;
  DOUBLE_TYPE c1 = h; /* deflation; c2 is 1 */
  DOUBLE_TYPE c0 = c1 * h + b1;
  solve_quadratic_equation(c0, c1, x);
  if (x[1] > x[2]) { /* sort results */
    swap(x, 1, 2);
    if (x[0] > x[1])
      swap(x, 0, 1);
  }
}

inline int exponent_of(DOUBLE_TYPE f) {
  int exponent;
  frexp(f, &exponent);
  return exponent;
}

// Returns all three real solutions of the depressed cubic equation:
//  x^3 + b1 * x + b0 == 0
// The solutions are written to x[]. Smallest solution first.
inline void solve_depressed_cubic_equation(DOUBLE_TYPE b0, DOUBLE_TYPE b1,
                                           DOUBLE_TYPE x[]) {
  int e0 = exponent_of(b0) / 3;
  int e1 = exponent_of(b1) / 2;
  int e = -max(e0, e1);
  DOUBLE_TYPE scaleFactor = ldexp(1.0, -e);
  b1 = ldexp(b1, 2 * e);
  b0 = ldexp(b0, 3 * e);
  solve_cubic_scaled_equation(b0, b1, x);
  x[0] *= scaleFactor;
  x[1] *= scaleFactor;
  x[2] *= scaleFactor;
}

// Returns all three real solutions of the cubic equation:
//  x^3 + b2 * x^2 + b1 * x + b0 == 0
// The solutions are written to x[]. Smallest solution first.
inline void solve_cubic_equation(DOUBLE_TYPE b0, DOUBLE_TYPE b1, DOUBLE_TYPE b2,
                                 DOUBLE_TYPE x[]) {
  DOUBLE_TYPE s = 1.0 / 3.0 * b2;
  DOUBLE_TYPE q = (2. * s * s - b1) * s + b0;
  DOUBLE_TYPE p = b1 - b2 * s;
  solve_depressed_cubic_equation(q, p, x);
  x[0] = x[0] - s;
  x[1] = x[1] - s;
  x[2] = x[2] - s;
}

__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE |
                               CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

inline void compute_gaussian_hessian(
    IMAGE_src_TYPE src,       // Input 3D image
    IMAGE_gsd_xx_TYPE gsd_xx, // Gaussian second derivative
    IMAGE_gsd_xy_TYPE gsd_xy, // Gaussian second derivative mixed
    int x, int y, int z,      // Coordinates in the image
    DOUBLE_TYPE hessian[]) {

  // Temporary variables for derivatives
  float I_xx = 0.0f;
  float I_yy = 0.0f;
  float I_zz = 0.0f;
  float I_xy = 0.0f;
  float I_xz = 0.0f;
  float I_yz = 0.0f;

  const int width = GET_IMAGE_WIDTH(src);
  const int height = GET_IMAGE_HEIGHT(src);
  const int depth = GET_IMAGE_DEPTH(src);

  const int kernel_width = GET_IMAGE_WIDTH(gsd_xx);
  const int kernel_height = GET_IMAGE_HEIGHT(gsd_xx);
  const int kernel_depth = GET_IMAGE_DEPTH(gsd_xx);

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

        float value_kernel_xx =
            (float)READ_IMAGE(gsd_xx, sampler,
                              POS_gsd_xx_INSTANCE(i + center_w, j + center_h,
                                                  k + center_d, 0))
                .x;
        I_xx += value * value_kernel_xx;

        float value_kernel_yy =
            (float)READ_IMAGE(gsd_xx, sampler,
                              POS_gsd_xx_INSTANCE(j + center_h, i + center_w,
                                                  k + center_d, 0))
                .x;
        I_yy += value * value_kernel_yy;

        if (depth > 1) {
          float value_kernel_zz =
              (float)READ_IMAGE(gsd_xx, sampler,
                                POS_gsd_xx_INSTANCE(k + center_d, i + center_w,
                                                    j + center_h, 0))
                  .x;
          I_zz += value * value_kernel_zz;
        }

        float value_xy_kernel =
            (float)READ_IMAGE(gsd_xy, sampler,
                              POS_gsd_xy_INSTANCE(i + center_w, j + center_h,
                                                  k + center_d, 0))
                .x;
        I_xy += value * value_xy_kernel;

        if (depth > 1) {
          float value_xz_kernel =
              (float)READ_IMAGE(gsd_xy, sampler,
                                POS_gsd_xy_INSTANCE(i + center_w, k + center_d,
                                                    j + center_h, 0))
                  .x;
          I_xz += value * value_xz_kernel;

          float value_yz_kernel =
              (float)READ_IMAGE(gsd_xy, sampler,
                                POS_gsd_xy_INSTANCE(j + center_h, k + center_d,
                                                    i + center_w, 0))
                  .x;
          I_yz += value * value_yz_kernel;
        }
      }
    }
  }

  // Store results in the Hessian matrix
  hessian[0] = I_xx; // xx
  hessian[1] = I_xy; // xy
  hessian[2] = I_xz; // xz
  hessian[3] = I_yy; // yy
  hessian[4] = I_yz; // yz
  hessian[5] = I_zz; // zz
}

/*
  This kernel computes the eigenvalues of the hessian matrix of a 3d image
  using the Gaussian derivative.

  Hessian matrix:
    [Ixx, Ixy, Ixz]
    [Ixy, Iyy, Iyz]
    [Ixz, Iyz, Izz]
  Where Ixx denotes the second derivative in x.

  Ixx and Iyy are calculated by convolving the image with the 1d kernel [1
  -2 1]. Ixy is calculated by a convolution with the 2d kernel: [ 0.25 0
  -0.25] [ 0 0     0]
    [-0.25 0  0.25]
*/
__kernel void hessian_gaussian_eigenvalues(
    IMAGE_src_TYPE src,       // Input 2D image
    IMAGE_gsd_xx_TYPE gsd_xx, // Gaussian second derivative 1d array
    IMAGE_gsd_xy_TYPE gsd_xy, // Gaussian second derivative mixed 2d array
    IMAGE_small_eigenvalue_TYPE small_eigenvalue,
    IMAGE_middle_eigenvalue_TYPE middle_eigenvalue,
    IMAGE_large_eigenvalue_TYPE large_eigenvalue) {

  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const bool is_3d = GET_IMAGE_DEPTH(src) > 1;
  DOUBLE_TYPE eigenvalues[3] = {0, 0, 0};
  DOUBLE_TYPE hessian[6] = {0, 0, 0, 0, 0, 0};

  compute_gaussian_hessian(src, gsd_xx, gsd_xy, x, y, z,
                           hessian); // Compute the Hessian matrix

  DOUBLE_TYPE a, b, c;
  a = (hessian[0] + hessian[3] + hessian[5]); // trace
  if (is_3d) {
    b = hessian[0] * hessian[3] + hessian[0] * hessian[5] +
        hessian[3] * hessian[5] - hessian[1] * hessian[1] -
        hessian[2] * hessian[2] - hessian[4] * hessian[4];
    c = hessian[0] * (hessian[4] * hessian[4] - hessian[3] * hessian[5]) +
        hessian[3] * hessian[2] * hessian[2] +
        hessian[5] * hessian[1] * hessian[1] -
        2 * hessian[1] * hessian[2] * hessian[4];
    solve_cubic_equation(c, b, -a, eigenvalues);
    WRITE_IMAGE(middle_eigenvalue, POS_middle_eigenvalue_INSTANCE(x, y, z, 0),
                CONVERT_middle_eigenvalue_PIXEL_TYPE(eigenvalues[1]));
  } else {
    eigenvalues[0] =
        (DOUBLE_TYPE)(a / 2.0 - sqrt(4 * hessian[1] * hessian[1] +
                                     (hessian[0] - hessian[3]) *
                                         (hessian[0] - hessian[3])) /
                                    2.0);
    eigenvalues[2] =
        (DOUBLE_TYPE)(a / 2.0 + sqrt(4 * hessian[1] * hessian[1] +
                                     (hessian[0] - hessian[3]) *
                                         (hessian[0] - hessian[3])) /
                                    2.0);
  }
  WRITE_IMAGE(small_eigenvalue, POS_small_eigenvalue_INSTANCE(x, y, z, 0),
              CONVERT_small_eigenvalue_PIXEL_TYPE(eigenvalues[0]));
  WRITE_IMAGE(large_eigenvalue, POS_large_eigenvalue_INSTANCE(x, y, z, 0),
              CONVERT_large_eigenvalue_PIXEL_TYPE(eigenvalues[2]));
}
