import numpy as np
import pytest
from preprocessing_image.scripts.morph_close import preprocess
from preprocessing_image.validation.morph_close_validation import validate


@pytest.fixture
def test_image():
    return np.full((100, 100), 255, dtype=np.uint8)  # Example binary image


@pytest.mark.sanity
def test_morph_close(test_image):
    params = {
        "ksize": 5,
        "kernel_shape": "ellipse",
        "target": "dark"
    }
    output = preprocess(test_image, **params)
    result = validate(test_image, output, params)

    # Check that the result is a success and that the processed image is valid
    assert result["status"] == "success"
    assert "added_pixels" in result["metrics"]  # Change from 'filled_holes' to 'added_pixels'


@pytest.mark.sanity
def test_invalid_kernel_size():
    params = {
        "ksize": 0,  # Invalid kernel size
        "kernel_shape": "ellipse",
        "target": "dark"
    }
    with pytest.raises(ValueError):
        preprocess(np.ones((100, 100), dtype=np.uint8), **params)


@pytest.mark.sanity
def test_morph_close_default_params(test_image):
    params = {}  # Test default behavior
    output = preprocess(test_image, **params)
    result = validate(test_image, output, params)

    # Check that the result is a success and that the processed image is valid
    assert result["status"] == "success"
    assert "added_pixels" in result["metrics"]  # Change from 'filled_holes' to 'added_pixels'


@pytest.mark.sanity
def test_empty_image():
    empty_image = np.zeros((100, 100), dtype=np.uint8)
    params = {
        "ksize": 5,
        "kernel_shape": "rect",
        "target": "dark"
    }
    output = preprocess(empty_image, **params)
    result = validate(empty_image, output, params)

    # Check that the result is a success
    assert result["status"] == "success"


@pytest.mark.sanity
def test_large_kernel_size(test_image):
    params = {
        "ksize": 101,  # Large kernel size
        "kernel_shape": "cross",
        "target": "dark"
    }
    output = preprocess(test_image, **params)
    result = validate(test_image, output, params)

    # Check that the result is a success
    assert result["status"] == "success"
    assert "added_pixels" in result["metrics"]  # Change from 'filled_holes' to 'added_pixels'


@pytest.mark.sanity
def test_kernel_shape_cross(test_image):
    params = {
        "ksize": 5,
        "kernel_shape": "cross",
        "target": "dark"
    }
    output = preprocess(test_image, **params)
    result = validate(test_image, output, params)

    # Check that the result is a success
    assert result["status"] == "success"


@pytest.mark.sanity
def test_kernel_shape_ellipse(test_image):
    params = {
        "ksize": 5,
        "kernel_shape": "ellipse",
        "target": "dark"
    }
    output = preprocess(test_image, **params)
    result = validate(test_image, output, params)

    # Check that the result is a success
    assert result["status"] == "success"


@pytest.mark.sanity
def test_target_bright(test_image):
    params = {
        "ksize": 5,
        "kernel_shape": "rect",
        "target": "bright"
    }
    output = preprocess(test_image, **params)
    result = validate(test_image, output, params)

    # Check that the result is a success
    assert result["status"] == "success"
    assert "added_pixels" in result["metrics"]  # Change from 'filled_holes' to 'added_pixels'
