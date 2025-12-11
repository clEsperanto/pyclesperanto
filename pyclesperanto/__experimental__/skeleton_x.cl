// Author: Robert Haase
//         March 2020
//
// Translated from:
// https://github.com/fiji/Skeletonize3D/blob/master/src/main/java/sc/fiji/skeletonize3D/Skeletonize3D_.java
/**
 * Skeletonize3D plugin for ImageJ(C).
 * Copyright (C) 2008 Ignacio Arganda-Carreras
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation (http://www.gnu.org/licenses/gpl.txt )
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 */

// EULER LUT
// source: https://github.com/fiji/Skeletonize3D/blob/master/src/main/java/sc/fiji/skeletonize3D/Skeletonize3D_.java#L494
__constant int LUT[256] = {
0,  1,  0, -1,  0, -1,  0,  1,
0, -3,  0, -1,  0, -1,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,
		
0, -3,  0, -1,  0,  3,  0,  1,
0,  1,  0, -1,  0,  3,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,

0, -3,  0,  3,  0, -1,  0,  1,
0,  1,  0,  3,  0, -1,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,

0,  1,  0,  3,  0,  3,  0,  1,
0,  5,  0,  3,  0,  3,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,

0, -7,  0, -1,  0, -1,  0,  1,
0, -3,  0, -1,  0, -1,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,

0, -3,  0, -1,  0,  3,  0,  1,
0,  1,  0, -1,  0,  3,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,

0, -3,  0,  3,  0, -1,  0,  1,
0,  1,  0,  3,  0, -1,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1,

0,  1,  0,  3,  0,  3,  0,  1,
0,  5,  0,  3,  0,  3,  0,  1,
0, -1,  0,  1,  0,  1,  0, -1,
0,  3,  0,  1,  0,  1,  0, -1
};


__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


inline char indexOctantNEB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[2] != 0 )
      n |= 128;
    if( neighbors[1] != 0 )
      n |=  64;
    if( neighbors[11] != 0 )
      n |=  32;
    if( neighbors[10] != 0 )
      n |=  16;
    if( neighbors[5] != 0 )
      n |=   8;
    if( neighbors[4] != 0 )
      n |=   4;
    if( neighbors[14] != 0 )
      n |=   2;
    return n;
  }

inline char indexOctantNWB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[0] != 0 )
      n |= 128;
    if( neighbors[9] != 0 )
      n |=  64;
    if( neighbors[3] != 0 )
      n |=  32;
    if( neighbors[12] != 0 )
      n |=  16;
    if( neighbors[1] != 0 )
      n |=   8;
    if( neighbors[10] != 0 )
      n |=   4;
    if( neighbors[4] != 0 )
      n |=   2;
    return n;
  }

inline char indextOctantSEB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[8] != 0 )
      n |= 128;
    if( neighbors[7] != 0 )
      n |=  64;
    if( neighbors[17] != 0 )
      n |=  32;
    if( neighbors[16] != 0 )
      n |=  16;
    if( neighbors[5] != 0 )
      n |=   8;
    if( neighbors[4] != 0 )
      n |=   4;
    if( neighbors[14] != 0 )
      n |=   2;
    return n;
  }

inline char indexOctantSWB(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[6] != 0 )
      n |= 128;
    if( neighbors[15] != 0 )
      n |=  64;
    if( neighbors[7] != 0 )
      n |=  32;
    if( neighbors[16] != 0 )
      n |=  16;
    if( neighbors[3] != 0 )
      n |=   8;
    if( neighbors[12] != 0 )
      n |=   4;
    if( neighbors[4] != 0 )
      n |=   2;
    return n;
  }

inline char indexOctantNEU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[20] != 0 )
      n |= 128;
    if( neighbors[23] != 0 )
      n |=  64;
    if( neighbors[19] != 0 )
      n |=  32;
    if( neighbors[22] != 0 )
      n |=  16;
    if( neighbors[11] != 0 )
      n |=   8;
    if( neighbors[14] != 0 )
      n |=   4;
    if( neighbors[10] != 0 )
      n |=   2;
    return n;
  }

inline char indexOctantNWU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[18] != 0 )
      n |= 128;
    if( neighbors[21] != 0 )
      n |=  64;
    if( neighbors[9] != 0 )
      n |=  32;
    if( neighbors[12] != 0 )
      n |=  16;
    if( neighbors[19] != 0 )
      n |=   8;
    if( neighbors[22] != 0 )
      n |=   4;
    if( neighbors[10] != 0 )
      n |=   2;
    return n;
  }

