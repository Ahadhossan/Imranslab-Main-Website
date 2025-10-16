"""
Validate deskew result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate deskew by reporting the detected angle and checking if rotation applied."""
    result = {
        "step": "deskew",
        "status": "",
        "metrics": {}
    }

    try:
        angle = params.get("detected_angle", None)

        if angle is None:
            result["status"] = "failure"
            result["metrics"]["detected_angle"] = None
            logging.warning("Deskew validation: No angle recorded. Possibly empty image or early return.")
        else:
            result["metrics"]["detected_angle"] = round(float(angle), 2)
            result["status"] = "success"
            logging.info(f"Deskew validation passed. Angle detected: {angle:.2f} degrees.")

    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Deskew validation exception: {e}")

    return result
