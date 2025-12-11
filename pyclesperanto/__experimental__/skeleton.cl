
__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


__constant int neighb_idx[8][7] = {
    {2, 1, 11, 10, 5, 4, 14},
    {0, 9, 3, 12, 1, 10, 4},
    {8, 7, 17, 16, 5, 4, 14},
    {6, 15, 7, 16, 3, 12, 4},
    {20, 23, 19, 22, 11, 14, 10},
    {18, 21, 9, 12, 19, 22, 10},
    {26, 23, 17, 14, 25, 22, 16},
    {24, 25, 15, 16, 21, 22, 12},
};

__constant int LUT[256] = {
    0,  1,  0, -1,  0, -1,  0,  1,  0, -3,  0, -1,  0, -1,  0,  1,  0, -1,  0,  1,  0,  1,  0, -1,
    0,  3,  0,  1,  0,  1,  0, -1,  0, -3,  0, -1,  0,  3,  0,  1,  0,  1,  0, -1,  0,  3,  0,  1,
    0, -1,  0,  1,  0,  1,  0, -1,  0,  3,  0,  1,  0,  1,  0, -1,  0, -3,  0,  3,  0, -1,  0,  1,
    0,  1,  0,  3,  0, -1,  0,  1,  0, -1,  0,  1,  0,  1,  0, -1,  0,  3,  0,  1,  0,  1,  0, -1,
    0,  1,  0,  3,  0,  3,  0,  1,  0,  5,  0,  3,  0,  3,  0,  1,  0, -1,  0,  1,  0,  1,  0, -1,
    0,  3,  0,  1,  0,  1,  0, -1,  0, -7,  0, -1,  0, -1,  0,  1,  0, -3,  0, -1,  0, -1,  0,  1,
    0, -1,  0,  1,  0,  1,  0, -1,  0,  3,  0,  1,  0,  1,  0, -1,  0, -3,  0, -1,  0,  3,  0,  1,
    0,  1,  0, -1,  0,  3,  0,  1,  0, -1,  0,  1,  0,  1,  0, -1,  0,  3,  0,  1,  0,  1,  0, -1,
    0, -3,  0,  3,  0, -1,  0,  1,  0,  1,  0,  3,  0, -1,  0,  1,  0, -1,  0,  1,  0,  1,  0, -1,
    0,  3,  0,  1,  0,  1,  0, -1,  0,  1,  0,  3,  0,  3,  0,  1,  0,  5,  0,  3,  0,  3,  0,  1,
    0, -1,  0,  1,  0,  1,  0, -1,  0,  3,  0,  1,  0,  1,  0, -1,
};

__constant int border[6] = { 4, 3, 2, 1, 5, 6 };


inline int is_euler_invariant(const uchar *neighbors) {
    int euler_char = 0;
    for (int octant = 0; octant < 8; ++octant) {
        int n = 1;
        for (int j = 0; j < 7; ++j) {
            int idx = neighb_idx[octant][j];
            if (neighbors[idx] == 1) {
                n |= (1 << (7 - j));
            }
        }
        euler_char += LUT[n];
    }
    return (euler_char == 0) ? 1 : 0; // return 1 (true) if Euler invariant, 0 (false) otherwise
}

inline int is_end_point(const uchar * neighborhood)
{
    // sum the neighborhood array of 27 elements
    int sum = 0;
    for (int i = 0; i < 9; i++) {
        sum += (int) neighborhood[i];
    }
    return (sum == 2)? 1 : 0; // return 1 (true) if end point, 0 (false) otherwise
}


inline void _get_neighborhood(IMAGE_src_TYPE src, const int c, const int r, const int p, uchar * neighborhood)
{
    // should be 0 if out of bounds
    neighborhood[ 0] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p-1, 0)).x;
    neighborhood[ 1] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r,   p-1, 0)).x;
    neighborhood[ 2] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p-1, 0)).x;

    neighborhood[ 3] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r-1, p-1, 0)).x;
    neighborhood[ 4] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r,   p-1, 0)).x;
    neighborhood[ 5] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p-1, 0)).x;

    neighborhood[ 6] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r-1, p-1, 0)).x;
    neighborhood[ 7] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r,   p-1, 0)).x;
    neighborhood[ 8] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r+1, p-1, 0)).x;

    neighborhood[ 9] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p, 0)).x;
    neighborhood[10] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r,   p, 0)).x;
    neighborhood[11] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p, 0)).x;

    neighborhood[12] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r-1, p, 0)).x;
    neighborhood[13] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r,   p, 0)).x;
    neighborhood[14] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p, 0)).x;

    neighborhood[15] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r-1, p, 0)).x;
    neighborhood[16] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r,   p, 0)).x;
    neighborhood[17] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r+1, p, 0)).x;

    neighborhood[18] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r-1, p+1, 0)).x;
    neighborhood[19] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r,   p+1, 0)).x;
    neighborhood[20] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r+1, p+1, 0)).x;

    neighborhood[21] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r-1, p+1, 0)).x;
    neighborhood[22] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r,   p+1, 0)).x;
    neighborhood[23] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p+1, 0)).x;

    neighborhood[24] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r-1, p+1, 0)).x;
    neighborhood[25] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r,   p+1, 0)).x;
    neighborhood[26] = (uchar) READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r+1, p+1, 0)).x;
}   