inline char indexOctantSEU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[26] != 0 )
      n |= 128;
    if( neighbors[23] != 0 )
      n |=  64;
    if( neighbors[17] != 0 )
      n |=  32;
    if( neighbors[14] != 0 )
      n |=  16;
    if( neighbors[25] != 0 )
      n |=   8;
    if( neighbors[22] != 0 )
      n |=   4;
    if( neighbors[16] != 0 )
      n |=   2;
    return n;
  }

inline char indexOctantSWU(float neighbors[]) {
    char n;
    n = 1;
    if( neighbors[24] != 0  )
      n |= 128;
    if( neighbors[25] != 0 )
      n |=  64;
    if( neighbors[15] != 0 )
      n |=  32;
    if( neighbors[16] != 0 )
      n |=  16;
    if( neighbors[21] != 0 )
      n |=   8;
    if( neighbors[22] != 0 )
      n |=   4;
    if( neighbors[12] != 0 )
      n |=   2;
    return n;
  }


  /**
   * Check if a point is Euler invariant
   * 
   * @param neighbors neighbor pixels of the point
   * @return true or false if the point is Euler invariant or not
   */
inline bool is_euler_invariant(float neighbors[])
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

    return eulerChar == 0;
}

inline void get_neighborhood(IMAGE_src_TYPE src, POS_src_TYPE pos, int dimension, float neighborhood[])
{
  if (dimension == 3) {
    neighborhood[0] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1, -1, -1, 0 )).x;
    neighborhood[1] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0, -1, -1, 0 )).x;
    neighborhood[2] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1, -1, -1, 0 )).x;
    neighborhood[3] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1,  0, -1, 0 )).x;
    neighborhood[4] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0,  0, -1, 0 )).x;
    neighborhood[5] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1,  0, -1, 0 )).x;
    neighborhood[6] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1,  1, -1, 0 )).x;
    neighborhood[7] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0,  1, -1, 0 )).x;
    neighborhood[8] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1,  1, -1, 0 )).x;
  }

  neighborhood[ 9] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1, -1, 0, 0 )).x;
  neighborhood[10] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0, -1, 0, 0 )).x;
  neighborhood[11] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1, -1, 0, 0 )).x;
  neighborhood[12] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1,  0, 0, 0 )).x;
  // skipping the center pixel
  neighborhood[14] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1,  0, 0, 0 )).x;
  neighborhood[15] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1,  1, 0, 0 )).x;
  neighborhood[16] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0,  1, 0, 0 )).x;
  neighborhood[17] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1,  1, 0, 0 )).x;

  if (dimension == 3) {
    neighborhood[18] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1, -1, 1, 0 )).x;
    neighborhood[19] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0, -1, 1, 0 )).x;
    neighborhood[20] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1, -1, 1, 0 )).x;
    neighborhood[21] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1,  0, 1, 0 )).x;
    neighborhood[22] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0,  0, 1, 0 )).x;
    neighborhood[23] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1,  0, 1, 0 )).x;
    neighborhood[24] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE( -1,  1, 1, 0 )).x;
    neighborhood[25] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  0,  1, 1, 0 )).x;
    neighborhood[26] = READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(  1,  1, 1, 0 )).x;
  }
}


// __constant int octree_indices[8][7] = {
//     {0, 1, 3, 4, 9, 10, 12},
//     {1, 4, 10, 2, 5, 11, 13},
//     {3, 4, 12, 6, 7, 14, 15},
//     {4, 5, 13, 7, 15, 8, 16},
//     {9, 10, 12, 17, 18, 20, 21},
//     {10, 11, 13, 18, 21, 19, 22},
//     {12, 14, 15, 20, 21, 23, 24},
//     {13, 15, 16, 21, 22, 24, 25}
// };

