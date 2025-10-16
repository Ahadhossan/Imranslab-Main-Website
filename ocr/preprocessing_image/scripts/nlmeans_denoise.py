import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Apply Non-local Means denoising (fastNlMeansDenoising) for noise reduction.

    This function performs **Non-local Means (NLM) denoising** on the input image, which is a sophisticated denoising algorithm 
    that works by comparing patches of the image and reducing noise while preserving image details. The method is applied to 
    grayscale or color images and is effective for reducing noise without blurring the edges.

    Args:
        image (np.ndarray): The input image to be denoised. It can be a grayscale or color image.
        params (dict): A dictionary containing configuration parameters for the denoising process:
            - 'h' (float): The filter strength. Higher values result in more aggressive denoising (default is 10).
            - 'templateWindowSize' (int): The size of the template window used for denoising. Should be an odd number (default is 7).
            - 'searchWindowSize' (int): The size of the search window used for denoising (default is 21).
            - 'hColor' (float, optional): The filter strength for color images. Default is the same as 'h'.

    Returns:
        np.ndarray: The denoised image with reduced noise.

    Logging:
        - Logs an info message with the filter parameters used for denoising (e.g., h, hColor).
        - Logs an error message if an exception occurs during the denoising process.

    Example:
        denoised_image = preprocess(input_image, params)
        print(denoised_image)
    """
    try:
        # Extract parameters from the configuration dictionary
        h = params.get("h", 10)
        templateWindowSize = params.get("templateWindowSize", 7)
        searchWindowSize = params.get("searchWindowSize", 21)
        
        if len(image.shape) == 3 and image.shape[2] == 3:
            # Color image denoising
            hColor = params.get("hColor", h)
            denoised = cv2.fastNlMeansDenoisingColored(image, None, h, hColor, templateWindowSize, searchWindowSize)
            logging.info(f"Applied fastNlMeansDenoisingColored with h={h}, hColor={hColor}.")
        else:
            # Grayscale image denoising
            denoised = cv2.fastNlMeansDenoising(image, None, h, templateWindowSize, searchWindowSize)
            logging.info(f"Applied fastNlMeansDenoising with h={h}.")
        
        return denoised
    except Exception as e:
        logging.error(f"NLMeans denoising preprocessing failed: {e}")
        raise
