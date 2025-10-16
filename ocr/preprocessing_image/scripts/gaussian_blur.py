import cv2
import numpy as np
import logging
def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    try:
        ksize = params.get("ksize", 5)
        if ksize % 2 == 0:
            ksize += 1  
        sigma = params.get("sigma", 0)
        if not isinstance(sigma, (int, float)):
            raise ValueError("Sigma must be a numeric value.")
        blurred = cv2.GaussianBlur(image, (ksize, ksize), sigma)
        logging.info(f"Applied Gaussian blur with ksize={ksize}, sigma={sigma}.")
        return blurred
    except Exception as e:
        logging.error(f"Gaussian blur preprocessing failed: {e}")
        raise