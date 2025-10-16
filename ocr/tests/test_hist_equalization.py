import numpy as np
import pytest
from preprocessing_image.scripts.hist_equalization import preprocess as histogram_equalization_preprocess

# Utility functions to keep tests clean and DRY
def random_gray_image(size=(100, 100), low=0, high=255):
    return np.random.randint(low, high, size=size, dtype=np.uint8)

def random_color_image(size=(100, 100, 3), low=0, high=255):
    return np.random.randint(low, high, size=size, dtype=np.uint8)


@pytest.mark.sanity
def test_histogram_equalization_grayscale():
    img = random_gray_image()
    output = histogram_equalization_preprocess(img, {})
    assert output.ndim == 2
    assert output.shape == img.shape
    assert np.min(output) >= 0 and np.max(output) <= 255


@pytest.mark.sanity
def test_histogram_equalization_color():
    color_img = random_color_image()
    output = histogram_equalization_preprocess(color_img, {})
    assert output.ndim == 3
    assert output.shape == color_img.shape
    assert np.min(output) >= 0 and np.max(output) <= 255


@pytest.mark.sanity
def test_histogram_equalization_empty_image():
    img = np.zeros((0, 0), dtype=np.uint8)
    with pytest.raises(ValueError, match="Input image is empty or None."):
        histogram_equalization_preprocess(img, {})


@pytest.mark.sanity
def test_histogram_equalization_invalid_image():
    img = None
    with pytest.raises(ValueError, match="Input image is empty or None."):
        histogram_equalization_preprocess(img, {})


@pytest.mark.sanity
def test_histogram_equalization_invalid_image_type():
    img = np.random.randint(0, 256, size=(100, 100, 4), dtype=np.uint8)
    with pytest.raises(ValueError, match="Unsupported image format. Only 3-channel color images are supported."):
        histogram_equalization_preprocess(img, {})


@pytest.mark.sanity
def test_histogram_equalization_edge_case():
    img = random_gray_image((1, 1))
    output = histogram_equalization_preprocess(img, {})
    assert output.shape == img.shape
    assert output[0, 0] == img[0, 0]


@pytest.mark.sanity
def test_histogram_equalization_color_image_edge_case():
    color_img = random_color_image((1, 1, 3))  # A tiny color image
    output = histogram_equalization_preprocess(color_img, {})

    # Check if the output has the same shape as the input
    assert output.shape == color_img.shape

    # Allow a small tolerance for pixel value differences
    assert np.allclose(output, color_img, atol=1)  # Tolerance of 1 unit difference


@pytest.mark.sanity
def test_histogram_equalization_grayscale_contrast_increase():
    img = random_gray_image(low=100, high=150)
    output = histogram_equalization_preprocess(img, {})
    assert np.min(output) < np.min(img)
    assert np.max(output) > np.max(img)


@pytest.mark.sanity
def test_histogram_equalization_validation_success():
    img = random_gray_image()
    output = histogram_equalization_preprocess(img, {})
    assert isinstance(output, np.ndarray)
    assert output.shape == img.shape
    assert output.ndim == 2
    assert np.min(output) >= 0 and np.max(output) <= 255
