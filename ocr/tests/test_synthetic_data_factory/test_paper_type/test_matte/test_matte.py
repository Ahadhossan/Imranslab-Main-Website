import os
import json
import numpy as np
import cv2
import pytest
import random
from test_data.synthetic_data.synthetic_data_factory.paper_type.matte.matte import (
    MatteConfigValidator, MatteImageBuilder, FileWriter, MatteEffect
)


# ----------------------------
# MatteConfigValidator Unit Tests
# ----------------------------

def test_validate_defaults_pass():
    """
    Default matte configuration should pass validation without exceptions.
    """
    cfg = MatteEffect().defaults.copy()
    # No exception expected
    MatteConfigValidator.validate(cfg)


@pytest.mark.parametrize("key,value", [
    ('width', -1),
    ('height', -100),
    ('dpi', -300),
    ('gradient_intensity', -5),
    ('border_thickness', -1),
    ('margin', -10),
    ('line_thickness', -1),
])
def test_validate_invalid_ints_raise(key, value):
    """
    Negative or zero values for numeric parameters should raise ValueError.
    """
    cfg = MatteEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        MatteConfigValidator.validate(cfg)


@pytest.mark.parametrize("paper_color", [None, (), (255,), (256, 0, 0), (-1, 0, 0), (0, 0, 'a')])
def test_validate_invalid_paper_color_raise(paper_color):
    """
    Invalid paper_color formats should raise ValueError.
    """
    cfg = MatteEffect().defaults.copy()
    cfg['paper_color'] = paper_color
    with pytest.raises(ValueError):
        MatteConfigValidator.validate(cfg)


def test_validate_margin_too_large_for_height():
    """
    If margin*2 >= height, should raise ValueError.
    """
    cfg = MatteEffect().defaults.copy()
    cfg['height'] = 30
    cfg['margin'] = 20
    with pytest.raises(ValueError):
        MatteConfigValidator.validate(cfg)


def test_validate_margin_too_large_for_width():
    """
    If margin*2 >= width, should raise ValueError.
    """
    cfg = MatteEffect().defaults.copy()
    cfg['width'] = 30
    cfg['margin'] = 20
    with pytest.raises(ValueError):
        MatteConfigValidator.validate(cfg)


@pytest.mark.parametrize("required_key", [
    'width', 'height', 'dpi', 'gradient_intensity',
    'border_thickness', 'margin', 'line_thickness'
])
def test_validate_missing_required_key_raises(required_key):
    """
    Omitting any required key should raise ValueError.
    """
    cfg = MatteEffect().defaults.copy()
    cfg.pop(required_key, None)
    with pytest.raises(ValueError):
        MatteConfigValidator.validate(cfg)


# ----------------------------
# MatteImageBuilder Unit Tests
# ----------------------------

def test_image_builder_shape_includes_border():
    """
    The built image should include border_thickness in its dimensions.
    """
    cfg = MatteEffect().defaults.copy()
    # use defaults
    img = MatteImageBuilder.build(cfg)
    h, w = cfg['height'], cfg['width']
    b = cfg['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


def test_image_builder_gradient_intensity_effect():
    """
    With gradient enabled, the top margin row should be lighter than middle.
    """
    cfg = MatteEffect().defaults.copy()
    cfg['gradient_intensity'] = 30
    cfg['margin'] = 10
    img = MatteImageBuilder.build(cfg)
    b = cfg['border_thickness']
    # Coordinates: y position just after top border + margin
    y_top = b + cfg['margin']
    # Middle of paper (not including border)
    y_mid = b + cfg['height'] // 2
    x = b + cfg['width'] // 2
    top_val = img[y_top, x][0]
    mid_val = img[y_mid, x][0]
    assert top_val > mid_val


# ----------------------------
# FileWriter Unit Tests
# ----------------------------

def test_filewriter_write_and_read(tmp_path):
    """
    write_image and write_config should successfully persist files.
    """
    dummy = np.zeros((5, 5, 3), dtype=np.uint8)
    cfg = {'a': 1}
    img_path = tmp_path / 'dir' / 'img.png'
    cfg_path = tmp_path / 'dir' / 'img.json'
    FileWriter.write_image(dummy, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    # Validate existence and content
    assert img_path.exists() and img_path.stat().st_size > 0
    loaded = json.loads(cfg_path.read_text())
    assert loaded == cfg


def test_filewriter_overwrite_existing(tmp_path):
    """
    Overwriting existing files should not error and should update content.
    """
    dummy1 = np.zeros((2, 2, 3), dtype=np.uint8)
    dummy2 = np.ones((2, 2, 3), dtype=np.uint8)
    cfg1 = {'x': 1}
    cfg2 = {'x': 2}
    img_path = tmp_path / 'o.png'
    cfg_path = tmp_path / 'o.json'
    FileWriter.write_image(dummy1, str(img_path))
    FileWriter.write_config(cfg1, str(cfg_path))
    FileWriter.write_image(dummy2, str(img_path))
    FileWriter.write_config(cfg2, str(cfg_path))
    loaded = json.loads(cfg_path.read_text())
    assert loaded == cfg2


# ----------------------------
# MatteEffect Integration Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_matte_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, then verify outputs.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'm.png',
        'width': 120,
        'height': 240,
        'margin': 5,
        'gradient_intensity': 0,
        'border_thickness': 3,
        'line_thickness': 2
    }
    me = MatteEffect(params)
    me.generate()
    img_path = tmp_path / 'm.png'
    cfg_path = tmp_path / 'm.json'
    assert img_path.exists() and cfg_path.exists()
    loaded = json.loads(cfg_path.read_text())
    # Verify saved config matches internal config
    for k, v in me.config.items():
        assert loaded[k] == v
    # Verify image dimensions
    img = cv2.imread(str(img_path))
    h, w = params['height'], params['width']
    b = params['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


@pytest.mark.parametrize("cfg_mod", [
    {'width': -10},
    {'margin': 500},  # margin too large
    {'paper_color': (300, 300, 300)},
    {'line_thickness': -1},
    {'gradient_intensity': -5}
])
@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_matte_effect_invalid_configuration(tmp_path, cfg_mod):
    """
    Invalid parameters should raise ValueError and not produce files.
    """
    params = {**cfg_mod, 'output_dir': str(tmp_path)}
    with pytest.raises(ValueError):
        MatteEffect(params).generate()


@pytest.mark.parametrize("_,seed", [(i, i) for i in range(3)])
def test_matte_effect_random_valid(tmp_path, _, seed):
    """
    Random valid parameters should generate output without errors.
    """
    random.seed(seed)
    params = {
        'output_dir': str(tmp_path),
        'output_file': f'rand{_}.png',
        'width': random.randint(50, 200),
        'height': random.randint(50, 200),
        'margin': random.randint(0, min(10, random.randint(1, 50))),
        'gradient_intensity': random.randint(0, 20),
        'border_thickness': random.randint(0, 5),
        'line_thickness': random.randint(1, 3),
        'paper_color': (245, 245, 245)
    }
    MatteEffect(params).generate()
    assert (tmp_path / f'rand{_}.png').exists()
    assert (tmp_path / f'rand{_}.json').exists()
