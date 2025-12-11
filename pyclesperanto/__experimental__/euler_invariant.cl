__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


// // EULER LUT
// // source: https://github.com/fiji/Skeletonize3D/blob/master/src/main/java/sc/fiji/skeletonize3D/Skeletonize3D_.java#L494
// __constant int LUT[256] = {
// 0,  1,  0, -1,  0, -1,  0,  1,
// 0, -3,  0, -1,  0, -1,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,
		
// 0, -3,  0, -1,  0,  3,  0,  1,
// 0,  1,  0, -1,  0,  3,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,

// 0, -3,  0,  3,  0, -1,  0,  1,
// 0,  1,  0,  3,  0, -1,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,

// 0,  1,  0,  3,  0,  3,  0,  1,
// 0,  5,  0,  3,  0,  3,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,

// 0, -7,  0, -1,  0, -1,  0,  1,
// 0, -3,  0, -1,  0, -1,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,

// 0, -3,  0, -1,  0,  3,  0,  1,
// 0,  1,  0, -1,  0,  3,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,

// 0, -3,  0,  3,  0, -1,  0,  1,
// 0,  1,  0,  3,  0, -1,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1,

// 0,  1,  0,  3,  0,  3,  0,  1,
// 0,  5,  0,  3,  0,  3,  0,  1,
// 0, -1,  0,  1,  0,  1,  0, -1,
// 0,  3,  0,  1,  0,  1,  0, -1
// };


__constant int LUT[256] = {0, 1, 0, -1, 0, -1, 0, 1, 0, -3, 0, -1, 0, -1, 0, 1, 0, -1, 0, 1, 0, 1, 0, -1,
0, 3, 0, 1, 0, 1, 0, -1, 0, -3, 0, -1, 0, 3, 0, 1, 0, 1, 0, -1, 0, 3, 0, 1,
0, -1, 0, 1, 0, 1, 0, -1, 0, 3, 0, 1, 0, 1, 0, -1, 0, -3, 0, 3, 0, -1, 0, 1,
0, 1, 0, 3, 0, -1, 0, 1, 0, -1, 0, 1, 0, 1, 0, -1, 0, 3, 0, 1, 0, 1, 0, -1,
0, 1, 0, 3, 0, 3, 0, 1, 0, 5, 0, 3, 0, 3, 0, 1, 0, -1, 0, 1, 0, 1, 0, -1,
0, 3, 0, 1, 0, 1, 0, -1, 0, -7, 0, -1, 0, -1, 0, 1, 0, -3, 0, -1, 0, -1, 0, 1,
0, -1, 0, 1, 0, 1, 0, -1, 0, 3, 0, 1, 0, 1, 0, -1, 0, -3, 0, -1, 0, 3, 0, 1,
0, 1, 0, -1, 0, 3, 0, 1, 0, -1, 0, 1, 0, 1, 0, -1, 0, 3, 0, 1, 0, 1, 0, -1,
0, -3, 0, 3, 0, -1, 0, 1, 0, 1, 0, 3, 0, -1, 0, 1, 0, -1, 0, 1, 0, 1, 0, -1,
0, 3, 0, 1, 0, 1, 0, -1, 0, 1, 0, 3, 0, 3, 0, 1, 0, 5, 0, 3, 0, 3, 0, 1,
0, -1, 0, 1, 0, 1, 0, -1, 0, 3, 0, 1, 0, 1, 0, -1};



inline char indexOctantNEB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[2] > 0 )
      n |= 128;
    if( neighbors[1] > 0 )
      n |=  64;
    if( neighbors[11] > 0 )
      n |=  32;
    if( neighbors[10] > 0 )
      n |=  16;
    if( neighbors[5] > 0 )
      n |=   8;
    if( neighbors[4] > 0 )
      n |=   4;
    if( neighbors[14] > 0 )
      n |=   2;
    return n;
  }

inline char indexOctantNWB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[0] > 0 )
      n |= 128;
    if( neighbors[9] > 0 )
      n |=  64;
    if( neighbors[3] > 0 )
      n |=  32;
    if( neighbors[12] > 0 )
      n |=  16;
    if( neighbors[1] > 0 )
      n |=   8;
    if( neighbors[10] > 0 )
      n |=   4;
    if( neighbors[4] > 0 )
      n |=   2;
    return n;
  }

inline char indextOctantSEB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[8] > 0 )
      n |= 128;
    if( neighbors[7] > 0 )
      n |=  64;
    if( neighbors[17] > 0 )
      n |=  32;
    if( neighbors[16] > 0 )
      n |=  16;
    if( neighbors[5] > 0 )
      n |=   8;
    if( neighbors[4] > 0 )
      n |=   4;
    if( neighbors[14] > 0 )
      n |=   2;
    return n;
  }

