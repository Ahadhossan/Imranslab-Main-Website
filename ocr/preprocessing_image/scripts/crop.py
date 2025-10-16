import cv2
import numpy as np
import logging

"""
Crop image to the specified rectangle.

This is used in OCR preprocessing to isolate text regions.
If crop parameters are missing, it will attempt to crop the full image.
Invalid crop dimensions will raise errors.
"""

import numpy as np


def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Crop the input image based on given parameters.

    Parameters:
        image (np.ndarray): The input image (grayscale or RGB).
        params (dict): Dictionary with keys 'x', 'y', 'width', 'height'

    Returns:
        np.ndarray: Cropped image region.
    """

    if not isinstance(image, np.ndarray) or image.size == 0:
        raise ValueError("Invalid or empty image provided.")

    try:
        x = int(params.get("x", 0))
        y = int(params.get("y", 0))
        width = int(params.get("width", image.shape[1] - x))
        height = int(params.get("height", image.shape[0] - y))
    except (TypeError, ValueError):
        raise ValueError("Crop parameters must be convertible to int.")

    if x < 0 or y < 0:
        raise ValueError("Crop coordinates must be non-negative.")
    if width <= 0 or height <= 0:
        raise ValueError("Crop size must be positive.")

    max_h, max_w = image.shape[:2]
    x_end = min(x + width, max_w)
    y_end = min(y + height, max_h)

    return image[y:y_end, x:x_end]
