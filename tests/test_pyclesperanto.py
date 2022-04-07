import time
import numpy as np

def test_gpu_info():
    from pyclesperanto import gpu
    print(gpu().info())


def test_pycle_p():
    from pyclesperanto_prototype import available_device_names
    print(available_device_names())




def test_execute_kernel():
    # init gpu and print info
    import pyclesperanto as cle
    gpu = cle.gpu()
    gpu.set_wait_for_kernel_to_finish()
        
    input = np.ones((3,3,1), dtype=np.float32)
    valid = np.ones((3,3,1), dtype=np.float32) + 100

    # push and create buffer
    output_gpu = gpu.create(input.shape)
    input_gpu = gpu.push(input)
    
    # apply kernel
    cle.add_image_and_scalar(gpu, input_gpu, output_gpu, 100)
    
    # pull from device result and assert
    result = gpu.pull(output_gpu)
        
    print("input:", input.flatten(), input.dtype)
    print("valid:", valid.flatten(), valid.dtype)
    print("result:", result.flatten(), result.dtype)
            
    assert(np.sum(result.flatten()) == np.sum(valid.flatten()))
