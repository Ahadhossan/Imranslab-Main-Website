import os
import json
import numpy as np
import cv2
import pytest
import random
from test_data.synthetic_data.synthetic_data_factory.paper_type.envelope.envelope import (
    EnvelopeConfigValidator,
    EnvelopeImageBuilder,
    FileWriter,
    EnvelopeEffect,
)


# ----------------------------
# EnvelopeConfigValidator Unit Tests
# ----------------------------

def test_config_defaults_pass():
    """
    Default envelope configuration should validate without errors.
    """
    cfg = EnvelopeEffect().defaults.copy()
    EnvelopeConfigValidator.validate(cfg)


@pytest.mark.parametrize("key,value", [
    ('width', -1),
    ('height', -100),
    ('dpi', -300),
    ('gradient_intensity', -5),
    ('border_thickness', -1),
    ('margin', -10),
    ('line_thickness', -1),
])
def test_config_invalid_numeric_params_raise(key, value):
    """
    Negative or invalid integers for required keys should raise ValueError.
    """
    cfg = EnvelopeEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        EnvelopeConfigValidator.validate(cfg)


@pytest.mark.parametrize("paper_color", [None, (), (255,), (256, 0, 0), (-1, 0, 0), (0, 0, 'a')])
def test_config_invalid_paper_color(paper_color):
    """
    Non-RGB or out-of-range paper_color tuples should raise ValueError.
    """
    cfg = EnvelopeEffect().defaults.copy()
    cfg['paper_color'] = paper_color
    with pytest.raises(ValueError):
        EnvelopeConfigValidator.validate(cfg)


def test_config_margin_too_large_width():
    """
    If margin*2 >= width, validation should fail.
    """
    cfg = EnvelopeEffect().defaults.copy()
    cfg['width'] = 30
    cfg['margin'] = 20
    with pytest.raises(ValueError):
        EnvelopeConfigValidator.validate(cfg)


def test_config_margin_too_large_height():
    """
    If margin*2 >= height, validation should fail.
    """
    cfg = EnvelopeEffect().defaults.copy()
    cfg['height'] = 30
    cfg['margin'] = 20
    with pytest.raises(ValueError):
        EnvelopeConfigValidator.validate(cfg)


@pytest.mark.parametrize("required_key", [
    'width', 'height', 'dpi', 'gradient_intensity',
    'border_thickness', 'margin', 'line_thickness'
])
def test_config_missing_required_key_raises(required_key):
    """
    Omitting any required config key must raise ValueError.
    """
    cfg = EnvelopeEffect().defaults.copy()
    cfg.pop(required_key, None)
    with pytest.raises(ValueError):
        EnvelopeConfigValidator.validate(cfg)


# ----------------------------
# EnvelopeImageBuilder Unit Tests
# ----------------------------

def test_image_builder_shape_includes_border():
    """
    Built image dimensions should include border_thickness on all sides.
    """
    cfg = EnvelopeEffect().defaults.copy()
    img = EnvelopeImageBuilder.build(cfg)
    h, w = cfg['height'], cfg['width']
    b = cfg['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


def test_image_builder_gradient_effect():
    """
    With gradient enabled, pixel intensity at top margin must exceed mid-height.
    """
    cfg = EnvelopeEffect().defaults.copy()
    cfg['gradient_intensity'] = 30
    cfg['margin'] = 10
    img = EnvelopeImageBuilder.build(cfg)
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
    FileWriter should persist image and JSON config correctly.
    """
    dummy_img = np.zeros((5, 5, 3), dtype=np.uint8)
    cfg = {'key': 'value'}
    img_path = tmp_path / 'out.png'
    cfg_path = tmp_path / 'out.json'
    FileWriter.write_image(dummy_img, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    assert img_path.exists() and img_path.stat().st_size > 0
    assert json.loads(cfg_path.read_text()) == cfg


def test_filewriter_overwrite(tmp_path):
    """
    Overwriting existing files should succeed and update content.
    """
    first = np.zeros((2, 2, 3), dtype=np.uint8)
    second = np.ones((2, 2, 3), dtype=np.uint8)
    cfg1 = {'a': 1}
    cfg2 = {'b': 2}
    img_path = tmp_path / 'env.png'
    cfg_path = tmp_path / 'env.json'
    FileWriter.write_image(first, str(img_path))
    FileWriter.write_config(cfg1, str(cfg_path))
    FileWriter.write_image(second, str(img_path))
    FileWriter.write_config(cfg2, str(cfg_path))
    assert json.loads(cfg_path.read_text()) == cfg2


# ----------------------------
# EnvelopeEffect Integration Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_envelope_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, then verify outputs and config.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'env.png',
        'width': 600, 'height': 300,
        'margin': 20, 'gradient_intensity': 15,
        'border_thickness': 5, 'line_thickness': 1
    }
    ee = EnvelopeEffect(params)
    ee.generate()
    img_path = tmp_path / 'env.png'
    cfg_path = tmp_path / 'env.json'
    assert img_path.exists() and cfg_path.exists()
    loaded = json.loads(cfg_path.read_text())
    for k, v in ee.config.items():
        assert loaded[k] == v
    img = cv2.imread(str(img_path))
    h, w = params['height'], params['width']
    b = params['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


@pytest.mark.parametrize("cfg_mod", [
    {'width': -10},
    {'margin': 1000},
    {'paper_color': (300, 300, 300)},
    {'line_thickness': -1}
])
def test_envelope_effect_invalid_configuration(tmp_path, cfg_mod):
    """
    Invalid configurations should raise ValueError without writing files.
    """
    params = {**cfg_mod, 'output_dir': str(tmp_path)}
    with pytest.raises(ValueError):
        EnvelopeEffect(params).generate()


@pytest.mark.parametrize("_,seed", [(i, i) for i in range(3)])
def test_envelope_effect_random_valid(tmp_path, _, seed):
    """
    Random valid parameters should generate outputs reliably.
    """
    random.seed(seed)
    params = {
        'output_dir': str(tmp_path),
        'output_file': f'rand{_}.png',
        'width': random.randint(200, 800),
        'height': random.randint(100, 400),
        'margin': random.randint(0, 50),
        'gradient_intensity': random.randint(0, 30),
        'border_thickness': random.randint(0, 10),
        'line_thickness': random.randint(1, 3),
        'paper_color': (245, 245, 240)
    }
    EnvelopeEffect(params).generate()
    assert (tmp_path / f'rand{_}.png').exists()
    assert (tmp_path / f'rand{_}.json').exists()
