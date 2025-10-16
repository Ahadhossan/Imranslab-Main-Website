import numpy as np
import pytest
import cv2
import logging
from preprocessing_image.scripts.invert import preprocess


# Helper functions to generate test images
def generate_grayscale_image(size=(100, 100), color_value=255):
    """Generate a simple grayscale image with a given color value."""
    return np.full(size, color_value, dtype=np.uint8)


def generate_color_image(size=(100, 100), color_value=(255, 0, 0)):
    """Generate a simple color image (BGR) with the given color value."""
    img = np.zeros((size[0], size[1], 3), dtype=np.uint8)
    img[:] = color_value  # Apply the color value to all pixels
    return img


def generate_black_and_white_image(size=(100, 100)):
    """Generate an image that is completely black and white."""
    img = np.zeros(size, dtype=np.uint8)  # Black image
    cv2.rectangle(img, (10, 10), (90, 90), 255, -1)  # White square in the middle
    return img


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_grayscale():
    """Test the inversion of a grayscale image."""
    print("\nRunning test: Invert Grayscale Image")
    img = generate_grayscale_image(color_value=0)  # Black image
    inverted = preprocess(img, {})

    # The inverted image should be white (255) in all pixels
    assert np.all(inverted == 255), "Grayscale inversion failed."
    print("Test Passed: Grayscale image inverted successfully.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_color_image():
    """Test the inversion of a color (BGR) image."""
    print("\nRunning test: Invert Color Image (BGR)")
    img = generate_color_image(color_value=(0, 255, 0))  # Green image
    inverted = preprocess(img, {})

    # The inverted image should be red (255, 0, 0) in all pixels
    # assert np.all(inverted == (255, 0, 0)), "Color inversion failed."
    assert np.all(inverted == (255, 0, 255))  # Green (0,255,0) inverts to magenta (255,0,255)
    print("Test Passed: Color image inverted successfully.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_black_and_white_image():
    """Test inversion on an image that has both black and white regions."""
    print("\nRunning test: Invert Black and White Image")
    img = generate_black_and_white_image()
    inverted = preprocess(img, {})

    # Check if black regions are now white and white regions are black
    assert np.count_nonzero(inverted == 255) > 0, "Inversion did not change black to white."
    assert np.count_nonzero(inverted == 0) > 0, "Inversion did not change white to black."
    print("Test Passed: Black and white regions inverted successfully.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_empty_image():
    """Test inversion on an empty image (should handle gracefully)."""
    print("\nRunning test: Invert Empty Image")
    img = np.zeros((1, 1), dtype=np.uint8)  # Empty image
    inverted = preprocess(img, {})

    # The inverted image should still be the same size
    assert inverted.shape == img.shape, "Shape mismatch after inversion."
    # The pixel should now be white (255)
    assert inverted[0, 0] == 255, "Empty image inversion failed."
    print("Test Passed: Empty image inverted successfully.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_invalid_image_input():
    """Test that the function raises an error for invalid image input."""
    print("\nRunning test: Invert Invalid Image Input")

    invalid_inputs = [[], {}, "string", None, 1234]
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError):
            preprocess(invalid_input, {})
    print("Test Passed: Invalid inputs correctly handled.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_single_pixel_image():
    """Test inversion on a single pixel image."""
    print("\nRunning test: Invert Single Pixel Image")
    img = np.zeros((1, 1), dtype=np.uint8)  # Black pixel
    inverted = preprocess(img, {})

    # The single pixel should now be white (255)
    assert inverted[0, 0] == 255, "Single pixel inversion failed."
    print("Test Passed: Single pixel image inverted successfully.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_with_large_image():
    """Test inversion on a large image."""
    print("\nRunning test: Invert Large Image (1000x1000)")
    img = generate_grayscale_image(size=(1000, 1000), color_value=0)  # Black image
    inverted = preprocess(img, {})

    # The inverted image should be white (255) in all pixels
    assert np.all(inverted == 255), "Large image inversion failed."
    print("Test Passed: Large image inverted successfully.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_on_non_numpy_input():
    """Test inversion when a non-NumPy input (like a list) is passed."""
    print("\nRunning test: Invert on non-NumPy input")
    img = "This is a string, not an image."
    with pytest.raises(TypeError):
        preprocess(img, {})
    print("Test Passed: Non-NumPy input correctly rejected.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_transparency_image():
    """Test inversion on an image with transparency (RGBA)."""
    print("\nRunning test: Invert Image with Transparency (RGBA)")
    img = np.zeros((100, 100, 4), dtype=np.uint8)  # Transparent image
    img[:, :, 3] = 255  # Set alpha channel to 255 (opaque)
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)
    inverted = preprocess(img, {})

    # Ensure the alpha channel stays intact and only the RGB channels are inverted
    assert np.all(inverted[:, :, 3] == 255), "Alpha channel should remain intact."
    print("Test Passed: Inversion on RGBA image handled correctly.")


@pytest.mark.preprocessing
@pytest.mark.invert
def test_invert_on_noisy_image():
    """Test inversion on a noisy image."""
    print("\nRunning test: Invert on Noisy Image")
    img = generate_grayscale_image()
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    noisy_img = cv2.add(img, noise)

    inverted = preprocess(noisy_img, {})

    # Ensure the noise is inverted correctly (should still be noisy but with inverted values)
    assert np.count_nonzero(inverted != noisy_img) > 0, "Inversion did not affect noisy pixels."
    print("Test Passed: Inversion on noisy image handled correctly.")


@pytest.mark.preprocessing
@pytest.mark.invert
@pytest.mark.skip
def test_invert_with_empty_image_should_log():
    """Test inversion on an empty image and check if it logs the operation."""
    print("\nRunning test: Invert Empty Image and Log")
    img = np.zeros((1, 1), dtype=np.uint8)  # Empty image
    inverted = preprocess(img, {})

    # Check that logging occurred
    # log_output = open('log.txt', 'r').read()
    assert 'Inverted image colors' in log_output, "Inversion log message missing."
    print("Test Passed: Logging verified for empty image inversion.")
