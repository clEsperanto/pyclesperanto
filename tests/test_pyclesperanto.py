import numpy as np
import pyclesperanto as cle


def test_gpu_info():
    gpu = cle.gpu()
    print(gpu.info())


def test_execute_kernel():
    # init gpu and print info
    device = cle.gpu()
    device.set_wait_for_kernel_to_finish()
        
    input = np.ones((3,3,1), dtype=np.float32)
    valid = np.ones((3,3,1), dtype=np.float32) + 100

    # push and create buffer
    gpu_output = device.create(input.shape)
    gpu_input = device.push(input)

    # apply kernel
    cle.add_image_and_scalar(device=device, input=gpu_input, output=gpu_output, scalar=100)

    # pull from device result and assert
    result = device.pull(gpu_output)
    
    print("input:", input.flatten(), input.dtype)
    print("valid:", valid.flatten(), valid.dtype)
    print("result:", result.flatten(), result.dtype)
            
    assert(np.sum(result.flatten()) == np.sum(valid.flatten()))
