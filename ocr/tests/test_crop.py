"""
tests/testcrop.py

Tests for the crop preprocessing script used in OCR pipeline.
"""

import numpy as np
import pytest
from preprocessing_image.scripts.crop import preprocess


def generate_sample_image(shape=(100, 100), value=255):
    """Generate a dummy grayscale image for testing."""
    return np.full(shape, value, dtype=np.uint8)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_valid_area():
    """Test cropping with valid coordinates and size."""
    image = generate_sample_image()
    params = {"x": 10, "y": 10, "width": 20, "height": 30}
    output = preprocess(image, params)
    assert output.shape == (30, 20)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_at_edge():
    """Test cropping near the bottom-right edge."""
    image = generate_sample_image()
    params = {"x": 90, "y": 90, "width": 20, "height": 20}
    output = preprocess(image, params)
    assert output.shape == (10, 10)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_zero_width_height():
    """Test crop with zero width and height."""
    image = generate_sample_image()
    params = {"x": 10, "y": 10, "width": 0, "height": 0}
    with pytest.raises(ValueError):
        preprocess(image, params)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_negative_coords():
    """Test crop with negative x and y."""
    image = generate_sample_image()
    params = {"x": -5, "y": -5, "width": 10, "height": 10}
    with pytest.raises(ValueError):
        preprocess(image, params)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_negative_size():
    """Test crop with negative width and height."""
    image = generate_sample_image()
    params = {"x": 10, "y": 10, "width": -30, "height": -40}
    with pytest.raises(ValueError):
        preprocess(image, params)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_full_image_on_empty_params():
    """Test when no params are given, it should return full image."""
    image = generate_sample_image()
    output = preprocess(image, {})
    assert output.shape == (100, 100)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_exceeds_image_bounds():
    """Test crop larger than actual image bounds."""
    image = generate_sample_image()
    params = {"x": 0, "y": 0, "width": 200, "height": 150}
    output = preprocess(image, params)
    assert output.shape == (100, 100)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_rgb_image():
    """Test that RGB image crop preserves 3 channels."""
    image = np.full((100, 100, 3), 255, dtype=np.uint8)
    params = {"x": 5, "y": 5, "width": 50, "height": 50}
    output = preprocess(image, params)
    assert output.shape == (50, 50, 3)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_float_params():
    """Test crop with float values in params."""
    image = generate_sample_image()
    params = {"x": 10.5, "y": 20.2, "width": 30.9, "height": 40.7}
    output = preprocess(image, params)
    assert output.shape == (40, 30)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_empty_image():
    """Test that cropping empty image raises error."""
    image = np.array([], dtype=np.uint8)
    params = {"x": 0, "y": 0, "width": 10, "height": 10}
    with pytest.raises(Exception):
        preprocess(image, params)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_list_input():
    """Test that list input raises ValueError."""
    image = [[255] * 100] * 100  # not a NumPy array
    params = {"x": 0, "y": 0, "width": 10, "height": 10}
    with pytest.raises(ValueError):
        preprocess(image, params)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_partial_param_x_missing():
    """Test with missing x parameter."""
    image = generate_sample_image()
    params = {"y": 10, "width": 20, "height": 20}
    output = preprocess(image, params)
    assert output.shape == (20, 20)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_partial_param_y_missing():
    """Test with missing y parameter."""
    image = generate_sample_image()
    params = {"x": 10, "width": 20, "height": 20}
    output = preprocess(image, params)
    assert output.shape == (20, 20)


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_partial_param_width_missing():
    """Test with missing width parameter."""
    image = generate_sample_image()
    params = {"x": 10, "y": 10, "height": 20}
    output = preprocess(image, params)
    assert output.shape == (20, 90)  # 100 - x


@pytest.mark.preprocessing
@pytest.mark.crop
def test_crop_partial_param_height_missing():
    """Test with missing height parameter."""
    image = generate_sample_image()
    params = {"x": 10, "y": 10, "width": 20}
    output = preprocess(image, params)
    assert output.shape == (90, 20)
