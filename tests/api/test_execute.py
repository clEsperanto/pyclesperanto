import numpy as np

import pyclesperanto as cle

absolute_ocl = """
__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_ADDRESS_CLAMP_TO_EDGE | CLK_FILTER_NEAREST;

__kernel void absolute(
    IMAGE_src_TYPE  src,
    IMAGE_dst_TYPE  dst
)
{
  const int x = get_global_id(0);
  const int y = get_global_id(1);
  const int z = get_global_id(2);

  IMAGE_src_PIXEL_TYPE value = READ_IMAGE(src, sampler, POS_src_INSTANCE(x,y,z,0)).x;
  if ( value < 0 ) {
    value = -1 * value;
  }

  WRITE_IMAGE(dst, POS_dst_INSTANCE(x,y,z,0), CONVERT_dst_PIXEL_TYPE(value));
}
"""

add_native_ocl = """
__kernel void add_arrays(__global const float* a, __global const float* b, __global float* c, const unsigned int n) {
    int id = get_global_id(0);
    if (id < n) {
        c[id] = a[id] + b[id];
    }
}
"""


def test_execute_native_from_file():
    input1 = cle.push(np.ones(10).astype(float))
    input2 = cle.push(np.ones(10).astype(float) * 2)
    output = cle.create(input1)

    param = {"a": input1, "b": input2, "c": output, "n": int(np.prod(input1.shape))}
    cle.native_execute(
        anchor=__file__,
        kernel_source="_test_add_arrays.cl",
        kernel_name="add_arrays",
        global_size=input1.shape,
        local_size=(1, 1, 1),
        parameters=param,
    )

    print(output)

    a = cle.pull(output)
    assert np.min(a) == 3
    assert np.max(a) == 3
    assert np.mean(a) == 3


def test_execute_absolute_from_file():
    input = cle.push(np.asarray([[1, -1], [1, -1]]).astype(float))
    output = cle.create(input)

    param = {"src": input, "dst": output}
    cle.execute(
        anchor=__file__,
        kernel_source="_test_absolute.cl",
        kernel_name="absolute",
        global_size=input.shape,
        parameters=param,
    )

    print(output)

    a = cle.pull(output)
    assert np.min(a) == 1
    assert np.max(a) == 1
    assert np.mean(a) == 1


def test_execute_native():
    input1 = cle.push(np.ones(10).astype(float))
    input2 = cle.push(np.ones(10).astype(float) * 2)
    output = cle.create(input1)

    param = {"a": input1, "b": input2, "c": output, "n": int(np.prod(input1.shape))}
    cle.native_execute(
        kernel_source=add_native_ocl,
        kernel_name="add_arrays",
        global_size=input1.shape,
        local_size=(1, 1, 1),
        parameters=param,
    )

    print(output)

    a = cle.pull(output)
    assert np.min(a) == 3
    assert np.max(a) == 3
    assert np.mean(a) == 3


def test_execute_absolute():
    input = cle.push(np.asarray([[1, -1], [1, -1]]).astype(float))
    output = cle.create(input)

    param = {"src": input, "dst": output}
    cle.execute(
        kernel_source=absolute_ocl,
        kernel_name="absolute",
        global_size=input.shape,
        parameters=param,
    )

    print(output)

    a = cle.pull(output)
    assert np.min(a) == 1
    assert np.max(a) == 1
    assert np.mean(a) == 1
