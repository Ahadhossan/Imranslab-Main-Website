import os
import json
import numpy as np
import cv2


class MatteConfigValidator:
    """
    Validates configuration parameters for matte paper effect.
    """

    @staticmethod
    def validate(cfg: dict):
        # Required integer parameters >= 0
        int_keys = [
            'width', 'height', 'dpi', 'gradient_intensity',
            'border_thickness', 'margin', 'line_thickness'
        ]
        for k in int_keys:
            if k not in cfg:
                raise ValueError(f"Missing required config '{k}'")
            v = cfg[k]
            if not isinstance(v, int) or v < 0:
                raise ValueError(f"{k} must be non-negative int, got {v}")
        # paper_color: tuple of 3 ints 0-255
        pc = cfg.get('paper_color')
        if (not isinstance(pc, tuple) or len(pc) != 3 or
                any((not isinstance(c, int) or c < 0 or c > 255) for c in pc)):
            raise ValueError(f"paper_color must be tuple of 3 ints 0-255, got {pc}")
        # Margin fits within dimensions
        if cfg['margin'] * 2 >= cfg['height']:
            raise ValueError("margin too large for height")
        if cfg['margin'] * 2 >= cfg['width']:
            raise ValueError("margin too large for width")


class MatteImageBuilder:
    """
    Builds the matte paper image in memory.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base matte-colored canvas
        img = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Subtle horizontal gradient lines
        for y in range(cfg['margin'], h - cfg['margin']):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(
                img,
                (cfg['margin'], y),
                (w - cfg['margin'], y),
                (intensity, intensity, intensity),
                cfg['line_thickness']
            )
        # Light border to mimic scan edge
        edge_color = (220, 220, 220)
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
    Handles saving images and config JSON to disk.
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


class MatteEffect:
    """
    Orchestrates validation, image building, and file I/O for matte paper.
    """

    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.defaults = {
            'width': 2480,  # A4 @300 DPI
            'height': 3508,
            'dpi': 300,
            'gradient_intensity': 15,  # softer for matte feel
            'border_thickness': 8,
            'paper_color': (245, 245, 245),
            'margin': 20,
            'line_thickness': 2,
            'output_file': 'matte.png',
            'output_dir': script_dir,
        }
        # Merge defaults with any overrides
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        cfg = self.config
        # Validate parameters
        MatteConfigValidator.validate(cfg)
        # Build image
        img = MatteImageBuilder.build(cfg)
        # Determine output paths
        img_path = os.path.join(cfg['output_dir'], cfg['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        # Write out
        FileWriter.write_image(img, img_path)
        FileWriter.write_config(cfg, cfg_path)
        print(f"Matte image saved to {img_path}")
        print(f"Configuration saved to {cfg_path}")


def main():
    """
    Default invocation; override in input_params as needed.
    """
    input_params = {
        # 'width': 2480,
        # 'height': 3508,
        # 'dpi': 300,
        # 'gradient_intensity': 15,
        # 'border_thickness': 8,
        # 'paper_color': (245, 245, 245),
        # 'margin': 20,
        # 'line_thickness': 2,
        # 'output_file': 'matte.png',
        # 'output_dir': '.',
    }
    MatteEffect(input_params).generate()


if __name__ == '__main__':
    main()