
import numpy as np
import pyclesperanto as cle

def test_execute_kernel():
    # init gpu and print info
    gpu = cle.gpu()
    gpu.set_wait_for_kernel_to_finish(True)
    
    print(gpu.info())
    
    input = np.ones((3,3,3), dtype=np.float32)
    valid = np.ones((3,3,3), dtype=np.float32) + 100

    # push and create buffer
    out = gpu.create(input.shape)
    int = gpu.push(input)

    # apply kernel
    cle.add_image_and_scalar(gpu, int, out, 100)

    # pull from device result and assert
    result = gpu.pull(out)
    
    print("input:", input.flatten())
    print("result:", result.flatten())
    print("valid:", valid.flatten())

    assert(np.sum(result.flatten()) == np.sum(valid.flatten()))
