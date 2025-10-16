import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Normalize image intensity to 0-255 range using min-max normalization.

    This function performs **min-max normalization** on the input image, which scales the pixel values to a specified range (default is 0 to 255). 
    The normalization is done using a linear transformation, adjusting the pixel values based on the minimum and maximum intensity values in the image.

    Args:
        image (np.ndarray): The input image to be normalized. It can be a grayscale or color image.
        params (dict): A dictionary containing configuration parameters for the normalization process:
            - 'norm_type' (int): The normalization type. Default is `cv2.NORM_MINMAX`, which normalizes the image intensity to the specified range.
            - 'alpha' (int): The lower bound of the normalization range (default is 0).
            - 'beta' (int): The upper bound of the normalization range (default is 255).

    Returns:
        np.ndarray: The normalized image with pixel values scaled to the specified range.

    Logging:
        - Logs an info message with the normalization range applied.
        - Logs an error message if an exception occurs during the normalization process.

    Example:
        normalized_image = preprocess(input_image, params)
        print(normalized_image)
    """
    try:
        # Create an empty image with the same shape as the input image for storing the result
        norm_img = np.zeros_like(image)
        
        # Extract parameters for normalization
        norm_type = params.get("norm_type", cv2.NORM_MINMAX)
        alpha = params.get("alpha", 0)   # lower range value
        beta = params.get("beta", 255)   # upper range value
        
        # Perform normalization
        normalized = cv2.normalize(image, norm_img, alpha, beta, norm_type)
        
        # Log the normalization range
        logging.info(f"Normalized image intensities to range [{alpha}, {beta}].")
        
        return normalized
    except Exception as e:
        logging.error(f"Normalization preprocessing failed: {e}")
        raise
