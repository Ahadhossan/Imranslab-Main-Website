"""
Validate nlmeans denoise result
"""

import numpy as np
import cv2
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate NLMeans denoising by checking if high-frequency noise is reduced."""
    result = {"step": "nlmeans_denoise", "status": "", "metrics": {}}
    try:
        in_var = float(cv2.Laplacian(input_image, cv2.CV_64F).var())
        out_var = float(cv2.Laplacian(output_image, cv2.CV_64F).var())
        result["metrics"]["laplacian_var_before"] = round(in_var, 2)
        result["metrics"]["laplacian_var_after"] = round(out_var, 2)
        if out_var <= in_var:
            result["status"] = "success"
            logging.info("NLMeans denoising validation passed (Laplacian variance reduced).")
        else:
            result["status"] = "failure"
            logging.error("NLMeans denoising validation failed (Laplacian variance increased).")
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"NLMeans denoising validation exception: {e}")
    return result
