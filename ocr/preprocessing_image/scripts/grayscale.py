import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Convert the input image to grayscale for OCR preprocessing.

    Grayscale Conversion:
        In OCR (Optical Character Recognition) pipelines, converting an image to grayscale 
        is a common preprocessing step. This simplifies the image by removing color information, 
        reducing computational complexity, and making subsequent steps (like thresholding, 
        binarization, or text detection) more accurate and efficient.

    Parameters:
    ----------
    image : np.ndarray
        The input image as a NumPy array. It can be a color image (3 channels) or already a grayscale image (1 channel).

    params : dict
        A dictionary reserved for storing processing parameters and flags.
        (Currently unused in this function but included for interface consistency.)

    Returns:
    -------
    np.ndarray
        The grayscale image if the input was a color image.
        If the input image is already grayscale, returns the original image.

    Raises:
    ------
    ValueError:
        - If the input image is None.
        - If the input is not a NumPy ndarray.

    Notes:
    -----
    - This function checks whether the image has 3 channels (BGR).
    - If yes, it uses OpenCV's `cv2.cvtColor` to convert the image to grayscale.
    - If the image is already in grayscale, it returns the image unchanged.
    - Grayscale conversion ensures uniform input format for later OCR steps.

    Example Usage:
    -------------
    image = cv2.imread("input.jpg")
    params = {}
    gray_image = preprocess(image, params)
    """
    
    if image is None:
        raise ValueError("Input image is None.")

    if not isinstance(image, np.ndarray):
        raise ValueError("Invalid input type. Expected numpy ndarray.")

    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image
    else:
        return image  # Already grayscale
