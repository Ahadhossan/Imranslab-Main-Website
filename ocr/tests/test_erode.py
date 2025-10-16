import numpy as np
import pytest
import cv2
from preprocessing_image.scripts.erode import preprocess

def generate_image_with_noise(shape=(100, 100)):
    img = np.full(shape, 255, dtype=np.uint8)
    coords = np.random.randint(0, min(shape), (50, 2))
    for x, y in coords:
        img[y, x] = 0  
    return img

def generate_text_image(shape=(100, 100)):
    img = np.full(shape, 255, dtype=np.uint8)
    cv2.putText(img, "Test", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, 0, thickness=2)
    return img

@pytest.mark.preprocessing
@pytest.mark.erode
def test_erode_removes_noise_from_image_with_small_random_dots():
    img = generate_image_with_noise()
    out = preprocess(img, {"ksize": 3})
    assert np.count_nonzero(out == 0) < np.count_nonzero(img == 0)

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_dilates_and_then_erosion_should_not_remove_text():
    img = generate_text_image()
    dilated = preprocess(img, {"ksize": 5, "iterations": 1, "target": "bright"})
    eroded = preprocess(dilated, {"ksize": 5, "iterations": 1, "target": "bright"})
    assert np.count_nonzero(np.abs(dilated - eroded)) < 10  # Allow for small differences

@pytest.mark.preprocessing
@pytest.mark.erode
def test_erode_shrinks_small_text():
    img = generate_text_image()
    out = preprocess(img, {"ksize": 3, "iterations": 1, "target": "bright"})
    assert np.count_nonzero(out) < np.count_nonzero(img)

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_shrinks_noise_in_low_res_image():
    img = generate_image_with_noise(shape=(50, 50))
    out = preprocess(img, {"ksize": 5, "iterations": 2})
    assert np.count_nonzero(out) < np.count_nonzero(img)

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_dilated_text_should_preserve_characters():
    img = generate_text_image()
    dilated = preprocess(img, {"ksize": 3, "iterations": 1, "target": "bright"})
    eroded = preprocess(dilated, {"ksize": 3, "iterations": 1, "target": "bright"})
    assert np.count_nonzero(np.abs(dilated - eroded)) < 10  # Allow for small differences

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_preserves_multi_column_layout():
    img = generate_image_with_noise()
    out = preprocess(img, {"ksize": 3, "iterations": 1, "target": "bright"})
    assert np.array_equal(out, img)

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_compressed_image_with_artifacts():
    img = generate_image_with_noise()
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)
    img_compressed = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    out = preprocess(img_compressed, {"ksize": 5, "iterations": 3})
    assert np.count_nonzero(out) < np.count_nonzero(img_compressed)

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_large_iterations_should_preserve_structure():
    img = generate_text_image()
    out = preprocess(img, {"ksize": 3, "iterations": 3})
    assert np.count_nonzero(np.abs(img - out)) < 10  # Allow for small differences

@pytest.mark.preprocessing
@pytest.mark.erode
@pytest.mark.skip
def test_erode_on_rgba_image_should_preserve_channels():
    img = np.full((100, 100, 4), 255, dtype=np.uint8)  
    out = preprocess(img, {"ksize": 3, "iterations": 1})
    assert out.shape == img.shape
    assert out.dtype == img.dtype
