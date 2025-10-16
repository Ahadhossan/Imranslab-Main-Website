"""
Validate resize result
"""

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """Validate resizing by checking new dimensions against target and original."""
    result = {"step": "resize", "status": "", "metrics": {}}
    try:
        resized_flag = params.get("resized", False)
        new_w = params.get("new_width", output_image.shape[1])
        new_h = params.get("new_height", output_image.shape[0])
        result["metrics"]["new_width"] = new_w
        result["metrics"]["new_height"] = new_h
        if resized_flag:
            # If resized, ensure output dimensions match expected
            if output_image.shape[1] == new_w and output_image.shape[0] == new_h:
                result["status"] = "success"
                logging.info("Resize validation passed. Image dimensions updated correctly.")
            else:
                result["status"] = "failure"
                logging.error("Resize validation failed: output dimensions do not match expected.")
        else:
            # Not resized, so output dims should equal input dims
            if output_image.shape == input_image.shape:
                result["status"] = "success"
                logging.info("Resize validation passed. Image size unchanged as expected.")
            else:
                result["status"] = "failure"
                logging.error("Resize validation failed: image was resized when it shouldn't have been.")
        # Clean up transient params
        if "resized" in params:
            params.pop("resized", None)
            params.pop("new_width", None)
            params.pop("new_height", None)
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Resize validation exception: {e}")
    return result
