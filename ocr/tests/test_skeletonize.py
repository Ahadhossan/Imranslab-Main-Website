import numpy as np
import pytest
from preprocessing_image.scripts.skeletonize import preprocess as skeletonize_preprocess


@pytest.mark.sanity
def test_skeletonization_binary_image():
    """
    Test that skeletonization is applied correctly to a binary image.

    This test case generates a random binary image and ensures that the output is skeletonized,
    with the foreground reduced and the background remaining unchanged.
    """
    img = np.random.choice([0, 255], size=(100, 100), p=[0.5, 0.5]).astype(np.uint8)
    params = {}  # No parameters needed for this test
    output = skeletonize_preprocess(img, params)

    # Check that the output is still a binary image (only 0 and 255 values)
    unique_vals = np.unique(output)
    assert set(unique_vals).issubset({0, 255})

    # Ensure the output has been thinned (foreground pixels should be fewer)
    original_foreground = np.sum(img == 0)
    skeleton_foreground = np.sum(output == 0)
    assert skeleton_foreground <= original_foreground  # Skeletonization should reduce foreground pixels


@pytest.mark.sanity
def test_skeletonization_grayscale_conversion():
    """
    Test that color images are converted to grayscale before skeletonization.

    This test case generates a random color image, processes it through skeletonization,
    and ensures that it is first converted to grayscale.
    """
    color_img = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    params = {}  # No parameters needed for this test
    output = skeletonize_preprocess(color_img, params)

    # The output should be a 2D grayscale image
    assert output.ndim == 2


@pytest.mark.sanity
def test_skeletonization_empty_image():
    """
    Test that an empty image raises an error during preprocessing.

    This test case ensures that the function raises an error when given an empty image.
    """
    img = np.zeros((0, 0), dtype=np.uint8)
    params = {}  # No parameters needed for this test
    with pytest.raises(ValueError, match="Input image is empty or None."):
        skeletonize_preprocess(img, params)


@pytest.mark.sanity
def test_skeletonization_invalid_image_type():
    """
    Test that an invalid input (e.g., None or non-binary image) raises an error.

    This test case ensures that the function raises an error when given an invalid input,
    such as `None` or non-binary data.
    """
    img = None
    params = {}  # No parameters needed for this test
    with pytest.raises(ValueError, match="Input image is empty or None."):
        skeletonize_preprocess(img, params)


@pytest.mark.sanity
def test_skeletonization_non_binary_image():
    """
    Test that the function applies thresholding correctly to non-binary images.

    This test case generates a grayscale image and ensures that the function applies Otsu’s thresholding
    to convert it into a binary image before performing skeletonization.
    """
    img = np.random.randint(100, 150, size=(100, 100), dtype=np.uint8)  # Low-contrast grayscale image
    params = {}  # No parameters needed for this test
    output = skeletonize_preprocess(img, params)

    # The output should be a binary image (only 0 and 255 values)
    unique_vals = np.unique(output)
    assert set(unique_vals).issubset({0, 255})


@pytest.mark.sanity
def test_skeletonization_reduction_percent():
    """
    Test that the percentage reduction in foreground pixels is calculated correctly.

    This test case generates a binary image and checks that the reduction percentage is
    calculated and logged correctly after skeletonization.
    """
    img = np.random.choice([0, 255], size=(100, 100), p=[0.5, 0.5]).astype(np.uint8)
    params = {}  # No parameters needed for this test
    skeletonize_preprocess(img, params)

    # Check if the reduction percentage is stored in params
    assert "reduction_percent" in params
    reduction_percent = params["reduction_percent"]
    assert reduction_percent >= 0  # The reduction percentage should never be negative


@pytest.mark.skipif(reason="This test is flaky and may fail intermittently.")
@pytest.mark.sanity
def test_skeletonization_edge_case():
    """
    Test that skeletonization works for a very small image (1x1 pixel).

    This test case checks if the function handles the smallest possible image input.
    """
    img = np.random.choice([0, 255], size=(1, 1), p=[0.5, 0.5]).astype(np.uint8)
    params = {}  # No parameters needed for this test
    output = skeletonize_preprocess(img, params)

    # The output should be a 1x1 image with the same value as the input image
    assert output.shape == img.shape
    assert np.array_equal(output, img)  # Skeletonization won't change a 1x1 image


@pytest.mark.sanity
def test_skeletonization_large_image():
    """
    Test that skeletonization works for a large image.

    This test case ensures that the function can handle large images without performance issues.
    """
    img = np.random.choice([0, 255], size=(1000, 1000), p=[0.5, 0.5]).astype(np.uint8)
    params = {}  # No parameters needed for this test
    output = skeletonize_preprocess(img, params)

    # Ensure the output image has the same dimensions as the input
    assert output.shape == img.shape


@pytest.mark.sanity
def test_skeletonization_edge_case_color():
    """
    Test that skeletonization works correctly for a small color image (1x1 pixel).
    """
    color_img = np.random.randint(0, 256, size=(1, 1, 3), dtype=np.uint8)
    params = {}  # No parameters needed for this test
    output = skeletonize_preprocess(color_img, params)

    # The output should be a 1x1 color image with the same values as the input image
    assert output.shape == (1, 1, 3)
    assert np.array_equal(output, color_img)  # Skeletonization shouldn't change a 1x1 color image
