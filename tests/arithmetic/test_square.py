import numpy as np

import pyclesperanto as cle
import pytest
@pytest.mark.backend
def test_square(gpu_backend):
    test1 = cle.push(np.asarray([4, 6]))

    reference = cle.push(np.asarray([16, 36]))

    result = cle.square(test1)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)

    print(a)
    print(b)

    assert np.allclose(a, b, 0.001)
