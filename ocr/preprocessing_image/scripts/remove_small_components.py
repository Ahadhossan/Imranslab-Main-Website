import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Remove small connected components (noise) from a binary image.

    This function removes small connected components (such as noise) from a binary image. It first ensures that the image is binary, and if not, it applies Otsu’s thresholding method to convert it. Then, it identifies connected components and removes those smaller than a specified size, effectively cleaning the image by removing small noise.

    Args:
        image (np.ndarray): The input binary image. If it is a color image, it will be converted to grayscale.
        params (dict): A dictionary containing configuration parameters for the processing:
            - 'min_size' (int): The minimum size of connected components to keep. Smaller components are removed (default is 5).

    Returns:
        np.ndarray: The cleaned binary image with small components removed.

    Logging:
        - Logs an info message if the image was not binary and Otsu's thresholding was applied.
        - Logs the number of small components removed and their size.
        - Logs an error message if an exception occurs during the processing.

    Example:
        cleaned_image = preprocess(input_image, params)
        print(cleaned_image)
    """
    try:
        # Ensure the image is binary (if not, threshold using Otsu as fallback)
        img = image
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        vals = np.unique(img)
        bin_img = img
        if not (len(vals) == 2 and 0 in vals and 255 in vals):
            _, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            logging.info("Image was not binary, applied Otsu threshold for remove_small_components step.")
        
        # Invert the image so that text/foreground becomes white (255)
        inv = cv2.bitwise_not(bin_img)
        
        # Find connected components
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(inv, connectivity=8)
        
        # Get minimum component size to keep
        min_size = params.get("min_size", 5)
        mask = np.zeros(inv.shape, dtype=np.uint8)
        removed_count = 0
        
        # Remove small connected components
        for label in range(1, num_labels):  # label 0 is the background
            area = stats[label, cv2.CC_STAT_AREA]
            if area >= min_size:
                mask[labels == label] = 255  # Keep large components
            else:
                removed_count += 1
        
        # Final result after removing small components
        result_img = cv2.bitwise_not(mask)
        logging.info(f"Removed {removed_count} small components smaller than {min_size}px.")
        
        return result_img
    except Exception as e:
        logging.error(f"Remove small components preprocessing failed: {e}")
        raise
