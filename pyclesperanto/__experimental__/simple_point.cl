
#define STACK_SIZE 128

__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;


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

__kernel void simple_point(
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

    if (is_simple_point(neighborhood)) {
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 0, 0, 0), CONVERT_dst_PIXEL_TYPE(x_coord));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 1, 0, 0), CONVERT_dst_PIXEL_TYPE(y_coord));
        WRITE_IMAGE(dst, POS_dst_INSTANCE(idx, 2, 0, 0), CONVERT_dst_PIXEL_TYPE(z_coord));
    }
}