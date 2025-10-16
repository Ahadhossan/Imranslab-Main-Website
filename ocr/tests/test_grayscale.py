import numpy as np
import pytest
from preprocessing_image.scripts.grayscale import preprocess as to_grayscale


@pytest.mark.sanity
def test_grayscale_conversion():
    color_img = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    gray_img = to_grayscale(color_img, {})
    assert gray_img.ndim == 2, "Output should be grayscale (2D)"
    assert gray_img.shape == (100, 100), "Dimensions should match input"


@pytest.mark.sanity
def test_already_grayscale():
    gray_img = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    result = to_grayscale(gray_img, {})
    assert np.array_equal(gray_img, result), "Grayscale input should remain unchanged"


@pytest.mark.sanity
def test_grayscale_primary_colors_conversion():
    colors = {
        "red": (np.array([[[0, 0, 255]]], dtype=np.uint8), 76),
        "green": (np.array([[[0, 255, 0]]], dtype=np.uint8), 150),
        "blue": (np.array([[[255, 0, 0]]], dtype=np.uint8), 29)
    }
    for name, (color_img, expected_gray) in colors.items():
        gray_img = to_grayscale(color_img, {})
        assert gray_img.shape == (1, 1), f"Shape incorrect for {name}"
        assert abs(gray_img[0, 0] - expected_gray) < 5, f"Conversion failed for {name}"


@pytest.mark.sanity
def test_grayscale_output_is_single_channel():
    color_image = np.random.randint(0, 256, size=(5, 7, 3), dtype=np.uint8)
    gray_image = to_grayscale(color_image, {})
    assert gray_image.shape == (5, 7), "Should be single channel"


@pytest.mark.sanity
def test_grayscale_invalid_input():
    with pytest.raises(ValueError):
        to_grayscale(None, {})
    with pytest.raises(ValueError):
        to_grayscale("not an image", {})