// __constant int octree_adj[8][7][4] = {
//     {{0,0,0,0}, {2,0,0,0}, {3,0,0,0}, {2,3,4,0}, {5,0,0,0}, {2,5,6,0}, {3,5,7,0}},
//     {{1,0,0,0}, {1,3,4,0}, {1,5,6,0}, {0,0,0,0}, {4,0,0,0}, {6,0,0,0}, {4,6,8,0}},
//     {{1,0,0,0}, {1,2,4,0}, {1,5,7,0}, {0,0,0,0}, {4,0,0,0}, {7,0,0,0}, {4,7,8,0}},
//     {{1,2,3,0}, {2,0,0,0}, {2,6,8,0}, {3,0,0,0}, {3,7,8,0}, {0,0,0,0}, {8,0,0,0}},
//     {{1,0,0,0}, {1,2,6,0}, {1,3,7,0}, {0,0,0,0}, {6,0,0,0}, {7,0,0,0}, {6,7,8,0}},
//     {{1,2,5,0}, {2,0,0,0}, {2,4,8,0}, {5,0,0,0}, {5,7,8,0}, {0,0,0,0}, {8,0,0,0}},
//     {{1,3,5,0}, {3,0,0,0}, {3,4,8,0}, {5,0,0,0}, {5,6,8,0}, {0,0,0,0}, {8,0,0,0}},
//     {{2,4,6,0}, {3,4,7,0}, {4,0,0,0}, {5,6,7,0}, {6,0,0,0}, {7,0,0,0}, {0,0,0,0}}
// };

// __constant int octree_adj_len[8][7] = {
//     {0,1,1,3,1,3,3},
//     {1,3,3,0,1,1,3},
//     {1,3,3,0,1,1,3},
//     {3,1,3,1,3,0,1},
//     {1,3,3,0,1,1,3},
//     {3,1,3,1,3,0,1},
//     {3,1,3,1,3,0,1},
//     {3,3,1,3,1,1,0}
// };

// typedef struct StackElem {
//     int octant;
//     int label;
//     int idx_in_octant;
// } StackElem;

// inline bool is_simple_point(const float neighbors[27]) {
//     // Octree structure for labeling
//     // Copy neighbors, skipping center (index 13)
//     float cube[26];
//     for (int i = 0; i < 13; ++i) cube[i] = neighbors[i];
//     for (int i = 13; i < 26; ++i) cube[i] = neighbors[i+1];

//     int label = 2;
//     for (int i = 0; i < 26; ++i) {
//         if (cube[i] > 0) {
//             // Find which octant this index belongs to
//             int octant = 0;
//             if (i == 0 || i == 1 || i == 3 || i == 4 || i == 9 || i == 10 || i == 12) octant = 1;
//             else if (i == 2 || i == 5 || i == 11 || i == 13) octant = 2;
//             else if (i == 6 || i == 7 || i == 14 || i == 15) octant = 3;
//             else if (i == 8 || i == 16) octant = 4;
//             else if (i == 17 || i == 18 || i == 20 || i == 21) octant = 5;
//             else if (i == 19 || i == 22) octant = 6;
//             else if (i == 23 || i == 24) octant = 7;
//             else if (i == 25) octant = 8;
//             if (octant != 0) {
//                 // --- Begin non-recursive octree_labeling ---
//                 StackElem stack[128];
//                 int stack_size = 0;
//                 int o = octant - 1;
//                 for (int j = 0; j < 7; ++j) {
//                     int idx = octree_indices[o][j];
//                     if (cube[idx] == 1) {
//                         stack[stack_size].octant = octant;
//                         stack[stack_size].label = label;
//                         stack[stack_size].idx_in_octant = j;
//                         stack_size++;
//                     }
//                 }
//                 while (stack_size > 0) {
//                     stack_size--;
//                     StackElem elem = stack[stack_size];
//                     int oct = elem.octant;
//                     int oo = oct - 1;
//                     int jj = elem.idx_in_octant;
//                     int idx = octree_indices[oo][jj];
//                     if (cube[idx] != label) {
//                         cube[idx] = label;
//                         for (int k = 0; k < octree_adj_len[oo][jj]; ++k) {
//                             int next_oct = octree_adj[oo][jj][k];
//                             int next_oo = next_oct - 1;
//                             for (int m = 0; m < 7; ++m) {
//                                 int next_idx = octree_indices[next_oo][m];
//                                 if (cube[next_idx] == 1) {
//                                     stack[stack_size].octant = next_oct;
//                                     stack[stack_size].label = label;
//                                     stack[stack_size].idx_in_octant = m;
//                                     stack_size++;
//                                 }
//                             }
//                         }
//                     }
//                 }
//                 // --- End non-recursive octree_labeling ---
//             }
//             label++;
//             if (label - 2 >= 2)
//                 return false;
//         }
//     }
//     return true;
// }





