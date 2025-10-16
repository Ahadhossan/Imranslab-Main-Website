"""
Validate sharpen result
"""

import numpy as np
import cv2
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate sharpening by checking if edge variance increased."""
    result = {"step": "sharpen", "status": "", "metrics": {}}
    try:
        in_sharpness = float(cv2.Laplacian(input_image, cv2.CV_64F).var())
        out_sharpness = float(cv2.Laplacian(output_image, cv2.CV_64F).var())
        result["metrics"]["input_sharpness"] = round(in_sharpness, 2)
        result["metrics"]["output_sharpness"] = round(out_sharpness, 2)
        if out_sharpness >= in_sharpness:
            result["status"] = "success"
            logging.info("Sharpening validation passed. Sharpness increased or maintained.")
        else:
            result["status"] = "failure"
            logging.error("Sharpening validation failed. Output appears less sharp than input.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Sharpening validation exception: {e}")
    return result
