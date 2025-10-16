import os
import cv2
import yaml
import logging
import importlib
from utils import load_config, save_image, update_result_yaml

def run_pipeline(image_dir: str, config: dict) -> dict:
    """Run the preprocessing pipeline on all images in the given directory using the provided config."""
    results = {}
    # Prepare output directory
    output_dir = os.path.join(image_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    save_intermediate = config.get("save_intermediate", False)
    steps = config.get("steps", [])
    for image_name in os.listdir(image_dir):
        if not image_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            continue  # skip non-image files
        image_path = os.path.join(image_dir, image_name)
        try:
            img = cv2.imread(image_path)
            if img is None:
                logging.error(f"Failed to read image: {image_path}")
                continue
            logging.info(f"Processing image: {image_name}")
            original_img = img.copy()
            results[image_name] = {}
            current_img = img
            # Sequentially apply each preprocessing step
            for step in steps:
                name = step.get('name')
                enabled = step.get('enabled', True)
                params = step.get('params', {})
                if not enabled:
                    logging.info(f"Skipping step {name}")
                    continue
                module_path = f"preprocessing_image.scripts.{name}"
                validation_path = f"preprocessing_image.validation.{name}_validation"
                try:
                    step_module = importlib.import_module(module_path)
                except ImportError as ie:
                    logging.error(f"Step module {module_path} not found: {ie}")
                    results[image_name][name] = {"status": "failure", "error": "module not found"}
                    break
                try:
                    # Copy params to avoid cross-image modifications
                    step_params = dict(params)
                    output_img = step_module.preprocess(current_img, step_params)
                except Exception as e:
                    logging.error(f"Error in step '{name}': {e}")
                    results[image_name][name] = {"status": "failure", "error": str(e)}
                    break
                try:
                    val_module = importlib.import_module(validation_path)
                except ImportError as ie:
                    logging.error(f"Validation module {validation_path} not found: {ie}")
                    results[image_name][name] = {"status": "failure", "error": "validation module not found"}
                    break
                try:
                    val_result = val_module.validate(current_img, output_img, step_params)
                except Exception as e:
                    logging.error(f"Validation error in step '{name}': {e}")
                    val_result = {"step": name, "status": "failure", "error": str(e)}
                # Record validation result for this step
                results[image_name][name] = val_result
                # Optionally save intermediate output
                if save_intermediate:
                    inter_path = os.path.join(output_dir, f"{os.path.splitext(image_name)[0]}_{name}.png")
                    save_image(output_img, inter_path)
                # Set current image for next step
                current_img = output_img
            # Save final output image
            final_path = os.path.join(output_dir, image_name)
            save_image(current_img, final_path)
            logging.info(f"Saved processed image to {final_path}")
        except Exception as e:
            logging.exception(f"Pipeline error processing image {image_name}: {e}")
    # Write summary results to YAML
    result_path = os.path.join(output_dir, "result.yaml")
    update_result_yaml(results, result_path)
    logging.info(f"Pipeline completed. Results saved to {result_path}")
    return results
