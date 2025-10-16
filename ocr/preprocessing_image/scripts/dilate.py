import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Dilate the image to expand bright regions (or dark text regions if inverted).

    This function performs morphological dilation on the input image, which expands the bright regions or dark text regions in the image.
    Dilation is typically used to enhance features such as text regions or object boundaries by increasing their size.

    Args:
        image (np.ndarray): The input image to be dilated. It can be in color or grayscale.
        params (dict): A dictionary containing configuration parameters for the dilation process:
            - 'ksize' (int): The size of the kernel used for dilation (default is 3).
            - 'kernel_shape' (str): The shape of the kernel. Can be "rect", "ellipse", or "cross" (default is "rect").
            - 'target' (str): Specifies whether to dilate bright regions ("bright") or dark text regions ("dark"). 
                               The image will be inverted if "dark" is selected (default is "dark").
            - 'iterations' (int): The number of iterations for the dilation (default is 1).

    Returns:
        np.ndarray: The dilated image, with expanded bright or dark regions depending on the target specified.

    Logging:
        - Logs an info message with the kernel size, shape, and number of iterations applied for dilation.
        - Logs an error message if an exception occurs during the dilation process.

    Example:
        dilated_image = preprocess(input_image, params)
        print(dilated_image)
    """
    try:
        # Check for valid image type (uint8, int32, int16)
        if image.dtype not in [np.uint8, np.int32, np.int16]:
            raise TypeError("Image must be of type uint8, int32 or int16.")

        # Get the kernel size and ensure it's odd
        ksize = params.get("ksize", 3)
        if ksize % 2 == 0:
            ksize += 1

        # Ensure kernel size is within a reasonable range
        if ksize <= 0:
            raise ValueError("Kernel size must be a positive odd integer.")

        # If the kernel size is too small for thin features, adjust it
        if np.count_nonzero(image) < 10 and ksize < 5:
            ksize = 5
            logging.warning("Adjusted kernel size to 5 for better dilation of thin features.")

        # Get the kernel shape (rectangular, elliptical, or cross)
        kernel_shape = params.get("kernel_shape", "rect").lower()
        if kernel_shape == "ellipse":
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
        elif kernel_shape == "cross":
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (ksize, ksize))
        else:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))

        # Determine whether to target bright or dark regions
        target = params.get("target", "dark").lower()
        img = image
        inverted = False
        if target == "dark":
            img = cv2.bitwise_not(image)  # Invert the image for dark region dilation
            inverted = True

        # Apply dilation
        dilated = cv2.dilate(img, kernel, iterations=params.get("iterations", 1))

        # If the image was inverted, invert it back to restore the original bright/dark regions
        if inverted:
            dilated = cv2.bitwise_not(dilated)

        # Log the applied parameters
        logging.info(f"Applied dilation with ksize={ksize}, shape={kernel_shape}, iterations={params.get('iterations', 1)}.")
        return dilated

    except TypeError as e:
        logging.error(f"Invalid image type: {e}")
        # You can raise this error or return a response indicating an invalid image type
        raise

    except ValueError as e:
        logging.error(f"Invalid parameter: {e}")
        # Graceful error response: can be logged, or a user-friendly message can be returned
        raise

    except Exception as e:
        logging.error(f"Dilation preprocessing failed: {e}")
        # Catch any other unforeseen errors and log them
        raise
