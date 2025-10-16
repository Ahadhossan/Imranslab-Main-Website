import os
import json
import numpy as np
import cv2


class ConfigValidator:
    """
    Validates publication configuration parameters for logical consistency.
    """

    @staticmethod
    def validate(cfg: dict):
        # Required numeric parameters
        ints = ['width', 'height', 'dpi', 'noise_intensity', 'noise_blur_ksize',
                'header_height', 'footer_height', 'margin_top', 'margin_bottom',
                'margin_left', 'margin_right', 'column_count', 'gutter_width',
                'line_thickness', 'border_thickness', 'gradient_intensity']
        for key in ints:
            val = cfg.get(key)
            if not isinstance(val, int) or val < 0:
                raise ValueError(f"{key} must be non-negative int, got {val}")
        # Paper color tuple of three ints
        pc = cfg.get('paper_color')
        if (not isinstance(pc, tuple) or len(pc) != 3 or
                any((not isinstance(c, int) or c < 0 or c > 255) for c in pc)):
            raise ValueError(f"paper_color must be tuple of 3 ints 0-255, got {pc}")
        # Jitter scale
        js = cfg.get('jitter_scale')
        if not isinstance(js, float) or js < 0.0:
            raise ValueError(f"jitter_scale must be non-negative float, got {js}")
        # Layout constraints: header+footer+vertical margins < height
        total_vert = cfg['margin_top'] + cfg['header_height'] + cfg['footer_height'] + cfg['margin_bottom']
        if total_vert >= cfg['height']:
            raise ValueError("Vertical layout exceeds page height")
        # Columns must fit
        usable_w = cfg['width'] - cfg['margin_left'] - cfg['margin_right']
        min_total_gutter = (cfg['column_count'] - 1) * cfg['gutter_width']
        if cfg['column_count'] <= 0 or usable_w - min_total_gutter <= 0:
            raise ValueError("Columns and gutters do not fit in width")


class ImageBuilder:
    """
    Builds the publication image according to the config without I/O.
    """

    @staticmethod
    def build(cfg: dict) -> np.ndarray:
        h, w = cfg['height'], cfg['width']
        # Base canvas
        canvas = np.full((h, w, 3), cfg['paper_color'], dtype=np.uint8)
        # Scanning gradient
        for y in range(h):
            intensity = 255 - int((y / h) * cfg['gradient_intensity'])
            cv2.line(canvas, (0, y), (w, y), (intensity,) * 3, 1)
        # Noise
        noise = np.zeros_like(canvas)
        cv2.randn(noise, (0,) * 3, (cfg['noise_intensity'],) * 3)
        noise = cv2.GaussianBlur(noise, (cfg['noise_blur_ksize'],) * 2, 0)
        canvas = cv2.add(canvas, noise)
        # Jitter
        jitter = np.random.normal(1.0, cfg['jitter_scale'], (h, w, 3))
        canvas = np.clip(canvas.astype(np.float32) * jitter, 0, 255).astype(np.uint8)
        # Header and footer
        x0, x1 = cfg['margin_left'], w - cfg['margin_right']
        y0 = cfg['margin_top'];
        yh = y0 + cfg['header_height']
        yf = h - cfg['margin_bottom'] - cfg['footer_height'];
        y2 = h - cfg['margin_bottom']
        cv2.rectangle(canvas, (x0, y0), (x1, yh), cfg['line_color'], cfg['line_thickness'])
        cv2.rectangle(canvas, (x0, yf), (x1, y2), cfg['line_color'], cfg['line_thickness'])
        # Columns
        usable_w = w - cfg['margin_left'] - cfg['margin_right']
        col_w = (usable_w - (cfg['column_count'] - 1) * cfg['gutter_width']) // cfg['column_count']
        y_start = yh + cfg['line_thickness']
        y_end = yf - cfg['line_thickness']
        for i in range(1, cfg['column_count']):
            xi = cfg['margin_left'] + i * (col_w + cfg['gutter_width'])
            cv2.line(canvas, (xi, y_start), (xi, y_end), cfg['line_color'], cfg['line_thickness'])
        # Border
        edge = tuple(max(c - 20, 0) for c in cfg['paper_color'])
        canvas = cv2.copyMakeBorder(
            canvas,
            cfg['border_thickness'], cfg['border_thickness'],
            cfg['border_thickness'], cfg['border_thickness'],
            cv2.BORDER_CONSTANT, value=edge
        )
        return canvas


class FileWriter:
    """
    Handles saving images and configs to disk.
    """

    @staticmethod
    def write_image(image: np.ndarray, path: str):
        dirname = os.path.dirname(path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        if not cv2.imwrite(path, image):
            raise IOError(f"Failed to write image to {path}")

    @staticmethod
    def write_config(cfg: dict, path: str):
        dirname = os.path.dirname(path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(path, 'w') as f:
            json.dump(cfg, f, indent=4)


class PublicationEffect:
    """
    Orchestrates validation, image building, and file writing.
    """
    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.defaults = {
            'width': 2480, 'height': 3508, 'dpi': 300,
            'paper_color': (230, 230, 225), 'noise_intensity': 30,
            'noise_blur_ksize': 7, 'jitter_scale': 0.03,
            'gradient_intensity': 20,
            'margin_top': 100, 'margin_bottom': 100,
            'margin_left': 80, 'margin_right': 80,
            'header_height': 250, 'footer_height': 80,
            'column_count': 2, 'gutter_width': 40,
            'line_color': (200, 200, 200), 'line_thickness': 2,
            'border_thickness': 8,
            'output_file': 'publication.png', 'output_dir': script_dir,
        }
        self.config = {**self.defaults, **(params or {})}

    def generate(self):
        # Validate
        ConfigValidator.validate(self.config)
        # Build image
        img = ImageBuilder.build(self.config)
        # Write outputs
        img_path = os.path.join(self.config['output_dir'], self.config['output_file'])
        FileWriter.write_image(img, img_path)
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        FileWriter.write_config(self.config, cfg_path)
        print(f"Saved image: {img_path}")
        print(f"Saved config: {cfg_path}")


def main():
    """
    Default invocation; override in input_params dict as needed.
    """
    input_params = {
        # 'column_count': 3,
        # 'noise_intensity': 40,
        # 'output_dir': '.',
        # etc.
    }
    PublicationEffect(input_params).generate()


if __name__ == '__main__':
    main()
