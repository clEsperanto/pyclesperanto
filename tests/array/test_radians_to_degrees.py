import numpy as np
import pytest

import pyclesperanto as cle


def test_radians_to_degrees(gpu_backend):
    test = cle.push(np.asarray([[np.pi, 0, -0.5 * np.pi]]))

    reference = cle.push(np.asarray([[180, 0, -90]]))

    result = cle.radians_to_degrees(test)

    a = cle.pull(result)
    b = cle.pull(reference)

    assert np.allclose(a, b, 0.01)
