from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json


class SyntheticOutputDataFactory:
    def __init__(self, output_dir: Path, dpi: int = 300):
        self.output_dir = Path(output_dir)
        self.dpi = dpi
        # A4 size at 300 DPI in pixels (1/4 scale for testing)
        self.page_width = 2480 // 4
        self.page_height = 3508 // 4

    def create_image(self, spec_path: Path) -> Path:
        with open(spec_path, 'r', encoding='utf-8') as f:
            spec = json.load(f)

        image = Image.new("RGB", (self.page_width, self.page_height), color="white")
        draw = ImageDraw.Draw(image)

        for item in spec.get("text", []):
            font_size = item.get("size", 12)
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"  # Replace if using a different font
            font = ImageFont.truetype(font_path, font_size)

            position = tuple(item.get("position", [0, 0]))
            draw.text(position, item["content"], fill="black", font=font)

        out_path = self.output_dir / "output.png"
        image.save(out_path, dpi=(self.dpi, self.dpi))
        return out_path
