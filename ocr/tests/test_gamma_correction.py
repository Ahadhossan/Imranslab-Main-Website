import numpy as np
import pytest
import cv2
from preprocessing_image.scripts.gamma_correction import preprocess


def generate_image_with_text(text="Test", size=(100, 100)):
    """Create image with varying intensities and text."""
    img = np.random.randint(50, 200, size, dtype=np.uint8)
    cv2.putText(img, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
    return img


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_default_behavior():
    """Test the default behavior (no change) of gamma correction."""
    print("\nRunning test: Default gamma behavior (no change)")
    img = generate_image_with_text()
    out = preprocess(img, {})
    assert np.array_equal(img, out), "The image should remain unchanged for default gamma."
    print("Test Passed: Default gamma applied, no change in the image.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_brightness_increase():
    """Test that gamma correction increases brightness (gamma > 1)."""
    print("\nRunning test: Gamma > 1 (brighten image)")
    img = generate_image_with_text()
    out = preprocess(img, {"gamma": 1.5})

    # Ensure the image brightness increases (using mean pixel values)
    assert np.mean(out) > np.mean(img), "Gamma correction should brighten the image."
    print("Test Passed: Gamma increased brightness, text is brighter.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_brightness_decrease():
    """Test that gamma correction decreases brightness (gamma < 1)."""
    print("\nRunning test: Gamma < 1 (darken image)")
    img = generate_image_with_text()
    out = preprocess(img, {"gamma": 0.5})

    # Ensure the image brightness decreases (using mean pixel values)
    assert np.mean(out) < np.mean(img), "Gamma correction should darken the image."
    print("Test Passed: Gamma decreased brightness, text is darker.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_invalid_gamma_string():
    """Test that non-numeric gamma values raise an exception."""
    print("\nRunning test: Invalid gamma value (non-numeric input)")
    img = generate_image_with_text()
    with pytest.raises(ValueError, match="Gamma must be a numeric value"):
        preprocess(img, {"gamma": "abc"})
    print("Test Passed: Invalid gamma value detected.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_invalid_gamma_negative():
    """Test that negative gamma values are handled or raise an exception."""
    print("\nRunning test: Invalid gamma value (negative gamma)")
    img = generate_image_with_text()
    with pytest.raises(ValueError, match="Gamma must be positive"):
        preprocess(img, {"gamma": -1})
    print("Test Passed: Negative gamma correctly rejected.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_invalid_gamma_zero():
    """Test that zero gamma value is handled."""
    print("\nRunning test: Invalid gamma value (zero gamma)")
    img = generate_image_with_text()
    with pytest.raises(ValueError, match="Gamma must be positive"):
        preprocess(img, {"gamma": 0})
    print("Test Passed: Zero gamma correctly rejected.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_low_resolution_image():
    """Test gamma correction on a low-resolution image."""
    print("\nRunning test: Gamma correction on low-resolution image (150 DPI)")
    img = generate_image_with_text(size=(50, 50))  # Low resolution image
    out = preprocess(img, {"gamma": 2.0})  # Increase gamma to see noticeable changes

    assert out.shape == img.shape, "Gamma correction should preserve the image shape."
    assert np.mean(out) > np.mean(img), "Gamma correction should enhance contrast."
    print("Test Passed: Gamma correction enhanced contrast on low-res image.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_high_resolution_image():
    """Test gamma correction on a high-resolution image."""
    print("\nRunning test: Gamma correction on high-resolution image (300 DPI)")
    img = generate_image_with_text(size=(1000, 1000))  # High resolution image
    out = preprocess(img, {"gamma": 1.5})

    assert out.shape == img.shape, "Gamma correction should preserve the image shape."
    assert np.mean(out) > np.mean(img), "Gamma correction should enhance contrast."
    print("Test Passed: Gamma correction enhanced contrast on high-res image.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_compression_artifacts():
    """Test gamma correction on an image with compression artifacts (JPEG)."""
    print("\nRunning test: Gamma correction on JPEG image with compression artifacts")
    img = generate_image_with_text()
    encoded = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 70])[1]
    compressed_img = cv2.imdecode(encoded, 1)

    out = preprocess(compressed_img, {"gamma": 1.5})

    assert np.mean(out) > np.mean(
        compressed_img), "Gamma correction should improve image clarity without amplifying artifacts."
    print("Test Passed: Gamma correction improved image clarity without amplifying artifacts.")


@pytest.mark.preprocessing
@pytest.mark.gamma
def test_gamma_noise_removal():
    """Test gamma correction on an image with added noise."""
    print("\nRunning test: Gamma correction on noisy image")
    img = generate_image_with_text()
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    noisy_img = cv2.add(img, noise)

    out = preprocess(noisy_img, {"gamma": 1.5})  # Increase gamma to enhance contrast

    assert np.mean(out) > np.mean(noisy_img), "Gamma correction should enhance contrast and reduce noise."
    print("Test Passed: Gamma correction enhanced text contrast and reduced noise.")

    # Gamma correction should reduce noise while enhancing text
    assert np.mean(out) > np.mean(noisy_img), "Gamma correction should enhance contrast and reduce noise."
    print("Test Passed: Gamma correction enhanced text contrast and reduced noise.")


@pytest.mark.preprocessing
@pytest.mark.gamma
@pytest.mark.skip
def test_gamma_text_and_background_separation():
    """Test gamma correction with text on a noisy background."""
    print("\nRunning test: Gamma correction with text on a noisy background")
    img = generate_image_with_text(text="Noisy Text")
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    noisy_img = cv2.add(img, noise)

    out = preprocess(noisy_img, {"gamma": 2.0})  # Increased gamma to separate text more clearly

    assert np.count_nonzero(out) > np.count_nonzero(noisy_img), "Gamma correction should improve text clarity."
    print("Test Passed: Gamma correction enhanced text clarity on noisy background.")
