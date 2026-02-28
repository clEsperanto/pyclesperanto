import numpy as np
import pytest

import pyclesperanto as cle

cle.select_device("TX")


class TestEvaluate:
    """Test suite for the evaluate function"""

    def test_evaluate_simple_addition(self):
        """Test simple addition expression"""
        a = cle.push(np.ones((10, 10)))

        result = cle.evaluate("a + 1", {"a": a})
        result_np = cle.pull(result)

        assert result_np.shape == (10, 10)
        assert np.allclose(result_np, 2.0)

    def test_evaluate_multiplication(self):
        """Test multiplication expression"""
        a = cle.push(np.full((5, 5), 2.0))

        result = cle.evaluate("a * 3", {"a": a})
        result_np = cle.pull(result)

        assert np.allclose(result_np, 6.0)

    def test_evaluate_two_arrays(self):
        """Test expression with two Array parameters"""
        a = cle.push(np.ones((8, 8)) * 2)
        b = cle.push(np.ones((8, 8)) * 3)

        result = cle.evaluate("a + b", {"a": a, "b": b})
        result_np = cle.pull(result)

        assert np.allclose(result_np, 5.0)

    def test_evaluate_complex_expression(self):
        """Test more complex expression"""
        a = cle.push(np.ones((4, 4)) * 2)

        result = cle.evaluate("a * 2 + 3", {"a": a})
        result_np = cle.pull(result)

        assert np.allclose(result_np, 7.0)

    def test_evaluate_with_numpy_array(self):
        """Test that numpy arrays are automatically converted to Array objects"""
        np_array = np.ones((6, 6)) * 5

        result = cle.evaluate("a - 1", {"a": np_array})
        result_np = cle.pull(result)

        assert np.allclose(result_np, 4.0)

    def test_evaluate_shape_mismatch_error(self):
        """Test that error is raised when Array parameters have different shapes"""
        a = cle.push(np.ones((5, 5)))
        b = cle.push(np.ones((3, 3)))

        with pytest.raises(
            ValueError, match="All Array parameters must have the same shape"
        ):
            cle.evaluate("a + b", {"a": a, "b": b})

    def test_evaluate_mixed_array_and_scalar(self):
        """Test expression with both Array and scalar parameters"""
        a = cle.push(np.ones((5, 5)) * 4)

        result = cle.evaluate(
            "a * scale + offset", {"a": a, "scale": 2.0, "offset": 1.0}
        )
        result_np = cle.pull(result)

        assert np.allclose(result_np, 9.0)

    def test_evaluate_output_dtype(self):
        """Test that output is float32"""
        a = cle.push(np.ones((3, 3)))

        result = cle.evaluate("a", {"a": a})

        assert result.dtype == np.float32

    def test_evaluate_device_inference(self):
        """Test that device is correctly inferred from Array parameter"""
        device = cle.get_device()
        a = cle.push(np.ones((4, 4)), device=device)

        result = cle.evaluate("a + 2", {"a": a})

        assert result.device == device

    def test_evaluate_trigonometric(self):
        """Test expression with trigonometric functions"""

        a = np.ones((3, 3)) * 1  # cos(1)
        b = np.ones((3, 3)) * 2  # sin(2)
        
        result = cle.evaluate("pow(cos(a),2) + pow(sin(b),2)", {"a": a, "b": b})
        
        reference = np.power(np.cos(a), 2) + np.power(np.sin(b), 2)
    
        assert np.allclose(result.get(), reference)
