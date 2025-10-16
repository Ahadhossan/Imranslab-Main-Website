import os
import json
import numpy as np
import cv2


class NotebookConfigValidator:
    """
    Validates configuration for a scanned notebook paper effect.
    """

    @staticmethod
    def validate(cfg: dict):
        # Required integer parameters
        int_keys = [
            'width', 'height', 'dpi',
            'gradient_intensity', 'border_thickness',
            'margin', 'line_thickness',
            'ruled_line_spacing', 'ruled_line_thickness',
            'margin_line_offset', 'margin_line_thickness'
        ]
        for k in int_keys:
            if k not in cfg:
                raise ValueError(f"Missing required config '{k}'")
            v = cfg[k]
            if not isinstance(v, int) or v < 0:
                raise ValueError(f"{k} must be non-negative int, got {v}")
        # Color tuples: paper_color, ruled_line_color, margin_line_color
        color_keys = ['paper_color', 'ruled_line_color', 'margin_line_color']
        for ck in color_keys:
            pc = cfg.get(ck)
            if (not isinstance(pc, tuple) or len(pc) != 3 or
                    any((not isinstance(c, int) or c < 0 or c > 255) for c in pc)):
                raise ValueError(f"{ck} must be tuple of 3 ints 0-255, got {pc}")
        # Dimensions vs margins
        if cfg['margin'] * 2 >= cfg['height']:
            raise ValueError("margin too large for height")
        if cfg['margin'] * 2 >= cfg['width']:
            raise ValueError("margin too large for width")
        if cfg['margin_line_offset'] >= cfg['width']:
            raise ValueError("margin_line_offset must be < width")


class NotebookImageBuilder:
    """
    Builds the notebook paper scan effect in memory.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base canvas
        img = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Scanning gradient lines
        for y in range(cfg['margin'], h - cfg['margin']):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(img,
                     (0, y), (w, y),
                     (intensity,) * 3,
                     cfg['line_thickness'])
        # Draw ruled horizontal lines
        for y in range(cfg['margin'], h - cfg['margin'], cfg['ruled_line_spacing']):
            cv2.line(img,
                     (0, y), (w, y),
                     cfg['ruled_line_color'],
                     cfg['ruled_line_thickness'])
        # Draw red margin line
        x0 = cfg['margin_line_offset']
        cv2.line(img,
                 (x0, 0), (x0, h),
                 cfg['margin_line_color'],
                 cfg['margin_line_thickness'])
        # Add border to simulate scan edge
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
    Handles saving images and config JSON.
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


class NotebookEffect:
    """
    Orchestrates notebook config validation, image building, and file I/O.
    """

    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.defaults = {
            'width': 2480,  # A4 @300 DPI
            'height': 3508,
            'dpi': 300,
            'gradient_intensity': 20,
            'border_thickness': 10,
            'paper_color': (255, 255, 255),  # white notebook paper
            'margin': 50,
            'line_thickness': 1,
            'ruled_line_spacing': 80,  # px between lines
            'ruled_line_thickness': 2,
            'ruled_line_color': (200, 200, 255),  # light blue
            'margin_line_offset': 200,
            'margin_line_thickness': 3,
            'margin_line_color': (255, 0, 0),  # red margin line
            'output_file': 'notebook.png',
            'output_dir': script_dir,
        }
        # Merge user overrides
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        cfg = self.config
        NotebookConfigValidator.validate(cfg)
        img = NotebookImageBuilder.build(cfg)
        img_path = os.path.join(cfg['output_dir'], cfg['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        FileWriter.write_image(img, img_path)
        FileWriter.write_config(cfg, cfg_path)
        print(f"Image saved to {img_path}")
        print(f"Config saved to {cfg_path}")


def main():
    """
    Default invocation; override in input_params as needed.
    """
    input_params = {
        # 'width': 2480,
        # 'height': 3508,
        # 'dpi': 300,
        # 'gradient_intensity': 20,
        # 'border_thickness': 10,
        # 'paper_color': (255,255,255),
        # 'margin': 50,
        # 'line_thickness': 1,
        # 'ruled_line_spacing': 80,
        # 'ruled_line_thickness': 2,
        # 'ruled_line_color': (200,200,255),
        # 'margin_line_offset': 200,
        # 'margin_line_thickness': 3,
        # 'margin_line_color': (255,0,0),
        # 'output_file': 'notebook.png',
        # 'output_dir': '.',
    }
    NotebookEffect(input_params).generate()


if __name__ == '__main__':
    main()
