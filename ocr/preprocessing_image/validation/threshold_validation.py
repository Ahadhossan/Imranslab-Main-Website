"""
Validate threshold result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate thresholding by checking resulting binary values and ratio of foreground."""
    result = {"step": "threshold", "status": "", "metrics": {}}
    try:
        unique_vals = np.unique(output_image)
        # Check that output is binary (only 0 and 255 values)
        is_binary = all(val in [0, 255] for val in unique_vals)
        if is_binary:
            result["status"] = "success"
            total_pixels = output_image.size
            black_pixels = int(np.sum(output_image == 0))
            percent_black = (black_pixels / total_pixels) * 100 if total_pixels > 0 else 0
            result["metrics"]["black_pixels_percent"] = round(percent_black, 2)
            logging.info(f"Threshold validation passed. Black pixel percentage: {percent_black:.2f}%.")
        else:
            result["status"] = "failure"
            result["metrics"]["unique_values"] = unique_vals.tolist()
            logging.error("Threshold validation failed: output is not binary.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Threshold validation exception: {e}")
    return result
