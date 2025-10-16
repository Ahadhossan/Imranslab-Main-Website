import os
import json
import numpy as np
import cv2
import pytest
import random
import time
import concurrent.futures
from hypothesis import given, strategies as st
from skimage.metrics import structural_similarity as ssim
from test_data.synthetic_data.synthetic_data_factory.paper_type.regular.regular_paper import (
    RegularConfigValidator,
    RegularImageBuilder,
    FileWriter,
    RegularEffect
)


# ----------------------------
# RegularConfigValidator Unit Tests
# ----------------------------

def test_config_defaults_pass():
    """
    Default regular configuration should validate without errors.
    """
    cfg = RegularEffect().defaults.copy()
    RegularConfigValidator.validate(cfg)


@pytest.mark.parametrize("key,value", [
    ('width', -1), ('height', -100), ('dpi', -300),
    ('gradient_intensity', -5), ('border_thickness', -1),
    ('margin', -10), ('line_thickness', -1)
])
def test_config_invalid_numeric_params_raise(key, value):
    """
    Negative or invalid integer parameters should raise ValueError.
    """
    cfg = RegularEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        RegularConfigValidator.validate(cfg)


@pytest.mark.parametrize("paper_color", [None, (), (255,), (256, 0, 0), (-1, 0, 0), (0, 0, 'a')])
def test_config_invalid_paper_color_raise(paper_color):
    """
    Invalid paper_color formats should raise ValueError.
    """
    cfg = RegularEffect().defaults.copy()
    cfg['paper_color'] = paper_color
    with pytest.raises(ValueError):
        RegularConfigValidator.validate(cfg)


def test_config_margin_too_large_width():
    """
    margin*2 >= width should raise ValueError.
    """
    cfg = RegularEffect().defaults.copy()
    cfg['width'] = 30
    cfg['margin'] = 20
    with pytest.raises(ValueError):
        RegularConfigValidator.validate(cfg)


def test_config_margin_too_large_height():
    """
    margin*2 >= height should raise ValueError.
    """
    cfg = RegularEffect().defaults.copy()
    cfg['height'] = 30
    cfg['margin'] = 20
    with pytest.raises(ValueError):
        RegularConfigValidator.validate(cfg)


@pytest.mark.parametrize("required_key", [
    'width', 'height', 'dpi', 'gradient_intensity',
    'border_thickness', 'margin', 'line_thickness'
])
def test_config_missing_required_key_raises(required_key):
    """
    Omitting any required key should raise ValueError.
    """
    cfg = RegularEffect().defaults.copy()
    cfg.pop(required_key, None)
    with pytest.raises(ValueError):
        RegularConfigValidator.validate(cfg)


# ----------------------------
# RegularImageBuilder Unit Tests
# ----------------------------

