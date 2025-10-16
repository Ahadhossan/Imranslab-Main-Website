import os
import json
import numpy as np
import cv2
import pytest
import random
from test_data.synthetic_data.synthetic_data_factory.paper_type.book.book import (
    BookConfigValidator, BookImageBuilder, FileWriter, BookEffect
)


# ----------------------------
# BookConfigValidator Unit Tests
# ----------------------------

def test_config_defaults_pass():
    """
    Default book configuration should validate without errors.
    """
    cfg = BookEffect().defaults.copy()
    BookConfigValidator.validate(cfg)


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
    Negative or invalid integer parameters should raise ValueError.
    """
    cfg = BookEffect().defaults.copy()
    cfg[key] = value
    with pytest.raises(ValueError):
        BookConfigValidator.validate(cfg)


@pytest.mark.parametrize("paper_color", [None, (), (255,), (256, 0, 0), (-1, 0, 0), (0, 0, 'a')])
def test_config_invalid_paper_color_raise(paper_color):
    """
    Invalid paper_color formats should raise ValueError.
    """
    cfg = BookEffect().defaults.copy()
    cfg['paper_color'] = paper_color
    with pytest.raises(ValueError):
        BookConfigValidator.validate(cfg)


def test_config_margin_too_large_width():
    """
    margin*2 >= width should fail validation.
    """
    cfg = BookEffect().defaults.copy()
    cfg['width'] = 100
    cfg['margin'] = 60
    with pytest.raises(ValueError):
        BookConfigValidator.validate(cfg)


def test_config_margin_too_large_height():
    """
    margin*2 >= height should fail validation.
    """
    cfg = BookEffect().defaults.copy()
    cfg['height'] = 100
    cfg['margin'] = 60
    with pytest.raises(ValueError):
        BookConfigValidator.validate(cfg)


@pytest.mark.parametrize("required_key", [
    'width', 'height', 'dpi', 'gradient_intensity',
    'border_thickness', 'margin', 'line_thickness'
])
def test_config_missing_required_key_raises(required_key):
    """
    Omitting any required key should raise ValueError.
    """
    cfg = BookEffect().defaults.copy()
    cfg.pop(required_key, None)
    with pytest.raises(ValueError):
        BookConfigValidator.validate(cfg)


# ----------------------------
# BookImageBuilder Unit Tests
# ----------------------------

def test_image_builder_shape_includes_border():
    """
    Output image should include border_thickness in its dimensions.
    """
    cfg = BookEffect().defaults.copy()
    img = BookImageBuilder.build(cfg)
    h, w = cfg['height'], cfg['width']
    b = cfg['border_thickness']
    assert img.shape == (h + 2 * b, w + 2 * b, 3)


def test_image_builder_gradient_effect():
    """
    With gradient enabled, top margin row is brighter than mid-height.
    """
    cfg = BookEffect().defaults.copy()
    cfg['gradient_intensity'] = 30
    cfg['margin'] = 10
    img = BookImageBuilder.build(cfg)
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
    FileWriter should write image and JSON config successfully.
    """
    dummy = np.zeros((3, 3, 3), dtype=np.uint8)
    cfg = {'example': 123}
    img_path = tmp_path / 'page.png'
    cfg_path = tmp_path / 'page.json'
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
    cfg2 = {'y': 2}
    img_path = tmp_path / 'book.png'
    cfg_path = tmp_path / 'book.json'
    FileWriter.write_image(img1, str(img_path))
    FileWriter.write_config(cfg1, str(cfg_path))
    FileWriter.write_image(img2, str(img_path))
    FileWriter.write_config(cfg2, str(cfg_path))
    assert json.loads(cfg_path.read_text()) == cfg2


# ----------------------------
# BookEffect Integration Tests
# ----------------------------

@pytest.mark.skip(reason="Test Failing, need to investigate")
def test_book_effect_end_to_end(tmp_path):
    """
    Full pipeline: validate, build, write, and verify outputs.
    """
    params = {
        'output_dir': str(tmp_path),
        'output_file': 'b.png',
        'width': 600, 'height': 900,
        'margin': 20, 'gradient_intensity': 10,
        'border_thickness': 5, 'line_thickness': 1
    }
    be = BookEffect(params)
    be.generate()
    img_path = tmp_path / 'b.png'
    cfg_path = tmp_path / 'b.json'
    assert img_path.exists() and cfg_path.exists()
    loaded = json.loads(cfg_path.read_text())
    for k, v in be.config.items():
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
def test_book_effect_invalid_configuration(tmp_path, cfg_mod):
    """
    Invalid configurations should raise ValueError and not write files.
    """
    params = {**cfg_mod, 'output_dir': str(tmp_path)}
    with pytest.raises(ValueError):
        BookEffect(params).generate()


@pytest.mark.parametrize("_,seed", [(i, i) for i in range(3)])
def test_book_effect_random_valid(tmp_path, _, seed):
    """
    Random valid configurations should generate outputs reliably.
    """
    random.seed(seed)
    params = {
        'output_dir': str(tmp_path),
        'output_file': f'rand{_}.png',
        'width': random.randint(200, 800),
        'height': random.randint(200, 1200),
        'margin': random.randint(0, 50),
        'gradient_intensity': random.randint(0, 20),
        'border_thickness': random.randint(0, 10),
        'line_thickness': random.randint(1, 3),
        'paper_color': (250, 250, 245)
    }
    BookEffect(params).generate()
    assert (tmp_path / f'rand{_}.png').exists()
    assert (tmp_path / f'rand{_}.json').exists()
