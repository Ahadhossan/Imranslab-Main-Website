"""
Validate remove small components result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate small components removal by checking reduction in object count or area."""
    result = {"step": "remove_small_components", "status": "", "metrics": {}}
    try:
        # Assuming dark text on white background
        in_pixels = int(np.sum(input_image == 0))
        out_pixels = int(np.sum(output_image == 0))
        removed_pixels = in_pixels - out_pixels
        result["metrics"]["removed_pixels"] = removed_pixels if removed_pixels > 0 else 0
        if removed_pixels >= 0:
            result["status"] = "success"
            logging.info(f"Remove small components validation passed. Pixels removed: {removed_pixels}.")
        else:
            result["status"] = "failure"
            logging.error(f"Remove small components validation failed. Foreground pixels increased by {abs(removed_pixels)}.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Remove small components validation exception: {e}")
    return result