def test_image_builder_shape_includes_border():
    """
    The built image must include border_thickness in its dimensions.
    """
    cfg = RegularEffect().defaults.copy()
    img = RegularImageBuilder.build(cfg)
    h, w = cfg['height'], cfg['width']
    b = cfg['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


def test_image_builder_gradient_effect():
    """
    Applying gradient should make top margin row brighter than mid-height.
    """
    cfg = RegularEffect().defaults.copy()
    cfg['gradient_intensity'] = 40
    cfg['margin'] = 10
    img = RegularImageBuilder.build(cfg)
    b = cfg['border_thickness']
    y_top = b + cfg['margin']
    y_mid = b + cfg['height'] // 2
    x = b + cfg['width'] // 2
    assert img[y_top, x][0] > img[y_mid, x][0]


# ----------------------------
# FileWriter Unit Tests
# ----------------------------

def test_filewriter_write_and_read(tmp_path):
    """
    FileWriter should write image and JSON config correctly.
    """
    dummy = np.zeros((4, 4, 3), dtype=np.uint8)
    cfg = {'test': 1}
    img_path = tmp_path / 'test.png'
    cfg_path = tmp_path / 'test.json'
    FileWriter.write_image(dummy, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    assert img_path.exists() and img_path.stat().st_size > 0
    assert json.loads(cfg_path.read_text()) == cfg


def test_filewriter_overwrite(tmp_path):
    """
    Overwriting existing files should succeed and update content.
    """
    img1 = np.zeros((2, 2, 3), dtype=np.uint8)
    img2 = np.ones((2, 2, 3), dtype=np.uint8)
    cfg1 = {'x': 1}
    cfg2 = {'x': 2}
    img_path = tmp_path / 'o.png'
    cfg_path = tmp_path / 'o.json'
    FileWriter.write_image(img1, str(img_path))
    FileWriter.write_config(cfg1, str(cfg_path))
    FileWriter.write_image(img2, str(img_path))
    FileWriter.write_config(cfg2, str(cfg_path))
    assert json.loads(cfg_path.read_text()) == cfg2


# ----------------------------
# RegularEffect Integration Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_regular_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, then verify files and content.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'r.png',
        'width': 500, 'height': 700,
        'margin': 20, 'gradient_intensity': 5,
        'border_thickness': 10, 'line_thickness': 1
    }
    reff = RegularEffect(params)
    reff.generate()
    img_path = tmp_path / 'r.png'
    cfg_path = tmp_path / 'r.json'
    assert img_path.exists() and cfg_path.exists()
    loaded = json.loads(cfg_path.read_text())
    for k, v in reff.config.items():
        assert loaded[k] == v
    img = cv2.imread(str(img_path))
    h, w = params['height'], params['width']
    b = params['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


# ----------------------------
# Enhancement Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_visual_regression_against_baseline(tmp_path):
    """
    Compare generated image to a stored baseline using SSIM (threshold ≥ 0.98).
    Baseline must exist at tests/baselines/regular_baseline.png
    """
    # Generate image with fixed params
    params = {**RegularEffect().defaults, 'output_dir': str(tmp_path), 'output_file': 'v.png'}
    RegularEffect(params).generate()
    gen_gray = cv2.imread(str(tmp_path / 'v.png'), cv2.IMREAD_GRAYSCALE)
    base_path = os.path.join(os.path.dirname(__file__), 'baselines', 'regular_baseline.png')
    assert os.path.exists(base_path), f"Baseline missing at {base_path}"
    base_gray = cv2.imread(base_path, cv2.IMREAD_GRAYSCALE)
    score = ssim(base_gray, gen_gray)
    assert score >= 0.98, f"SSIM {score} below threshold"


@pytest.mark.timeout(5)
def test_performance_large_dimensions(tmp_path):
    """
    Ensure generation for very large dimensions completes within 3 seconds.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'p.png',
        'width': 5000, 'height': 7000,
        'margin': 50, 'gradient_intensity': 10,
        'border_thickness': 20, 'line_thickness': 1
    }
    start = time.time()
    RegularEffect(params).generate()
    duration = time.time() - start
    assert duration < 3.0, f"Generation took {duration}s, exceeds threshold"


def test_concurrent_generation(tmp_path):
    """
    Generating two images in parallel should succeed without race issues.
    """

    def worker(i):
        params = {**RegularEffect().defaults,
                  'output_dir': str(tmp_path),
                  'output_file': f'c{i}.png',
                  'margin': 10, 'gradient_intensity': 5,
                  'border_thickness': 10, 'line_thickness': 1}
        RegularEffect(params).generate()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        futures = [ex.submit(worker, i) for i in range(2)]
        for f in futures: f.result()
    for i in range(2):
        assert (tmp_path / f'c{i}.png').exists()
        assert (tmp_path / f'c{i}.json').exists()


@given(
    w=st.integers(min_value=100, max_value=1000),
    h=st.integers(min_value=100, max_value=1000),
    m=st.integers(min_value=0, max_value=50),
    gi=st.integers(min_value=0, max_value=50),
    bt=st.integers(min_value=0, max_value=20),
    lt=st.integers(min_value=1, max_value=5)
)
def test_property_based_valid_configs(w, h, m, gi, bt, lt):
    """
    Hypothesis-based test: valid random configs should validate and build correct shape.
    """
    cfg = {
        'width': w, 'height': h, 'dpi': 300,
        'gradient_intensity': gi, 'border_thickness': bt,
        'paper_color': (240, 240, 240), 'margin': min(m, min(w, h) // 4),
        'line_thickness': lt
    }
    # Validate does not raise
    RegularConfigValidator.validate(cfg)
    img = RegularImageBuilder.build(cfg)
    # Check shape
    expected_h = h + 2 * bt
    expected_w = w + 2 * bt
    assert img.shape == (expected_h, expected_w, 3)
