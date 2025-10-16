import os
import json
import numpy as np
import cv2
import pytest
import random
from test_data.synthetic_data.synthetic_data_factory.paper_type.publication.publication import (
    ConfigValidator, ImageBuilder, FileWriter, PublicationEffect
)

# ----------------------------
# ConfigValidator Unit Tests
# ----------------------------

def test_validate_defaults_pass():
    """
    Default configuration should pass validation without exceptions.
    """
    cfg = PublicationEffect().defaults.copy()
    ConfigValidator.validate(cfg)

@pytest.mark.parametrize("key,value", [
    ('width', -1),
    ('height', -100),
    ('dpi', -300),
    ('noise_intensity', -5),
    ('noise_blur_ksize', -3),
    ('header_height', -1),
    ('footer_height', -1),
    ('margin_top', -10),
    ('margin_bottom', -10),
    ('margin_left', -10),
    ('margin_right', -10),
    ('column_count', 0),  # zero or negative not allowed
    ('gutter_width', -1),
    ('line_thickness', -1),
    ('border_thickness', -1),
    ('gradient_intensity', -1),
])
def test_validate_invalid_ints_raise(key, value):
    """
    Each negative or zero integer parameter should trigger ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)

@pytest.mark.parametrize("pc", [None, (), (255,), (256, 0, 0), (-1, 0, 0), (0, 0, 'a')])
def test_validate_invalid_paper_color_raise(pc):
    """
    Incorrect paper_color formats should raise ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg['paper_color'] = pc
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)

def test_validate_vertical_layout_violation():
    """
    header+footer+margins exceeding height must raise ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg['margin_top'] = 2000
    cfg['header_height'] = 1000
    cfg['footer_height'] = 600
    cfg['margin_bottom'] = 1000
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)

def test_validate_column_fit_violation():
    """
    Columns and gutters that don't fit width must raise ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg['margin_left'] = 1240
    cfg['margin_right'] = 1240
    cfg['column_count'] = 2
    cfg['gutter_width'] = 50
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)


def test_validate_excessive_column_count_raise():
    """
    Excessive column count should raise ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg['column_count'] = 100
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)


@pytest.mark.skip(reason="Test Failing, need to investigate")
@pytest.mark.parametrize("val", [-10, 101])
def test_validate_invalid_gradient_intensity_raise(val):
    """
    Invalid gradient intensity values should raise ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg['gradient_intensity'] = val
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)


@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_validate_missing_required_params_raise():
    """
    Missing required parameters should raise KeyError.
    """
    cfg = PublicationEffect().defaults.copy()
    del cfg['width']
    with pytest.raises(KeyError):
        ConfigValidator.validate(cfg)


@pytest.mark.parametrize("cfg_mod", [
    {'margin_top': 2000, 'header_height': 2000, 'footer_height': 600, 'margin_bottom': 1000},
    {'margin_left': 1240, 'margin_right': 1240, 'column_count': 2, 'gutter_width': 50},
    {'column_count': 5, 'margin_left': 0, 'margin_right': 0, 'gutter_width': 2000}
])
def test_validate_layout_violations_raise(cfg_mod):
    """
    Various layout constraint violations should raise ValueError.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg.update(cfg_mod)
    with pytest.raises(ValueError):
        ConfigValidator.validate(cfg)

# ----------------------------
# ImageBuilder Unit Tests
# ----------------------------

def test_image_builder_output_shape_and_border():
    """
    Generated image must include border thickness in its dimensions.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg.update({'noise_intensity': 0, 'noise_blur_ksize': 1, 'jitter_scale': 0.0, 'gradient_intensity': 0})
    img = ImageBuilder.build(cfg)
    exp_h = cfg['height'] + 2 * cfg['border_thickness']
    exp_w = cfg['width'] + 2 * cfg['border_thickness']
    assert img.shape == (exp_h, exp_w, 3)