inline char indexOctantSWB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[6] > 0 )
      n |= 128;
    if( neighbors[15] > 0 )
      n |=  64;
    if( neighbors[7] > 0 )
      n |=  32;
    if( neighbors[16] > 0 )
      n |=  16;
    if( neighbors[3] > 0 )
      n |=   8;
    if( neighbors[12] > 0 )
      n |=   4;
    if( neighbors[4] > 0 )
      n |=   2;
    return n;
  }

inline char indexOctantNEU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[20] > 0 )
      n |= 128;
    if( neighbors[23] > 0 )
      n |=  64;
    if( neighbors[19] > 0 )
      n |=  32;
    if( neighbors[22] > 0 )
      n |=  16;
    if( neighbors[11] > 0 )
      n |=   8;
    if( neighbors[14] > 0 )
      n |=   4;
    if( neighbors[10] > 0 )
      n |=   2;
    return n;
  }

inline char indexOctantNWU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[18] > 0 )
      n |= 128;
    if( neighbors[21] > 0 )
      n |=  64;
    if( neighbors[9] > 0 )
      n |=  32;
    if( neighbors[12] > 0 )
      n |=  16;
    if( neighbors[19] > 0 )
      n |=   8;
    if( neighbors[22] > 0 )
      n |=   4;
    if( neighbors[10] > 0 )
      n |=   2;
    return n;
  }

inline char indexOctantSEU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[26] > 0 )
      n |= 128;
    if( neighbors[23] > 0 )
      n |=  64;
    if( neighbors[17] > 0 )
      n |=  32;
    if( neighbors[14] > 0 )
      n |=  16;
    if( neighbors[25] > 0 )
      n |=   8;
    if( neighbors[22] > 0 )
      n |=   4;
    if( neighbors[16] > 0 )
      n |=   2;
    return n;
  }

inline char indexOctantSWU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[24] > 0  )
      n |= 128;
    if( neighbors[25] > 0 )
      n |=  64;
    if( neighbors[15] > 0 )
      n |=  32;
    if( neighbors[16] > 0 )
      n |=  16;
    if( neighbors[21] > 0 )
      n |=   8;
    if( neighbors[22] > 0 )
      n |=   4;
    if( neighbors[12] > 0 )
      n |=   2;
    return n;
  }


  /**
   * Check if a point is Euler invariant
   * 
   * @param neighbors neighbor pixels of the point
   * @return true or false if the point is Euler invariant or not
   */
inline bool is_euler_invariant(float neighbors[], int dimension, int x, int y, int z)
  {
    // Calculate Euler characteristic for each octant and sum up
    int eulerChar = 0;
    char n;
    // Octant SWU
    n = indexOctantSWU(neighbors);
    eulerChar += LUT[n];
    
    // Octant SEU
    n = indexOctantSEU(neighbors);
    eulerChar += LUT[n];
    
    // Octant NWU
    n = indexOctantNWU(neighbors);
    eulerChar += LUT[n];
    
    // Octant NEU
    n = indexOctantNEU(neighbors);
    eulerChar += LUT[n];
    
    // Octant SWB
    n = indexOctantSWB(neighbors);
    eulerChar += LUT[n];
    
    // Octant SEB
    n = indextOctantSEB(neighbors);
    eulerChar += LUT[n];
    
    // Octant NWB
    n = indexOctantNWB(neighbors);
    eulerChar += LUT[n];
    
    // Octant NEB
    n = indexOctantNEB(neighbors);
    eulerChar += LUT[n];


    // if (dimension == 3) {
    //     // For 3D, we check if the Euler characteristic is 1 (it never 0 in 3d apparently ...)
    //     return eulerChar == 1;
    // }

    return eulerChar == 0;
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

__kernel void euler_invariant(
    IMAGE_src_TYPE src,      // 3D coord array
    IMAGE_img_TYPE img,      // nD image
    IMAGE_dst_TYPE dst       // Output array (N, 3)
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

    if (is_euler_invariant(neighborhood, dimensions, x_coord, y_coord, z_coord)) {
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 0, 0, 0), CONVERT_dst_PIXEL_TYPE(x_coord));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 1, 0, 0), CONVERT_dst_PIXEL_TYPE(y_coord));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 2, 0, 0), CONVERT_dst_PIXEL_TYPE(z_coord));
    }
}