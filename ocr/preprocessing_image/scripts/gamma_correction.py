import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Apply gamma correction to adjust brightness and contrast.

    This function applies gamma correction to an image, which is a nonlinear transformation often used to adjust the brightness and contrast of images. Gamma correction can be used to lighten or darken the image without affecting the linearity of pixel values.

    Args:
        image (np.ndarray): The input image to which gamma correction will be applied. It can be a grayscale or color image.
        params (dict): A dictionary containing configuration parameters for the gamma correction:
            - 'gamma' (float): The gamma value used for correction. A value greater than 1.0 brightens the image, and a value less than 1.0 darkens it. The default is 1.0, meaning no adjustment.

    Returns:
        np.ndarray: The gamma-corrected image.

    Logging:
        - Logs an info message with the gamma value applied for the correction.
        - Logs an error message if an exception occurs during the gamma correction process.

    Example:
        gamma_corrected_image = preprocess(input_image, params)
        print(gamma_corrected_image)
    """

    # try:
    #     # Fetch gamma value from params, default to 1.0 if not provided
    #     gamma = params.get("gamma", 1.0)

    #     # Ensure gamma is a numeric value
    #     if not isinstance(gamma, (int, float)):
    #         raise ValueError("Gamma must be a numeric value.")

    #     # Ensure gamma is positive
    #     if gamma <= 0:
    #         raise ValueError("Gamma must be positive.")

    #     logging.info(f"Applying gamma correction with gamma = {gamma}")

    #     # Handle color images
    #     if len(image.shape) == 3:
    #         # Apply gamma correction to each channel of the image (for color images)
    #         channels = [cv2.LUT(ch, ((np.arange(256) / 255.0) ** gamma) * 255).astype("uint8") 
    #                     for ch in cv2.split(image)]
    #         corrected = cv2.merge(channels)
    #     else:
    #         # Apply gamma correction for grayscale images
    #         corrected = cv2.LUT(image, ((np.arange(256) / 255.0) ** gamma) * 255).astype("uint8")

    #     return corrected
    # except Exception as e:
    #     logging.error(f"Gamma correction preprocessing failed: {e}")
    #     raise 
    # try:
    #     # Fetch gamma value from params, default to 1.0 if not provided
    #     gamma = params.get("gamma", 1.0)

    #     # Ensure gamma is a numeric value
    #     if not isinstance(gamma, (int, float)):
    #         raise ValueError("Gamma must be a numeric value.")

    #     # Ensure gamma is positive
    #     if gamma <= 0:
    #         raise ValueError("Gamma must be positive.")

    #     logging.info(f"Applying gamma correction with gamma = {gamma}")

    #     # Handle color images
    #     if len(image.shape) == 3:
    #         # Apply gamma correction to each channel of the image (for color images)
    #         channels = [cv2.LUT(ch, ((np.arange(256) / 255.0) ** gamma) * 255).astype("uint8") 
    #                     for ch in cv2.split(image)]
    #         corrected = cv2.merge(channels)
    #     else:
    #         # Apply gamma correction for grayscale images
    #         corrected = cv2.LUT(image, ((np.arange(256) / 255.0) ** gamma) * 255).astype("uint8")

    #     # Ensure pixel values are clamped between 0 and 255
    #     corrected = np.clip(corrected, 0, 255)

    #     return corrected
    # except Exception as e:
    #     logging.error(f"Gamma correction preprocessing failed: {e}")
    #     raise

    try:
        gamma = params.get("gamma", 1.0)
        if not isinstance(gamma, (int, float)):
            raise ValueError("Gamma must be a numeric value.")
        if gamma <= 0:
            raise ValueError("Gamma must be positive.")
        logging.info(f"Applying gamma correction with gamma = {gamma}")
        lookup_table = np.array([(i / 255.0) ** (1.0 / gamma) * 255 for i in range(256)], dtype=np.uint8)
        if len(image.shape) == 3:
            channels = cv2.split(image)
            channels = [cv2.LUT(ch, lookup_table) for ch in channels]
            corrected = cv2.merge(channels)
        else:
            corrected = cv2.LUT(image, lookup_table)
        corrected = np.clip(corrected, 0, 255)
        return corrected
    except Exception as e:
        logging.error(f"Gamma correction preprocessing failed: {e}")
        raise