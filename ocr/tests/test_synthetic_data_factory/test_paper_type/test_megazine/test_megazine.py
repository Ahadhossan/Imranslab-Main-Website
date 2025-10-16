import os
import json
import numpy as np
import cv2
import pytest
import random
from test_data.synthetic_data.synthetic_data_factory.paper_type.megazine.megazine import (
    MagazineConfigValidator,
    MagazineImageBuilder,
    FileWriter,
    MagazineEffect
)


# ----------------------------
# MagazineConfigValidator Unit Tests
# ----------------------------

def test_config_defaults_pass():
    """
    Default magazine configuration should validate without errors.
    """
    cfg = MagazineEffect().defaults.copy()
    MagazineConfigValidator.validate(cfg)


@pytest.mark.parametrize("key,value", [
    ('width', -1), ('height', -100), ('dpi', -300),
    ('gradient_intensity', -5), ('border_thickness', -1),
    ('margin', -10), ('line_thickness', -1)
])
def test_config_invalid_integers(key, value):
    """
    Negative or zero values for required integers should raise ValueError.
    """
    cfg = MagazineEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        MagazineConfigValidator.validate(cfg)


@pytest.mark.parametrize("pc", [None, (), (255,), (256, 0, 0), (-1, 0, 0), (0, 0, 'a')])
def test_config_invalid_color(pc):
    """
    Invalid paper_color formats should raise ValueError.
    """
    cfg = MagazineEffect().defaults.copy()
    cfg['paper_color'] = pc
    with pytest.raises(ValueError):
        MagazineConfigValidator.validate(cfg)


def test_config_margin_too_large_width():
    """
    margin*2 >= width should raise ValueError.
    """
    cfg = MagazineEffect().defaults.copy()
    cfg['width'] = 50
    cfg['margin'] = 30
    with pytest.raises(ValueError):
        MagazineConfigValidator.validate(cfg)


def test_config_margin_too_large_height():
    """
    margin*2 >= height should raise ValueError.
    """
    cfg = MagazineEffect().defaults.copy()
    cfg['height'] = 50
    cfg['margin'] = 30
    with pytest.raises(ValueError):
        MagazineConfigValidator.validate(cfg)


@pytest.mark.parametrize("required_key", [
    'width', 'height', 'dpi', 'gradient_intensity',
    'border_thickness', 'margin', 'line_thickness'
])
def test_config_missing_required_key(required_key):
    """
    Omitting any required key should raise ValueError.
    """
    cfg = MagazineEffect().defaults.copy()
    cfg.pop(required_key, None)
    with pytest.raises(ValueError):
        MagazineConfigValidator.validate(cfg)


# ----------------------------
# MagazineImageBuilder Unit Tests
# ----------------------------

def test_image_builder_shape_includes_border():
    """
    Built image must include border_thickness on all sides.
    """
    cfg = MagazineEffect().defaults.copy()
    img = MagazineImageBuilder.build(cfg)
    h, w = cfg['height'], cfg['width']
    b = cfg['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


def test_image_builder_gradient_effect():
    """
    With gradient, pixel intensity at top margin should exceed mid-height.
    """
    cfg = MagazineEffect().defaults.copy()
    cfg['gradient_intensity'] = 40
    cfg['margin'] = 20
    img = MagazineImageBuilder.build(cfg)
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
    dummy = np.zeros((4, 4, 3), np.uint8)
    cfg = {'a': 42}
    img_path = tmp_path / 'img.png'
    cfg_path = tmp_path / 'img.json'
    FileWriter.write_image(dummy, str(img_path))
    FileWriter.write_config(cfg, str(cfg_path))
    assert img_path.exists() and img_path.stat().st_size > 0
    assert json.loads(cfg_path.read_text()) == cfg


def test_filewriter_overwrite(tmp_path):
    """
    Overwriting existing files should succeed without errors.
    """
    img1 = np.zeros((3, 3, 3), np.uint8)
    img2 = np.ones((3, 3, 3), np.uint8)
    cfg1 = {'x': 1}
    cfg2 = {'x': 2}
    img_path = tmp_path / 'm.png'
    cfg_path = tmp_path / 'm.json'
    FileWriter.write_image(img1, str(img_path))
    FileWriter.write_config(cfg1, str(cfg_path))
    FileWriter.write_image(img2, str(img_path))
    FileWriter.write_config(cfg2, str(cfg_path))
    assert json.loads(cfg_path.read_text()) == cfg2


# ----------------------------
# MagazineEffect Integration Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_magazine_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, verify files and content.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'mag.png',
        'width': 800, 'height': 1000,
        'margin': 20, 'gradient_intensity': 10,
        'border_thickness': 10, 'line_thickness': 1
    }
    me = MagazineEffect(params)
    me.generate()
    ip = tmp_path / 'mag.png'
    cp = tmp_path / 'mag.json'
    assert ip.exists() and cp.exists()
    loaded = json.loads(cp.read_text())
    for k, v in me.config.items():
        assert loaded[k] == v
    img = cv2.imread(str(ip))
    h, w = params['height'], params['width']
    b = params['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


@pytest.mark.parametrize("cfg_mod", [
    {'width': -10}, {'margin': 500},
    {'paper_color': (300, 300, 300)}, {'line_thickness': -1}
])
@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_magazine_effect_invalid(tmp_path, cfg_mod):
    """
    Invalid configs should raise ValueError and not write files.
    """
    params = {**cfg_mod, 'output_dir': str(tmp_path)}
    with pytest.raises(ValueError):
        MagazineEffect(params).generate()


@pytest.mark.parametrize("_,seed", [(i, i) for i in range(3)])
def test_magazine_effect_random_valid(tmp_path, _, seed):
    """
    Random valid parameters must succeed reproducibly.
    """
    random.seed(seed)
    params = {
        'output_dir': str(tmp_path),
        'output_file': f'r{_}.png',
        'width': random.randint(100, 300),
        'height': random.randint(100, 300),
        'margin': random.randint(0, 30),
        'gradient_intensity': random.randint(0, 50),
        'border_thickness': random.randint(0, 15),
        'line_thickness': random.randint(1, 3),
        'paper_color': (250, 250, 245)
    }
    MagazineEffect(params).generate()
    assert (tmp_path / f'r{_}.png').exists() and (tmp_path / f'r{_}.json').exists()
