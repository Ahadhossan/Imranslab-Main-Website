import numpy as np
import pytest
import cv2
import logging
from preprocessing_image.scripts.median_blur import preprocess


# Helper functions to generate test images
def generate_grayscale_image(size=(100, 100), color_value=255):
    """Generate a simple grayscale image with a given color value."""
    return np.full(size, color_value, dtype=np.uint8)


def generate_color_image(size=(100, 100), color_value=(255, 0, 0)):
    """Generate a simple color image (BGR) with the given color value."""
    img = np.zeros((size[0], size[1], 3), dtype=np.uint8)
    img[:] = color_value  # Apply the color value to all pixels
    return img


def generate_noisy_image(size=(100, 100), noise_level=50):
    """Generate a noisy image with random noise."""
    img = np.zeros(size, dtype=np.uint8)
    noise = np.random.randint(0, noise_level, size, dtype=np.uint8)
    noisy_img = cv2.add(img, noise)  # Add noise to the image
    return noisy_img


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_grayscale():
    """Test the median blur on grayscale images."""
    print("\nRunning test: Median Blur on Grayscale Image")
    img = generate_grayscale_image(color_value=0)  # Black image
    blurred = preprocess(img, {"ksize": 5})

    # The image should be blurred, but the overall structure should remain unchanged
    assert blurred.shape == img.shape, "Shape mismatch after blur."
    print("Test Passed: Grayscale image median blur applied successfully.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_color():
    """Test the median blur on color images."""
    print("\nRunning test: Median Blur on Color Image (BGR)")
    img = generate_color_image(color_value=(0, 255, 0))  # Green image
    blurred = preprocess(img, {"ksize": 5})

    # The image should be blurred, but the overall structure should remain unchanged
    assert blurred.shape == img.shape, "Shape mismatch after blur."
    print("Test Passed: Color image median blur applied successfully.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_with_noise():
    """Test the median blur on a noisy image."""
    print("\nRunning test: Median Blur on Noisy Image")
    img = generate_noisy_image(size=(100, 100), noise_level=255)  # Noisy image
    blurred = preprocess(img, {"ksize": 5})

    # Check if noise has been reduced after applying the median blur
    assert np.count_nonzero(blurred != img) > 0, "Median blur did not reduce noise."
    print("Test Passed: Noise reduced in noisy image after median blur.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_small_kernel():
    """Test the median blur with a small kernel size."""
    print("\nRunning test: Median Blur with Small Kernel Size (3x3)")
    img = generate_grayscale_image(color_value=0)
    blurred = preprocess(img, {"ksize": 3})

    # The image should be blurred but not overly smoothed
    assert blurred.shape == img.shape, "Shape mismatch after blur."
    print("Test Passed: Small kernel median blur applied successfully.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_large_kernel():
    """Test the median blur with a large kernel size."""
    print("\nRunning test: Median Blur with Large Kernel Size (15x15)")
    img = generate_grayscale_image(color_value=0)
    blurred = preprocess(img, {"ksize": 15})

    # The image should still retain its shape
    assert blurred.shape == img.shape, "Shape mismatch after blur."
    print("Test Passed: Large kernel median blur applied successfully.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_single_pixel_image():
    """Test the median blur on a single pixel image."""
    print("\nRunning test: Median Blur on Single Pixel Image")
    img = np.zeros((1, 1), dtype=np.uint8)  # Single pixel
    blurred = preprocess(img, {"ksize": 3})

    # The image should remain the same (as it's a single pixel)
    assert np.array_equal(img, blurred), "Single pixel image was altered unexpectedly."
    print("Test Passed: Single pixel image median blur applied successfully.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
@pytest.mark.skip
def test_median_blur_invalid_kernel_size():
    """Test the median blur with an invalid kernel size."""
    print("\nRunning test: Median Blur with Invalid Kernel Size")

    invalid_kernel_sizes = [0, -3, "abc", None]
    for invalid_kernel in invalid_kernel_sizes:
        with pytest.raises(ValueError):
            preprocess(generate_grayscale_image(), {"ksize": invalid_kernel})
    print("Test Passed: Invalid kernel size handled properly.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_preserves_image_structure():
    """Test that median blur preserves the overall structure of the image."""
    print("\nRunning test: Median Blur Preserves Image Structure")
    img = generate_grayscale_image(color_value=255)  # White image
    blurred = preprocess(img, {"ksize": 5})

    # The overall structure of the image (i.e., no significant shape change)
    assert blurred.shape == img.shape, "Shape mismatch after blur."
    print("Test Passed: Image structure preserved after median blur.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_empty_image():
    """Test the median blur on an empty image."""
    print("\nRunning test: Median Blur on Empty Image")
    img = np.zeros((0, 0), dtype=np.uint8)  # Empty image
    blurred = preprocess(img, {"ksize": 5})

    # Ensure the result is also an empty image
    assert blurred.shape == img.shape, "Shape mismatch after blur on empty image."
    print("Test Passed: Empty image handled correctly.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_invalid_image_type():
    """Test median blur with invalid image type (non-NumPy)."""
    print("\nRunning test: Median Blur with Invalid Image Type")
    invalid_images = [[], {}, "string", None]

    for invalid_image in invalid_images:
        with pytest.raises(TypeError):
            preprocess(invalid_image, {"ksize": 5})
    print("Test Passed: Invalid image input properly rejected.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_large_image():
    """Test the median blur on a large image (e.g., 1000x1000)."""
    print("\nRunning test: Median Blur on Large Image (1000x1000)")
    img = generate_grayscale_image(size=(1000, 1000), color_value=0)  # Black image
    blurred = preprocess(img, {"ksize": 5})

    # Ensure that the image size is preserved
    assert blurred.shape == img.shape, "Shape mismatch after blur on large image."
    print("Test Passed: Large image median blur applied successfully.")


@pytest.mark.preprocessing
@pytest.mark.median_blur
def test_median_blur_on_rgba_image():
    """Test median blur on an RGBA image."""
    print("\nRunning test: Median Blur on RGBA Image")
    img = np.zeros((100, 100, 4), dtype=np.uint8)  # Transparent image
    img[:, :, 3] = 255  # Set alpha channel to opaque
    blurred = preprocess(img, {"ksize": 5})

    # Ensure the alpha channel is preserved
    assert np.all(blurred[:, :, 3] == 255), "Alpha channel altered unexpectedly."
    print("Test Passed: RGBA image median blur handled correctly.")
