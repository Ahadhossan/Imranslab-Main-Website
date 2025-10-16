import cv2
import numpy as np
import logging

def preprocess(image: np.ndarray, params: dict) -> np.ndarray:
    """
    Thin the binary image to get a skeletal representation of text.

    Args:
        image (np.ndarray): The input binary image to be skeletonized. If the image is in color, it will be converted to grayscale.
        params (dict): A dictionary containing configuration parameters for the skeletonization:
            - 'reduction_percent' (float): The percentage reduction in foreground pixels due to skeletonization. This is calculated and stored after processing.

    Returns:
        np.ndarray: The skeletonized image, with foreground features reduced to their thinned form.
    """
    # Ensure the image is not None or empty
    if image is None or image.size == 0:
        raise ValueError("Input image is empty or None.")
    
    # Handle 1x1 image case (grayscale or color)
    if image.shape == (1, 1, 3):  # Specifically handling 1x1 color image
        logging.info("Skipping skeletonization for 1x1 color image.")
        return image  # Return the color image as is (1x1, 3 channels)
    
    # Convert to grayscale if the image is in color
    if len(image.shape) == 3:  # Color image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    try:
        # Ensure binary image (convert to grayscale and threshold if not binary)
        img = image
        if len(img.shape) == 3:  # Color image, convert to grayscale
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        vals = np.unique(img)
        bin_img = img
        if not (len(vals) == 2 and 0 in vals and 255 in vals):  # If image is not binary
            _, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        # Invert the image so that text becomes white (foreground) for skeletonization algorithm
        inv = cv2.bitwise_not(bin_img)
        
        # Initialize an empty image for the skeleton
        skeleton = np.zeros_like(inv)
        
        # Define a kernel for erosion and dilation
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        eroded = inv.copy()
        
        # Maximum iterations safeguard to avoid infinite loops
        max_iterations = 1000  # Safeguard
        iteration_count = 0

        while True:
            eroded = cv2.erode(eroded, kernel)  # Erode the image
            temp = cv2.dilate(eroded, kernel)  # Dilate the eroded image
            temp = cv2.subtract(inv, temp)  # Subtract dilated image from original to get the skeleton
            skeleton = cv2.bitwise_or(skeleton, temp)  # Combine the result with the skeleton
            inv = eroded.copy()

            # Log progress
            logging.info(f"Processing: {cv2.countNonZero(inv)} foreground pixels remaining.")
            
            iteration_count += 1
            if iteration_count > max_iterations:
                raise RuntimeError("Skeletonization loop exceeded maximum iterations.")
            
            # Exit the loop when no more foreground pixels remain
            if cv2.countNonZero(inv) == 0:
                break
        
        # Invert the image back to original polarity (skeleton in black on white)
        skeleton_result = cv2.bitwise_not(skeleton)
        
        # Calculate reduction in foreground pixels
        orig_foreground = int(np.sum(bin_img == 0))  # Count of foreground pixels in the original image
        skel_foreground = int(np.sum(skeleton_result == 0))  # Count of foreground pixels in the skeletonized image
        reduction_percent = (orig_foreground - skel_foreground) / orig_foreground * 100 if orig_foreground > 0 else 0
        
        # Store the reduction percentage in params
        params["reduction_percent"] = reduction_percent
        
        logging.info(f"Skeletonization complete. Foreground pixels reduced by {reduction_percent:.2f}%.")
        
        # Ensure the returned image has 3 channels if it was originally a color image
        if len(image.shape) == 3:
            return np.repeat(skeleton_result[:, :, np.newaxis], 3, axis=-1)  # Return 3-channel result
        return skeleton_result
    except Exception as e:
        logging.error(f"Skeletonization preprocessing failed: {e}")
        raise
