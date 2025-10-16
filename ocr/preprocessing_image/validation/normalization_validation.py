"""
Validate normalization result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate normalization step by checking intensity range."""
    result = {"step": "normalization", "status": "", "metrics": {}}
    try:
        out_min = int(output_image.min()) if output_image.size > 0 else None
        out_max = int(output_image.max()) if output_image.size > 0 else None
        result["metrics"]["min_val"] = out_min
        result["metrics"]["max_val"] = out_max
        alpha = params.get("alpha", 0)
        beta = params.get("beta", 255)
        if out_min is not None and out_max is not None and out_min >= alpha and out_max <= beta:
            result["status"] = "success"
            logging.info(f"Normalization validation passed: range = [{out_min}, {out_max}].")
        else:
            result["status"] = "failure"
            logging.error(f"Normalization validation failed: range = [{out_min}, {out_max}] not within [{alpha}, {beta}].")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Normalization validation exception: {e}")
    return result
