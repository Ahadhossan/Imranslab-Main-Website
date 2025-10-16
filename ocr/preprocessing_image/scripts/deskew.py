import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Perform skew detection and deskewing on the input image for OCR preprocessing.

    Skew:
        Skew refers to the unintentional tilt or rotation of text lines in an image.
        In OCR (Optical Character Recognition) systems, skewed images reduce the accuracy
        of text extraction because the text alignment is not horizontal.

    Deskew:
        Deskew is the process of correcting the skew by detecting the angle of rotation 
        and rotating the image in the opposite direction to align the text horizontally.
        This step is critical in OCR pipelines to improve text recognition performance.

    Process Details:
        - Converts the image to grayscale if it is in color (BGR).
        - Applies binarization (thresholding) if the image is not already binary.
        - Detects the skew angle using the minimum area bounding rectangle of foreground pixels.
        - Rotates the image to correct the skew (deskewing).
        - Updates `params` with the detected skew angle for logging or debugging purposes.
        - If the detected angle is very small (less than 5 degrees), the rotation is skipped.

    Parameters:
        image (np.ndarray): Input image as a NumPy array. Can be grayscale or color (BGR).
        params (dict): Dictionary to store processing parameters and results.
                      The key "detected_angle" will be updated with the skew angle (float).

    Returns:
        np.ndarray: Deskewed (or original if no skew detected) image suitable for OCR.
    """
    gray = image
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    vals = np.unique(gray)
    bin_img = gray 
    if not (len(vals) == 2 and 0 in vals and 255 in vals):
        _, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    inv = cv2.bitwise_not(bin_img)
    coords = np.column_stack(np.where(inv > 0))

    angle = 0.0
    if coords.shape[0] > 0:
        rect = cv2.minAreaRect(coords)
        angle = rect[-1]

        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        # Handle rare case where it detects 90 degree rotation for straight line
        if abs(angle) == 90:
            angle = 0.0

    params["detected_angle"] = angle  # Always set this before return

    if abs(angle) < 5:  # If image is already straight
        logging.info("Image is already straight. Skipping deskew.")
        return image

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    logging.info(f"Detected skew angle: {angle:.2f} degrees. Image rotated to deskew.")
    return rotated
