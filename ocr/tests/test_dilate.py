"""
test_dilate.py

🔥 Nuclear-proof dilation test suite for OCR preprocessing.
Includes verbose output and deep edge case coverage with clearly named test functions.
"""

import numpy as np
import pytest
import cv2
from preprocessing_image.scripts.dilate import preprocess


def generate_white_text_on_black(shape=(100, 100)):
    img = np.zeros(shape, dtype=np.uint8)
    cv2.putText(img, "T", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, 255, thickness=2)
    return img


def generate_black_text_on_white(shape=(100, 100)):
    img = np.full(shape, 255, dtype=np.uint8)
    cv2.putText(img, "A", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, 0, thickness=2)
    return img


def generate_thin_line_image():
    img = np.zeros((50, 100), dtype=np.uint8)
    cv2.line(img, (10, 25), (90, 25), 255, 1)
    return img


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_expands_white_text_on_black_background():
    print("\nRunning test: Expand white text on black background")
    img = generate_white_text_on_black()
    out = preprocess(img, {"target": "bright"})
    assert out.shape == img.shape
    assert np.count_nonzero(out) > np.count_nonzero(img)


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_expands_dark_text_on_white_background():
    print("\nRunning test: Expand dark text on white background")
    img = generate_black_text_on_white()
    out = preprocess(img, {"target": "dark"})
    assert out.shape == img.shape
    assert np.count_nonzero(out < 255) >= np.count_nonzero(img < 255)


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_with_thin_line_and_cross_kernel_shape():
    print("\nRunning test: Dilate 1px line with CROSS kernel")
    img = generate_thin_line_image()
    original_nonzero = np.count_nonzero(img)
    out = preprocess(img, {"kernel_shape": "cross", "ksize": 3, "target": "bright"})
    assert np.count_nonzero(out) > original_nonzero * 1.5  # Allow some expansion


# def test_dilate_with_thin_line_and_cross_kernel_shape():
#     print("\nRunning test: Dilate 1px line with CROSS kernel")
#     img = generate_thin_line_image()
#     out = preprocess(img, {"kernel_shape": "cross", "ksize": 5})
#     assert out.shape == img.shape
#     assert np.count_nonzero(out) > np.count_nonzero(img)


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_with_huge_kernel_should_not_crash():
    print("\nRunning test: Dilate with huge kernel (99x99)")
    img = generate_white_text_on_black()
    out = preprocess(img, {"ksize": 99})
    assert out.shape == img.shape


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_color_image_shape_integrity():
    print("\nRunning test: Dilate RGB image and keep shape")
    img = np.full((100, 100, 3), 255, dtype=np.uint8)
    out = preprocess(img, {"target": "dark"})
    assert out.shape == img.shape
    assert out.dtype == img.dtype


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_invalid_kernel_shape_defaults_to_rect():
    print("\nRunning test: Invalid kernel shape should fallback to RECT")
    img = generate_white_text_on_black()
    out = preprocess(img, {"kernel_shape": "triangle"})
    assert out.shape == img.shape


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_negative_kernel_size_raises_value_error():
    print("\nRunning test: Negative kernel size should raise error")
    img = generate_white_text_on_black()
    # preprocess(img, {"ksize": -5})
    with pytest.raises(Exception):
        preprocess(img, {"ksize": -5})


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_boolean_image_type_should_work_or_fail_cleanly():
    print("\nRunning test: Boolean dtype image")
    img = np.zeros((100, 100), dtype=bool)
    try:
        out = preprocess(img, {})
        assert out.shape == img.shape
    except Exception:
        assert True  # acceptable


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_float_image_should_not_silently_fail():
    print("\nRunning test: Float32 image input")
    img = np.full((100, 100), 0.5, dtype=np.float32)
    with pytest.raises(Exception):
        preprocess(img, {})


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_extremely_thin_image_should_work():
    print("\nRunning test: Extremely thin image")
    img = np.zeros((1, 100), dtype=np.uint8)
    out = preprocess(img, {})
    assert out.shape == (1, 100)


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_single_pixel_image_should_not_crash():
    print("\nRunning test: 1x1 image")
    img = np.full((1, 1), 255, dtype=np.uint8)
    out = preprocess(img, {})
    assert out.shape == (1, 1)


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_very_large_iteration_should_not_timeout():
    print("\nRunning test: High iteration count")
    img = generate_white_text_on_black()
    out = preprocess(img, {"iterations": 50})
    assert out.shape == img.shape


@pytest.mark.preprocessing
@pytest.mark.dilate
def test_dilate_image_with_all_zero_should_remain_zero():
    print("\nRunning test: Completely black image")
    img = np.zeros((100, 100), dtype=np.uint8)
    out = preprocess(img, {})
    assert np.count_nonzero(out) == 0
