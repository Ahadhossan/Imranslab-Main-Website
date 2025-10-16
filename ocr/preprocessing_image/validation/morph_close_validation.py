import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate morphological closing by checking if gaps are filled (foreground pixels added or same)."""
    result = {"step": "morph_close", "status": "", "metrics": {}}
    try:
        target = params.get("target", "dark").lower()
        if target == "dark":
            in_foreground = int(np.sum(input_image == 0))
            out_foreground = int(np.sum(output_image == 0))
        else:
            in_foreground = int(np.sum(input_image == 255))
            out_foreground = int(np.sum(output_image == 255))
        added = out_foreground - in_foreground
        result["metrics"]["added_pixels"] = added if added > 0 else 0  # Change from 'filled_holes' to 'added_pixels'
        if added >= 0:
            result["status"] = "success"
            logging.info(f"Morphological close validation passed. Foreground pixels added: {added}.")
        else:
            result["status"] = "failure"
            logging.error(f"Morphological close validation failed. Foreground pixels decreased by {abs(added)}.")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Morphological close validation exception: {e}")
    return result
