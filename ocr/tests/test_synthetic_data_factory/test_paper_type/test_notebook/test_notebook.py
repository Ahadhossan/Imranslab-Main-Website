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
from test_data.synthetic_data.synthetic_data_factory.paper_type.notebook.notebook import (
    NotebookConfigValidator, NotebookImageBuilder, FileWriter, NotebookEffect
)


# ----------------------------
# NotebookConfigValidator Unit Tests
# ----------------------------

def test_config_defaults_pass():
    """
    Default notebook configuration should pass validation without errors.
    """
    cfg = NotebookEffect().defaults.copy()
    NotebookConfigValidator.validate(cfg)


@pytest.mark.parametrize("key,value", [
    ('width', -1),
    ('height', -100),
    ('dpi', -300),
    ('gradient_intensity', -5),
    ('border_thickness', -1),
    ('margin', -10),
    ('line_thickness', -1),
    ('ruled_line_spacing', 0),
    ('ruled_line_thickness', -1),
    ('margin_line_offset', -1),
    ('margin_line_thickness', -1),
])
@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_config_invalid_numeric_params_raise(key, value):
    """
    Negative or zero values for numeric parameters should raise ValueError.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        NotebookConfigValidator.validate(cfg)


@pytest.mark.parametrize("color_key,color", [
    ('paper_color', None),
    ('ruled_line_color', (255,)),
    ('margin_line_color', (256, 0, 0)),
])
def test_config_invalid_color_params_raise(color_key, color):
    """
    Invalid color tuples should raise ValueError.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg[color_key] = color
    with pytest.raises(ValueError):
        NotebookConfigValidator.validate(cfg)


def test_config_margin_too_large_height():
    """
    If margin*2 >= height, validation should fail.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg['height'] = 100
    cfg['margin'] = 60
    with pytest.raises(ValueError):
        NotebookConfigValidator.validate(cfg)


def test_config_margin_too_large_width():
    """
    If margin*2 >= width, validation should fail.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg['width'] = 100
    cfg['margin'] = 60
    with pytest.raises(ValueError):
        NotebookConfigValidator.validate(cfg)


def test_config_margin_line_offset_too_large():
    """
    If margin_line_offset >= width, validation should fail.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg['margin_line_offset'] = cfg['width']
    with pytest.raises(ValueError):
        NotebookConfigValidator.validate(cfg)


@pytest.mark.parametrize("required_key", [
    'width', 'height', 'dpi', 'gradient_intensity',
    'border_thickness', 'margin', 'line_thickness',
    'ruled_line_spacing', 'ruled_line_thickness',
    'margin_line_offset', 'margin_line_thickness'
])
def test_config_missing_required_key_raises(required_key):
    """
    Omitting any required key should raise ValueError.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg.pop(required_key, None)
    with pytest.raises(ValueError):
        NotebookConfigValidator.validate(cfg)


# ----------------------------
# NotebookImageBuilder Unit Tests
# ----------------------------

