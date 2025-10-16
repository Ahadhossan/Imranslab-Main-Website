import cv2
import numpy as np
import pytest
from preprocessing_image.scripts.resize import preprocess as resize_preprocess
from preprocessing_image.validation.resize_validation import validate as resize_validate

@pytest.mark.parametrize("input_size,target_size,expected_size", [
    ((100, 100), (200, 200), (200, 200)),       # Upscale both dimensions
    ((200, 200), (100, 100), (100, 100)),       # Downscale
    ((100, 200), (50, None), (25, 50)),         # Width-based scaling
    ((200, 100), (None, 50), (50, 25)),         # Height-based scaling
    ((100, 100), (100, 100), (100, 100)),       # Same size
    ((50, 50), (0, 0), (50, 50)),               # Zero dimensions (no resize)
])
@pytest.mark.sanity
def test_resize_operations(input_size, target_size, expected_size):
    img = np.random.randint(0, 255, size=(input_size[0], input_size[1], 3), dtype=np.uint8)
    params = {
        "target_width": target_size[0],
        "target_height": target_size[1],
        "upscale_only": False
    }
    output = resize_preprocess(img, params)
    assert output.shape[:2] == expected_size


@pytest.mark.sanity
def test_upscale_only():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    params = {"target_width": 150, "target_height": 150, "upscale_only": True}
    output = resize_preprocess(img, params)
    assert output.shape == (150, 150, 3)
    params = {"target_width": 50, "target_height": 50, "upscale_only": True}
    output = resize_preprocess(img, params)
    assert output.shape == (100, 100, 3)


@pytest.mark.sanity
def test_invalid_inputs():
    with pytest.raises(ValueError):
        resize_preprocess(None, {})
    with pytest.raises(ValueError):
        resize_preprocess(np.zeros((0, 0, 3), dtype=np.uint8), {})
    output = resize_preprocess(np.zeros((10, 10, 3), dtype=np.uint8), {"scale_factor": -1})
    assert np.array_equal(output, np.zeros((10, 10, 3), dtype=np.uint8))


@pytest.mark.sanity
def test_preserve_metadata():
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    params = {"target_width": 50, "target_height": None, "upscale_only": False}
    output = resize_preprocess(img, params)
    assert output.dtype == img.dtype
    assert output.shape[2] == img.shape[2]
