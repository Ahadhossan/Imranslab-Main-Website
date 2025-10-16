import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Sharpen the image using an enhancement filter.

    This function applies a **sharpening filter** (high-pass filter) to the input image. The filter enhances the edges and fine details in the image by emphasizing the high-frequency components. It uses a simple 3x3 kernel for sharpening.

    Args:
        image (np.ndarray): The input image to be sharpened. It can be a grayscale or color image.
        params (dict): A dictionary containing configuration parameters for sharpening (currently unused but can be extended).

    Returns:
        np.ndarray: The sharpened image with enhanced edges and details.

    Logging:
        - Logs an info message when the sharpening filter is applied.
        - Logs an error message if an exception occurs during the sharpening process.

    Example:
        sharpened_image = preprocess(input_image, params)
        print(sharpened_image)
    """
    try:
        # Simple sharpening kernel (high-pass filter)
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], dtype=np.float32)
        
        # Apply the filter to the image
        sharpened = cv2.filter2D(image, -1, kernel)
        
        # Log the operation
        logging.info("Applied sharpening filter.")
        
        return sharpened
    except Exception as e:
        logging.error(f"Sharpen preprocessing failed: {e}")
        raise
