
__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


inline int black_neighbors_around(IMAGE_src_TYPE src, const int c, const int r, const int p)
{
    // sum the neighborhood array of 27 elements
    int count = 0;


    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p, 0)).x;
    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r,   p, 0)).x;
    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p, 0)).x;

    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r-1, p, 0)).x;
    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r,   p, 0)).x;
    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p, 0)).x;

    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r-1, p, 0)).x;
    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r,   p, 0)).x;
    count +=  READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r+1, p, 0)).x;


    return count;
}


inline int wb_transitions_around(IMAGE_src_TYPE src, const int c, const int r, const int p)
{
    int count = 0;

    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r-1, p, 0)).x   == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p, 0)).x == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p, 0)).x == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r, p, 0)).x   == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p, 0)).x == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p, 0)).x == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p, 0)).x   == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p, 0)).x == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p, 0)).x == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p, 0)).x   == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p, 0)).x   == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r+1, p, 0)).x == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r+1, p, 0)).x == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r, p, 0)).x   == 0);
    count += (READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r, p, 0)).x   == 1) && (READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r-1, p, 0)).x == 0);

    return count;
}


__kernel void compute_thin_image(IMAGE_src_TYPE src, IMAGE_dst_TYPE dst )
{
    const int x = get_global_id(0);  // X coordinate of the pixel
    const int y = get_global_id(1);  // Y coordinate of the pixel
    const int z = get_global_id(2);  // Z coordinate of the pixel

    IMAGE_src_PIXEL_TYPE value = READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
    if (value == 0) {
        WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(0)); // Write 0 to the output image
        return; // Skip if the pixel is not foreground
    }

    int NZ    = black_neighbors_around(src, x, y, z);
    int TR_P1 = wb_transitions_around(src, x, y, z);
    int TR_P2 = wb_transitions_around(src, x, y-1, z);
    int TR_P4 = wb_transitions_around(src, x-1, y, z);

    int P2 = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y-1, z, 0)).x;
    int P4 = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(x-1, y, z, 0)).x;
    int P6 = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y+1, z, 0)).x;
    int P8 = (int) READ_IMAGE(src, sampler, POS_src_INSTANCE(x+1, y, z, 0)).x;

    int thinning_cond_1 = ((2 <= NZ) & (NZ <= 6));
    int thinning_cond_2 = (TR_P1 == 1);
    int thinning_cond_3 = (((P2 & P4 & P8) == 0) | (TR_P2 != 1));
    int thinning_cond_4 = (((P2 & P4 & P6) == 0) | (TR_P4 != 1));
    int thinning_cond_ok = thinning_cond_1 & thinning_cond_2 & thinning_cond_3 & thinning_cond_4;


    if (thinning_cond_ok) {
        WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(0));
        return; // Skip further processing for this pixel
    }
    WRITE_IMAGE(dst, POS_dst_INSTANCE(x, y, z, 0), CONVERT_dst_PIXEL_TYPE(value)); // Write original value to the output image
}

