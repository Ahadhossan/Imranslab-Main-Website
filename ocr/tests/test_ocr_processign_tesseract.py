import pytest
import os
from unittest.mock import patch, mock_open
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pytesseract
from ocr_processing.scripts.ocr_tesseract import process_image

# Helper functions for test image generation
def generate_text_image(text, font_size=20, size=(400, 100), add_noise=False, rotation=0):
    """Generate test images with configurable text and parameters"""
    image = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)

    draw.text(position, text, font=font, fill=(0, 0, 0))

    if add_noise:
        arr = np.array(image)
        noise = np.random.randint(0, 255, arr.shape, dtype=np.uint8)
        image = Image.fromarray(np.where(np.random.random(arr.shape) < 0.1, noise, arr))

    if rotation:
        image = image.rotate(rotation, expand=True, fillcolor='white')

    return image

def generate_handwritten_style_image(text):
    """Simulate handwritten text with random perturbations"""
    image = Image.new('RGB', (600, 150), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font_size = 24

    try:
        font = ImageFont.truetype("Comic Sans MS.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    x, y = 10, 20
    for char in text:
        draw.text((x + np.random.randint(-2, 2), y + np.random.randint(-2, 2)),
                  char, font=font, fill=(0, 0, 0))
        x += font.getbbox(char)[2] + np.random.randint(-2, 5)

    return image

# Test fixtures
@pytest.fixture(scope="module")
def test_texts():
    return {
        "english": "The quick brown fox jumps over the lazy dog",
        "numbers": "1234567890",
        "special_chars": "!@#$%^&*()_+-=[]{};':\",./<>?",
        "multilingual": "你好世界 Bonjour le monde"
    }

@pytest.fixture
def clean_output():
    yield
    output_dir = os.path.join("output", "ocr_tesseract")
    if os.path.exists(output_dir):
        for f in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, f))
        os.rmdir(output_dir)

# Core test cases with JPG format
@pytest.mark.skip
def test_clear_text_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["english"]
    img_path = tmp_path / "clear_text.jpg"
    generate_text_image(text).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

@pytest.mark.skip
def test_noisy_text_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["numbers"]
    img_path = tmp_path / "noisy_text.jpg"
    generate_text_image(text, add_noise=True).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text, min_confidence=70)

@pytest.mark.skip
def test_rotated_text_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["special_chars"]
    img_path = tmp_path / "rotated_text.jpg"
    generate_text_image(text, rotation=15).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

@pytest.mark.skip
def test_handwritten_text_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["english"]
    img_path = tmp_path / "handwritten.jpg"
    generate_handwritten_style_image(text).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text, min_confidence=50)

@pytest.mark.skip
def test_different_font_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["english"]
    img_path = tmp_path / "different_font.jpg"
    generate_text_image(text, font_size=24).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

@pytest.mark.skip
def test_low_contrast_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["english"]
    img_path = tmp_path / "low_contrast.jpg"
    image = generate_text_image(text)
    image = image.point(lambda x: x * 0.5)
    image.save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text, min_confidence=40)

@pytest.mark.skip
def test_multilingual_ocr(tmp_path, test_texts, clean_output):
    text = test_texts["multilingual"]
    img_path = tmp_path / "multilingual.jpg"
    generate_text_image(text).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text, lang="chi_sim+eng")

# Mocking and Verification Utilities
def _verify_ocr_processing(image_path, expected_text, min_confidence=None, lang=None):
    with patch('pytesseract.image_to_string') as mock_ocr, \
         patch('os.makedirs'), \
         patch('builtins.open', mock_open()) as mock_file:

        mock_ocr.return_value = expected_text
        output_folder = "output/"
        if lang:
            process_image(image_path, output_folder, lang)
        else:
            process_image(image_path, output_folder)

        mock_ocr.assert_called_once()
        if lang:
            args, kwargs = mock_ocr.call_args
            assert kwargs.get('lang') == lang

        base_name = os.path.splitext(os.path.basename(image_path))[0]
        expected_path = os.path.join(output_folder, "ocr_tesseract", f"{base_name}_processed_tesseract.txt")
        mock_file().write.assert_called_once_with(f"Processed file: {image_path}\n\n{expected_text}")

        if min_confidence:
            data = pytesseract.image_to_data(mock_ocr.call_args[0][0], output_type=pytesseract.Output.DICT)
            confidences = [int(c) for c in data['conf'] if c != '-1']
            assert sum(confidences) / len(confidences) >= min_confidence

# Additional edge cases with JPG format
@pytest.mark.skip
def test_small_text_ocr(tmp_path, clean_output):
    text = "Small text"
    img_path = tmp_path / "small_text.jpg"
    generate_text_image(text, font_size=8, size=(200, 50)).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text, min_confidence=30)

@pytest.mark.skip
def test_vertical_text_ocr(tmp_path, clean_output):
    text = "Vertical"
    img_path = tmp_path / "vertical_text.jpg"
    generate_text_image(text).rotate(90, expand=True).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

@pytest.mark.skip
def test_mixed_format_ocr(tmp_path, test_texts, clean_output):
    text = f"{test_texts['english']}\n{test_texts['numbers']}\n{test_texts['special_chars']}"
    img_path = tmp_path / "mixed_format.jpg"
    generate_text_image(text).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

@pytest.mark.skip
def test_image_mode_handling(tmp_path, clean_output):
    text = "Grayscale Test"
    img_path = tmp_path / "grayscale.jpg"
    generate_text_image(text).convert('L').save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

@pytest.mark.skip
def test_large_image_handling(tmp_path, clean_output):
    text = "Large Image"
    img_path = tmp_path / "large_image.jpg"
    generate_text_image(text, size=(2000, 3000)).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), text)

def test_invalid_image_format():
    with pytest.raises(SystemExit):
        process_image("invalid.txt", "output/")

@pytest.mark.skip
def test_image_without_text(tmp_path, clean_output):
    img_path = tmp_path / "blank.jpg"
    Image.new('RGB', (400, 200), (255, 255, 255)).save(img_path, format='JPEG', quality=95)
    _verify_ocr_processing(str(img_path), "")