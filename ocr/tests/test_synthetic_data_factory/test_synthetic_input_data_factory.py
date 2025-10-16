import sys
import pytest
from pathlib import Path



@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path

@pytest.mark.skip
def test_create_json_spec(tmp_dir):
    # arrange
    factory = SyntheticInputDataFactory(output_dir=tmp_dir)
    spec_kwargs = {
        "paper_type": "glossy",
        "text": [
            {
                "content": "Hello, OCR!",
                "font": "Arial",
                "size": 14,
                "bold": True,
                "italic": False,
                "underline": False,
                "position": [20, 30]
            }
        ],
        "distortion": {
            "noise_level": 0.05,
            "smudges": 2,
            "distortion_factor": 0.03
        }
    }

    # act
    spec_path = factory.create_spec(**spec_kwargs)  # we’ll define this API
    assert spec_path.exists()

    # assert JSON structure
    data = json.loads(spec_path.read_text())
    assert data["paper_type"] == "glossy"
    assert isinstance(data["text"], list) and data["text"][0]["content"] == "Hello, OCR!"
    assert "distortion_factor" in data["distortion"]

@pytest.mark.skip
def test_invalid_paper_type_raises(tmp_dir):
    factory = SyntheticInputDataFactory(output_dir=tmp_dir)
    with pytest.raises(ValueError):
        factory.create_spec(paper_type="papyrus", text=[], distortion={})
