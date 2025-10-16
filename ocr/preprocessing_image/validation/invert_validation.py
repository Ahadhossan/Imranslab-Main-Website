"""
Validate invert result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate inversion by checking pixel values are complements (255 - original)."""
    result = {"step": "invert", "status": "", "metrics": {}}
    try:
        if input_image.shape == output_image.shape:
            diff = (255 - input_image) - output_image
            if np.all(diff == 0):
                result["status"] = "success"
                logging.info("Invert validation passed: output is exact inversion of input.")
            else:
                result["status"] = "failure"
                logging.error("Invert validation failed: output is not the exact inverse of input.")
        else:
            result["status"] = "failure"
            logging.error("Invert validation failed: input and output shapes differ.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Invert validation exception: {e}")
    return result
