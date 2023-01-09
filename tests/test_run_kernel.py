def test_run():
    import pyclesperanto as cle
    import numpy as np

    rand_arr = np.ones((100, 100)).astype(np.uint8)
    binary = cle.add_image_and_scalar(rand_arr, scalar=10)
    res = cle.pull(binary)

    assert res.sum() == (rand_arr + 10).sum()
