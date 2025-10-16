import os
import json
import numpy as np
import cv2


class GlossyConfigValidator:
    """
    Validates configuration for glossy paper effect.
    """

    @staticmethod
    def validate(cfg: dict):
        # Required integer parameters >= 0
        int_keys = ['width', 'height', 'dpi', 'gradient_intensity',
                    'border_thickness', 'margin', 'line_thickness']
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
        # Margins must fit inside height
        if cfg['margin'] * 2 >= cfg['height']:
            raise ValueError("margin too large for height")
        # Margins must fit inside width
        if cfg['margin'] * 2 >= cfg['width']:
            raise ValueError("margin too large for width")


class GlossyImageBuilder:
    """
    Builds the glossy paper image in memory.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base white canvas
        img = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Gradient scan lines
        for y in range(cfg['margin'], h - cfg['margin']):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(img,
                     (cfg['margin'], y),
                     (w - cfg['margin'], y),
                     (intensity,) * 3,
                     cfg['line_thickness'])
        # Border to simulate scanner edges
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
    Handles saving image and config json.
    """

    @staticmethod
    def write_image(img: np.ndarray, path: str):
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        if not cv2.imwrite(path, img):
            raise IOError(f"Failed to write image to {path}")

    @staticmethod
    def write_config(cfg: dict, path: str):
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        with open(path, 'w') as f:
            json.dump(cfg, f, indent=4)


class GlossyEffect:
    """
    Orchestrates config validation, image building, and writing for glossy paper.
    """

    def __init__(self, params=None):
        # Defaults
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.defaults = {
            'width': 2480,  # A4 @300 DPI
            'height': 3508,
            'dpi': 300,
            'gradient_intensity': 30,
            'border_thickness': 10,
            'paper_color': (255, 255, 255),
            'margin': 20,
            'line_thickness': 1,
            'output_file': 'glossy.png',
            'output_dir': script_dir,
        }
        # Merge overrides
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        cfg = self.config
        # Validate parameters
        GlossyConfigValidator.validate(cfg)
        # Build image
        img = GlossyImageBuilder.build(cfg)
        # Paths
        img_path = os.path.join(cfg['output_dir'], cfg['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        # Write outputs
        FileWriter.write_image(img, img_path)
        FileWriter.write_config(cfg, cfg_path)
        print(f"Image saved to {img_path}")
        print(f"Config saved to {cfg_path}")


def main():
    """
    Default invocation; override in input_params as needed.
    """
    params = {
        # 'width': 2480,
        # 'height': 3508,
        # 'dpi': 300,
        # 'gradient_intensity': 30,
        # 'border_thickness': 10,
        # 'paper_color': (255, 255, 255),
        # 'margin': 20,
        # 'line_thickness': 1,
        # 'output_file': 'glossy.png',
        'output_dir': '.',
    }
    GlossyEffect(params).generate()


if __name__ == '__main__':
    main()
