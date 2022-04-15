import numpy as np
from pyclesperanto import Clesperanto


def test_gpu_info():
    cle = Clesperanto()
    print(cle.info())


def test_execute_kernel():
    # init gpu and print info
    cle = Clesperanto()
    cle.set_wait_for_kernel_to_finish()
        
    input_image = np.ones((5,10), dtype=np.float32)
    valid = np.ones((5,10), dtype=np.float32) + 100

    # push and create buffer
    output_gpu = cle.create(input_image.shape)
    input_gpu = cle.push(input_image)
    

    # apply kernel
    cle.add_image_and_scalar(input_gpu, output_gpu, scalar=100)
    

    # pull from device result and assert
    result = cle.pull(output_gpu)   
    
    print("input:", input_image.flatten(), input_image.dtype)
    print("valid:", valid.flatten(), valid.dtype)
    print("result:", result.flatten(), result.dtype)
            
    assert(np.sum(result.flatten()) == np.sum(valid.flatten()))

