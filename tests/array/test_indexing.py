import numpy as np
import pytest

import pyclesperanto as cle


@pytest.mark.backend
def test_indexing(gpu_backend):
    data = np.asarray([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]).astype(np.float32)

    cl_data = cle.push(data)

    assert cl_data[0, 0] == 1
    assert cl_data[0, 1] == 2
