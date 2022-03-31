
import numpy as np
import pyclesperanto as cle

def test_execute_kernel():
    # init gpu and print info
    gpu = cle.gpu()
    print(gpu.info())

    # push and create buffer
    out = gpu.create((5,5,5))
    int = gpu.push(np.ones((5,5,5), dtype=np.float32))

    # apply kernel
    cle.add_image_and_scalar(gpu, int, out, 100)

    # pull from device result and assert
    result = gpu.pull(out)
    assert(np.sum(result.flatten()) == (result.size * 101))
