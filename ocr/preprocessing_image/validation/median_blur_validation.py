"""
Validate median blur result
"""

import numpy as np
import cv2
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate median blur by checking that it does not alter image dimensions and type."""
    result = {"step": "median_blur", "status": "", "metrics": {}}
    try:
        if output_image.shape == input_image.shape and output_image.dtype == input_image.dtype:
            diff = cv2.absdiff(input_image, output_image)
            diff_var = float(diff.var())
            result["metrics"]["diff_variance"] = round(diff_var, 2)
            result["status"] = "success"
            logging.info("Median blur validation passed (output shape matches input, diff variance={:.2f}).".format(diff_var))
        else:
            result["status"] = "failure"
            logging.error("Median blur validation failed (output shape/type differs from input).")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Median blur validation exception: {e}")
    return result
