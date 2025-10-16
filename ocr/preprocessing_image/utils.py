import os
import cv2
import yaml
import logging

def load_config(config_path: str) -> dict:
    """Load YAML configuration file."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def save_image(image, path: str) -> None:
    """Save an image to disk."""
    try:
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        cv2.imwrite(path, image)
        logging.debug(f"Image saved to {path}")
    except Exception as e:
        logging.error(f"Failed to save image {path}: {e}")

def update_result_yaml(results: dict, path: str) -> None:
    """Write the results dictionary to a YAML file."""
    try:
        with open(path, 'w') as f:
            yaml.safe_dump(results, f, sort_keys=False)
        logging.info(f"Results YAML saved to {path}")
    except Exception as e:
        logging.error(f"Failed to write result YAML: {e}")
