import cv2
import numpy as np
import logging
def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("Input must be a numpy array.")
        if image.shape[-1] == 4:
            bgr = cv2.bitwise_not(image[..., :3])
            alpha = image[..., 3]
            return np.dstack((bgr, alpha))
        else:
            return cv2.bitwise_not(image)
    except Exception as e:
        logging.error(f"Invert preprocessing failed: {e}")
        raise