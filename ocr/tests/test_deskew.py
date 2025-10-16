import cv2
import numpy as np
import pytest
from preprocessing_image.scripts.deskew import preprocess as deskew_preprocess
from preprocessing_image.validation.deskew_validation import validate as deskew_validate


@pytest.fixture
def skewed_image():
    img = np.full((200, 200, 3), 255, dtype=np.uint8)
    cv2.line(img, (20, 180), (180, 20), (0, 0, 0), 5)
    return img


@pytest.fixture
def straight_image():
    img = np.full((200, 200, 3), 255, dtype=np.uint8)
    cv2.line(img, (20, 100), (180, 100), (0, 0, 0), 5)
    return img


@pytest.mark.sanity
def test_deskew_positive_angle(skewed_image):
    params = {}
    output = deskew_preprocess(skewed_image, params)
    result = deskew_validate(skewed_image, output, params)
    assert result["status"] == "success"
    assert "detected_angle" in params, "Detected angle missing in params"
    detected = abs(params.get("detected_angle", 0))
    assert abs(detected - 45) < 2, f"Detected angle {detected}° should be ~45° within tolerance"
    assert output.shape == skewed_image.shape


@pytest.mark.sanity
def test_deskew_negative_angle():
    img = np.full((200, 200, 3), 255, dtype=np.uint8)
    cv2.line(img, (20, 20), (180, 180), (0, 0, 0), 5)
    params = {}
    output = deskew_preprocess(img, params)
    result = deskew_validate(img, output, params)
    assert result["status"] == "success"
    assert "detected_angle" in params, "Detected angle missing in params"
    detected = abs(params.get("detected_angle", 0))
    assert abs(detected - 45) < 2, f"Detected angle {detected}° should be ~45° within tolerance"
    assert output.shape == img.shape


@pytest.mark.sanity
def test_already_straight_image(straight_image):
    params = {}
    output = deskew_preprocess(straight_image, params)
    result = deskew_validate(straight_image, output, params)
    assert result["status"] == "success"
    assert "detected_angle" in params, "Detected angle missing in params"
    detected = abs(params.get("detected_angle", 0))
    assert detected < 5, f"Detected angle {detected}° should be near 0° for a straight image"


@pytest.mark.sanity
def test_empty_image():
    img = np.zeros((0, 0), dtype=np.uint8)
    params = {}
    with pytest.raises(Exception):
        deskew_preprocess(img, params)


@pytest.mark.sanity
def test_single_pixel_image():
    img = np.array([[128]], dtype=np.uint8)
    params = {}
    output = deskew_preprocess(img, params)
    assert output.shape == img.shape


@pytest.mark.sanity
def test_multi_orientation_text():
    img = np.full((300, 300, 3), 255, dtype=np.uint8)
    cv2.putText(img, "Horizontal", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 2)
    cv2.putText(img, "Vertical", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 0, 2, cv2.LINE_AA, True)
    params = {}
    output = deskew_preprocess(img, params)
    result = deskew_validate(img, output, params)
    assert result["status"] == "success"
    assert "detected_angle" in params, "Detected angle missing in params"
    detected = abs(params.get("detected_angle", 0))
    assert detected < 10, f"Detected angle {detected}° should be near 0° for mixed orientations"
    assert output.shape == img.shape
