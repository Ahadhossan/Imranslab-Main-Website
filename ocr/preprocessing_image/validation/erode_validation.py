"""
Validate erode result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate erosion by ensuring foreground area did not increase."""
    result = {"step": "erode", "status": "", "metrics": {}}
    try:
        target = params.get("target", "dark").lower()
        if target == "dark":
            in_foreground = int(np.sum(input_image == 0))
            out_foreground = int(np.sum(output_image == 0))
        else:
            in_foreground = int(np.sum(input_image == 255))
            out_foreground = int(np.sum(output_image == 255))
        removed = in_foreground - out_foreground
        result["metrics"]["removed_pixels"] = removed if removed > 0 else 0
        if removed >= 0:
            result["status"] = "success"
            logging.info(f"Erosion validation passed. Foreground pixels removed: {removed}.")
        else:
            result["status"] = "failure"
            logging.error(f"Erosion validation failed. Foreground pixels increased by {abs(removed)}.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Erosion validation exception: {e}")
    return result
