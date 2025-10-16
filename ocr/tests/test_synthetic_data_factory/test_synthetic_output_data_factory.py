import json
from pathlib import Path
from PIL import Image
import pytest

from test_data.synthetic_data.synthetic_data_factory.synthetic_output_data_factory import SyntheticOutputDataFactory


@pytest.fixture
def sample_spec(tmp_path):
    spec = {
        "paper_type": "regular",
        "text": [
            {
                "content": "Test page",
                "font": "Times New Roman",
                "size": 24,
                "bold": False,
                "italic": False,
                "underline": False,
                "position": [50, 50]
            }
        ],
        "distortion": {
            "noise_level": 0.0,
            "smudges": 0.0,
            "distortion_factor": 0.0
        }
    }
    p = tmp_path / "spec.json"
    p.write_text(json.dumps(spec))
    return p

@pytest.mark.skip
def test_create_image_from_spec(sample_spec, tmp_path):
    factory = SyntheticOutputDataFactory(output_dir=tmp_path, dpi=300)
    img_path = factory.create_image(sample_spec)

    # Check that the image was saved correctly
    assert img_path.exists()

    # Check the image properties
    img = Image.open(img_path)
    # A4@300dpi is 2480×3508 pixels; 1/16th (divide both dims by 4) → 620×877
    assert img.size == (620, 877)
    assert img.mode == "RGB"

    # Check that some pixels aren’t just white (i.e. text got drawn)
    pixels = img.getdata()
    assert any(px != (255, 255, 255) for px in pixels)
    assert img_path.exists()

    img = Image.open(img_path)
    # A4@300dpi is 2480×3508 pixels; 1/16th (divide both dims by 4) → 620×877
    assert img.size == (620, 877)
    assert img.mode == "RGB"

    # check that some pixels aren’t just white (i.e. text got drawn)
    pixels = img.getdata()
    assert any(px != (255, 255, 255) for px in pixels)
