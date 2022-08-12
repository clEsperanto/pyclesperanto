
def test_gpu_info():
    print("run test_gpu_info")
    from pyclesperanto import cle

    print(cle.Info())

def test_execute_kernel():
    # init gpu and print info
    import numpy as np
    from pyclesperanto import cle

    input_image = np.ones((3, 3, 1), dtype=np.float32)
    valid = np.ones((3, 3, 1), dtype=np.float32) + 100

    # push and create buffer
    output_gpu = cle.Create(input_image.shape)
    input_gpu = cle.Push(input_image)

    print(input_gpu.ToString())
    print(output_gpu.ToString())

    # apply kernel
    cle.AddImageAndScalar(input_gpu, output_gpu, 100)

    # # pull from device result and assert
    result = cle.Pull(output_gpu)

    print("input:", input_image.flatten(), input_image.dtype)
    print("valid:", valid.flatten(), valid.dtype)
    print("result:", result.flatten(), result.dtype)

    assert np.sum(result.flatten()) == np.sum(valid.flatten())
    