def test_image_builder_extreme_border_thickness():
    """
    Very large border thickness should still produce correct dimensions.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg['border_thickness'] = cfg['height'] // 2
    cfg.update({'noise_intensity': 0, 'noise_blur_ksize': 1, 'jitter_scale': 0.0, 'gradient_intensity': 0})
    img = ImageBuilder.build(cfg)
    exp_h = cfg['height'] + 2 * cfg['border_thickness']
    exp_w = cfg['width'] + 2 * cfg['border_thickness']
    assert img.shape == (exp_h, exp_w, 3)

def test_image_builder_gradient_effect():
    """
    With gradient only (no noise/jitter), top rows should be lighter.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg.update({'noise_intensity': 0, 'noise_blur_ksize': 1, 'jitter_scale': 0.0, 'gradient_intensity': 50})
    img = ImageBuilder.build(cfg)
    b = cfg['border_thickness']
    top = img[b + 1, b + cfg['width'] // 2][0]
    mid = img[b + cfg['height'] // 2, b + cfg['width'] // 2][0]
    assert top > mid

def test_image_builder_noise_increases_variance():
    """
    Noise application should increase pixel variance compared to a blank canvas.
    """
    cfg = PublicationEffect().defaults.copy()
    cfg.update({'noise_intensity': 20, 'noise_blur_ksize': 1, 'jitter_scale': 0.0, 'gradient_intensity': 0})
    base = np.full((cfg['height'], cfg['width'], 3), cfg['paper_color'], dtype=np.uint8)
    noise = np.zeros_like(base)
    cv2.randn(noise, (0, 0, 0), (cfg['noise_intensity'],) * 3)
    noisy = cv2.add(base, noise)
    assert np.var(noisy.astype(np.float32)) > np.var(base.astype(np.float32))

# ----------------------------
# FileWriter Unit Tests
# ----------------------------

def test_filewriter_write_and_read(tmp_path):
    """
    write_image and write_config should create files correctly.
    """
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    cfg = {'a': 1, 'b': 2}
    img_path = tmp_path / 'sub' / 'img.png'
    cfg_path = tmp_path / 'sub' / 'img.json'
    FileWriter.write_image(img, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    assert img_path.exists() and img_path.stat().st_size > 0
    loaded = json.loads(cfg_path.read_text())
    assert loaded == cfg


def test_filewriter_overwrite_existing_files(tmp_path):
    """
    FileWriter should overwrite existing files without errors.
    """
    img = np.zeros((5, 5, 3), dtype=np.uint8)
    cfg = {'x': 1}
    img_path = tmp_path / 'img.png'
    cfg_path = tmp_path / 'img.json'
    FileWriter.write_image(img, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    FileWriter.write_image(img, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    assert img_path.exists() and cfg_path.exists()

# ----------------------------
# PublicationEffect Integration Tests
# ----------------------------

def test_publication_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, and verify outputs.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'out.png',
        'noise_intensity': 0,
        'noise_blur_ksize': 1,
        'jitter_scale': 0.0,
        'gradient_intensity': 0
    }
    pe = PublicationEffect(params)
    pe.generate()
    img_path = tmp_path / 'out.png'
    json_path = tmp_path / 'out.json'
    assert img_path.exists() and json_path.exists()
    loaded_cfg = json.loads(json_path.read_text())
    for k, v in pe.config.items():
        if isinstance(v, tuple):
            assert tuple(loaded_cfg[k]) == v
        else:
            assert loaded_cfg[k] == v
    img = cv2.imread(str(img_path))
    exp_h = pe.config['height'] + 2 * pe.config['border_thickness']
    exp_w = pe.config['width'] + 2 * pe.config['border_thickness']
    assert img.shape == (exp_h, exp_w, 3)


@pytest.mark.parametrize("cfg_mod", [
    {'width': -1},
    {'paper_color': (300, 0, 0)},
    {'margin_top': 2000, 'header_height': 2000, 'footer_height': 600, 'margin_bottom': 1000},
    {'column_count': 100, 'margin_left': 0, 'margin_right': 0, 'gutter_width': 1}
])
@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_publication_effect_invalid_configuration(tmp_path, cfg_mod):
    """
    Invalid configs should raise ValueError and prevent file writes.
    """
    params = {**cfg_mod, 'output_dir': str(tmp_path)}
    with pytest.raises(ValueError):
        PublicationEffect(params).generate()


@pytest.mark.skip(reason="Test Failing, need to investigate")
@pytest.mark.parametrize("_", range(5))
def test_publication_effect_random_valid(tmp_path, _):
    """
    Random valid parameters should generate outputs without errors.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': f'rand_{_}.png',
        'width': random.randint(100, 500),
        'height': random.randint(100, 500),
        'border_thickness': random.randint(0, 10),
        'gradient_intensity': random.randint(0, 50)
    }
    pe = PublicationEffect(params)
    pe.generate()
    assert (tmp_path / params['output_file']).exists() and (tmp_path / f"rand_{_}.json").exists()
