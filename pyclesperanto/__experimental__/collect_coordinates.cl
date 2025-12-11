
__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


__kernel void collect_coordinates(
    IMAGE_src_TYPE src,      // 3D array flattened
    IMAGE_dst_TYPE dst,      // Output array (N, 3)
    IMAGE_idx_TYPE idx,       // Atomic counter
    const int direction
) 
{
    int x = get_global_id(0);
    int y = get_global_id(1);
    int z = get_global_id(2);
    float value = (float) READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
    if (value <= 0) {
        return; // Skip if the value is not positive
    }

    const POS_src_TYPE pos = POS_src_INSTANCE(x, y, z, 0);
    bool is_border_point = false;
    if( direction == 1 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(-1, 0, 0, 0)).x == 0 ) { // north
        is_border_point = true;
    }
    else if( direction == 2 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(1, 0, 0, 0)).x == 0 ) { // south
        is_border_point = true;
    }
    else if( direction == 3 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, 1, 0, 0)).x == 0 ) { // east
        is_border_point = true;
    }
    else if( direction == 4 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, -1, 0, 0)).x == 0 ) { // west
        is_border_point = true;
    }
    else if( direction == 5 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, 0, 1, 0)).x == 0 ) { // lower
        is_border_point = true;
    }
    else if( direction == 6 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, 0, -1, 0)).x == 0 ) { // upper
        is_border_point = true;
    }

    if (is_border_point) {
        int out_idx = atomic_inc(idx);
        WRITE_IMAGE(dst, POS_dst_INSTANCE(out_idx, 0, 0, 0), CONVERT_dst_PIXEL_TYPE(x));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(out_idx, 1, 0, 0), CONVERT_dst_PIXEL_TYPE(y));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(out_idx, 2, 0, 0), CONVERT_dst_PIXEL_TYPE(z));
    }
}


