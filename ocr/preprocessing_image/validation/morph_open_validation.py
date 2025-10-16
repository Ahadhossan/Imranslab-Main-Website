import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate morphological opening by checking if small objects are removed."""
    result = {"step": "morph_open", "status": "", "metrics": {}}
    try:
        target = params.get("target", "dark").lower()
        if target == "dark":
            # dark text (black) on white background
            in_foreground = int(np.sum(input_image == 0))
            out_foreground = int(np.sum(output_image == 0))
        else:
            # light text (white) on black background
            in_foreground = int(np.sum(input_image == 255))
            out_foreground = int(np.sum(output_image == 255))
        
        removed = in_foreground - out_foreground
        result["metrics"]["removed_pixels"] = removed if removed > 0 else 0
        if removed >= 0:
            result["status"] = "success"
            logging.info(f"Morphological open validation passed. Foreground pixels removed: {removed}.")
        else:
            result["status"] = "failure"
            logging.error(f"Morphological open validation failed. Foreground pixels increased by {abs(removed)}.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Morphological open validation exception: {e}")
    return result
