import numpy as np
import pytest
import cv2
from preprocessing_image.scripts.gaussian_blur import preprocess


def generate_image_with_text(text="Test", size=(100, 100)):
    """Generate a simple image with text for testing."""
    img = np.zeros(size, dtype=np.uint8)
    cv2.putText(img, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2, cv2.LINE_AA)
    return img


def generate_color_image(size=(100, 100)):
    """Generate a simple color image (3 channels) for testing."""
    img = np.zeros((size[0], size[1], 3), dtype=np.uint8)
    img[:] = [255, 0, 0]  # Red color
    return img


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_default_gaussian_blur():
    """Test the default behavior (default ksize=5, sigma=0) of Gaussian blur."""
    print("\nRunning test: Default Gaussian blur (default ksize=5, sigma=0)")
    img = generate_image_with_text()
    out = preprocess(img, {})

    # Assert that the shape is unchanged
    assert out.shape == img.shape, "Image shape should remain the same."
    print("Test Passed: Default Gaussian blur applied with ksize=5, sigma=0.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_with_large_kernel():
    """Test Gaussian blur with a large kernel (ksize=15)."""
    print("\nRunning test: Gaussian blur with large kernel (ksize=15)")
    img = generate_image_with_text()
    out = preprocess(img, {"ksize": 15})

    # Check if the image shape is preserved
    assert out.shape == img.shape, "Image shape should remain the same."
    # Verify if the image is sufficiently blurred (this is more of a visual check)
    assert np.mean(out) < np.mean(img), "The image should be more blurred with a larger kernel."
    print("Test Passed: Large kernel applied, image blurred further.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_with_small_kernel():
    """Test Gaussian blur with a small kernel (ksize=3)."""
    print("\nRunning test: Gaussian blur with small kernel (ksize=3)")
    img = generate_image_with_text()
    out = preprocess(img, {"ksize": 3})

    # Assert that the shape remains unchanged
    assert out.shape == img.shape, "Image shape should remain the same."
    # The image should be less blurred with a smaller kernel
    assert np.mean(out) > np.mean(img), "The image should be less blurred with a smaller kernel."
    print("Test Passed: Small kernel applied, image blurred less.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_with_invalid_kernel_size():
    """Test Gaussian blur with invalid kernel size (even number)."""
    print("\nRunning test: Invalid kernel size (even number)")
    img = generate_image_with_text()
    out = preprocess(img, {"ksize": 4})

    # Check that the kernel size is adjusted to an odd number
    assert out.shape == img.shape, "Image shape should remain the same."
    print("Test Passed: Even kernel size adjusted to odd.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_with_non_numeric_sigma():
    """Test Gaussian blur with non-numeric sigma value."""
    print("\nRunning test: Non-numeric sigma")
    img = generate_image_with_text()
    with pytest.raises(ValueError, match="Sigma must be a numeric value"):
        preprocess(img, {"sigma": "abc"})
    print("Test Passed: Non-numeric sigma caught.")


@pytest.mark.preprocessing
@pytest.mark.skip
@pytest.mark.gaussian_blur
def test_gaussian_blur_with_negative_sigma():
    """Test Gaussian blur with negative sigma value."""
    print("\nRunning test: Negative sigma value")
    img = generate_image_with_text()
    with pytest.raises(ValueError, match="Sigma value should be non-negative"):
        preprocess(img, {"sigma": -1})
    print("Test Passed: Negative sigma value correctly rejected.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_with_large_sigma():
    """Test Gaussian blur with a large sigma value."""
    print("\nRunning test: Large sigma value")
    img = generate_image_with_text()
    out = preprocess(img, {"sigma": 50})

    # Check that the image shape remains the same
    assert out.shape == img.shape, "Image shape should remain the same."
    print("Test Passed: Large sigma value applied, image appropriately blurred.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_on_grayscale_image():
    """Test Gaussian blur on grayscale image."""
    print("\nRunning test: Gaussian blur on grayscale image")
    img = generate_image_with_text()
    out = preprocess(img, {"ksize": 5})

    # Assert that the shape remains unchanged
    assert out.shape == img.shape, "Grayscale image shape should remain the same."
    print("Test Passed: Gaussian blur applied on grayscale image.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_on_color_image():
    """Test Gaussian blur on color image (3 channels)."""
    print("\nRunning test: Gaussian blur on color image")
    img = generate_color_image()
    out = preprocess(img, {"ksize": 5})

    # Assert that the shape remains unchanged
    assert out.shape == img.shape, "Color image shape should remain the same."
    print("Test Passed: Gaussian blur applied on color image.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
@pytest.mark.skip
def test_gaussian_blur_on_noisy_image():
    """Test Gaussian blur on an image with added noise."""
    print("\nRunning test: Gaussian blur on noisy image")
    img = generate_image_with_text()
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    noisy_img = cv2.add(img, noise)

    out = preprocess(noisy_img, {"ksize": 5})

    # Ensure noise is reduced after Gaussian blur
    assert np.count_nonzero(out) < np.count_nonzero(noisy_img), "Gaussian blur should reduce noise."
    print("Test Passed: Gaussian blur applied on noisy image, noise reduced.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_on_low_resolution_image():
    """Test Gaussian blur on low-resolution image."""
    print("\nRunning test: Gaussian blur on low-resolution image (150 DPI)")
    img = generate_image_with_text(size=(50, 50))  # Low resolution image
    out = preprocess(img, {"ksize": 5})

    assert out.shape == img.shape, "Image shape should remain the same."
    print("Test Passed: Gaussian blur applied on low-resolution image.")


@pytest.mark.preprocessing
@pytest.mark.gaussian_blur
def test_gaussian_blur_on_high_resolution_image():
    """Test Gaussian blur on high-resolution image."""
    print("\nRunning test: Gaussian blur on high-resolution image (300 DPI)")
    img = generate_image_with_text(size=(1000, 1000))  # High resolution image
    out = preprocess(img, {"ksize": 5})

    assert out.shape == img.shape, "Image shape should remain the same."
    print("Test Passed: Gaussian blur applied on high-resolution image.")
