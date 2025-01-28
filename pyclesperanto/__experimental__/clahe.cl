# //
# // adapted from: https://github.com/HugoRaveton/pyopencl_clahe
# //
# // MIT License
# //
# // Copyright (c) 2024 Hugo Raveton
# //
# // Permission is hereby granted, free of charge, to any person obtaining a copy
# // of this software and associated documentation files (the "Software"), to deal
# // in the Software without restriction, including without limitation the rights
# // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# // copies of the Software, and to permit persons to whom the Software is
# // furnished to do so, subject to the following conditions:
# //
# // The above copyright notice and this permission notice shall be included in all
# // copies or substantial portions of the Software.
# //
# // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# // SOFTWARE.
# //

__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void clahe(
    IMAGE_src_TYPE src,             // Input image, flattened 3D array
    IMAGE_dst_TYPE dst,             // Output image, flattened 3D array
    int            tileSize,        // Size of each tile (cube)
    float          clipLimit,       // Clipping limit for histogram equalization
    float          minIntensity,    // Minimum intensity value
    float          maxIntensity     // Maximum intensity value
) {
    // Calculate global positions (flattened index) from 3D grid
    const int global_x = get_global_id(0);  // X coordinate of the pixel
    const int global_y = get_global_id(1);  // Y coordinate of the pixel
    const int global_z = get_global_id(2);  // Z coordinate of the pixel

    const int width = GET_IMAGE_WIDTH(src);    // src width
    const int height = GET_IMAGE_HEIGHT(src);  // src height
    const int depth = GET_IMAGE_DEPTH(src);    // src depth

    if (global_x >= width || global_y >= height || global_z >= depth) {
        return; // Out of bounds check
    }

    const float range = maxIntensity - minIntensity;
    const int numBins = 256; //number of bins (in a 8bit image)
    float hist[256] = {0}; // Histogram array

    // Calculate the start and end coordinates of each tile (current pixel position +/- tilesize/2)
    const int x_start = max(0, global_x - tileSize / 2);
    const int y_start = max(0, global_y - tileSize / 2);
    const int z_start = max(0, global_z - tileSize / 2);
    const int x_end = min(x_start + tileSize, width);
    const int y_end = min(y_start + tileSize, height);
    const int z_end = min(z_start + tileSize, depth);

    // Calculate the histogram for the current tile
    for (int z = z_start; z < z_end; z++) {
        for (int y = y_start; y < y_end; y++) {
            for (int x = x_start; x < x_end; x++) {
                const float pixelVal = (float) READ_IMAGE(src, sampler, POS_src_INSTANCE(x, y, z, 0)).x;
                const uint indx_x = convert_uint_sat(( (pixelVal - minIntensity) * (float)(numBins - 1) ) / range + 0.5 );
                hist[indx_x]++;
            }
        }
    }

    // Clip the histogram and redistribute the excess
    const float totalPixels = (x_end - x_start) * (y_end - y_start) * (z_end - z_start);
    const float limit = clipLimit * totalPixels / numBins;
    float excess = 0.0f;

    for (int i = 0; i < numBins; i++) {
        if (hist[i] > limit) {
            excess += hist[i] - limit;
            hist[i] = limit;
        }
    }

    const float increment = excess / numBins;
    for (int i = 0; i < numBins; i++) {
        hist[i] += increment;
    }

    // Compute the cumulative distribution function (CDF)
    float cdf[256];
    cdf[0] = hist[0];
    for (int i = 1; i < numBins; i++) {
        cdf[i] = cdf[i - 1] + hist[i];
    }

    // Normalize the CDF
    for (int i = 0; i < numBins; i++) {
        cdf[i] = (cdf[i] - cdf[0]) / (totalPixels - cdf[0]) * (maxIntensity - minIntensity) + minIntensity;
    }

    // Map the pixel value using the CDF
    float pixelVal = (float) READ_IMAGE(src, sampler, POS_src_INSTANCE(global_x, global_y, global_z, 0)).x;
    const uint indx_x = convert_uint_sat(( (pixelVal - minIntensity) * (float)(numBins - 1) ) / range + 0.5 );
    WRITE_IMAGE(dst, POS_dst_INSTANCE(global_x, global_y, global_z, 0), CONVERT_dst_PIXEL_TYPE(cdf[indx_x]));

}
