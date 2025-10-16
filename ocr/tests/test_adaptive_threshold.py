import numpy as np
import pytest
from preprocessing_image.scripts.adaptive_threshold import preprocess as adaptive_threshold_preprocess
from preprocessing_image.validation.adaptive_threshold_validation import validate as adaptive_threshold_validate

@pytest.mark.sanity
def test_adaptive_threshold_methods():
    """
    Test the different thresholding methods (mean/gaussian) and ensure output is binary.
    """
    methods = [("mean", 11, 2), ("gaussian", 11, 2), ("mean", 7, 1), ("gaussian", 9, 3)]
    for method, block_size, C in methods:
        img = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
        params = {"method": method, "block_size": block_size, "C": C}
        output = adaptive_threshold_preprocess(img, params)
        unique_vals = np.unique(output)
        # Check that the output is binary (0 or 255)
        assert set(unique_vals).issubset({0, 255})


@pytest.mark.sanity
def test_adaptive_threshold_grayscale_conversion():
    """
    Test if color images are converted to grayscale before thresholding.
    """
    color_img = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    params = {"method": "mean", "block_size": 11, "C": 2}
    output = adaptive_threshold_preprocess(color_img, params)
    # The output should be a 2D grayscale image
    assert output.ndim == 2

@pytest.mark.sanity
def test_adaptive_threshold_empty_image():
    """
    Test that an empty image raises an error during preprocessing.
    """
    img = np.zeros((0, 0), dtype=np.uint8)
    params = {"method": "mean", "block_size": 11, "C": 2}
    with pytest.raises(ValueError, match="Input image is empty."):
        adaptive_threshold_preprocess(img, params)

@pytest.mark.smoke
def test_adaptive_threshold_invalid_method():
    """
    Test that an invalid thresholding method raises an error.
    """
    img = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    params = {"method": "invalid", "block_size": 11, "C": 2}
    with pytest.raises(ValueError, match="Invalid thresholding method: invalid"):
        adaptive_threshold_preprocess(img, params)

@pytest.mark.sanity
def test_adaptive_threshold_validation_success():
    """
    Test that validation passes for a binary image with adaptive thresholding.
    """
    # Create a binary image (black and white only)
    binary_img = np.random.choice([0, 255], size=(100, 100), p=[0.5, 0.5]).astype(np.uint8)
    result = adaptive_threshold_validate(None, binary_img, {})

    # Validation should pass and status should be 'success'
    assert result["status"] == "success"
    # Black pixel percentage should be calculated
    assert "black_pixels_percent" in result["metrics"]

@pytest.mark.sanity
@pytest.mark.performance
def test_adaptive_threshold_validation_failure_non_binary_image():
    """
    Test that validation fails when the image is not binary.
    """
    # Create a non-binary image (contains values other than 0 or 255)
    non_binary_img = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    result = adaptive_threshold_validate(None, non_binary_img, {})

    # Validation should fail and status should be 'failure'
    assert result["status"] == "failure"
    assert "unique_values" in result["metrics"]

@pytest.mark.performance
@pytest.mark.sanity
def test_adaptive_threshold_validation_black_pixel_percentage():
    """
    Test that the black pixel percentage is correctly calculated.
    """
    # Create a binary image with a known number of black pixels
    binary_img = np.zeros((100, 100), dtype=np.uint8)
    binary_img[50:60, 50:60] = 255  # Add white pixels in a small section
    result = adaptive_threshold_validate(None, binary_img, {})

    # Validate the black pixel percentage
    assert result["status"] == "success"
    assert result["metrics"]["black_pixels_percent"] == 99.0  # 9900 black pixels, 100 total pixels


@pytest.mark.sanity
def test_adaptive_threshold_validation_invalid_image_type():
    """
    Test that validation raises an error when the output image is not of valid type.
    """
    invalid_img = None
    result = adaptive_threshold_validate(None, invalid_img, {})

    # Should fail due to invalid image type
    assert result["status"] == "failure"
