import time
import numpy as np
import pyclesperanto as cle


def test_gpu_info():
    gpu = cle.gpu()
    print(gpu.info())


def test_execute_kernel():
    # init gpu and print info
    gpu = cle.gpu()
    gpu.set_wait_for_kernel_to_finish()
        
    input = np.ones((3,3,1), dtype=np.float32)
    valid = np.ones((3,3,1), dtype=np.float32) + 100

    # push and create buffer
    out = gpu.create(input.shape)
    int = gpu.push(input)
    
    time.sleep(1)

    # apply kernel
    cle.add_image_and_scalar(gpu, int, out, 100)
    
    time.sleep(1)

    # pull from device result and assert
    result = gpu.pull(out)
    
    time.sleep(1)
    
    print("input:", input.flatten(), input.dtype)
    print("valid:", valid.flatten(), valid.dtype)
    print("result:", result.flatten(), result.dtype)
            
    assert(np.sum(result.flatten()) == np.sum(valid.flatten()))
