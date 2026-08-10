"""Tests for comparison operators returning uint8 (device stand-in for bool)."""

import operator
import subprocess
import sys

import numpy as np
import pytest

import pyclesperanto as cle


def _run_subprocess(code):
    return subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, timeout=300
    )


_COMPARISONS = [
    operator.gt,
    operator.ge,
    operator.lt,
    operator.le,
    operator.eq,
    operator.ne,
]


@pytest.mark.parametrize("op", _COMPARISONS, ids=lambda o: o.__name__)
def test_comparison_array_scalar(gpu_backend, op):
    data = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    arr = cle.Array.from_array(data)
    result = op(arr, 2.0)
    assert isinstance(result, cle.Array)
    assert result.dtype == np.uint8
    np.testing.assert_array_equal(np.asarray(result), op(data, 2.0).astype(np.uint8))


@pytest.mark.parametrize("op", _COMPARISONS, ids=lambda o: o.__name__)
def test_comparison_array_array(gpu_backend, op):
    d1 = np.asarray([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    d2 = np.asarray([[4.0, 2.0], [3.0, 1.0]], dtype=np.float32)
    a1 = cle.Array.from_array(d1)
    a2 = cle.Array.from_array(d2)
    result = op(a1, a2)
    assert result.dtype == np.uint8
    np.testing.assert_array_equal(np.asarray(result), op(d1, d2).astype(np.uint8))


def test_bool_dtype_maps_to_uint8_on_creation(gpu_backend):
    assert cle.Array.empty((2, 2), dtype=bool).dtype == np.uint8
    assert cle.Array.zeros((2, 2), dtype=np.bool_).dtype == np.uint8
    assert cle.Array.from_array(np.ones((2, 2), dtype=bool)).dtype == np.uint8
    assert (
        cle.Array.from_array(np.ones((2, 2), np.float32), dtype=bool).dtype == np.uint8
    )


def test_astype_bool_maps_to_uint8(gpu_backend):
    arr = cle.Array.from_array(np.asarray([[0.0, 1.0]], dtype=np.float32))
    result = arr.astype(bool)
    assert result.dtype == np.uint8


def test_hash_and_set_membership(gpu_backend):
    a = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    b = cle.Array.from_array(np.asarray([1.0, 2.0], dtype=np.float32))
    assert hash(a) is not None
    s = {a, b}
    assert a in s and b in s
    d = {a: "first", b: "second"}
    assert d[a] == "first"
    assert d[b] == "second"


def test_comparison_with_none_does_not_crash():
    code = (
        "import numpy as np, pyclesperanto as cle\n"
        "A = cle.Array.from_array(np.ones((2, 2), np.float32))\n"
        "r = A == None\n"
        "print(int(np.asarray(r).sum()))\n"
    )
    proc = _run_subprocess(code)
    assert proc.returncode == 0
    assert proc.stdout.strip() == "0"


def test_ordering_comparison_with_none_does_not_crash():
    code = (
        "import numpy as np, pyclesperanto as cle\n"
        "A = cle.Array.from_array(np.ones((2, 2), np.float32))\n"
        "try:\n"
        "    A > None\n"
        "except TypeError:\n"
        "    pass\n"
        "print('ok')\n"
    )
    proc = _run_subprocess(code)
    assert proc.returncode == 0
    assert proc.stdout.strip() == "ok"
