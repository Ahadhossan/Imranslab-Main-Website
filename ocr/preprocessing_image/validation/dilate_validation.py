"""
Validate dilate result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate dilation by ensuring foreground area did not decrease."""
    result = {"step": "dilate", "status": "", "metrics": {}}
    try:
        target = params.get("target", "dark").lower()
        if target == "dark":
            in_foreground = int(np.sum(input_image == 0))
            out_foreground = int(np.sum(output_image == 0))
        else:
            in_foreground = int(np.sum(input_image == 255))
            out_foreground = int(np.sum(output_image == 255))
        added = out_foreground - in_foreground
        result["metrics"]["added_pixels"] = added if added > 0 else 0
        if added >= 0:
            result["status"] = "success"
            logging.info(f"Dilation validation passed. Foreground pixels added: {added}.")
        else:
            result["status"] = "failure"
            logging.error(f"Dilation validation failed. Foreground pixels decreased by {abs(added)}.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Dilation validation exception: {e}")
    return result
