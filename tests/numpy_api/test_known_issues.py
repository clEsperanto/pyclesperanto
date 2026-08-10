"""Regression tests for still-open numpy-API known issues.

Only tests for unresolved issues should stay in this module.
"""

import numpy as np
import pytest

import pyclesperanto as cle

DOC = "docs/numpy_api_issues.md"


@pytest.mark.xfail(strict=False, reason=f"{DOC} #3: integer arithmetic saturates")
def test_uint8_subtraction_wraps_like_numpy(gpu_backend):
    data = np.asarray([[1, 5], [7, 3]], dtype=np.uint8)
    arr = cle.Array.from_array(data)
    np.testing.assert_array_equal(np.asarray(arr - 10), data - 10)


def test_uint8_float_scalar_promotes(gpu_backend):
    data = np.asarray([[1, 5], [7, 3]], dtype=np.uint8)
    arr = cle.Array.from_array(data)
    result = arr * 2.5
    np.testing.assert_allclose(np.asarray(result), data * 2.5)
