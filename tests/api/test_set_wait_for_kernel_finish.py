import pytest

import pyclesperanto as cle


@pytest.mark.backend
def test_set_wait_for_kernel_finish(gpu_backend):
    cle.wait_for_kernel_to_finish(True)