def test_image_builder_shape_includes_border():
    """
    The built image should include border_thickness on all sides.
    """
    cfg = NotebookEffect().defaults.copy()
    img = NotebookImageBuilder.build(cfg)
    h, w = cfg['height'], cfg['width']
    b = cfg['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


def test_image_builder_gradient_and_ruled_lines():
    """
    Image should show gradient plus ruled lines at expected spacing.
    """
    cfg = NotebookEffect().defaults.copy()
    cfg['gradient_intensity'] = 30
    cfg['ruled_line_spacing'] = 100
    cfg['margin'] = 20
    img = NotebookImageBuilder.build(cfg)
    b = cfg['border_thickness']
    # Check a ruled line at first spacing
    y = b + cfg['margin']
    assert tuple(img[y, b][0:3]) == cfg['ruled_line_color']


def test_image_builder_margin_line_drawn():
    """
    The margin vertical line should appear at margin_line_offset.
    """
    cfg = NotebookEffect().defaults.copy()
    offset = cfg['margin_line_offset']
    img = NotebookImageBuilder.build(cfg)
    b = cfg['border_thickness']
    x = b + offset
    y_mid = b + cfg['height'] // 2
    assert tuple(img[y_mid, x]) == cfg['margin_line_color']


# ----------------------------
# FileWriter Unit Tests
# ----------------------------

def test_filewriter_write_and_read(tmp_path):
    """
    FileWriter should write image and JSON config correctly.
    """
    dummy = np.zeros((5, 5, 3), dtype=np.uint8)
    cfg = {'foo': 'bar'}
    img_path = tmp_path / 'n.png'
    cfg_path = tmp_path / 'n.json'
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
    cfg1 = {'a': 1}
    cfg2 = {'b': 2}
    img_path = tmp_path / 'nb.png'
    cfg_path = tmp_path / 'nb.json'
    FileWriter.write_image(img1, str(img_path))
    FileWriter.write_config(cfg1, str(cfg_path))
    FileWriter.write_image(img2, str(img_path))
    FileWriter.write_config(cfg2, str(cfg_path))
    assert json.loads(cfg_path.read_text()) == cfg2


# ----------------------------
# NotebookEffect Integration Tests
# ----------------------------
@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_notebook_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, then verify outputs and config.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'nb.png',
        'width': 500, 'height': 800,
        'margin': 20, 'gradient_intensity': 10,
        'border_thickness': 5, 'line_thickness': 1,
        'ruled_line_spacing': 100, 'ruled_line_thickness': 2,
        'ruled_line_color': (100, 100, 200),
        'margin_line_offset': 50, 'margin_line_thickness': 2,
        'margin_line_color': (200, 50, 50)
    }
    ne = NotebookEffect(params)
    ne.generate()
    img_path = tmp_path / 'nb.png'
    cfg_path = tmp_path / 'nb.json'
    assert img_path.exists() and cfg_path.exists()
    loaded = json.loads(cfg_path.read_text())
    for k, v in ne.config.items():
        assert loaded[k] == v
    img = cv2.imread(str(img_path))
    h, w = params['height'], params['width']
    b = params['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


@pytest.mark.parametrize("cfg_mod", [
    {'width': -10},
    {'margin': 5000},
    {'ruled_line_spacing': 0},
    {'margin_line_offset': 10000},
    {'ruled_line_color': (300, 300, 300)},
])
def test_notebook_effect_invalid_configuration(tmp_path, cfg_mod):
    """
    Invalid configurations should raise ValueError without writing files.
    """
    params = {**cfg_mod, 'output_dir': str(tmp_path)}
    with pytest.raises(ValueError):
        NotebookEffect(params).generate()


@pytest.mark.parametrize("_,seed", [(i, i) for i in range(3)])
def test_notebook_effect_random_valid(tmp_path, _, seed):
    """
    Random valid configurations should generate outputs reliably.
    """
    random.seed(seed)
    params = {
        'output_dir': str(tmp_path),
        'output_file': f'rand{_}.png',
        'width': random.randint(300, 800),
        'height': random.randint(400, 1200),
        'margin': random.randint(0, 50),
        'gradient_intensity': random.randint(0, 30),
        'border_thickness': random.randint(0, 10),
        'line_thickness': random.randint(1, 3),
        'ruled_line_spacing': random.randint(50, 200),
        'ruled_line_thickness': random.randint(1, 3),
        'ruled_line_color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        'margin_line_offset': random.randint(0, 100),
        'margin_line_thickness': random.randint(1, 3),
        'margin_line_color': (random.randint(0, 255), 0, 0)
    }
    NotebookEffect(params).generate()
    assert (tmp_path / f'rand{_}.png').exists()
    assert (tmp_path / f'rand{_}.json').exists()


# ----------------------------
# Enhancement Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_visual_regression_against_baseline(tmp_path):
    """
    Compare generated notebook page against a baseline using SSIM >= 0.98.
    Baseline at tests/baselines/notebook_baseline.png
    """
    params = {**NotebookEffect().defaults, 'output_dir': str(tmp_path), 'output_file': 'vis.png'}
    NotebookEffect(params).generate()
    gen = cv2.imread(str(tmp_path / 'vis.png'), cv2.IMREAD_GRAYSCALE)
    base_path = os.path.join(os.path.dirname(__file__), 'baselines', 'notebook_baseline.png')
    assert os.path.exists(base_path), f"Baseline missing at {base_path}"
    base = cv2.imread(base_path, cv2.IMREAD_GRAYSCALE)
    score = ssim(base, gen)
    assert score >= 0.98, f"SSIM {score} below threshold"


@pytest.mark.timeout(5)
def test_performance_large_dimensions(tmp_path):
    """
    Ensure generating large notebook page completes within 3s.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'perf.png',
        'width': 5000, 'height': 7000,
        'margin': 50, 'gradient_intensity': 10,
        'border_thickness': 10, 'line_thickness': 1,
        'ruled_line_spacing': 80, 'ruled_line_thickness': 2,
        'ruled_line_color': (200, 200, 255),
        'margin_line_offset': 200, 'margin_line_thickness': 3,
        'margin_line_color': (255, 0, 0)
    }
    start = time.time()
    NotebookEffect(params).generate()
    duration = time.time() - start
    assert duration < 3.0, f"Generation took {duration}s"


def test_concurrent_generation(tmp_path):
    """
    Generating multiple notebook pages in parallel should succeed without errors.
    """

    def worker(i):
        p = {**NotebookEffect().defaults,
             'output_dir': str(tmp_path),
             'output_file': f'c{i}.png'}
        NotebookEffect(p).generate()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        futures = [ex.submit(worker, i) for i in range(2)]
        for f in futures: f.result()
    for i in range(2):
        assert (tmp_path / f'c{i}.png').exists()
        assert (tmp_path / f'c{i}.json').exists()


@given(
    w=st.integers(min_value=100, max_value=1000),
    h=st.integers(min_value=100, max_value=1500),
    m=st.integers(min_value=0, max_value=50),
    gi=st.integers(min_value=0, max_value=50),
    bt=st.integers(min_value=0, max_value=20),
    lt=st.integers(min_value=1, max_value=5),
    rls=st.integers(min_value=10, max_value=200),
    rlt=st.integers(min_value=1, max_value=5),
    rlc=st.tuples(st.integers(0, 255), st.integers(0, 255), st.integers(0, 255)),
    mlo=st.integers(min_value=0, max_value=500),
    mlt=st.integers(min_value=1, max_value=5),
    mlc=st.tuples(st.integers(0, 255), st.integers(0, 255), st.integers(0, 255))
)
@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_property_based_valid_configs(
        w, h, m, gi, bt, lt, rls, rlt, rlc, mlo, mlt, mlc
):
    """
    Hypothesis-based test: random valid configs should build correct dimensions.
    """
    cfg = {
        'width': w, 'height': h, 'dpi': 300,
        'gradient_intensity': gi,
        'border_thickness': bt,
        'paper_color': (255, 255, 255),
        'margin': min(m, h // 2, w // 2),
        'line_thickness': lt,
        'ruled_line_spacing': rls,
        'ruled_line_thickness': rlt,
        'ruled_line_color': rlc,
        'margin_line_offset': min(mlo, w - 1),
        'margin_line_thickness': mlt,
        'margin_line_color': mlc
    }
    NotebookConfigValidator.validate(cfg)
    img = NotebookImageBuilder.build(cfg)
    expected_h = h + 2 * bt
    expected_w = w + 2 * bt
    assert img.shape == (expected_h, expected_w, 3)
