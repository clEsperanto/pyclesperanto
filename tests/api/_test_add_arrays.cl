
__kernel void add_arrays(__global const float* a, __global const float* b, __global float* c, const unsigned int n) {
    int id = get_global_id(0);
    if (id < n) {
        c[id] = a[id] + b[id];
    }
}