#define STACK_SIZE 128

typedef struct {
    int octant;
    int cube[26];
} StackItem;

void octreeLabeling(int start_octant, int label, float cube[26]) {
    // Stack for iterative DFS
    int stack[STACK_SIZE][2];
    int stack_top = 0;

    // Push initial octant
    stack[stack_top][0] = start_octant;
    stack[stack_top][1] = -1; // -1 means no specific cube index
    stack_top++;

    while (stack_top > 0) {
        stack_top--;
        int octant = stack[stack_top][0];

        // For each octant, process as in the original code
        if (octant == 1) {
            if (cube[0] == 1) cube[0] = label;
            if (cube[1] == 1) {
                cube[1] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
            }
            if (cube[3] == 1) {
                cube[3] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
            }
            if (cube[4] == 1) {
                cube[4] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
            }
            if (cube[9] == 1) {
                cube[9] = label;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
            }
            if (cube[10] == 1) {
                cube[10] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[12] == 1) {
                cube[12] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 2) {
            if (cube[1] == 1) {
                cube[1] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
            }
            if (cube[4] == 1) {
                cube[4] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
            }
            if (cube[10] == 1) {
                cube[10] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[2] == 1) cube[2] = label;
            if (cube[5] == 1) {
                cube[5] = label;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
            }
            if (cube[11] == 1) {
                cube[11] = label;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[13] == 1) {
                cube[13] = label;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 3) {
            if (cube[3] == 1) {
                cube[3] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
            }
            if (cube[4] == 1) {
                cube[4] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
            }
            if (cube[12] == 1) {
                cube[12] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[6] == 1) cube[6] = label;
            if (cube[7] == 1) {
                cube[7] = label;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
            }
            if (cube[14] == 1) {
                cube[14] = label;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[15] == 1) {
                cube[15] = label;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 4) {
            if (cube[4] == 1) {
                cube[4] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
            }
            if (cube[5] == 1) {
                cube[5] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
            }
            if (cube[13] == 1) {
                cube[13] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
            if (cube[7] == 1) {
                cube[7] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
            }
            if (cube[15] == 1) {
                cube[15] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
            if (cube[8] == 1) cube[8] = label;
            if (cube[16] == 1) {
                cube[16] = label;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 5) {
            if (cube[9] == 1) {
                cube[9] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
            }
            if (cube[10] == 1) {
                cube[10] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[12] == 1) {
                cube[12] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[17] == 1) cube[17] = label;
            if (cube[18] == 1) {
                cube[18] = label;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[20] == 1) {
                cube[20] = label;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[21] == 1) {
                cube[21] = label;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 6) {
            if (cube[10] == 1) {
                cube[10] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
            }
            if (cube[11] == 1) {
                cube[11] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
            }
            if (cube[13] == 1) {
                cube[13] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
            if (cube[18] == 1) {
                cube[18] = label;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
            }
            if (cube[21] == 1) {
                cube[21] = label;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
            if (cube[19] == 1) cube[19] = label;
            if (cube[22] == 1) {
                cube[22] = label;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 7) {
            if (cube[12] == 1) {
                cube[12] = label;
                stack[stack_top][0] = 1; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
            }
            if (cube[14] == 1) {
                cube[14] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
            }
            if (cube[15] == 1) {
                cube[15] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
            if (cube[20] == 1) {
                cube[20] = label;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
            }
            if (cube[21] == 1) {
                cube[21] = label;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
            if (cube[23] == 1) cube[23] = label;
            if (cube[24] == 1) {
                cube[24] = label;
                stack[stack_top][0] = 8; stack[stack_top++][1] = -1;
            }
        }
        if (octant == 8) {
            if (cube[13] == 1) {
                cube[13] = label;
                stack[stack_top][0] = 2; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[15] == 1) {
                cube[15] = label;
                stack[stack_top][0] = 3; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[16] == 1) {
                cube[16] = label;
                stack[stack_top][0] = 4; stack[stack_top++][1] = -1;
            }
            if (cube[21] == 1) {
                cube[21] = label;
                stack[stack_top][0] = 5; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[22] == 1) {
                cube[22] = label;
                stack[stack_top][0] = 6; stack[stack_top++][1] = -1;
            }
            if (cube[24] == 1) {
                cube[24] = label;
                stack[stack_top][0] = 7; stack[stack_top++][1] = -1;
            }
            if (cube[25] == 1) cube[25] = label;
        }
    }
}


bool is_simple_point(const float neighbors[27]) {
    float cube[26];
    int i;
    // Copy neighbors for labeling
    for (i = 0; i < 13; i++) // i = 0..12 -> cube[0..12]
        cube[i] = neighbors[i];
    // i != 13 : ignore center pixel when counting (see [Lee94])
    for (i = 14; i < 27; i++) // i = 14..26 -> cube[13..25]
        cube[i - 1] = neighbors[i];

    int label = 2;
    // For all points in the neighborhood
    for (i = 0; i < 26; i++) {
        if (cube[i] == 1) { // voxel has not been labeled yet
            // Start recursion with any octant that contains the point i
            switch (i) {
                case 0: case 1: case 3: case 4: case 9: case 10: case 12:
                    octreeLabeling(1, label, cube);
                    break;
                case 2: case 5: case 11: case 13:
                    octreeLabeling(2, label, cube);
                    break;
                case 6: case 7: case 14: case 15:
                    octreeLabeling(3, label, cube);
                    break;
                case 8: case 16:
                    octreeLabeling(4, label, cube);
                    break;
                case 17: case 18: case 20: case 21:
                    octreeLabeling(5, label, cube);
                    break;
                case 19: case 22:
                    octreeLabeling(6, label, cube);
                    break;
                case 23: case 24:
                    octreeLabeling(7, label, cube);
                    break;
                case 25:
                    octreeLabeling(8, label, cube);
                    break;
            }
            label++;
            if ((label - 2) >= 2) {
                return false;
            }
        }
    }
    // return label-2; // if the number of connected components is needed
    return true;
}


inline bool is_end_point(const float neighborhood[27]) {
    int count = -1; // -1 because the center pixel is not counted
    for (int i = 0; i < 27; i++) {
        if (neighborhood[i] != 0) {
            count++;
        }
    }
    return (count == 1) ? true : false; // return 1 if it's an end point, otherwise return 0
}



__kernel void skeletonize(
    IMAGE_src_TYPE src,
    IMAGE_flag_dst_TYPE flag_dst,
    IMAGE_dst_TYPE dst,
    const int direction,
    const int dimension
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  const POS_src_TYPE pos = POS_src_INSTANCE(x, y, z, 0);

  float pixel = (float) READ_IMAGE(src, sampler, pos).x;
  if (pixel == 0) {
    WRITE_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(pixel));
    return; // pixel is background already.
  }


  const POS_src_TYPE pos_dist;

  bool is_border_point = false;
  if( direction == 1 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(-1, 0, 0, 0)).x == 0 ) { // north
    is_border_point = true;
  }
  if( direction == 2 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(1, 0, 0, 0)).x == 0 ) { // south
    is_border_point = true;
  }
  if( direction == 3 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, -1, 0, 0)).x == 0 ) { // east
    is_border_point = true;
  }
  if( direction == 4 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, 1, 0, 0)).x == 0 ) { // west
    is_border_point = true;
  }
  if( direction == 5 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, 0, -1, 0)).x == 0 ) { // lower
    is_border_point = true;
  }
  if( direction == 6 && READ_IMAGE(src, sampler, pos + POS_src_INSTANCE(0, 0, 1, 0)).x == 0 ) { // upper
    is_border_point = true;
  }


  if (!is_border_point) {
    WRITE_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(pixel));
    return; // current point is not deletable
  }

  float neighborhood[27] = {0};
  neighborhood[13] = pixel; // center pixel
  get_neighborhood(src, pos, dimension, neighborhood);


  if (is_end_point(neighborhood)) { // current pixel is an end point and cannot be deleted
    WRITE_IMAGE (dst, pos, CONVERT_dst_PIXEL_TYPE(pixel));
    return;
  }

  // Check if point is Euler invariant (condition 1 in Lee[94])
  if( !is_euler_invariant(neighborhood) )
  {
    WRITE_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(pixel));
    return;         // current point is not deletable
  }

  if( !is_simple_point(neighborhood) )
  {
    WRITE_IMAGE(dst, pos, CONVERT_dst_PIXEL_TYPE(pixel));
    return;         // current point is not deletable
  }

  // set flag to indicate a change
  WRITE_IMAGE (flag_dst, POS_flag_dst_INSTANCE(0, 0, 0, 0), 1);
  // delete current point
  WRITE_IMAGE (dst, pos, 0);

}