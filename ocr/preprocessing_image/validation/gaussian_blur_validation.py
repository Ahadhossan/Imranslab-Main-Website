"""
Validate gaussian blur result
"""

import numpy as np
import cv2
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate Gaussian blur by checking that it does not alter image dimensions and type."""
    result = {"step": "gaussian_blur", "status": "", "metrics": {}}
    try:
        # Check image shape and type remain the same
        if output_image.shape == input_image.shape and output_image.dtype == input_image.dtype:
            # Check that the output is actually blurred: compute variance of difference
            diff = cv2.absdiff(input_image, output_image)
            diff_var = float(diff.var())
            result["metrics"]["diff_variance"] = round(diff_var, 2)
            result["status"] = "success"
            logging.info("Gaussian blur validation passed (output shape matches input, diff variance={:.2f}).".format(diff_var))
        else:
            result["status"] = "failure"
            logging.error("Gaussian blur validation failed (output shape/type differs from input).")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Gaussian blur validation exception: {e}")
    return result
