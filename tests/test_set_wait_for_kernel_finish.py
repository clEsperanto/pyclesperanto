import pyclesperanto as cle

cle.select_device("TX")


def test_set_wait_for_kernel_finish():
    cle.wait_for_kernel_to_finish(True)
