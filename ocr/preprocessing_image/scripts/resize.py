import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Resize the input image based on target width and/or height while considering
    optional upscale-only behavior.

    This function is commonly used in OCR (Optical Character Recognition) preprocessing 
    pipelines to ensure images meet minimum size requirements before further processing 
    (like binarization, deskew, or text extraction). Proper resizing improves OCR accuracy.

    Parameters:
    ----------
    image : np.ndarray
        The input image as a NumPy array. Can be grayscale or color.

    params : dict
        A dictionary containing configuration parameters:
            - "target_width" (int, optional): Desired width of the output image.
            - "target_height" (int, optional): Desired height of the output image.
            - "upscale_only" (bool, optional): If True, the image will only be resized 
                                               when the target size is larger than the original 
                                               (default is True).

        The function will also update this dictionary with:
            - "resized" (bool): True if resizing was performed.
            - "new_width" (int): The resulting image width after resizing.
            - "new_height" (int): The resulting image height after resizing.

    Returns:
    -------
    np.ndarray
        The resized image if conditions for resizing were met; otherwise, 
        the original image is returned.

    Raises:
    ------
    ValueError:
        If the input image is None, not a valid NumPy array, or empty.

    Notes:
    -----
    - The function preserves the aspect ratio of the image.
    - It supports flexible resizing:
        * Width-based scaling if only target_width is provided.
        * Height-based scaling if only target_height is provided.
        * Minimum or maximum scaling based on both dimensions depending on upscale_only.
    - If upscale_only=True, the function avoids downscaling.
    - Uses OpenCV's INTER_CUBIC interpolation for upscaling and INTER_AREA for downscaling.

    Example Usage:
    -------------
    params = {"target_width": 1024, "target_height": 768, "upscale_only": True}
    output = preprocess(image, params)
    """
        
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("Invalid input image.")

    if image.size == 0:
        raise ValueError("Empty image provided.")

    height, width = image.shape[:2]
    target_width = params.get("target_width", None)
    target_height = params.get("target_height", None)
    upscale_only = params.get("upscale_only", True)

    if target_width == 0 and target_height == 0:
        logging.info("Resize step: Target size is zero, skipping resize.")
        return image

    # Width-based scaling
    if target_width and not target_height:
        scale = target_width / width
    # Height-based scaling
    elif target_height and not target_width:
        scale = target_height / height
    # Both provided
    else:
        scale_w = target_width / width if target_width else 1.0
        scale_h = target_height / height if target_height else 1.0
        scale = min(scale_w, scale_h) if upscale_only else max(scale_w, scale_h)

    new_w = max(1, int(width * scale))
    new_h = max(1, int(height * scale))

    # Skip resize if size same
    if new_w == width and new_h == height:
        logging.info("Resize step: Image already meets size requirements, skipping resize.")
        return image

    # Don't downscale if upscale_only
    if upscale_only and (new_w < width or new_h < height):
        logging.info("Resize step: Upscale only enabled. Skipping downscale.")
        return image

    interpolation = cv2.INTER_CUBIC if new_w > width or new_h > height else cv2.INTER_AREA
    resized = cv2.resize(image, (new_w, new_h), interpolation=interpolation)

    params["resized"] = True
    params["new_width"] = new_w
    params["new_height"] = new_h

    return resized
