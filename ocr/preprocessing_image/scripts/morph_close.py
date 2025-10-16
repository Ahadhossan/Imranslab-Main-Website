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
    Apply morphological closing to fill small holes and gaps.
    """
    # Ensure ksize is greater than 0
    if ksize <= 0:
        raise ValueError("Kernel size must be greater than zero.")

    try:
        # Ensure kernel size is odd
        if ksize % 2 == 0:
            ksize += 1  # Ensure kernel size is odd

        # Get the kernel based on shape
        kernel = get_kernel(kernel_shape, ksize)

        # Invert the image if needed
        img = invert_image(image, target)

        # Apply morphological closing (dilation followed by erosion)
        closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        # Invert the image back if it was originally inverted
        if target == "dark":
            closed = cv2.bitwise_not(closed)

        # Log the applied parameters
        logging.info(f"Applied morphological close with ksize={ksize}, shape={kernel_shape}.")
        
        return closed
    except Exception as e:
        logging.error(f"Morphological close preprocessing failed: {e}")
        raise