// inline int is_simple_point(uchar * neighborhood) {
//     // 3x3x3 neighborhood, center at index 13
//     // neighborhood: input array of 27 elements (0 or 1)
//     // result: output 1 if simple, 0 if not

//     // Helper arrays for 6-connectivity (foreground) and 26-connectivity (background)
//     const int fg_offsets[6] = { 1, -1, 3, -3, 9, -9 };
//     const int bg_offsets[26] = {
//         -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
//          1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13
//     };

//     // Copy neighborhood to local array and set center to 0 (simulate removal)
//     // uchar n[27];
//     // for (int i = 0; i < 27; ++i) n[i] = neighborhood[i];
//     // n[13] = 0;
//     neighborhood[13] = 0; // Set center to 0 to simulate removal

//     // Foreground connectivity: count 6-connected components of foreground (value 1)
//     uchar visited[27] = {0};
//     int fg_components = 0;
//     for (int i = 0; i < 27; ++i) {
//         if (neighborhood[i] == 1 && !visited[i]) {
//             // BFS for 6-connectivity
//             int queue[27], qh = 0, qt = 0;
//             queue[qt++] = i;
//             visited[i] = 1;
//             while (qh < qt) {
//                 int idx = queue[qh++];
//                 for (int j = 0; j < 6; ++j) {
//                     int ni = idx + fg_offsets[j];
//                     if (ni >= 0 && ni < 27 && neighborhood[ni] == 1 && !visited[ni]) {
//                         visited[ni] = 1;
//                         queue[qt++] = ni;
//                     }
//                 }
//             }
//             fg_components++;
//         }
//     }

//     // Background connectivity: count 26-connected components of background (value 0)
//     for (int i = 0; i < 27; ++i) 
//     {
//         visited[i] = 0;
//     }
//     int bg_components = 0;
//     for (int i = 0; i < 27; ++i) {
//         if (neighborhood[i] == 0 && !visited[i]) {
//             // BFS for 26-connectivity
//             int queue[27], qh = 0, qt = 0;
//             queue[qt++] = i;
//             visited[i] = 1;
//             while (qh < qt) {
//                 int idx = queue[qh++];
//                 for (int j = 0; j < 26; ++j) {
//                     int ni = idx + bg_offsets[j];
//                     if (ni >= 0 && ni < 27 && neighborhood[ni] == 0 && !visited[ni]) {
//                         visited[ni] = 1;
//                         queue[qt++] = ni;
//                     }
//                 }
//             }
//             bg_components++;
//         }
//     }

//     neighborhood[13] = 1; // Set center to 1 to simulate removal

//     // If both foreground and background have only one component, it's a simple point
//     return (fg_components == 1 && bg_components == 1) ? 1 : 0;
// }


__constant int octree_indices[8][7] = {
    {0, 1, 3, 4, 9, 10, 12},
    {1, 4, 10, 2, 5, 11, 13},
    {3, 4, 12, 6, 7, 14, 15},
    {4, 5, 13, 7, 15, 8, 16},
    {9, 10, 12, 17, 18, 20, 21},
    {10, 11, 13, 18, 21, 19, 22},
    {12, 14, 15, 20, 21, 23, 24},
    {13, 15, 16, 21, 22, 24, 25}
};

__constant int octree_adj[8][7][4] = {
    {{0,0,0,0}, {2,0,0,0}, {3,0,0,0}, {2,3,4,0}, {5,0,0,0}, {2,5,6,0}, {3,5,7,0}},
    {{1,0,0,0}, {1,3,4,0}, {1,5,6,0}, {0,0,0,0}, {4,0,0,0}, {6,0,0,0}, {4,6,8,0}},
    {{1,0,0,0}, {1,2,4,0}, {1,5,7,0}, {0,0,0,0}, {4,0,0,0}, {7,0,0,0}, {4,7,8,0}},
    {{1,2,3,0}, {2,0,0,0}, {2,6,8,0}, {3,0,0,0}, {3,7,8,0}, {0,0,0,0}, {8,0,0,0}},
    {{1,0,0,0}, {1,2,6,0}, {1,3,7,0}, {0,0,0,0}, {6,0,0,0}, {7,0,0,0}, {6,7,8,0}},
    {{1,2,5,0}, {2,0,0,0}, {2,4,8,0}, {5,0,0,0}, {5,7,8,0}, {0,0,0,0}, {8,0,0,0}},
    {{1,3,5,0}, {3,0,0,0}, {3,4,8,0}, {5,0,0,0}, {5,6,8,0}, {0,0,0,0}, {8,0,0,0}},
    {{2,4,6,0}, {3,4,7,0}, {4,0,0,0}, {5,6,7,0}, {6,0,0,0}, {7,0,0,0}, {0,0,0,0}}
};

__constant int octree_adj_len[8][7] = {
    {0,1,1,3,1,3,3},
    {1,3,3,0,1,1,3},
    {1,3,3,0,1,1,3},
    {3,1,3,1,3,0,1},
    {1,3,3,0,1,1,3},
    {3,1,3,1,3,0,1},
    {3,1,3,1,3,0,1},
    {3,3,1,3,1,1,0}
};

