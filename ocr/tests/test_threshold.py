# tests/test_threshold.py (fixed color handling test)
import numpy as np
import pytest
from preprocessing_image.scripts.threshold import preprocess as threshold_preprocess
from preprocessing_image.validation.threshold_validation import validate as threshold_validate


@pytest.mark.sanity
def test_threshold_methods():
    methods = [("otsu", 0), ("fixed", 127), ("fixed", 200), ("fixed", 50)]
    for method, th_val in methods:
        img = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
        params = {"method": method, "threshold_value": th_val}
        output = threshold_preprocess(img, params)
        result = threshold_validate(img, output, params)
        assert result["status"] == "success"
        assert set(np.unique(output)).issubset({0, 255})


@pytest.mark.sanity
def test_all_white_image():
    img = np.full((100, 100), 255, dtype=np.uint8)
    params = {"method": "otsu", "threshold_value": 0}
    output = threshold_preprocess(img, params)
    assert np.all(output == 255)


@pytest.mark.sanity
def test_all_black_image():
    img = np.zeros((100, 100), dtype=np.uint8)
    params = {"method": "otsu", "threshold_value": 0}
    output = threshold_preprocess(img, params)
    assert np.all(output == 0)


@pytest.mark.sanity
def test_already_binary():
    base = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
    binary_img = ((base > 127) * 255).astype(np.uint8)
    params = {"method": "otsu", "threshold_value": 0}
    output = threshold_preprocess(binary_img, params)
    assert np.array_equal(binary_img, output)


@pytest.mark.sanity
def test_invalid_threshold_values():
    with pytest.raises(ValueError):
        threshold_preprocess(np.zeros((10,10), dtype=np.uint8), {"method": "fixed", "threshold_value": 300})
    with pytest.raises(ValueError):
        threshold_preprocess(np.zeros((10,10), dtype=np.uint8), {"method": "fixed", "threshold_value": -5})


@pytest.mark.sanity
def test_color_image_handling():
    color_img = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
    params = {"method": "otsu", "threshold_value": 0}
    output = threshold_preprocess(color_img, params)
    assert output.ndim == 2  # Should convert to grayscale first


@pytest.mark.sanity
def test_low_contrast_image():
    img = np.full((100, 100), 128, dtype=np.uint8)
    img[40:60, 40:60] = 130
    params = {"method": "otsu", "threshold_value": 0}
    output = threshold_preprocess(img, params)
    unique_vals = np.unique(output)
    assert set(unique_vals).issubset({0, 255})


@pytest.mark.sanity
def test_noise_handling_in_threshold():
    img = np.full((100, 100), 128, dtype=np.uint8)
    noise = (np.random.normal(0, 10, (100, 100))).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    params = {"method": "otsu", "threshold_value": 0}
    output = threshold_preprocess(noisy_img, params)
    assert set(np.unique(output)).issubset({0, 255})