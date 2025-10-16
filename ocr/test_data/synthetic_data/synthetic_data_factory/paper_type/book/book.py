import os
import json
import numpy as np
import cv2


class BookConfigValidator:
    """
    Validates configuration parameters for a book-page scanned effect.
    """

    @staticmethod
    def validate(cfg: dict):
        # Required integer parameters
        required_ints = [
            'width', 'height', 'dpi',
            'gradient_intensity', 'border_thickness',
            'margin', 'line_thickness'
        ]
        for key in required_ints:
            if key not in cfg:
                raise ValueError(f"Missing required config '{key}'")
            val = cfg[key]
            if not isinstance(val, int) or val < 0:
                raise ValueError(f"{key} must be non-negative int, got {val}")

        # Validate paper_color as RGB tuple of ints 0-255
        pc = cfg.get('paper_color')
        if (not isinstance(pc, tuple) or len(pc) != 3 or
                any((not isinstance(c, int) or c < 0 or c > 255) for c in pc)):
            raise ValueError(f"paper_color must be tuple of 3 ints 0-255, got {pc}")

        # Margins must fit within dimensions
        if cfg['margin'] * 2 >= cfg['width']:
            raise ValueError("margin too large for width")
        if cfg['margin'] * 2 >= cfg['height']:
            raise ValueError("margin too large for height")


class BookImageBuilder:
    """
    Builds the book-page scanned effect in memory.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base book-page tone
        img = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Subtle horizontal gradient scan lines
        for y in range(cfg['margin'], h - cfg['margin']):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(
                img,
                (cfg['margin'], y),
                (w - cfg['margin'], y),
                (intensity, intensity, intensity),
                cfg['line_thickness']
            )
        # Add border to simulate scanned edge
        edge_color = (200, 200, 200)
        img = cv2.copyMakeBorder(
            img,
            cfg['border_thickness'], cfg['border_thickness'],
            cfg['border_thickness'], cfg['border_thickness'],
            cv2.BORDER_CONSTANT,
            value=edge_color
        )
        return img


class FileWriter:
    """
    Handles saving images and JSON configs to disk.
    """

    @staticmethod
    def write_image(img: np.ndarray, path: str):
        dirn = os.path.dirname(path) or '.'
        os.makedirs(dirn, exist_ok=True)
        if not cv2.imwrite(path, img):
            raise IOError(f"Failed to write image to {path}")

    @staticmethod
    def write_config(cfg: dict, path: str):
        dirn = os.path.dirname(path) or '.'
        os.makedirs(dirn, exist_ok=True)
        with open(path, 'w') as f:
            json.dump(cfg, f, indent=4)


class BookEffect:
    """
    Orchestrates validation, image building, and file I/O for book pages.
    """

    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Defaults for a 6×9" book page at 300 DPI
        self.defaults = {
            'width': int(6 * 300),  # 1800 px
            'height': int(9 * 300),  # 2700 px
            'dpi': 300,
            'gradient_intensity': 15,  # subtle scan artifact
            'border_thickness': 10,
            'paper_color': (250, 250, 245),  # off-white book paper tone
            'margin': 20,
            'line_thickness': 1,
            'output_file': 'book.png',
            'output_dir': script_dir,
        }
        # Merge user overrides
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        cfg = self.config
        # Validate config
        BookConfigValidator.validate(cfg)
        # Build image
        img = BookImageBuilder.build(cfg)
        # Determine paths
        img_path = os.path.join(cfg['output_dir'], cfg['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        # Save outputs
        FileWriter.write_image(img, img_path)
        FileWriter.write_config(cfg, cfg_path)
        print(f"Image saved to {img_path}")
        print(f"Config saved to {cfg_path}")


def main():
    """
    Default invocation; override parameters in input_params as needed.
    """
    input_params = {
        # 'width': 1800,
        # 'height': 2700,
        # 'dpi': 300,
        # 'gradient_intensity': 15,
        # 'border_thickness': 10,
        # 'paper_color': (250, 250, 245),
        # 'margin': 20,
        # 'line_thickness': 1,
        # 'output_file': 'book.png',
        # 'output_dir': '.',
    }
    BookEffect(input_params).generate()


if __name__ == '__main__':
    main()
