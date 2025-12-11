__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


inline bool is_end_point(const float neighborhood[27], int x, int y, int z) {
    int count = -1; // -1 because the center pixel is not counted
    for (int i = 0; i < 27; i++) {
        if (neighborhood[i] > 0) {
            count++;
        }
    }
    // printf("Neighborhood count: %d, Coordinates: (%d, %d, %d)\n", count, x, y, z);
    return (count == 1) ? true : false; // return 1 if it's an end point, otherwise return 0
}

inline void get_neighborhood(IMAGE_img_TYPE img, POS_img_TYPE pos, int dimension, float neighborhood[])
{
  if (dimension == 3) {
    neighborhood[0] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1, -1, -1, 0 )).x;
    neighborhood[1] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0, -1, -1, 0 )).x;
    neighborhood[2] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1, -1, -1, 0 )).x;
    neighborhood[3] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1,  0, -1, 0 )).x;
    neighborhood[4] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0,  0, -1, 0 )).x;
    neighborhood[5] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1,  0, -1, 0 )).x;
    neighborhood[6] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1,  1, -1, 0 )).x;
    neighborhood[7] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0,  1, -1, 0 )).x;
    neighborhood[8] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1,  1, -1, 0 )).x;
  }

  neighborhood[ 9] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1, -1, 0, 0 )).x;
  neighborhood[10] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0, -1, 0, 0 )).x;
  neighborhood[11] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1, -1, 0, 0 )).x;
  neighborhood[12] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1,  0, 0, 0 )).x;
  neighborhood[13] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0,  0, 0, 0 )).x;
  neighborhood[14] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1,  0, 0, 0 )).x;
  neighborhood[15] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1,  1, 0, 0 )).x;
  neighborhood[16] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0,  1, 0, 0 )).x;
  neighborhood[17] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1,  1, 0, 0 )).x;

  if (dimension == 3) {
    neighborhood[18] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1, -1, 1, 0 )).x;
    neighborhood[19] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0, -1, 1, 0 )).x;
    neighborhood[20] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1, -1, 1, 0 )).x;
    neighborhood[21] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1,  0, 1, 0 )).x;
    neighborhood[22] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0,  0, 1, 0 )).x;
    neighborhood[23] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1,  0, 1, 0 )).x;
    neighborhood[24] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE( -1,  1, 1, 0 )).x;
    neighborhood[25] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  0,  1, 1, 0 )).x;
    neighborhood[26] = READ_IMAGE(img, sampler, pos + POS_img_INSTANCE(  1,  1, 1, 0 )).x;
  }
}



__kernel void end_point(
    IMAGE_src_TYPE src,      // 3D coord array
    IMAGE_img_TYPE img,      // nD image
    IMAGE_dst_TYPE dst      // Output array (N, 3)
) 
{
    const int dimensions = (GET_IMAGE_DEPTH(img) > 1) ? 3 : 2;
    const int idx = get_global_id(0);
    const int x_coord = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(idx, 0, 0, 0)).x;
    const int y_coord = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(idx, 1, 0, 0)).x;
    const int z_coord = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(idx, 2, 0, 0)).x;

    if (x_coord < 0 || y_coord < 0 || z_coord < 0)
        return; // Skip if coordinates are negative


    float neighborhood[27] = {0};
    const POS_img_TYPE pos = POS_img_INSTANCE(x_coord, y_coord, z_coord, 0);
    get_neighborhood(img, pos, dimensions, neighborhood);

    if (!is_end_point(neighborhood, x_coord, y_coord, z_coord)) {
        // printf("Not an end point at (%d, %d, %d)\n", x_coord, y_coord, z_coord);
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 0, 0, 0), CONVERT_dst_PIXEL_TYPE(x_coord));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 1, 0, 0), CONVERT_dst_PIXEL_TYPE(y_coord));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 2, 0, 0), CONVERT_dst_PIXEL_TYPE(z_coord));
    }
}