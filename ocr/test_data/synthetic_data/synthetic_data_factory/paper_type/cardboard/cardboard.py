import os
import json
from dataclasses import dataclass, asdict
import cv2
import numpy as np


@dataclass(frozen=True)
class CardboardConfig:
    """
    Configuration for generating a cardboard-style paper effect.
    """
    width: int = 2480  # 8.27 inches at 300 DPI (A4)
    height: int = 3508  # 11.69 inches at 300 DPI (A4)
    dpi: int = 300
    noise_intensity: int = 10  # Gaussian noise level
    stripe_spacing: int = 15  # Vertical spacing between corrugation lines
    stripe_thickness: int = 3  # Thickness of each stripe
    border_thickness: int = 10  # Thickness of the border
    paper_color: tuple = (195, 155, 100)  # RGB cardboard base tone
    margin: int = 20  # Margin around edges
    output_file: str = 'cardboard.png'
    output_dir: str = '.'  # Directory to save outputs (default: current directory)


class CardboardEffect:
    """
    Applies a corrugated cardboard paper effect based on CardboardConfig.
    """

    def __init__(self, config: CardboardConfig):
        self.config = config
        # Ensure output directory exists
        os.makedirs(self.config.output_dir, exist_ok=True)

    def generate(self):
        """
        Orchestrates creation, texturing, border application, and saving.
        """
        canvas = self._create_base_canvas()
        textured = self._apply_noise(canvas)
        final = self._apply_border(textured)
        self._save(final)

    def _create_base_canvas(self) -> np.ndarray:
        """
        Creates the raw cardboard canvas and draws corrugation stripes.
        """
        cfg = self.config
        canvas = np.full((cfg.height, cfg.width, 3), cfg.paper_color, dtype=np.uint8)
        stripe_color = tuple(max(c - 20, 0) for c in cfg.paper_color)
        for y in range(cfg.margin, cfg.height - cfg.margin, cfg.stripe_spacing):
            cv2.line(
                canvas,
                (cfg.margin, y),
                (cfg.width - cfg.margin, y),
                stripe_color,
                cfg.stripe_thickness
            )
        return canvas

    def _apply_noise(self, canvas: np.ndarray) -> np.ndarray:
        """
        Adds Gaussian noise for texture.
        """
        cfg = self.config
        noise = np.zeros_like(canvas)
        cv2.randn(noise, (0, 0, 0), (cfg.noise_intensity,) * 3)
        return cv2.add(canvas, noise)

    def _apply_border(self, image: np.ndarray) -> np.ndarray:
        """
        Adds a solid border to simulate cardboard edges.
        """
        cfg = self.config
        border_color = tuple(max(c - 35, 0) for c in cfg.paper_color)
        return cv2.copyMakeBorder(
            image,
            cfg.border_thickness, cfg.border_thickness,
            cfg.border_thickness, cfg.border_thickness,
            cv2.BORDER_CONSTANT,
            value=border_color
        )

    def _save(self, image: np.ndarray):
        """
        Saves the final image and configuration JSON to disk.
        """
        cfg = self.config
        image_path = os.path.join(cfg.output_dir, cfg.output_file)
        cv2.imwrite(image_path, image)
        print(f"Cardboard effect image saved to {image_path}")
        # Write JSON config
        json_path = os.path.join(
            cfg.output_dir,
            os.path.splitext(cfg.output_file)[0] + '.json'
        )
        with open(json_path, 'w') as f:
            json.dump(asdict(cfg), f, indent=4)
        print(f"Configuration saved to {json_path}")


def main():
    """
    Default invocation; override any keys by uncommenting below.
    """
    input_params = {
        # 'width': 2480,
        # 'height': 3508,
        # 'dpi': 300,
        # 'noise_intensity': 10,
        # 'stripe_spacing': 15,
        # 'stripe_thickness': 3,
        # 'border_thickness': 10,
        # 'paper_color': (195, 155, 100),
        # 'margin': 20,
        # 'output_file': 'cardboard.png',
        # 'output_dir': '.',  # default: current directory
    }
    # Apply only valid config fields
    cfg_kwargs = {k: v for k, v in input_params.items() if k in CardboardConfig.__annotations__}
    config = CardboardConfig(**cfg_kwargs)
    effect = CardboardEffect(config)
    effect.generate()


if __name__ == '__main__':
    main()
