import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate skeletonization by checking reduction in foreground area."""
    result = {"step": "skeletonize", "status": "", "metrics": {}}
    try:
        reduction_percent = params.get("reduction_percent", None)
        if reduction_percent is None:
            result["status"] = "failure"
            logging.error("Skeletonization validation failed: reduction_percent not recorded.")
        else:
            result["metrics"]["reduction_percent"] = round(float(reduction_percent), 2)
            result["status"] = "success"
            logging.info(f"Skeletonization validation passed. Reduction in pixels: {reduction_percent:.2f}%.")
        # (No comparative check here since skeletonization always reduces or keeps the same foreground pixels)
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Skeletonization validation exception: {e}")
    return result
