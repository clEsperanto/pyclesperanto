import numpy as np

def test_gpu_info():
    print("run test_gpu_info")
    import pyclesperanto as cle

    # print(cle.list_available_devices())
    cle.select_device("GTX")
    # print(cle.info())

def test_execute_kernel_1(n:int=2048):
    import numpy as np
    import pyclesperanto_prototype as cle

    valid = np.round(np.random.rand(n,n) * 10)
    input_image = valid * -1

    input = cle.push(input_image)
    output_gpu = cle.create_like(input)

    for n in range(20):
        cle.absolute(input, output_gpu)

    result = cle.pull(output_gpu)

    assert np.all(result == valid)

def test_execute_kernel_2(n:int=2048):
    import numpy as np
    import pyclesperanto as cle

    valid = np.round(np.random.rand(n,n) * 10)
    input_image = valid * -1

    input = cle.push(input_image)
    output_gpu = cle.create_like(input)

    for n in range(20):
        cle.absolute(input, output_gpu)

    result = cle.pull(output_gpu)

    assert np.all(result == valid)

def test_execute_kernel_4(n:int=2048):
    import numpy as np

    valid = np.round(np.random.rand(n,n) * 10)
    input_image = valid * -1

    for n in range(20):
        result = np.abs(input_image)

    assert np.all(result == valid)

def timeit_absolute():
    import timeit
    num_runs = 10

    duration = timeit.Timer(test_execute_kernel_1).timeit(number = num_runs)
    avg_duration = duration/num_runs
    print(f'proto On average it took {avg_duration} seconds')

    duration = timeit.Timer(test_execute_kernel_2).timeit(number = num_runs)
    avg_duration = duration/num_runs
    print(f'pycle On average it took {avg_duration} seconds')

    duration = timeit.Timer(test_execute_kernel_4).timeit(number = num_runs)
    avg_duration = duration/num_runs
    print(f'numpy On average it took {avg_duration} seconds')

# test_gpu_info()
timeit_absolute()

