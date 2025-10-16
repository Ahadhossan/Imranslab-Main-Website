import os
import json
import numpy as np
import cv2
from abc import ABC, abstractmethod


class PaperEffect(ABC):
    """
    Abstract base for all paper effects, enforcing the template for generation.
    """

    def __init__(self, defaults: dict, params: dict, validator, builder, writer):
        # Merge defaults with user-provided overrides
        self.config = {**defaults, **(params or {})}
        self._validator = validator
        self._builder = builder
        self._writer = writer

    def generate(self):
        """
        Template method: validate config, build image, and write outputs.
        """
        # 1. Validate configuration
        self._validator.validate(self.config)
        # 2. Build image in memory
        img = self._builder.build(self.config)
        # 3. Determine output paths
        img_path = os.path.join(self.config['output_dir'], self.config['output_file'])
        cfg_path = os.path.splitext(img_path)[0] + '.json'
        # 4. Write to disk
        self._writer.write_image(img, img_path)
        self._writer.write_config(self.config, cfg_path)
        print(f"Image saved to {img_path}")
        print(f"Config saved to {cfg_path}")


class BaseImageBuilder(ABC):
    """
    Provides shared utilities for image builders, e.g. border addition.
    """

    @staticmethod
    def add_border(img: np.ndarray, thickness: int, color: tuple) -> np.ndarray:
        """
        Adds a constant-color border around the image.
        """
        return cv2.copyMakeBorder(
            img,
            thickness, thickness,
            thickness, thickness,
            cv2.BORDER_CONSTANT,
            value=color
        )


class PulpyConfigValidator:
    """
    Validates configuration parameters for pulpy paper effects.
    """

    @staticmethod
    def validate(cfg: dict):
        required_ints = [
            'width', 'height', 'dpi',
            'speckle_intensity', 'speckle_count',
            'noise_blur_ksize', 'border_thickness'
        ]
        for key in required_ints:
            if key not in cfg:
                raise ValueError(f"Missing required config '{key}'")
            val = cfg[key]
            if not isinstance(val, int) or val < 0:
                raise ValueError(f"{key} must be non-negative int, got {val}")

        # Validate paper_color RGB tuple
        pc = cfg.get('paper_color')
        if (not isinstance(pc, tuple) or len(pc) != 3 or
                any(not isinstance(c, int) or c < 0 or c > 255 for c in pc)):
            raise ValueError(f"paper_color must be tuple of 3 ints 0-255, got {pc}")

        # noise_blur_ksize must be positive odd
        k = cfg['noise_blur_ksize']
        if k <= 0 or k % 2 == 0:
            raise ValueError(f"noise_blur_ksize must be positive odd int, got {k}")


class PulpyImageBuilder(BaseImageBuilder):
    """
    Builds the pulpy paper effect by composing speckles, blur, gradient, and border.
    """

    @classmethod
    def build(cls, cfg: dict) -> np.ndarray:
        img = cls._create_canvas(cfg)
        img = cls._apply_speckles(img, cfg)
        img = cls._apply_blur(img, cfg)
        img = cls._apply_gradient(img, cfg)
        # Add border last for scan effect
        edge_color = (200, 200, 200)
        return cls.add_border(img, cfg['border_thickness'], edge_color)

    @staticmethod
    def _create_canvas(cfg: dict) -> np.ndarray:
        return np.full((cfg['height'], cfg['width'], 3), cfg['paper_color'], dtype=np.uint8)

    @staticmethod
    def _apply_speckles(img: np.ndarray, cfg: dict) -> np.ndarray:
        h, w = img.shape[:2]
        for _ in range(cfg['speckle_count']):
            y = np.random.randint(0, h)
            x = np.random.randint(0, w)
            intensity = np.random.randint(0, cfg['speckle_intensity'])
            cv2.circle(img, (x, y), radius=1, color=(intensity,) * 3, thickness=-1)
        return img

    @staticmethod
    def _apply_blur(img: np.ndarray, cfg: dict) -> np.ndarray:
        k = cfg['noise_blur_ksize']
        return cv2.GaussianBlur(img, (k, k), 0)

    @staticmethod
    def _apply_gradient(img: np.ndarray, cfg: dict) -> np.ndarray:
        h = img.shape[0]
        for i in range(h):
            alpha = 1.0 - (i / h) * 0.1
            img[i] = np.clip(img[i].astype(np.float32) * alpha, 0, 255).astype(np.uint8)
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


class PulpyEffect(PaperEffect):
    """
    Concrete PaperEffect for pulpy paper scans.
    """

    def __init__(self, params=None):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        defaults = {
            'width': 2480,
            'height': 3508,
            'dpi': 300,
            'speckle_intensity': 50,
            'speckle_count': 1000,
            'noise_blur_ksize': 5,
            'border_thickness': 10,
            'paper_color': (230, 230, 220),
            'output_file': 'pulpy.png',
            'output_dir': script_dir,
        }
        super().__init__(defaults, params, PulpyConfigValidator, PulpyImageBuilder, FileWriter)


def main():
    """
    Default invocation; override parameters by editing `input_params`.
    """
    input_params = {
        # 'width': 2480,
        # 'height': 3508,
        # 'dpi': 300,
        # 'speckle_intensity': 50,
        # 'speckle_count': 1000,
        # 'noise_blur_ksize': 5,
        # 'border_thickness': 10,
        # 'paper_color': (230,230,220),
        # 'output_file': 'pulpy.png',
        # 'output_dir': '.',
    }
    PulpyEffect(input_params).generate()


if __name__ == '__main__':
    main()
