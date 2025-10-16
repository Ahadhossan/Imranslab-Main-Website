import os
import json
import numpy as np
import cv2


class PapyrusConfigValidator:
    """
    Validates configuration parameters for a scanned papyrus effect.
    """

    @staticmethod
    def validate(cfg: dict):
        # Required integer parameters
        required_ints = [
            'width', 'height', 'dpi',
            'gradient_intensity', 'border_thickness',
            'margin', 'line_thickness',
            'fiber_count', 'fiber_thickness'
        ]
        for key in required_ints:
            if key not in cfg:
                raise ValueError(f"Missing required config '{key}'")
            val = cfg[key]
            if not isinstance(val, int) or val < 0:
                raise ValueError(f"{key} must be non-negative int, got {val}")

        # Color tuples: paper_color and fiber_color
        for ck in ('paper_color', 'fiber_color'):
            pc = cfg.get(ck)
            if (not isinstance(pc, tuple) or len(pc) != 3 or
                    any((not isinstance(c, int) or c < 0 or c > 255) for c in pc)):
                raise ValueError(f"{ck} must be tuple of 3 ints 0-255, got {pc}")

        # Margins must fit within dimensions
        if cfg['margin'] * 2 >= cfg['width']:
            raise ValueError("margin too large for width")
        if cfg['margin'] * 2 >= cfg['height']:
            raise ValueError("margin too large for height")


class PapyrusImageBuilder:
    """
    Builds the papyrus scanned effect image in memory.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base papyrus tone
        img = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Apply vertical gradient scan lines
        for y in range(cfg['margin'], h - cfg['margin']):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(img,
                     (cfg['margin'], y), (w - cfg['margin'], y),
                     (intensity, intensity, intensity),
                     cfg['line_thickness'])
        # Simulate papyrus fibers as random vertical streaks
        for _ in range(cfg['fiber_count']):
            x = np.random.randint(cfg['margin'], w - cfg['margin'])
            cv2.line(img,
                     (x, cfg['margin']), (x, h - cfg['margin']),
                     cfg['fiber_color'],
                     cfg['fiber_thickness'])
        # Add border to simulate scanned edge
        edge = (200, 180, 140)
        img = cv2.copyMakeBorder(
            img,
            cfg['border_thickness'], cfg['border_thickness'],
            cfg['border_thickness'], cfg['border_thickness'],
            cv2.BORDER_CONSTANT,
            value=edge
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


class PapyrusEffect:
    """
    Orchestrates config validation, image building, and file I/O for papyrus.
    """

    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Defaults for A4-size papyrus sheet scan
        self.defaults = {
            'width': 2480,  # A4 @300 DPI
            'height': 3508,
            'dpi': 300,
            'gradient_intensity': 30,
            'border_thickness': 10,
            'paper_color': (210, 180, 140),  # light papyrus tone
            'margin': 20,
            'line_thickness': 1,
            'fiber_count': 200,
            'fiber_thickness': 1,
            'fiber_color': (160, 120, 60),  # darker fiber tone
            'output_file': 'papyrus.png',
            'output_dir': script_dir,
        }
        # Merge with user overrides
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        cfg = self.config
        PapyrusConfigValidator.validate(cfg)
        img = PapyrusImageBuilder.build(cfg)
        img_path = os.path.join(cfg['output_dir'], cfg['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        FileWriter.write_image(img, img_path)
        FileWriter.write_config(cfg, cfg_path)
        print(f"Image saved to {img_path}")
        print(f"Config saved to {cfg_path}")


def main():
    """
    Default invocation; override parameters in input_params as needed.
    """
    input_params = {
        # 'width': 2480,
        # 'height': 3508,
        # 'dpi': 300,
        # 'gradient_intensity': 30,
        # 'border_thickness': 10,
        # 'paper_color': (210,180,140),
        # 'margin': 20,
        # 'line_thickness': 1,
        # 'fiber_count': 200,
        # 'fiber_thickness': 1,
        # 'fiber_color': (160,120,60),
        # 'output_file': 'papyrus.png',
        # 'output_dir': '.',
    }
    PapyrusEffect(input_params).generate()


if __name__ == '__main__':
    main()