typedef struct StackElem {
    int octant;
    int label;
    int idx_in_octant;
} StackElem;

inline bool is_simple_point(const uchar neighbors[27]) {
    // Octree structure for labeling


    uchar cube[26];
    // Copy neighbors, skipping center (index 13)
    for (int i = 0; i < 13; ++i) cube[i] = neighbors[i];
    for (int i = 13; i < 26; ++i) cube[i] = neighbors[i+1];

    int label = 2;
    for (int i = 0; i < 26; ++i) {
        if (cube[i] == 1) {
            // Find which octant this index belongs to
            int octant = 0;
            if (i == 0 || i == 1 || i == 3 || i == 4 || i == 9 || i == 10 || i == 12) octant = 1;
            else if (i == 2 || i == 5 || i == 11 || i == 13) octant = 2;
            else if (i == 6 || i == 7 || i == 14 || i == 15) octant = 3;
            else if (i == 8 || i == 16) octant = 4;
            else if (i == 17 || i == 18 || i == 20 || i == 21) octant = 5;
            else if (i == 19 || i == 22) octant = 6;
            else if (i == 23 || i == 24) octant = 7;
            else if (i == 25) octant = 8;
            if (octant) {
                // --- Begin non-recursive octree_labeling ---
                StackElem stack[128];
                int stack_size = 0;
                int o = octant - 1;
                for (int j = 0; j < 7; ++j) {
                    int idx = octree_indices[o][j];
                    if (cube[idx] == 1) {
                        stack[stack_size].octant = octant;
                        stack[stack_size].label = label;
                        stack[stack_size].idx_in_octant = j;
                        stack_size++;
                    }
                }
                while (stack_size > 0) {
                    stack_size--;
                    StackElem elem = stack[stack_size];
                    int oct = elem.octant;
                    int oo = oct - 1;
                    int jj = elem.idx_in_octant;
                    int idx = octree_indices[oo][jj];
                    if (cube[idx] != label) {
                        cube[idx] = label;
                        for (int k = 0; k < octree_adj_len[oo][jj]; ++k) {
                            int next_oct = octree_adj[oo][jj][k];
                            int next_oo = next_oct - 1;
                            for (int m = 0; m < 7; ++m) {
                                int next_idx = octree_indices[next_oo][m];
                                if (cube[next_idx] == 1) {
                                    stack[stack_size].octant = next_oct;
                                    stack[stack_size].label = label;
                                    stack[stack_size].idx_in_octant = m;
                                    stack_size++;
                                }
                            }
                        }
                    }
                }
                // --- End non-recursive octree_labeling ---
            }
            label++;
            if (label - 2 >= 2)
                return false;
        }
    }
    return true;
}




inline int is_simple_point_candidate(IMAGE_src_TYPE src, const int border, const int c, const int r, const int p)
{
    int is_border = (border == 1 && READ_IMAGE(src, sampler, POS_src_INSTANCE(c-1, r, p, 0)).x == 0) || 
                    (border == 2 && READ_IMAGE(src, sampler, POS_src_INSTANCE(c+1, r, p, 0)).x == 0) ||  
                    (border == 3 && READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r+1, p, 0)).x == 0) ||
                    (border == 4 && READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r-1, p, 0)).x == 0) ||
                    (border == 5 && READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r, p+1, 0)).x == 0) ||
                    (border == 6 && READ_IMAGE(src, sampler, POS_src_INSTANCE(c, r, p-1, 0)).x == 0);                         

    if (is_border == 0)
        return 0; // not a border point, skip

    uchar neighborhood[27] = {0};
    _get_neighborhood(src, c, r, p, neighborhood);

    if ( (is_end_point(neighborhood) == 1 ) || (is_euler_invariant(neighborhood) == 0) || (is_simple_point(neighborhood) == 0) ) 
        return 0; // skip

    return 1;
}



__kernel void compute_thin_image(IMAGE_src_TYPE src )
{
    const int x = get_global_id(0);  // X coordinate of the pixel
    const int y = get_global_id(1);  // Y coordinate of the pixel
    const int z = get_global_id(2);  // Z coordinate of the pixel

    int num_borders = (GET_IMAGE_DEPTH(src) > 1)? 6 : 4; // Number of borders to check based on image depth

    IMAGE_src_PIXEL_TYPE value = READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
    if (value == 0) {
        return; // Skip if the pixel is not foreground
    }

    uchar neighborhood[27] = {0};

    for (int border_index = 0; border_index < num_borders; border_index++) {
        int current_border = border[border_index];
        int candidate = is_simple_point_candidate(src, current_border, x, y, z);

        if (candidate == 0) {
            continue; // Not a simple point candidate, skip
        }

        _get_neighborhood(src, x, y, z, neighborhood);
        if (is_simple_point(neighborhood)) {
            WRITE_IMAGE(src, POS_src_INSTANCE(x, y, z, 0), CONVERT_src_PIXEL_TYPE(0));
        }
    }

}
