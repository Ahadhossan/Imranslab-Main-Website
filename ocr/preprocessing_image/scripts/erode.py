import cv2
import numpy as np
import logging


def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Erode the image to shrink bright regions (or dark text regions if inverted).

    This function performs morphological erosion on the input image, which shrinks bright regions or dark text regions in the image.
    Erosion is used to reduce the size of features or remove small bright areas (or dark areas if the image is inverted).

    Args:
        image (np.ndarray): The input image to be eroded. It can be in color or grayscale.
        params (dict): A dictionary containing configuration parameters for the erosion process:
            - 'ksize' (int): The size of the kernel used for erosion (default is 3).
            - 'kernel_shape' (str): The shape of the kernel. Can be "rect", "ellipse", or "cross" (default is "rect").
            - 'target' (str): Specifies whether to erode bright regions ("bright") or dark text regions ("dark").
                              The image will be inverted if "dark" is selected (default is "dark").
            - 'iterations' (int): The number of iterations for the erosion (default is 1).

    Returns:
        np.ndarray: The eroded image, with shrunk bright or dark regions depending on the target specified.

    Logging:
        - Logs an info message with the kernel size, shape, and number of iterations applied for erosion.
        - Logs an error message if an exception occurs during the erosion process.

    Example:
        eroded_image = preprocess(input_image, params)
        print(eroded_image)
    """

    try:
        ksize = params.get("ksize", 3)
        if ksize % 2 == 0:
            ksize += 1
        kernel_shape = params.get("kernel_shape", "rect").lower()
        if kernel_shape == "ellipse":
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
        elif kernel_shape == "cross":
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (ksize, ksize))
        else:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))
        target = params.get("target", "dark").lower()
        img = image
        inverted = False
        if target == "dark":
            img = cv2.bitwise_not(image)
            inverted = True
        iterations = params.get("iterations", 1)
        eroded = cv2.erode(img, kernel, iterations=iterations)
        if inverted:
            eroded = cv2.bitwise_not(eroded)
        logging.info(f"Applied erosion with ksize={ksize}, shape={kernel_shape}, iterations={iterations}.")
        return eroded
    except Exception as e:
        logging.error(f"Erosion preprocessing failed: {e}")
        raise
