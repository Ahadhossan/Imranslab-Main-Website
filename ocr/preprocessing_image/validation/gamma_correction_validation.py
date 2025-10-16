"""
Validate gamma correction result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate gamma correction by checking average brightness change."""
    result = {"step": "gamma_correction", "status": "", "metrics": {}}
    try:
        in_mean = float(input_image.mean())
        out_mean = float(output_image.mean())
        result["metrics"]["input_mean"] = round(in_mean, 2)
        result["metrics"]["output_mean"] = round(out_mean, 2)
        gamma = params.get("gamma", 1.0)
        # If gamma > 1, output should be darker (mean intensity lower or equal); if gamma < 1, output should be brighter (mean higher or equal)
        if (gamma > 1 and out_mean <= in_mean) or (gamma < 1 and out_mean >= in_mean) or (gamma == 1):
            result["status"] = "success"
            logging.info("Gamma correction validation passed (mean intensity changed as expected).")
        else:
            result["status"] = "failure"
            logging.error("Gamma correction validation failed (mean intensity change not as expected).")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Gamma correction validation exception: {e}")
    return result
