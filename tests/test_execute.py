import pyclesperanto as cle
import numpy as np

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

def test_execute_absolute():
    test = cle.push(np.asarray([
        [1, -1],
        [1, -1]
    ]))

    output = cle.create(test)

    cle.execute(device=cle.get_device(), kernel_name="absolute", kernel_source=absolute_ocl, parameters={'src': test, 'dst': output}, range=test.shape)

    print(output)

    a = cle.pull(output)
    assert (np.min(a) == 1)
    assert (np.max(a) == 1)
    assert (np.mean(a) == 1)
