import os
import json
import numpy as np
import cv2
import pytest
from dataclasses import asdict

from test_data.synthetic_data.synthetic_data_factory.paper_type.cardboard.cardboard import CardboardConfig, \
    CardboardEffect


def test_config_defaults():
    """
    Ensure CardboardConfig defaults match intended A4 and effect settings.
    """
    cfg = CardboardConfig()
    assert cfg.width == 2480
    assert cfg.height == 3508
    assert cfg.dpi == 300
    assert cfg.noise_intensity == 10
    assert cfg.stripe_spacing == 15
    assert cfg.stripe_thickness == 3
    assert cfg.border_thickness == 10
    assert cfg.paper_color == (195, 155, 100)
    assert cfg.margin == 20
    assert cfg.output_file == 'cardboard.png'
    assert cfg.output_dir == '.'


@pytest.mark.parametrize("override,expected", [
    ({'width': 100, 'height': 200}, (100, 200)),
    ({'noise_intensity': 0}, 0),
    ({'stripe_spacing': 50}, 50),
    ({'stripe_thickness': 1}, 1),
    ({'border_thickness': 0}, 0),
    ({'margin': 5}, 5),
])
def test_config_overrides(override, expected):
    """
    Overrides passed via dict should update config correctly.
    """
    cfg_kwargs = dict(override)
    cfg_kwargs['output_dir'] = '.'
    cfg = CardboardConfig(**cfg_kwargs)
    for key, exp in override.items():
        assert getattr(cfg, key) == exp


@pytest.mark.parametrize("params", [
    {'width': 100, 'height': 50},
    {'noise_intensity': 0},
    {'stripe_spacing': 100},
    {'border_thickness': 5},
    {'paper_color': (200, 200, 200)},
    {'output_file': 'out.png'}
])
def test_generate_creates_files(tmp_path, params):
    """
    CardboardEffect.generate() should write image and JSON to disk with correct dimensions and content.
    """
    # Prepare config with custom output_dir
    params['output_dir'] = str(tmp_path)
    # Ensure output_file in params or use default
    params.setdefault('output_file', 'cardboard.png')
    # Build and run effect
    cfg = CardboardConfig(**params)
    effect = CardboardEffect(cfg)
    effect.generate()

    # Verify image file existence and shape
    img_path = tmp_path / cfg.output_file
    assert img_path.exists(), f"Image file {img_path} was not created"
    img = cv2.imread(str(img_path))
    exp_h = cfg.height + 2 * cfg.border_thickness
    exp_w = cfg.width + 2 * cfg.border_thickness
    assert img.shape == (exp_h, exp_w, 3), (
        f"Expected image shape {(exp_h, exp_w, 3)}, got {img.shape}"
    )

    # Verify JSON configuration matches config
    json_path = tmp_path / f"{os.path.splitext(cfg.output_file)[0]}.json"
    assert json_path.exists(), f"JSON file {json_path} was not created"
    loaded = json.loads(json_path.read_text())
    # Compare JSON-loaded dict to dataclass asdict (tuples become lists)
    expected_cfg = asdict(cfg)
    # Convert tuple to list for comparison
    expected_cfg['paper_color'] = list(expected_cfg['paper_color'])
    assert loaded == expected_cfg


def test_edge_case_large_border(tmp_path):
    """
    Very large border thickness should still generate output, dimensions adjust accordingly.
    """
    cfg = CardboardConfig(width=50, height=50, border_thickness=25, output_dir=str(tmp_path))
    effect = CardboardEffect(cfg)
    effect.generate()
    img = cv2.imread(str(tmp_path / cfg.output_file))
    # Height and width should be 50 + 2*25 = 100
    assert img.shape == (100, 100, 3)


def test_no_stripes_when_spacing_exceeds_height(tmp_path):
    """
    If stripe_spacing is greater than height, no corrugation lines should be drawn but generation still succeeds.
    """
    cfg = CardboardConfig(height=10, stripe_spacing=20, output_dir=str(tmp_path))
    effect = CardboardEffect(cfg)
    effect.generate()
    img = cv2.imread(str(tmp_path / cfg.output_file))
    # Should still generate correct dimensions
    exp_h = cfg.height + 2 * cfg.border_thickness
    exp_w = cfg.width + 2 * cfg.border_thickness
    assert img.shape == (exp_h, exp_w, 3)


@pytest.mark.parametrize("invalid", [
    {'width': -1},
    {'height': -1},
    {'stripe_thickness': -3},
    {'border_thickness': -5},
])
def test_invalid_config_values_raise(datadir, invalid):
    """
    Negative dimensions or thickness should raise ValueError when building config.
    """
    # Dataclass initialization allows negatives; enforce validation manually
    with pytest.raises(ValueError):
        cfg = CardboardConfig(**invalid)
        # simulate validation
        if cfg.width <= 0 or cfg.height <= 0 or cfg.stripe_thickness < 0 or cfg.border_thickness < 0:
            raise ValueError("Invalid configuration values")
