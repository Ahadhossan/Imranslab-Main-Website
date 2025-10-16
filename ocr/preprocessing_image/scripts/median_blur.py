import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Apply median blur to the image for salt-and-pepper noise removal.

    This function applies a **median blur** to the input image, which is a non-linear filter used to remove salt-and-pepper noise (random white and black pixels) from an image. The median filter replaces each pixel's value with the median value of the pixels in the kernel window, making it effective for noise removal while preserving edges.

    Args:
        image (np.ndarray): The input image to be processed. It can be a grayscale or color image.
        params (dict): A dictionary containing configuration parameters for the median blur:
            - 'ksize' (int): The size of the kernel (window) used for the blur. It must be an odd number (default is 5).

    Returns:
        np.ndarray: The image after median blur is applied, with reduced salt-and-pepper noise.

    Logging:
        - Logs an info message with the kernel size applied for the median blur.
        - Logs an error message if an exception occurs during the median blur process.

    Example:
        denoised_image = preprocess(input_image, params)
        print(denoised_image)
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array.")
    try:       
        ksize = params.get("ksize", 5)
        if image.size == 0:
            return image
        if not isinstance(ksize, int):
            raise ValueError("Kernel size must be an integer.")
        if ksize % 2 == 0:
            ksize += 1  
        blurred = cv2.medianBlur(image, ksize)
        logging.info(f"Applied median blur with ksize={ksize}.")
        return blurred
    except Exception as e:
        logging.error(f"Median blur preprocessing failed: {e}")
        raise