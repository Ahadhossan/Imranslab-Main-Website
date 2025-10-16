import cv2
import numpy as np
import logging


# Helper function to get kernel based on shape
def get_kernel(shape: str, size: int) -> np.ndarray:
    """
    Returns the kernel based on the specified shape and size.
    """
    if shape == "ellipse":
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))
    elif shape == "cross":
        return cv2.getStructuringElement(cv2.MORPH_CROSS, (size, size))
    else:
        return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


# Helper function to invert image if required
def invert_image(image: np.ndarray, target: str) -> np.ndarray:
    """
    Inverts the image if the target is 'dark' (i.e., dark regions become white).
    """
    if target == "dark":
        return cv2.bitwise_not(image)
    return image


def preprocess(image: np.ndarray, ksize: int = 3, kernel_shape: str = "rect", target: str = "dark") -> np.ndarray:
    """
    Apply morphological opening to remove small objects and noise.
    """
    try:
        # Ensure kernel size is odd
        if ksize <= 0:
            raise ValueError("Kernel size must be a positive odd number.")
        if ksize % 2 == 0:
            ksize += 1  # Ensure kernel size is odd

        # Get the kernel based on shape
        kernel = get_kernel(kernel_shape, ksize)

        # Invert the image if needed
        img = invert_image(image, target)

        # Apply morphological opening (erosion followed by dilation)
        opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        # Invert the image back if it was originally inverted
        if target == "dark":
            opened = cv2.bitwise_not(opened)

        # Log the applied parameters
        logging.info(f"Applied morphological open with ksize={ksize}, shape={kernel_shape}.")
        
        return opened
    except Exception as e:
        logging.error(f"Morphological open preprocessing failed: {e}")
        raise
