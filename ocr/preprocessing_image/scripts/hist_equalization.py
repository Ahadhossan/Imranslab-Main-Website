import cv2
import numpy as np
import logging

def validate_input(image: np.ndarray) -> None:
    """
    Validates the input image before preprocessing.

    Raises:
        ValueError: If the input image is None, empty, or of unsupported format.
    """
    if image is None or image.size == 0:
        raise ValueError("Input image is empty or None.")
    if len(image.shape) not in [2, 3]:
        raise ValueError("Unsupported image format. Only grayscale and color images are supported.")
    if len(image.shape) == 3 and image.shape[2] != 3:
        raise ValueError("Unsupported image format. Only 3-channel color images are supported.")

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Improve contrast by histogram equalization (on grayscale image).
    
    This function applies **histogram equalization** to the input image, which improves the contrast by adjusting the intensities of the pixels. 
    It works differently for grayscale and color images: for color images, the luminance (Y) channel is equalized, while the chrominance channels remain unchanged.

    Args:
        image (np.ndarray): The input image to be equalized. It can be a grayscale or color image.
        params (dict): A dictionary containing configuration parameters for histogram equalization (not used in this function but can be extended in the future).

    Returns:
        np.ndarray: The contrast-enhanced image after histogram equalization.

    Logging:
        - Logs an info message if histogram equalization is applied to a grayscale or color image.
        - Logs an error message if an exception occurs during the histogram equalization process.

    Example:
        enhanced_image = preprocess(input_image, params)
        print(enhanced_image)
    """
    try:
        validate_input(image)  # ✅ Validate input before processing

        # If image is color, convert to YUV and equalize the Y (luminance) channel
        if len(image.shape) == 3:
            yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
            result_img = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
            logging.info("Applied histogram equalization to color image (Y channel).")
            return result_img
        else:
            result_img = cv2.equalizeHist(image)
            logging.info("Applied histogram equalization to grayscale image.")
            return result_img
    except Exception as e:
        logging.error(f"Histogram equalization preprocessing failed: {e}")
        raise
