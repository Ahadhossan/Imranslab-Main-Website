import os
import json
import numpy as np
import cv2


class RegularConfigValidator:
    """
    Validates configuration parameters for an A4 scanned paper effect.
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

        # paper_color: tuple of 3 ints 0-255
        pc = cfg.get('paper_color')
        if (not isinstance(pc, tuple) or len(pc) != 3 or
                any((not isinstance(c, int) or c < 0 or c > 255) for c in pc)):
            raise ValueError(f"paper_color must be tuple of 3 ints 0-255, got {pc}")

        # Margins must fit within dimensions
        if cfg['margin'] * 2 >= cfg['width']:
            raise ValueError("margin too large for width")
        if cfg['margin'] * 2 >= cfg['height']:
            raise ValueError("margin too large for height")


class RegularImageBuilder:
    """
    Builds the A4 scanned effect image in memory.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base canvas with specified paper color
        img = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Apply vertical gradient scan lines
        for y in range(cfg['margin'], h - cfg['margin']):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(
                img,
                (cfg['margin'], y),
                (w - cfg['margin'], y),
                (intensity, intensity, intensity),
                cfg['line_thickness']
            )
        # Add border to simulate scanning edge
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
    Handles saving images and configuration JSON to disk.
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


class RegularEffect:
    """
    Orchestrates validation, image building, and file output for A4 scanned paper.
    """

    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.defaults = {
            'width': 2480,  # A4 @300 DPI
            'height': 3508,
            'dpi': 300,
            'gradient_intensity': 50,
            'border_thickness': 20,
            'paper_color': (255, 255, 255),
            'margin': 50,
            'line_thickness': 1,
            'output_file': 'regular.png',
            'output_dir': script_dir,
        }
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        cfg = self.config
        # Validate configuration
        RegularConfigValidator.validate(cfg)
        # Build the image
        img = RegularImageBuilder.build(cfg)
        # Determine paths
        img_path = os.path.join(cfg['output_dir'], cfg['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        # Save outputs
        FileWriter.write_image(img, img_path)
        FileWriter.write_config(cfg, cfg_path)
        print(f"Image saved to {img_path}")
        print(f"Configuration saved to {cfg_path}")


def main():
    """
    Default invocation; override input_params for customization.
    """
    input_params = {
        'width': 2000,
        'dpi': 600,
        'gradient_intensity': 1,
        'paper_color': (240, 240, 240),  # Light gray paper
        'margin': 0,
        'line_thickness': 1,
        # 'height': 3508,
        # 'border_thickness': 20,
        # 'output_file': 'regular.png',
        # 'output_dir': '.',
    }
    RegularEffect(input_params).generate()


if __name__ == '__main__':
    main()