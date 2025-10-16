"""
Validate grayscale result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate grayscale conversion step."""
    result = {"step": "grayscale", "status": "", "metrics": {}}
    try:
        # Check that output image has one channel
        if output_image.ndim == 2 or (output_image.ndim == 3 and output_image.shape[2] == 1):
            result["status"] = "success"
            result["metrics"]["channels"] = 1
            logging.info("Grayscale validation passed: output is single-channel.")
        else:
            result["status"] = "failure"
            result["metrics"]["channels"] = output_image.shape[2] if output_image.ndim == 3 else output_image.ndim
            logging.error("Grayscale validation failed: output image is not single-channel.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Grayscale validation exception: {e}")
    return result