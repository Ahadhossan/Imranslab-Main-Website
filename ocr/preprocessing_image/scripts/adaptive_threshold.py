import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Binarize the image using adaptive thresholding.

    This function applies **adaptive thresholding** to the input image, which dynamically determines a threshold for each pixel based on its neighborhood. 
    It is particularly useful for images with varying lighting conditions. The thresholding method can be either **mean** or **Gaussian**.

    Args:
        image (np.ndarray): The input image to be binarized. It can be grayscale or color. If the image is in color, it will be converted to grayscale.
        params (dict): A dictionary containing configuration parameters for the adaptive thresholding process:
            - 'method' (str): The thresholding method to use. Can be "mean" or "gaussian" (default is "gaussian").
            - 'block_size' (int): The size of the neighborhood around each pixel to calculate the threshold (default is 11).
            - 'C' (int): A constant subtracted from the calculated threshold (default is 2).

    Returns:
        np.ndarray: The binarized image, where pixel values are either 0 (black) or 255 (white).

    Logging:
        - Logs an info message with the thresholding method, block size, and constant used.
        - Logs an error message if an exception occurs during the thresholding process.

    Example:
        binary_image = preprocess(input_image, params)
        print(binary_image)
    """

    try:
        # Ensure image is not empty
        if image.size == 0:
            raise ValueError("Input image is empty.")

        gray = image
        # Ensure grayscale input
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Get the thresholding method and parameters
        method = params.get("method", "gaussian").lower()
        block_size = params.get("block_size", 11)
        C = params.get("C", 2)

        # Ensure block_size is odd
        if block_size % 2 == 0:
            block_size += 1  # block_size must be odd

        # Choose the adaptive thresholding method
        if method == "mean":
            thresh_method = cv2.ADAPTIVE_THRESH_MEAN_C
        elif method == "gaussian":
            thresh_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        else:
            raise ValueError(f"Invalid thresholding method: {method}")

        # Apply adaptive thresholding
        binary = cv2.adaptiveThreshold(gray, 255, thresh_method, cv2.THRESH_BINARY, block_size, C)
        
        # Log the applied parameters
        logging.info(f"Applied adaptive thresholding (method={method}, block_size={block_size}, C={C}).")
        
        return binary
    except Exception as e:
        logging.error(f"Adaptive threshold preprocessing failed: {e}")
        raise