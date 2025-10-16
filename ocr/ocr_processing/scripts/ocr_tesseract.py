import pytesseract
from PIL import Image, UnidentifiedImageError
import logging
import sys
import os

# Configure logging to show updates and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_image(image_path: str, output_folder: str, lang: str = None):
    try:
        logging.info(f"Starting OCR with Tesseract on image: {image_path}")

        # Open the image using PIL
        try:
            image = Image.open(image_path)
            logging.info(f"Image {image_path} successfully opened.")
        except UnidentifiedImageError as e:
            logging.error(f"Failed to open image {image_path}: {e}")
            sys.exit(1)
        except Exception as e:
            logging.error(f"Unexpected error opening image {image_path}: {e}")
            sys.exit(1)

        # Perform OCR using Tesseract
        try:
            if lang:
                extracted_text = pytesseract.image_to_string(image, lang=lang)
            else:
                extracted_text = pytesseract.image_to_string(image)
            logging.info("OCR completed successfully.")
        except Exception as e:
            logging.error(f"Error during OCR process for image {image_path}: {e}")
            extracted_text = ""  # If OCR fails, leave text as empty

        # Use input file name as the base and append '_processed_tesseract' as the suffix
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        file_name = f"{base_name}_processed_tesseract.txt"
        output_file_path = os.path.join(output_folder, "ocr_tesseract", file_name)

        # Ensure the output folder exists
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        # Add the image file name at the beginning of the output text
        processed_text = f"Processed file: {image_path}\n\n{extracted_text}"

        # Write the processed text to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_text)
            logging.info(f"Processed text saved to {output_file_path}")

    except Exception as e:
        logging.error(f"An error occurred while processing the image {image_path}: {e}")