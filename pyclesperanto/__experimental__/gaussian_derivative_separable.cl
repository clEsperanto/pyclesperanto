__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void gaussian_derivative_separable(
    IMAGE_src_TYPE  src,
    IMAGE_dst_TYPE  dst,
    const int       dim,
    const int       N,
    const float     s,
    const int       order // Derivative order: 0 (Gaussian), 1 (1st derivative), 2 (2nd derivative)
)
{
    const int x = get_global_id(0);
    const int y = get_global_id(1);
    const int z = get_global_id(2);

    const POS_src_TYPE coord = POS_src_INSTANCE(x, y, z, 0);
    const POS_src_TYPE dir   = POS_src_INSTANCE(dim == 0, dim == 1, dim == 2, 0);

    const int   center = (int)(N - 1) / 2;
    const float norm   = -2 * s * s;
    const float inv_s2 = 1.0f / (s * s); // Precompute 1/(s^2) for efficiency
    const float inv_s4 = inv_s2 * inv_s2; // Precompute 1/(s^4) for second derivative

    float res = 0;
    float hsum = 0;

    for (int v = -center; v <= center; ++v) {
        float h = 0;

        // Compute kernel based on the order parameter
        const float exp_term = exp((v * v) / norm); // Precompute exponential term
        if (order == 0) {
            h = exp_term; // Gaussian kernel
        } else if (order == 1) {
            h = v * inv_s2 * exp_term; // First derivative of Gaussian
        } else if (order == 2) {
            h = (v * v - s * s) * inv_s4 * exp_term; // Second derivative of Gaussian
        }

        res += h * (float)READ_IMAGE(src, sampler, coord + v * dir).x;
        hsum += fabs(h); // Use absolute value to normalize properly
    }

    WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(res / hsum));
}
