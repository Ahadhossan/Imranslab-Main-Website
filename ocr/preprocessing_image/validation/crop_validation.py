# import numpy as np
# import logging

# def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
#     """Validate cropping by checking area reduction and content preservation."""
#     result = {"step": "crop", "status": "", "metrics": {}}
#     try:
#         removed_percent = params.get("removed_percent", None)
#         if removed_percent is None:
#             result["status"] = "failure"
#             logging.error("Crop validation failed: removed_percent not recorded.")
#         else:
#             orig_area = input_image.shape[0] * input_image.shape[1]
#             new_area = output_image.shape[0] * output_image.shape[1]
#             result["metrics"]["removed_percent"] = round(float(removed_percent), 2)
#             if new_area <= orig_area:
#                 result["status"] = "success"
#                 logging.info(f"Crop validation passed. Area removed: {removed_percent:.2f}%.")
#             else:
#                 result["status"] = "failure"
#                 logging.error("Crop validation failed: output area larger than input.")
#     except Exception as e:
#         result["status"] = "failure"
#         logging.exception(f"Crop validation exception: {e}")
#     return result



import numpy as np
import logging

def validate(input_image: np.ndarray, output_image: np.ndarray, params: dict) -> dict:
    """
    Validate the result of cropping by ensuring that the output image has a smaller area compared to the input image, 
    and checks that the percentage of area removed is consistent with the recorded value.

    This function ensures that the cropping operation properly reduces the image area and preserves content in the remaining portion.

    Args:
        input_image (np.ndarray): The original image before cropping.
        output_image (np.ndarray): The cropped image to be validated.
        params (dict): A dictionary containing configuration parameters for the validation process. 
                       Specifically, it should include the 'removed_percent', which indicates the expected 
                       percentage of the image area that was removed during cropping.

    Returns:
        dict: A dictionary containing the validation result, including:
            - 'step': Name of the validation step (always "crop").
            - 'status': Validation result status, either "success" or "failure".
            - 'metrics': A dictionary with validation metrics:
                - 'removed_percent': The percentage of the image area that was removed during cropping (if validation is successful).

    Logging:
        - Logs an info message with the removed percentage if validation is successful.
        - Logs an error message if 'removed_percent' is not provided or if the output area is larger than the input area.
        - Logs an exception if any error occurs during the validation process.

    Example:
        result = validate(input_image, output_image, params)
        print(result)
    """
    result = {"step": "crop", "status": "", "metrics": {}}
    
    try:
        # Get the percentage of the image area removed during cropping
        removed_percent = params.get("removed_percent", None)
        
        if removed_percent is None:
            result["status"] = "failure"
            logging.error("Crop validation failed: removed_percent not recorded.")
        else:
            # Calculate the original and new image areas
            orig_area = input_image.shape[0] * input_image.shape[1]
            new_area = output_image.shape[0] * output_image.shape[1]
            
            result["metrics"]["removed_percent"] = round(float(removed_percent), 2)
            
            # Check if the new image area is smaller than or equal to the original area
            if new_area <= orig_area:
                result["status"] = "success"
                logging.info(f"Crop validation passed. Area removed: {removed_percent:.2f}%.")
            else:
                result["status"] = "failure"
                logging.error("Crop validation failed: output area larger than input.")
    
    except Exception as e:
        result["status"] = "failure"
        logging.exception(f"Crop validation exception: {e}")
    
    return result
