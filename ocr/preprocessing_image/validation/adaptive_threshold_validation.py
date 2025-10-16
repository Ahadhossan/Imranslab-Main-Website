# import numpy as np
# import logging

# def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
#     """Validate adaptive thresholding by checking resulting binary values and ratio of foreground."""
#     result = {"step": "adaptive_threshold", "status": "", "metrics": {}}
#     try:
#         unique_vals = np.unique(output_image)
#         is_binary = all(val in [0, 255] for val in unique_vals)
#         if is_binary:
#             result["status"] = "success"
#             total_pixels = output_image.size
#             black_pixels = int(np.sum(output_image == 0))
#             percent_black = (black_pixels / total_pixels) * 100 if total_pixels > 0 else 0
#             result["metrics"]["black_pixels_percent"] = round(percent_black, 2)
#             logging.info(f"Adaptive threshold validation passed. Black pixel percentage: {percent_black:.2f}%.")
#         else:
#             result["status"] = "failure"
#             result["metrics"]["unique_values"] = unique_vals.tolist()
#             logging.error("Adaptive threshold validation failed: output is not binary.")
#     except Exception as e:
#         result["status"] = "failure"
#         logging.exception(f"Adaptive threshold validation exception: {e}")
#     return result

import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """
    Validate the result of adaptive thresholding by checking if the output image is binary (i.e., contains only 0 and 255) and calculates the percentage of black pixels in the output image.

    This function ensures that the adaptive thresholding operation produces a binary image and provides insights into the resulting foreground, specifically the percentage of black pixels.

    Args:
        input_image (np.ndarray): The original image before adaptive thresholding (not used directly in validation).
        output_image (np.ndarray): The binary image generated after adaptive thresholding that will be validated.
        params (dict): A dictionary containing configuration parameters for the validation process (currently unused).

    Returns:
        dict: A dictionary containing the validation result, including:
            - 'step': Name of the validation step (always "adaptive_threshold").
            - 'status': Validation result status, either "success" or "failure".
            - 'metrics': A dictionary with validation metrics:
                - 'black_pixels_percent': The percentage of black pixels in the image (only if validation is successful).
                - 'unique_values': A list of unique pixel values in the image (only if validation fails).
    
    Logging:
        - Logs an info message with the black pixel percentage if validation is successful.
        - Logs an error message if the output image is not binary.
        - Logs an exception if any error occurs during the validation process.

    Example:
        result = validate(input_image, output_image, params)
        print(result)
    """
    result = {"step": "adaptive_threshold", "status": "", "metrics": {}}
    
    try:
        # Get the unique pixel values from the output image
        unique_vals = np.unique(output_image)
        
        # Check if all unique values are either 0 (black) or 255 (white)
        is_binary = all(val in [0, 255] for val in unique_vals)
        
        if is_binary:
            result["status"] = "success"
            total_pixels = output_image.size
            black_pixels = int(np.sum(output_image == 0))
            percent_black = (black_pixels / total_pixels) * 100 if total_pixels > 0 else 0
            result["metrics"]["black_pixels_percent"] = round(percent_black, 2)
            logging.info(f"Adaptive threshold validation passed. Black pixel percentage: {percent_black:.2f}%.")
        else:
            result["status"] = "failure"
            result["metrics"]["unique_values"] = unique_vals.tolist()
            logging.error("Adaptive threshold validation failed: output is not binary.")
    
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Adaptive threshold validation exception: {e}")
    
    return result