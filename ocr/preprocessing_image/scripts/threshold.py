import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Binarize the image using global threshold (Otsu or specified value).

    This function applies **global thresholding** to the input image, converting it into a binary image. Depending on the specified method, 
    it either applies **Otsu’s thresholding**, which automatically determines the optimal threshold, or a **fixed threshold value** 
    provided by the user. This process is used to convert grayscale images into binary images, where pixels are either black or white.

    Args:
        image (np.ndarray): The input image to be binarized. It can be grayscale or color. If the image is color, it will be converted to grayscale.
        params (dict): A dictionary containing configuration parameters for the thresholding process:
            - 'method' (str): The method used for thresholding. Can be "otsu" (default) or "fixed" for a fixed threshold.
            - 'threshold_value' (int): The threshold value used for fixed thresholding. Should be between 0 and 255 (default is 0).

    Returns:
        np.ndarray: The binarized image with pixel values either 0 (black) or 255 (white).

    Logging:
        - Logs an info message with the thresholding method and threshold value used.
        - Logs an error message if an exception occurs during the thresholding process.

    Example:
        binary_image = preprocess(input_image, params)
        print(binary_image)
    """
    try:
        gray = image
        # Ensure grayscale input
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        method = params.get("method", "otsu").lower()
        thresh_val = params.get("threshold_value", 0)

        # Validate threshold value
        if thresh_val < 0 or thresh_val > 255:
            raise ValueError(f"Threshold value {thresh_val} is out of range (0-255).")

        if method == "otsu":
            # Otsu's binarization (threshold value determined automatically)
            thresh_val, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            logging.info(f"Applied Otsu's threshold. Threshold value={thresh_val:.2f}.")
        else:
            # Fixed threshold
            _, binary = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
            logging.info(f"Applied fixed threshold at value {thresh_val}.")
        
        return binary
    except Exception as e:
        logging.error(f"Threshold preprocessing failed: {e}")
        raise
